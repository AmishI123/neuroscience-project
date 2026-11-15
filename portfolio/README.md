# ASDRP Neuroscience Portfolio

An integrated portfolio of neuroscience research, human-centered neurotechnology,
and clear scientific communication.

## Portfolio thesis

We study how brain activity relates to behavior and build accessible tools that
help people understand and communicate complex experiences.

```text
scientific question -> experiment -> model -> interpretation -> usable tool -> public explanation
```

## Projects

### Research

- [Mouse visual cortex and behavioral state](research/mouse-visual-cortex.md) —
  Does pupil size and running behavior improve prediction of mouse V1 activity?
- [Complementary project: neural state and attention](research/neural-state-attention.md) —
  Completed EEG eye-state decoding study with a negative temporal-context result.
- [Future project: biological and artificial vision](research/biological-artificial-vision.md) —
  Planned comparison of neural and neural-network representations.

### Applied neurotechnology

- [Neurodivergent tools](applications/neurodivergent-tools.md) — accessibility,
  communication, and community-oriented applications.
- [Neurocomms](applications/neurocomms.md) — communication-focused neurotechnology
  and interface work.

### Communication

- [Presentation plan](communication/presentation-plan.md)
- [Video plan](communication/video-plan.md)
- [Portfolio roadmap](roadmap/ROADMAP.md)
- [ASDRP application package](application/README.md)

## Code and related work

- [AmishI123/neuroscience-project](https://github.com/AmishI123/neuroscience-project): the mouse visual-cortex analysis (notebooks, replication summary).
- [Next Step](https://next-step-live.onrender.com/) and [Helper Jobs](https://helper-jobs.onrender.com): the applied tools, linked as live apps (source: [AmishI123/next-step](https://github.com/AmishI123/next-step) and, for Helper Jobs, [AmishI123/neurocomms-app](https://github.com/AmishI123/neurocomms-app)). Both were built with AI coding tools, with advice and guidance from a parent..

This repository is the application-facing map that explains how the projects fit together.

## Website

**https://amishi123.github.io/neuroscience-project/** (GitHub Pages, published from `website/` by `.github/workflows/publish-site.yml`).

- [Landing page](website/index.html) · [Mouse study](website/mouse.html) · [EEG study](website/eeg.html) · [Tools for people](website/tools.html) · [Next experiments](website/next.html)
- The pages use the same stylesheets, icons and illustrations as Next Step and Helper Jobs (copied unchanged into `website/assets/`). Only the charts are new.
- `python3 website/build_results.py` rebuilds every number and chart from committed results; `python3 website/build_pages.py` rebuilds the pages.
- [Submission index](application/SUBMISSION_INDEX.md)

## Status

The mouse visual-cortex study is the flagship project, and the EEG eye-state study
is the completed complementary project. Planned tracks remain clearly labeled as
planned until they have a question, public data source, baseline, experiment,
limitations, and reproducible presentation.
