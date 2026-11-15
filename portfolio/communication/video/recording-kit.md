# Research video recording kit

This kit turns the verified storyboard videos into submission-ready narrated
videos without changing the scientific claims. The applicant records the voice;
the repository supplies the visuals, captions, timing, and source scripts.

## Recording specification

- Record one mono WAV per project at 48 kHz, 16-bit PCM.
- Use a quiet room, keep the microphone 15–20 cm away, and leave 0.5 seconds of
  silence at the beginning and end.
- Read one storyboard card per four-second visual card. The generated MP4s are
  24 seconds long; pause naturally rather than compressing the limitations.
- State that the mouse results are predictive, not causal, and that three mice
  do not establish population generalization.
- State that the EEG result is a single-recording proof of method and that the
  temporal-context extension did not improve the final chronological test.
- Credit the public datasets, the source repositories, and any collaborators or
  prior project work accurately. Do not imply sole authorship where it is not
  true.

## Mouse narration cue sheet

1. “This project asks whether behavioral state helps predict visual-cortex
   activity from natural images.”
2. “The analysis evaluates three Sensorium recordings with neural responses,
   pupil measurements, and running speed.”
3. “I compare a stimulus-only ridge model with a model that adds behavior, using
   the same held-out protocol and training-only preprocessing.”
4. “Mean held-out correlation changes from 0.126 to 0.158, from 0.154 to 0.203,
   and from 0.143 to 0.191 across the three evaluated mice.”
5. “Pupil improves all three in this analysis, while the running contribution
   varies across animals. This is predictive evidence, not causal evidence.”
6. “Three animals are not a population. The next test is replication beyond
   three animals with population-level uncertainty.”

## EEG narration cue sheet

1. “This complementary project asks whether short-term history helps decode an
   eye-state label from a public 14-channel EEG recording.”
2. “The data are one continuous recording with a chronological train,
   validation, and final test split.”
3. “The baseline uses pointwise standardized EEG and class-balanced logistic
   regression; the extension adds only causal temporal context.”
4. “The pointwise baseline reaches test ROC AUC 0.625.”
5. “The temporal-context extension reaches 0.530 on the final chronological
   block, despite looking better during validation.”
6. “The negative result is retained. More recordings and blocked evaluation are
   needed before making a broader claim.”

## Muxing the applicant’s recording

After recording `mouse-narration.wav` or `eeg-narration.wav`, run:

```bash
python3 communication/video/mux_narration.py mouse mouse-narration.wav
python3 communication/video/mux_narration.py eeg eeg-narration.wav
```

The command writes a normalized MP4 beside the storyboard render and refuses
to overwrite an existing final file. Review the result with captions enabled,
then copy the final MP4 and matching VTT into the website only after the
applicant confirms the voice, credits, and spoken limitations.
