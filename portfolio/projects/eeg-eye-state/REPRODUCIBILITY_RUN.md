# EEG reproducibility run

On 2026-11-08, a fresh virtual environment was created and installed from
`requirements.txt`. The resolved core versions were NumPy 2.5.4, SciPy 1.18.1,
and scikit-learn 1.9.1.

Running `python src/analyze.py` reproduced the committed metrics:

| Model | Test ROC AUC |
|---|---:|
| Pointwise EEG | 0.6252065 |
| EEG + causal temporal context | 0.5296496 |

The run uses the retained ARFF file, the chronological 70/15/15 split, and no
random row shuffling. It also writes five forward-chaining blocked-fold results
under `blocked_cross_validation` in `results/metrics.json`; mean ROC AUC is 0.478
for pointwise EEG and 0.488 for causal context. This is still one continuous
recording, not evidence of generalization to new participants. The same file also
contains the exploratory 3/9/30/90-sample temporal-window sweep.

The same run now adds a pre-specified label-shuffle negative control: 20 global
permutations of the eye-state labels, evaluated with the same five forward-
chaining folds. The mean shuffled ROC AUC is 0.499 (pointwise) and 0.501
(causal context), with ranges 0.491–0.508 and 0.491–0.512. These values are
consistent with chance and are a control result, not evidence of independent-
participant generalization.

Finally, a 90-sample purge gap was inserted before every forward test block, equal
to the largest exploratory context window. Mean ROC AUC was 0.448 for pointwise
EEG (range 0.288–0.572) and 0.443 for causal context (range 0.254–0.582). The
gap sensitivity remains near or below chance and does not reverse the study's
negative interpretation; it is still one continuous recording.

## Recording-glitch sensitivity (added 2026-11-10)

Four samples (rows 898, 10386, 11509 and 13179) are recording glitches: values up to
715,897 where typical readings are about 4,000 (more than 20 robust standard
deviations from each channel's median). The primary analysis above does not treat them
specially, and its results are left unchanged.

`artifact_sensitivity` in `results/metrics.json` repeats the main comparisons after
limiting each channel to the 0.5th–99.5th percentile of the **training rows only**
(recomputed for every fold), so test rows never influence the limits. This analysis was
added after the first results were seen, so it is reported as a sensitivity check, not as
a replacement:

| | Pointwise EEG | EEG + causal context |
|---|---:|---:|
| Final holdout ROC AUC | 0.728 (was 0.625) | 0.609 (was 0.530) |
| Mean blocked-fold ROC AUC | 0.448 (was 0.478) | 0.476 (was 0.488) |

Limiting the glitches helps the final holdout block, but the five forward folds stay near
or below chance, and several folds are well below 0.5. That pattern points to the
relationship between the signal and eye state changing across the 117-second recording
(drift), not only to noise.

Rerun environment: Python 3.13, NumPy 2.5.3, SciPy 1.18.1, scikit-learn 1.9.1. The
committed primary values were reproduced to three decimals except the causal-context
model’s fifth blocked fold (0.535 here vs 0.534 committed), a small numerical
difference between NumPy 2.5.3 and 2.5.4; the committed primary values are kept.
