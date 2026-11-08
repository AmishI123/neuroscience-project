"""Run the pre-specified four-model comparison on one Sensorium mouse.

Usage:
  python src/replicate_mouse.py /path/to/mouse-directory --output /tmp/result.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler


def correlation(predicted: np.ndarray, actual: np.ndarray) -> np.ndarray:
    p = predicted - predicted.mean(axis=0)
    a = actual - actual.mean(axis=0)
    return (p * a).sum(axis=0) / (np.sqrt((p**2).sum(axis=0) * (a**2).sum(axis=0)) + 1e-12)


def downsample(image: np.ndarray) -> np.ndarray:
    return image[0].reshape(36, 4, 64, 4).mean(axis=(1, 3)).ravel()


def load(root: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    data = root / "data"
    response_files = sorted((data / "responses").glob("*.npy"), key=lambda p: int(p.stem))
    n_trials = len(response_files)
    n_neurons = int(np.load(response_files[0]).shape[0])
    images = np.zeros((n_trials, 36 * 64), dtype=np.float32)
    responses = np.zeros((n_trials, n_neurons), dtype=np.float32)
    behavior = np.zeros((n_trials, 3), dtype=np.float32)
    for i in range(n_trials):
        images[i] = downsample(np.load(data / "images" / f"{i}.npy"))
        responses[i] = np.load(data / "responses" / f"{i}.npy")
        behavior[i] = np.load(data / "behavior" / f"{i}.npy").ravel()
    tiers = np.load(root / "meta" / "trials" / "tiers.npy", allow_pickle=True).astype(str)
    return images, responses, behavior, tiers


def fit_score(features: np.ndarray, responses: np.ndarray, train: np.ndarray, held_out: np.ndarray) -> float:
    model = Ridge(alpha=1000.0).fit(features[train], responses[train])
    return float(np.nanmean(correlation(model.predict(features[held_out]), responses[held_out])))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    images, responses, behavior, tiers = load(args.root)
    train = tiers == "train"
    held_out = (tiers == "validation") | (tiers == "test")

    image_scaler = StandardScaler().fit(images[train])
    scaled_images = image_scaler.transform(images)
    pca = PCA(n_components=150, random_state=0).fit(scaled_images[train])
    stimulus = pca.transform(scaled_images)
    behavior_scaled = StandardScaler().fit(behavior[train]).transform(behavior)

    values = {
        "stimulus_only": fit_score(stimulus, responses, train, held_out),
        "stimulus_plus_running": fit_score(np.hstack([stimulus, behavior_scaled[:, [2]]]), responses, train, held_out),
        "stimulus_plus_pupil": fit_score(np.hstack([stimulus, behavior_scaled[:, [0, 1]]]), responses, train, held_out),
        "stimulus_plus_both": fit_score(np.hstack([stimulus, behavior_scaled]), responses, train, held_out),
    }
    result = {
        "mouse": args.root.name,
        "trials": int(len(tiers)),
        "neurons": int(responses.shape[1]),
        "train_trials": int(train.sum()),
        "held_out_trials": int(held_out.sum()),
        "running_nonzero_fraction": float(np.mean(behavior[:, 2] > 0)),
        "pupil_std": float(np.std(behavior[:, 0])),
        "scores": values,
        "improvement_both_minus_stimulus": values["stimulus_plus_both"] - values["stimulus_only"],
        "relative_improvement_percent": (values["stimulus_plus_both"] / values["stimulus_only"] - 1) * 100,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
