# Rendered research videos

The storyboard renderer creates silent, captioned MP4 review artifacts and matching
WebVTT transcript files from the verified project facts. They are useful for
checking pacing, visual hierarchy, and caption timing.

They are not being presented as final narrated videos. Before application use, add
the applicant’s own narration, collaboration credit, and a spoken limitations
section as specified in `application/video-production-plan.md`; the generated VTT
files provide the current caption/transcript starting point.

Render locally:

```bash
python3 communication/video/build_storyboard.py mouse
python3 communication/video/build_storyboard.py eeg
```
