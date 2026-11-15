# ASDRP application package

This folder is the reviewer-facing index for the portfolio. It separates verified
project evidence from personal statements that still require the applicant’s own
voice and experiences.

## Recommended review path

1. Start with the [flagship mouse visual-cortex study](../research/mouse-visual-cortex.md).
2. Open the [interactive mouse explainer](../projects/mouse-visual-cortex/index.html).
3. Read the [EEG complementary study](../projects/eeg-eye-state/report.md).
4. Compare the [research contribution ledger](contribution-ledger.md) with the
   notebooks and scripts.
5. Use the [reproducibility checklist](reproducibility-checklist.md) to rerun the
   analyses.
6. Review the [application essay map](essay-map.md).
7. Use the [submission index](SUBMISSION_INDEX.md) for the complete live-artifact
   handoff, including the mobile build, presentations, videos, and PDF.

For a printable summary, use the [generated reviewer packet PDF](ASDRP-neuroscience-portfolio-packet.pdf).
The PDF is printed from the website itself by `build_packet_from_site.py`, so it has the same design, charts and numbers (the older text-only generator `build_packet.py` is kept for reference).

Run `python3 application/audit_portfolio.py` for the dependency-free handoff
audit covering required artifacts, three-mouse claims, EEG outputs, video files,
and the verified Android APK hash.
After a Site deployment, run `python3 application/verify_public_release.py` to
verify public routes and the live PDF hash.

## Existing drafts

- [Current essay drafts (all prompts)](https://github.com/AmishI123/neuroscience-project/blob/main/application/final_drafts.md)
- [Her submitted answers](https://github.com/AmishI123/neuroscience-project/blob/main/application/submitted_answers.md)
- [Story sketch](https://github.com/AmishI123/neuroscience-project/blob/main/application/story_sketch.md)

Use [personalization-form.md](personalization-form.md) to replace the remaining
bracketed prompts with verified applicant-specific details.

These drafts contain bracketed personal prompts. They must be personalized before
submission; the portfolio does not present invented experiences as fact.
