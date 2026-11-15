"""Reproducible time-aware EEG eye-state experiment.

The dataset is one chronological recording. We deliberately use contiguous
train/validation/test blocks rather than random row splitting.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.io import arff
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "EEG Eye State.arff"
RESULTS = ROOT / "results"
CHANNELS = ["AF3", "F7", "F3", "FC5", "T7", "P7", "O1", "O2", "P8", "T8", "FC6", "F4", "F8", "AF4"]


def load_data() -> tuple[np.ndarray, np.ndarray]:
    rows, _ = arff.loadarff(DATA)
    names = rows.dtype.names
    x = np.column_stack([rows[name].astype(float) for name in CHANNELS])
    target_name = [name for name in names if name not in CHANNELS][0]
    y = np.array([int(value.decode() if isinstance(value, bytes) else value) for value in rows[target_name]])
    return x, y


def trailing_features(x: np.ndarray, window: int = 9) -> np.ndarray:
    """Add causal trailing mean and standard deviation for each channel."""
    means = np.empty_like(x)
    stds = np.empty_like(x)
    for index in range(len(x)):
        start = max(0, index - window + 1)
        segment = x[start : index + 1]
        means[index] = segment.mean(axis=0)
        stds[index] = segment.std(axis=0)
    return np.hstack([x, means, stds])


def evaluate(name: str, x: np.ndarray, y: np.ndarray, train_end: int, val_end: int) -> dict:
    train = slice(0, train_end)
    validation = slice(train_end, val_end)
    test = slice(val_end, len(y))
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1200, class_weight="balanced"))
    model.fit(x[train], y[train])
    validation_probability = model.predict_proba(x[validation])[:, 1]
    test_probability = model.predict_proba(x[test])[:, 1]
    test_prediction = (test_probability >= 0.5).astype(int)
    return {
        "model": name,
        "train_samples": int(train_end),
        "validation_samples": int(val_end - train_end),
        "test_samples": int(len(y) - val_end),
        "validation_roc_auc": float(roc_auc_score(y[validation], validation_probability)),
        "test_roc_auc": float(roc_auc_score(y[test], test_probability)),
        "test_balanced_accuracy": float(balanced_accuracy_score(y[test], test_prediction)),
        "test_f1": float(f1_score(y[test], test_prediction)),
    }


def blocked_cross_validate(name: str, x: np.ndarray, y: np.ndarray, splits: int = 5, gap: int = 0) -> dict:
    """Evaluate contiguous future blocks using only earlier samples for fitting."""
    splitter = TimeSeriesSplit(n_splits=splits, gap=gap)
    folds = []
    for fold, (train_index, test_index) in enumerate(splitter.split(x), 1):
        model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1200, class_weight="balanced"))
        model.fit(x[train_index], y[train_index])
        probability = model.predict_proba(x[test_index])[:, 1]
        prediction = (probability >= 0.5).astype(int)
        fold_result = {
            "fold": fold,
            "train_start": int(train_index[0]),
            "train_end_exclusive": int(train_index[-1] + 1),
            "test_start": int(test_index[0]),
            "test_end_exclusive": int(test_index[-1] + 1),
            "train_samples": int(len(train_index)),
            "test_samples": int(len(test_index)),
            "test_roc_auc": float(roc_auc_score(y[test_index], probability)),
            "test_balanced_accuracy": float(balanced_accuracy_score(y[test_index], prediction)),
            "test_f1": float(f1_score(y[test_index], prediction)),
        }
        folds.append(fold_result)
    aucs = np.array([fold["test_roc_auc"] for fold in folds])
    return {
        "model": name,
        "splitter": "sklearn TimeSeriesSplit",
        "gap_samples": gap,
        "fold_count": len(folds),
        "folds": folds,
        "summary": {
            "mean_test_roc_auc": float(aucs.mean()),
            "std_test_roc_auc": float(aucs.std(ddof=1)),
            "min_test_roc_auc": float(aucs.min()),
            "max_test_roc_auc": float(aucs.max()),
        },
    }


def blocked_label_shuffle_control(
    name: str,
    x: np.ndarray,
    y: np.ndarray,
    permutations: int = 20,
    seed: int = 20261108,
) -> dict:
    """Break the signal/label relationship while keeping the same blocked folds."""
    rng = np.random.default_rng(seed)
    shuffled_means = []
    for _ in range(permutations):
        shuffled = rng.permutation(y)
        result = blocked_cross_validate(name, x, shuffled)
        shuffled_means.append(result["summary"]["mean_test_roc_auc"])
    values = np.asarray(shuffled_means)
    return {
        "model": name,
        "control": "global label permutation before five-fold forward-chaining evaluation",
        "permutations": permutations,
        "seed": seed,
        "mean_test_roc_auc": float(values.mean()),
        "std_test_roc_auc": float(values.std(ddof=1)),
        "min_test_roc_auc": float(values.min()),
        "max_test_roc_auc": float(values.max()),
        "shuffled_mean_test_roc_auc": [float(value) for value in values],
    }


def extreme_samples(x: np.ndarray, threshold: float = 20.0) -> list[int]:
    """Rows where any channel is more than `threshold` robust SDs from its median (recording glitches)."""
    median = np.median(x, axis=0)
    spread = np.median(np.abs(x - median), axis=0) * 1.4826
    return [int(index) for index in np.where((np.abs(x - median) / spread > threshold).any(axis=1))[0]]


def clip_to_training(x: np.ndarray, train_rows, window: int | None = None, low: float = 0.5, high: float = 99.5) -> np.ndarray:
    """Limit each channel to the 0.5th-99.5th percentile of the training rows only, then (optionally) add
    the causal trailing features. Test rows never influence the limits."""
    lower, upper = np.percentile(x[train_rows], [low, high], axis=0)
    clipped = np.clip(x, lower, upper)
    return trailing_features(clipped, window) if window else clipped


def blocked_cross_validate_clipped(name: str, x: np.ndarray, y: np.ndarray, window: int | None = None, splits: int = 5) -> dict:
    """The same forward-chaining folds, with glitch limits recomputed from each fold's training rows."""
    splitter = TimeSeriesSplit(n_splits=splits)
    aucs = []
    for train_index, test_index in splitter.split(x):
        features = clip_to_training(x, train_index, window)
        model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1200, class_weight="balanced"))
        model.fit(features[train_index], y[train_index])
        aucs.append(float(roc_auc_score(y[test_index], model.predict_proba(features[test_index])[:, 1])))
    values = np.asarray(aucs)
    return {
        "model": name,
        "fold_test_roc_auc": aucs,
        "summary": {
            "mean_test_roc_auc": float(values.mean()),
            "std_test_roc_auc": float(values.std(ddof=1)),
            "min_test_roc_auc": float(values.min()),
            "max_test_roc_auc": float(values.max()),
        },
    }


