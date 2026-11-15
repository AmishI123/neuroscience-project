"""Writes website/assets/results.js: every number the website shows, taken from committed results.

EEG numbers come from projects/eeg-eye-state/results/metrics.json (rerun with src/analyze.py).
Mouse numbers are the committed three-animal summary from the flagship repository
(AmishI123/neuroscience-project, results/per_mouse_replication_summary.json); they are copied
here so the website can be checked without that repository. Run: python3 website/build_results.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
metrics = json.loads((ROOT / "projects/eeg-eye-state/results/metrics.json").read_text())

MOUSE = {
    "source": "AmishI123/neuroscience-project · results/per_mouse_replication_summary.json",
    "dataset": "Sensorium 2022 (static image responses, mouse primary visual cortex)",
    "model": "4×4 image downsampling, 150-component PCA, training-only standardization, ridge regression, official held-out tiers",
    "metric": "mean held-out Pearson correlation across neurons",
    "mice": [
        {"id": "Original mouse", "code": "static21067", "stimulus": 0.126, "behavior": 0.158, "gain": 0.0318},
        {"id": "Second mouse", "code": "static22846", "stimulus": 0.154, "behavior": 0.203, "gain": 0.0491},
        {"id": "Third mouse", "code": "static23343", "stimulus": 0.143, "behavior": 0.191, "gain": 0.0474},
    ],
    "leave_one_out_mean_gain": [
        {"omit": "Original mouse", "gain": 0.0482},
        {"omit": "Second mouse", "gain": 0.0396},
        {"omit": "Third mouse", "gain": 0.0404},
    ],
    "behavior_shuffle": "20 behavior shuffles per animal give near-zero gains; aligned gains stay positive",
    "ablation": "Pupil improves all three animals; the running contribution varies by animal",
}

r3 = lambda v: round(float(v), 3)
blocked = {m["model"]: [r3(f["test_roc_auc"]) for f in m["folds"]] for m in metrics["blocked_cross_validation"]}
gap = {m["model"]: [r3(f["test_roc_auc"]) for f in m["folds"]] for m in metrics["blocked_gap_sensitivity"]}
art = metrics["artifact_sensitivity"]
EEG = {
    "source": "projects/eeg-eye-state/results/metrics.json",
    "dataset": {"samples": metrics["dataset"]["samples"], "channels": len(metrics["dataset"]["channels"]),
                "closed_fraction": r3(metrics["dataset"]["eye_closed_fraction"]), "seconds": 117},
    "holdout": [{"model": m["model"], "auc": r3(m["test_roc_auc"]), "balanced_accuracy": r3(m["test_balanced_accuracy"]),
                 "validation_auc": r3(m["validation_roc_auc"])} for m in metrics["models"]],
    "folds": {"pointwise": blocked["pointwise EEG"], "context": blocked["EEG + causal temporal context"]},
    "gap_folds": {"pointwise": gap["pointwise EEG"], "context": gap["EEG + causal temporal context"]},
    "fold_means": {m["model"]: r3(m["summary"]["mean_test_roc_auc"]) for m in metrics["blocked_cross_validation"]},
    "gap_means": {m["model"]: r3(m["summary"]["mean_test_roc_auc"]) for m in metrics["blocked_gap_sensitivity"]},
    "shuffle": [{"model": m["model"], "mean": r3(m["mean_test_roc_auc"]), "min": r3(m["min_test_roc_auc"]), "max": r3(m["max_test_roc_auc"]),
                 "permutations": m["permutations"]} for m in metrics["blocked_label_shuffle_control"]],
    "windows": [{"window": w["window_samples"], "holdout": r3(w["final_holdout"]["test_roc_auc"]),
                 "blocked": r3(w["blocked_summary"]["mean_test_roc_auc"])} for w in metrics["temporal_window_sweep"]],
    "glitches": {"rows": art["extreme_sample_indices"],
                 "holdout": [r3(m["test_roc_auc"]) for m in art["final_holdout"]],
                 "folds": {"pointwise": [r3(v) for v in art["blocked_cross_validation"][0]["fold_test_roc_auc"]],
                           "context": [r3(v) for v in art["blocked_cross_validation"][1]["fold_test_roc_auc"]]},
                 "means": [r3(m["summary"]["mean_test_roc_auc"]) for m in art["blocked_cross_validation"]]},
}
# The first mouse in more detail, from Amishi's saved results (results/summary_stats.npz) and her report
# (docs/REPORT.md, section 4.3, for the arousal-sensitive split). Copied here so the site can draw them.
MOUSE["first_mouse"] = {
    "ablation": {"Picture only": 0.126, "+ running": 0.127, "+ pupil": 0.158, "+ both": 0.158},
    "fraction_improved": 0.899, "median_gain": 0.017, "mean_gain": 0.032, "max_gain": 0.355,
    "follow_pupil_gain": 0.069, "follow_pupil_cells": 2750, "other_gain": 0.014,
    "best_cell": {"id": 3035, "picture_only": 0.049, "with_state": 0.404},
    "source": "AmishI123/neuroscience-project · results/summary_stats.npz and docs/REPORT.md",
}
# Experiment 2 (brain-wave bands), from projects/eeg-eye-state/results/bands.json (src/analyze_bands.py).
bands = json.loads((ROOT / "projects/eeg-eye-state/results/bands.json").read_text())
EEG["bands"] = {"with_gap": {k: {"stretches": [r3(v) for v in d["stretches"]], "mean": r3(d["mean"]), "below": d["stretches_below_coin_flip"]} for k, d in bands["with_gap"].items()},
                "without_gap_mean": {k: r3(d["mean"]) for k, d in bands["without_gap"].items()},
                "shuffle_mean": r3(bands["label_shuffle_all_bands_with_gap"]["mean"]), "holds_up_better": bands["holds_up_better"]}
out = ROOT / "website/assets/results.js"
out.write_text("// Generated by website/build_results.py from committed results. Do not edit by hand.\n"
               f"window.PortfolioResults = {json.dumps({'mouse': MOUSE, 'eeg': EEG}, indent=1, ensure_ascii=False)};\n")
print("wrote", out.relative_to(ROOT))
