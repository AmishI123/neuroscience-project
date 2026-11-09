# Replication plan: behavioral state and mouse visual cortex

The report began as a complete one-mouse discovery analysis and now includes a
pre-specified three-mouse replication. It remains a replication result, not a
population-level claim.

## Primary question

Does adding pupil size and running speed improve held-out prediction of visual-cortex
activity across mice, and does the useful behavioral signal depend on the animal’s
actual behavior distribution?

## Pre-registered comparison

For every selected mouse, fit the same four models:

1. stimulus only;
2. stimulus + running;
3. stimulus + pupil variables;
4. stimulus + running + pupil variables.

Use the official train/validation/test split when available. Fit image PCA,
standardization, and regularization choices on training data only. Report per-neuron
Pearson correlation on the untouched test block.

## Primary outcomes

- Mean test correlation for each model.
- Per-neuron improvement over stimulus only.
- Fraction of neurons with positive improvement.
- Difference between pupil-only and running-only gains.

## Replication rules

- Choose mice before inspecting the outcome metrics.
- Preserve the same feature construction and alpha grid across animals.
- Report every selected animal, including failed or low-quality runs.
- Use a hierarchical summary rather than pooling neurons as if they were independent
  animals.
- Keep the current mouse as a named reference case, not as the population estimate.

## Required outputs

- `results/per_mouse_metrics.csv`
- `results/per_mouse_replication_summary.png` — per-mouse model comparison and
  behavior-gain distribution
- confidence interval or bootstrap procedure documented in code
- updated report section distinguishing replication from discovery
- `results/per_mouse_replication_summary.json` — descriptive animal-level gain
  summary without pooling neurons, including leave-one-animal-out stability
- `results/shuffled_behavior_controls.json` and `.csv` — 20 trial-shuffle
  negative-control fits per animal

## Current status

The protocol has been run on the named reference mouse and two additional mice.
The committed results live in `results/per_mouse_metrics.csv`, and the report
contains the cross-animal interpretation. The current evidence supports a
three-mouse replication result, not a population estimate. The current bootstrap
intervals are descriptive within-animal intervals; hierarchical uncertainty and
replication beyond three animals remain open.
