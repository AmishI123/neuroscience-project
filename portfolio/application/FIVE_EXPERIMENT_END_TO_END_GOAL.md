# Five-experiment ASDRP neuroscience goal

## Objective

Build one coherent, reproducible research portfolio spanning five experiments.
Every experiment must move through the same chain:

`question → pre-specified analysis → held-out evaluation → negative/control tests → interpretation → report → web/mobile artifact → presentation → captioned video → release audit`

The portfolio must distinguish completed results from planned work, preserve
collaboration boundaries, and never turn a small dataset into a population claim.

## Experiments

### 1. Mouse behavior timing and alignment

Question: does behavior from the same trial predict neural activity better than
behavior shifted to neighboring trials?

Plan: compare aligned behavior with pre-specified trial offsets, using the same
stimulus-only baseline, the same held-out tiers, and the same training-only
standardization. Use behavior shuffles as a negative control. Interpret this as
alignment-specific prediction, not causal timing evidence.

Dependency: the raw Sensorium mouse directories are not committed; the existing
three-mouse summary is not sufficient to rerun this experiment.

### 2. EEG frequency-band representation

Question: do interpretable frequency-band features improve time-aware eye-state
prediction over the raw 14-channel representation?

Plan: define band features before evaluation, use chronological folds and the
90-sample purge gap, retain the label-shuffle control, and report ROC AUC,
balanced accuracy, F1, and calibration. Do not select a winning representation
from the final test block.

### 3. Mouse neuron-subgroup analysis

Question: is the behavior gain distributed across neurons or concentrated in
predefined spatial/depth subgroups?

Plan: define subgroups from metadata before inspecting gains, preserve each
animal as the unit of replication, report subgroup counts and uncertainty, and
avoid treating neurons as independent animals.

Dependency: raw responses and neuron metadata are required for a new run.

### 4. EEG concept drift across time

Question: how stable is eye-state prediction across chronological blocks?

Plan: report fold-by-fold AUC, balanced accuracy, calibration, and direction of
error; compare pointwise and context models without random row splitting. Keep
the existing near-chance blocked result and purge-gap result visible.

### 5. Human-centered usability study

Question: do the Neurocomms/Neurodivergent interaction patterns make the
neuroscience explainers easier to navigate and understand?

Plan: preregister tasks and measures, recruit only with appropriate consent,
avoid collecting unnecessary personal data, and report completion, errors, and
qualitative accessibility findings. This study cannot be claimed complete from
repository inspection alone.

## Acceptance criteria

- Each completed experiment has code, machine-readable results, a reproducible
  run record, limitations, and a reviewer-facing artifact.
- Each public claim is traceable to a committed result and its control analysis.
- The dashboard, PDF, presentations, captions, and release verifier agree on
  scope and numbers.
- Human-subject and applicant-owned work is never fabricated or silently marked
  complete.
