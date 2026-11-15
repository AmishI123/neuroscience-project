# Mouse visual cortex and behavioral state

## Question

Does knowing what a mouse is doing—especially its arousal and locomotion—help us
predict activity in visual cortex beyond the visual stimulus alone?

## Current result

Using Sensorium 2022 recordings and a transparent ridge-regression encoding model,
the original mouse rises from **0.126** for a stimulus-only model to **0.158** when
behavior is added; two replications rise from **0.154** to **0.203** and from
**0.143** to **0.191** under the same pipeline. Pupil improves all three animals,
while the running contribution varies by animal. These are predictive results, not
causal evidence.

## Next experiments

- Repeat the analysis across additional mice beyond the three already evaluated.
- Compare animals with different amounts of running behavior.
- Use the descriptive animal-level gain summary without pooling neurons.
- Check leave-one-animal-out stability before interpreting the mean gain.
- Extend beyond three animals before attempting hierarchical population uncertainty.
- Separate exploratory analysis from confirmatory evaluation.
- Document preprocessing and possible leakage risks.
- Compare pixel, PCA, and CNN feature representations.
- Run the committed behavior-shuffle negative control before interpreting added
  behavior features as aligned signal.

The flagship repository now includes a pinned core dependency manifest and a formal
[replication protocol](https://github.com/AmishI123/neuroscience-project/blob/main/docs/REPLICATION_PLAN.md).
The current descriptive cross-animal summary is in
[`per_mouse_replication_summary.json`](https://github.com/AmishI123/neuroscience-project/blob/main/results/per_mouse_replication_summary.json).

## Displayable artifacts

- Neuron explorer
- Stimulus-only versus behavior-enhanced model dashboard
- Cortical spatial map
- Research report
- Five-minute presentation and short video

Implementation: [AmishI123/neuroscience-project](https://github.com/AmishI123/neuroscience-project)
