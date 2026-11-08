# Reproducibility run record

## Core environment

The core manifest in `requirements.txt` was installed into a fresh `virtualenv`
on 2026-11-08 with Python 3.12.3. The resolved packages included:

- numpy 2.5.4
- matplotlib 3.11.2
- scikit-learn 1.9.1

The optional CNN dependencies are intentionally separated into
`requirements-cnn.txt`; the linear-model replication does not require them.

## Replication command

```bash
python src/replicate_mouse.py \
  /path/to/static21067-10-18-GrayImageNet-94c6ff995dac583098847cfecd43e7b6 \
  --output /tmp/replication.json
```

The clean-environment run completed successfully. It reproduced the committed
reference values: stimulus-only mean held-out correlation `0.126480`,
stimulus-plus-both `0.158263`, and relative improvement `25.13%`.

The same clean environment also completed the three-mouse run with 200
deterministic neuron-level bootstrap resamples per model. The resulting
descriptive intervals are recorded in `results/per_mouse_metrics.csv`.

This record validates the core dependency installation, reference-mouse pipeline,
and current three-mouse replication. It does not replace hierarchical uncertainty
analysis or replication beyond three animals.
