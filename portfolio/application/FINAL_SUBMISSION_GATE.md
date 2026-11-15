# Final submission gate

Run this gate immediately before sending the ASDRP application.

## Technical verification

- [ ] Run `python3 application/audit_portfolio.py`; it must end with
  `PORTFOLIO AUDIT PASSED`.
- [ ] Run `python3 application/verify_public_release.py`; it must end with
  `PUBLIC RELEASE VERIFICATION PASSED`.
- [ ] Confirm the GitHub links in `SUBMISSION_INDEX.md` resolve to the intended
  branches and commits.
- [ ] Open the live HTML explainer, mobile demo, slide pages, PDF, and both MP4s
  on the device used for the application review.
- [ ] Confirm the reviewer packet and PDF use the same mouse values and EEG
  metrics as the committed results.

## Applicant-owned completion

- [ ] Replace every bracketed prompt in the essay drafts with verified personal
  details; remove the bracketed instructions afterward.
- [ ] Complete the contribution ledger in first-person language, preserving the
  parent/collaborator boundary.
- [ ] Record the applicant’s mouse and EEG narration WAV files using
  `communication/video/recording-kit.md`.
- [ ] Mux and review the final MP4s with
  `communication/video/mux_narration.py`.
- [ ] Add spoken dataset credits, collaboration credit, and limitations.

## Optional strengthening, not a prerequisite for honest submission

- [ ] Run iOS/Xcode and physical Android acceptance on available devices.
- [ ] Add more mouse recordings and replace the descriptive within-animal
  intervals with a pre-specified hierarchical population analysis.
- [ ] Add EEG recordings or blocked cross-validation.

Do not check an item based on intent. Each checked item should have an artifact,
command result, or recorded observation that can be shown to a reviewer.
