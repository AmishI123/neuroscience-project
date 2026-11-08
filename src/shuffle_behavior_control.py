"""Negative-control experiment: shuffle behavior across trials per animal."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from replicate_mouse import fit_scores, load


def run(root: Path, permutations: int, seed: int) -> dict:
    images, responses, behavior, tiers = load(root)
    train = tiers == "train"
    held_out = (tiers == "validation") | (tiers == "test")
    image_scaler = StandardScaler().fit(images[train])
    pca = PCA(n_components=150, random_state=0).fit(image_scaler.transform(images[train]))
    stimulus = pca.transform(image_scaler.transform(images))
    aligned_behavior = StandardScaler().fit(behavior[train]).transform(behavior)
    aligned = float(np.nanmean(fit_scores(np.hstack([stimulus, aligned_behavior]), responses, train, held_out)))
    baseline = float(np.nanmean(fit_scores(stimulus, responses, train, held_out)))
    rng = np.random.default_rng(seed)
    shuffled_scores = []
    for _ in range(permutations):
        shuffled = behavior[rng.permutation(len(behavior))]
        shuffled_scaled = StandardScaler().fit(shuffled[train]).transform(shuffled)
        score = fit_scores(np.hstack([stimulus, shuffled_scaled]), responses, train, held_out)
        shuffled_scores.append(float(np.nanmean(score)))
    values = np.asarray(shuffled_scores)
    return {
        "mouse": root.name,
        "permutations": permutations,
        "seed": seed,
        "stimulus_only": baseline,
        "aligned_behavior": aligned,
        "aligned_gain": aligned - baseline,
        "shuffled_behavior_mean": float(values.mean()),
        "shuffled_behavior_sd": float(values.std(ddof=1)),
        "shuffled_gain_mean": float((values - baseline).mean()),
        "shuffled_gain_min": float((values - baseline).min()),
        "shuffled_gain_max": float((values - baseline).max()),
        "interpretation": "Negative control; shuffled behavior is not a population null distribution.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("roots", nargs="+", type=Path)
    parser.add_argument("--permutations", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20261108)
    parser.add_argument("--output", type=Path, default=Path("results/shuffled_behavior_controls.json"))
    args = parser.parse_args()
    results = [run(root, args.permutations, args.seed + index) for index, root in enumerate(args.roots)]
    args.output.parent.mkdir(exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2) + "\n")
    with args.output.with_suffix(".csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[key for key in results[0] if key != "interpretation"])
        writer.writeheader()
        writer.writerows([{key: value for key, value in row.items() if key != "interpretation"} for row in results])
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
