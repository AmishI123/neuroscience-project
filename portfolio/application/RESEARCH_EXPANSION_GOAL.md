# Research expansion goal

This is an extension of the existing ASDRP neuroscience portfolio objective.
The portfolio should continue growing after the first reviewer-ready release.

## New objective

Add more reproducible experiments and deeper analysis while preserving the
portfolio’s existing standards for held-out evaluation, collaboration credit,
and explicit uncertainty.

## First implementation tranche

1. **EEG blocked evaluation:** added five forward-chaining chronological folds to
   the EEG eye-state project. Compare pointwise EEG with causal temporal context
   on every fold, report fold-level ROC AUC and balanced accuracy, and retain the
   original final-block result rather than replacing it.
2. **Mouse cross-animal analysis:** add an animal-level summary of the three
   completed recordings, including per-animal gains, descriptive ranges, and a
   visualization. Do not pool neurons as independent animals or call the result
   a population estimate. The summary now also includes a leave-one-animal-out
   stability check; all three omitted-animal means remain positive.
3. **Next experiment queue:** identify additional recordings, alternative causal
   temporal windows, and pre-specified hierarchical uncertainty as follow-up
   experiments rather than silently changing the current claims. The first
   3/9/30/90-sample window sweep is now recorded as exploratory analysis.
4. **EEG label-shuffle control:** add 20 global label permutations evaluated
   with the same five forward-chaining folds. The shuffled means remain near
   chance (0.499 pointwise, 0.501 causal context), strengthening the negative
   result without implying subject-level generalization.
5. **EEG purge-gap sensitivity:** repeat the primary blocked evaluation with a
   90-sample gap before each test block. Mean AUC remains near or below chance
   (0.448 pointwise, 0.443 causal context), so the interpretation is not driven
   by immediately adjacent training samples.

## Completion evidence

- Source code and manifests are committed.
- Metrics are saved as machine-readable JSON/CSV.
- Reports and explainers state whether results are descriptive, predictive, or
  population-level.
- The reviewer audit checks the new outputs.
