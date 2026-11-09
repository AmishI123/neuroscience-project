"""Pre-specified trial-offset sensitivity analysis for mouse behavior features.

This is an alignment-specific prediction experiment, not a causal timing test.
Raw Sensorium data are required; the summary CSV is not sufficient input.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from replicate_mouse import fit_scores, load


DEFAULT_OFFSETS = (-10, -5, -2, -1, 0, 1, 2, 5, 10)


def shift_behavior(behavior: np.ndarray, offset: int, fill: np.ndarray) -> np.ndarray:
    """Return behavior from source trial ``i - offset`` for target trial i."""
    shifted = np.broadcast_to(fill, behavior.shape).copy()
    if offset >= 0:
        if offset < len(behavior):
            shifted[offset:] = behavior[: len(behavior) - offset]
    else:
        lead = -offset
        if lead < len(behavior):
            shifted[: len(behavior) - lead] = behavior[lead:]
    return shifted


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--offsets", type=int, nargs="+", default=DEFAULT_OFFSETS)
    args = parser.parse_args()

    images, responses, behavior, tiers = load(args.root)
    train = tiers == "train"
    held_out = (tiers == "validation") | (tiers == "test")
    image_scaler = StandardScaler().fit(images[train])
    scaled_images = image_scaler.transform(images)
    pca = PCA(n_components=150, random_state=0).fit(scaled_images[train])
    stimulus = pca.transform(scaled_images)
    behavior_mean = behavior[train].mean(axis=0)
    results = []
    for offset in args.offsets:
        shifted = shift_behavior(behavior, offset, behavior_mean)
        scaled = StandardScaler().fit(shifted[train]).transform(shifted)
        scores = fit_scores(np.hstack([stimulus, scaled]), responses, train, held_out)
        results.append({
            "offset_trials": offset,
            "behavior_source": "i - offset_trials",
            "mean_held_out_correlation": float(np.nanmean(scores)),
            "neuron_count": int(len(scores)),
        })
    result = {
        "mouse": args.root.name,
        "offsets": list(args.offsets),
        "train_tiers": ["train"],
        "held_out_tiers": ["validation", "test"],
        "fill_policy": "training behavior mean for out-of-range shifted rows",
        "interpretation_boundary": "alignment-specific prediction sensitivity; not causal timing evidence",
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
