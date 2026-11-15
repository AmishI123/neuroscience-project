# EEG eye state: can temporal context reveal a brain state?

## Research question

Can a simple, interpretable model classify whether a person’s eyes are open or
closed from 14-channel EEG, and does short-term temporal context improve the
prediction beyond the instantaneous EEG sample?

## Dataset

This project uses the UCI **EEG Eye State** dataset (Roesler, 2013): one continuous
117-second recording with 14 EEG values and a manually annotated binary eye-state
label. The repository keeps the downloaded ARFF file under `data/raw/` for
reproducibility. Dataset details and citation are on the [official UCI page](https://archive.ics.uci.edu/dataset/264/eeg%2Beye%2Bstate).

## Experiment

- **Baseline:** standardized 14-channel EEG at each time point.
- **Extended model:** the same EEG plus causal trailing mean and standard deviation
  over a nine-sample window.
- **Model:** class-balanced logistic regression.
- **Evaluation:** chronological 70% train / 15% validation / 15% test split. No
  random row split is used because this is one time series. The analysis also
  reports five forward-chaining `TimeSeriesSplit` folds as a robustness check
  and a 20-permutation global label-shuffle control using those same folds.
  It also reports a 90-sample purge-gap sensitivity check before each test block.
- **Metrics:** ROC AUC, balanced accuracy, and F1 on the held-out test block.

Run:

```bash
python3 -m pip install -r requirements.txt
python3 src/analyze.py
```

The project keeps its own small dependency manifest so the complementary study
can be reproduced independently of the flagship project.

## Interpretation boundary

This is a proof-of-method study on one continuous recording. It demonstrates
time-aware neural-signal modeling; it does not diagnose sleep, attention, or any
medical condition, and it does not establish generalization to new people.

## Experiment 2: brain-wave bands (follow-up)

Plan written before running: [`EXPERIMENT-2-PLAN.md`](EXPERIMENT-2-PLAN.md). Code: `src/analyze_bands.py`. Results: `results/bands.json`.
Bands averaged 0.566 across five forward stretches against 0.481 for raw readings, but two stretches stayed just below a coin flip, so by the rule set beforehand it did not hold up. Details in [`report.md`](report.md).
