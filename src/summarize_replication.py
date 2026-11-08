"""Create a descriptive animal-level summary without pooling neurons."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "results" / "per_mouse_metrics.csv"
OUTPUT = ROOT / "results" / "per_mouse_replication_summary.json"


def summary(values: list[float]) -> dict[str, float]:
    array = np.asarray(values, dtype=float)
    return {
        "mean": float(array.mean()),
        "median": float(np.median(array)),
        "sd_sample": float(array.std(ddof=1)) if len(array) > 1 else 0.0,
        "min": float(array.min()),
        "max": float(array.max()),
    }


def main() -> None:
    with INPUT.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    gains = [float(row["improvement_both_minus_stimulus"]) for row in rows]
    relative = [float(row["relative_improvement_percent"]) for row in rows]
    result = {
        "animal_count": len(rows),
        "unit_of_summary": "animal; neurons are not pooled as independent animals",
        "animals": [
            {
                "mouse": row["mouse"],
                "stimulus_only": float(row["stimulus_only"]),
                "stimulus_plus_both": float(row["stimulus_plus_both"]),
                "absolute_gain": float(row["improvement_both_minus_stimulus"]),
                "relative_gain_percent": float(row["relative_improvement_percent"]),
            }
            for row in rows
        ],
        "absolute_gain_summary": summary(gains),
        "relative_gain_percent_summary": summary(relative),
        "interpretation": "Descriptive three-animal summary; not a population estimate or hierarchical confidence interval.",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
