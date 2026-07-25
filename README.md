# neuro-research

A joint neuroscience + AI research project: **Does knowing what a mouse is *doing*
(running, arousal) help us predict what its visual cortex is *doing* — better than
using the image it sees alone?**

We build an **encoding model** of mouse visual cortex and test whether adding
**behavioral variables** (running speed, pupil size) improves how well we predict
neural activity, compared to using the visual stimulus alone.

## Where things live

| Folder | What's in it |
|--------|--------------|
| `docs/` | The project plan and notes. **Start with [`docs/PROJECT_PLAN.md`](docs/PROJECT_PLAN.md).** |
| `notebooks/` | The Jupyter/Colab notebooks — this is where the work happens, week by week. |
| `data/` | Datasets (downloaded locally; not committed to git). |
| `src/` | Reusable Python helper code. |
| `results/` | Figures and outputs. |
| `application/` | The written report and application materials. |

## The approach in one line

A **ridge-regression encoding model** (`scikit-learn`) — standard, transparent
neuroscience methodology — comparing a **stimulus-only** model against a
**stimulus + behavior** model on held-out data.

## Status

- [x] Project set up
- [ ] Week 1 — Python + data exploration
- [ ] Week 2 — first model (scikit-learn warm-up)
- [ ] Week 3 — baseline encoding model (Model A)
- [ ] Week 4 — add behavior (Model B), compare
- [ ] Week 5 — analysis + figures
- [ ] Week 6 — write-up
