"""Experiment 2: brain-wave bands over time. Follows EXPERIMENT-2-PLAN.md exactly.

For every reading, the strength of the delta, theta, alpha and beta bands over the previous second
(128 readings, looking back only), after capping broken readings with limits learned from each fold's
learning rows. Scored on five stretches forward in time, with and without a 128-reading gap.

Run: python3 projects/eeg-eye-state/src/analyze_bands.py   (writes results/bands.json)"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze import RESULTS, load_data  # noqa: E402

RATE = 128          # readings per second (14,980 readings over about 117 seconds)
WINDOW = 128        # one second, looking back only
GAP = 128           # the windows overlap, so leave one window between learning and testing
BANDS = {"delta": (1, 4), "theta": (4, 8), "alpha": (8, 13), "beta": (13, 30)}
SEED = 20261110


def band_power(x: np.ndarray) -> dict[str, np.ndarray]:
    """Log mean power in each band over the trailing window. Row i uses readings i-127..i.
    Returns arrays of shape (len(x) - WINDOW + 1, channels)."""
    windows = sliding_window_view(x, WINDOW, axis=0)               # (n-127, channels, 128)
    windows = windows - windows.mean(axis=-1, keepdims=True)
    spectrum = np.abs(np.fft.rfft(windows * np.hanning(WINDOW), axis=-1)) ** 2
    freqs = np.fft.rfftfreq(WINDOW, d=1 / RATE)
    out = {}
    for name, (lo, hi) in BANDS.items():
        pick = (freqs >= lo) & (freqs < hi)
        out[name] = np.log(spectrum[..., pick].mean(axis=-1) + 1e-9)
    return out


def features(x_capped: np.ndarray, kind: str) -> np.ndarray:
    """Feature rows aligned with readings WINDOW-1 .. end."""
    if kind == "raw readings":
        return x_capped[WINDOW - 1:]
    bands = band_power(x_capped)
    if kind == "alpha only":
        return bands["alpha"]
    return np.hstack([bands[b] for b in BANDS])


def cap(x: np.ndarray, learn_rows: np.ndarray) -> np.ndarray:
    lower, upper = np.percentile(x[learn_rows], [0.5, 99.5], axis=0)
    return np.clip(x, lower, upper)


def run(kind: str, x: np.ndarray, y: np.ndarray, gap: int, labels: np.ndarray | None = None) -> list[float]:
    """Five stretches forward in time over the shared rows (readings WINDOW-1 onwards)."""
    y_rows = (labels if labels is not None else y)[WINDOW - 1:]
    rows = np.arange(len(y_rows))
    aucs = []
    for learn, test in TimeSeriesSplit(n_splits=5, gap=gap).split(rows):
        # Caps come only from the raw readings behind the learning rows: feature row i ends at
        # reading i + WINDOW - 1, so the learning rows use readings 0 .. learn[-1] + WINDOW - 1.
        capped = cap(x, np.arange(0, learn[-1] + WINDOW))
        f = features(capped, kind)
        model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight="balanced"))
        model.fit(f[learn], y_rows[learn])
        aucs.append(float(roc_auc_score(y_rows[test], model.predict_proba(f[test])[:, 1])))
    return aucs


def summary(aucs: list[float]) -> dict:
    a = np.asarray(aucs)
    return {"stretches": [round(v, 4) for v in aucs], "mean": round(float(a.mean()), 4), "min": round(float(a.min()), 4), "max": round(float(a.max()), 4), "stretches_below_coin_flip": int((a < 0.5).sum())}


def main() -> None:
    x, y = load_data()
    out = {
        "plan": "projects/eeg-eye-state/EXPERIMENT-2-PLAN.md",
        "rows_scored": int(len(y) - WINDOW + 1),
        "window_readings": WINDOW, "rate_per_second": RATE, "bands_hz": BANDS,
        "with_gap": {}, "without_gap": {},
    }
    for kind in ("raw readings", "all four bands", "alpha only"):
        out["with_gap"][kind] = summary(run(kind, x, y, GAP))
        out["without_gap"][kind] = summary(run(kind, x, y, 0))
        print(kind, out["with_gap"][kind])
    rng = np.random.default_rng(SEED)
    shuffled = [float(np.mean(run("all four bands", x, y, GAP, labels=rng.permutation(y)))) for _ in range(20)]
    out["label_shuffle_all_bands_with_gap"] = {"permutations": 20, "seed": SEED, "mean": round(float(np.mean(shuffled)), 4), "min": round(min(shuffled), 4), "max": round(max(shuffled), 4)}
    main_bands, main_raw = out["with_gap"]["all four bands"], out["with_gap"]["raw readings"]
    out["holds_up_better"] = bool(main_bands["mean"] > main_raw["mean"] and main_bands["stretches_below_coin_flip"] == 0)
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "bands.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("label_shuffle_all_bands_with_gap", "holds_up_better")}, indent=2))


if __name__ == "__main__":
    main()
