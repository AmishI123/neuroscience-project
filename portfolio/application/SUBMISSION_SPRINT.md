# ASDRP submission sprint

This tracker starts the next end-to-end goal: turn the verified technical
portfolio into a genuinely applicant-ready submission.

## Baseline — complete

- Three-mouse visual-cortex replication, descriptive animal summary, and
  behavior-shuffle negative control are committed.
- EEG blocked folds and 3/9/30/90-sample temporal-window sweep are committed.
- Public portfolio Site is live and returns HTTP 200.
- Android APK, PDF packet, HTML demos, presentations, captioned videos, and
  release audit are present.

## Workstream 1 — applicant materials

- [ ] Fill `personalization-form.md` from verified memories and records.
- [ ] Replace the three essay placeholders with truthful first-person details.
- [ ] Complete the contribution ledger with exact applicant/collaborator boundaries.
- [ ] Rebuild and inspect the PDF packet after personalization.

## Workstream 2 — final media

- [ ] Record applicant narration for mouse, EEG, and portfolio overview.
- [ ] Mux narration into final MP4s with `mux_narration.py`.
- [ ] Review captions, spoken limitations, dataset credits, and collaboration credit.
- [ ] Publish the final narrated files only after voice review.

## Workstream 3 — optional scientific strengthening

- [ ] Add more mouse recordings and pre-specify hierarchical uncertainty.
- [ ] Add independent EEG recordings or a blocked multi-recording evaluation.
- [ ] Run iOS and physical-device acceptance where the required environments exist.

## Final gate

Run `python3 application/audit_portfolio.py`, inspect every public link, confirm
the essays contain no bracketed prompts, verify final media hashes, and have a
mentor/adult review the claims and contribution boundaries.
