# Neural state from EEG: eye-state decoding

Completed complementary study using the public UCI EEG Eye State dataset.

## Question

Can a simple model classify open-eye versus closed-eye state from 14-channel EEG,
and does short-term temporal context improve held-out prediction?

## Result

The pointwise baseline reached test ROC AUC **0.625**. The first causal temporal
context extension reached **0.530**, so the added features did not generalize on the
final chronological test block. The negative result is part of the evidence: it
prevents us from treating a validation improvement as a final claim.

## Artifacts

- [Project README](../projects/eeg-eye-state/README.md)
- [Reproducible analysis](../projects/eeg-eye-state/src/analyze.py)
- [Report](../projects/eeg-eye-state/report.md)
- [Interactive explainer](../projects/eeg-eye-state/index.html)
- [Presentation outline](../projects/eeg-eye-state/presentation-outline.md)
- [Video script](../projects/eeg-eye-state/video-script.md)
