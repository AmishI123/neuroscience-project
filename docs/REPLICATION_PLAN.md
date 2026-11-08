# Replication plan: behavioral state and mouse visual cortex

The current report is a complete one-mouse analysis, not a population-level claim.
This document defines the next experiment before new data are inspected.

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
- per-mouse model-comparison figure
- distribution of per-mouse behavior gains
- confidence interval or bootstrap procedure documented in code
- updated report section distinguishing replication from discovery

## Current status

The protocol has been run on the named reference mouse and one additional mouse.
The committed results live in `results/per_mouse_metrics.csv`, and the report
contains the cross-animal interpretation. The current evidence supports a
two-mouse replication result, not a population estimate. Confidence intervals,
per-neuron distributions, and replication beyond two animals remain open.
