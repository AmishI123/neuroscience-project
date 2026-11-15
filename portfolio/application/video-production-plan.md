# Video production plan

## Video 1 — Portfolio overview (2 minutes)

The verified visual storyboard is `communication/video/renders/portfolio-research-storyboard.mp4`;
the final narrated version still requires the applicant’s voice.

- 0:00–0:20: brain, behavior, and communication thesis
- 0:20–0:55: mouse visual-cortex experiment
- 0:55–1:20: EEG complementary study and negative result
- 1:20–1:45: neuro-divergent and Neurocomms translation layer
- 1:45–2:00: ASDRP goals and next experiments

## Video 2 — Flagship research walkthrough (5 minutes)

Use `communication/projects/mouse-visual-cortex/video-script.md`. Record the
interactive explainer, then show the report and notebook evidence.

## Video 3 — Complementary-study walkthrough (3 minutes)

Use `projects/eeg-eye-state/video-script.md`. Show the chronological split and make
the validation/test divergence visible.

## Production gate

Before calling a video complete:

- narrator uses the applicant’s own voice;
- every number shown matches the committed report or metrics file;
- collaboration is credited;
- limitations are spoken, not hidden in a footer;
- captions/transcript are included;
- final MP4 and source script are stored together.

The executable handoff is in `communication/video/recording-kit.md`; after the
applicant records a WAV, `communication/video/mux_narration.py` creates the
final narrated MP4 without altering the verified storyboard visuals.
