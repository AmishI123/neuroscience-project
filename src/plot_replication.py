"""Render the committed per-mouse replication summary."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "results" / "per_mouse_metrics.csv"
OUTPUT = ROOT / "results" / "per_mouse_replication_summary.png"


def main() -> None:
    with INPUT.open(newline="") as f:
        rows = list(csv.DictReader(f))
    labels = [row["mouse"][:12] for row in rows]
    stimulus = np.array([float(row["stimulus_only"]) for row in rows])
    both = np.array([float(row["stimulus_plus_both"]) for row in rows])
    gains = both - stimulus

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.3), constrained_layout=True)
    x = np.arange(len(rows))
    width = 0.36
    ax1.bar(x - width / 2, stimulus, width, label="stimulus only", color="#9bb8a5")
    ax1.bar(x + width / 2, both, width, label="+ behavior", color="#216b4c")
    ax1.set_title("Held-out correlation")
    ax1.set_ylabel("mean Pearson correlation")
    ax1.set_xticks(x, labels, rotation=25, ha="right")
    ax1.set_ylim(0, max(both) * 1.28)
    ax1.legend(frameon=False, fontsize=8)

    ax2.bar(x, gains, color="#d39a39")
    ax2.axhline(0, color="#17212b", linewidth=0.8)
    ax2.set_title("Behavior gain by mouse")
    ax2.set_ylabel("absolute correlation gain")
    ax2.set_xticks(x, labels, rotation=25, ha="right")
    ax2.set_ylim(0, max(gains) * 1.35)
    for i, value in enumerate(gains):
        ax2.text(i, value, f"+{value:.3f}", ha="center", va="bottom", fontsize=9)

    fig.suptitle("Sensorium visual-cortex replication", fontsize=13, fontweight="bold")
    fig.savefig(OUTPUT, dpi=180, bbox_inches="tight")
    print(OUTPUT)


if __name__ == "__main__":
    main()