def main() -> None:
    x, y = load_data()
    train_end = int(len(y) * 0.70)
    val_end = int(len(y) * 0.85)
    results = {
        "dataset": {
            "name": "UCI EEG Eye State",
            "samples": int(len(y)),
            "channels": CHANNELS,
            "eye_closed_fraction": float(y.mean()),
            "split": "chronological 70% train / 15% validation / 15% test",
        },
        "models": [
            evaluate("pointwise EEG", x, y, train_end, val_end),
            evaluate("EEG + causal temporal context", trailing_features(x), y, train_end, val_end),
        ],
        "blocked_cross_validation": [
            blocked_cross_validate("pointwise EEG", x, y),
            blocked_cross_validate("EEG + causal temporal context", trailing_features(x), y),
        ],
        "blocked_label_shuffle_control": [
            blocked_label_shuffle_control("pointwise EEG", x, y),
            blocked_label_shuffle_control("EEG + causal temporal context", trailing_features(x), y),
        ],
        "blocked_gap_sensitivity": [
            blocked_cross_validate("pointwise EEG", x, y, gap=90),
            blocked_cross_validate("EEG + causal temporal context", trailing_features(x), y, gap=90),
        ],
        "temporal_window_sweep": [],
    }
    # Sensitivity analysis added after the first results: four samples are recording glitches
    # (values up to ~700,000 where typical readings are ~4,000). The primary results above are unchanged;
    # this repeats the holdout and blocked folds with training-only limits on each channel.
    train_rows = slice(0, train_end)
    results["artifact_sensitivity"] = {
        "added_after_primary_analysis": True,
        "method": "clip each channel to the 0.5th-99.5th percentile of the training rows only (per fold), then refit",
        "robust_z_threshold": 20,
        "extreme_sample_indices": extreme_samples(x),
        "final_holdout": [
            evaluate("pointwise EEG, glitches limited", clip_to_training(x, train_rows), y, train_end, val_end),
            evaluate("EEG + causal temporal context, glitches limited", clip_to_training(x, train_rows, 9), y, train_end, val_end),
        ],
        "blocked_cross_validation": [
            blocked_cross_validate_clipped("pointwise EEG, glitches limited", x, y),
            blocked_cross_validate_clipped("EEG + causal temporal context, glitches limited", x, y, window=9),
        ],
    }
    for window in (3, 9, 30, 90):
        final_result = evaluate(f"EEG + causal context ({window} samples)", trailing_features(x, window), y, train_end, val_end)
        blocked_result = blocked_cross_validate(f"EEG + causal context ({window} samples)", trailing_features(x, window), y)
        results["temporal_window_sweep"].append({
            "window_samples": window,
            "final_holdout": final_result,
            "blocked_summary": blocked_result["summary"],
        })
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "metrics.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
