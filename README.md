# neuro-research

A joint neuroscience + AI research project: **Does knowing what a mouse is *doing*
(running, arousal) help us predict what its visual cortex is *doing* — better than
using the image it sees alone?**

We build an **encoding model** of mouse visual cortex and test whether adding
**behavioral variables** (running speed, pupil size) improves how well we predict
neural activity, compared to using the visual stimulus alone.

## Open the notebooks in Colab (one click each)

> These open the notebook directly from GitHub. In Colab, do **File → Save a copy in
> Drive** the first time so your work is saved to your own account.

- Week 1 — Python & data: [Open in Colab](https://colab.research.google.com/github/AmishI123/neuroscience-project/blob/main/notebooks/01_python_and_data.ipynb)
- Week 2 — real data exploration: [Open in Colab](https://colab.research.google.com/github/AmishI123/neuroscience-project/blob/main/notebooks/02_real_data_exploration.ipynb)
- Week 3 — baseline model: [Open in Colab](https://colab.research.google.com/github/AmishI123/neuroscience-project/blob/main/notebooks/03_baseline_model.ipynb)
- Week 4 — add behavior (the result): [Open in Colab](https://colab.research.google.com/github/AmishI123/neuroscience-project/blob/main/notebooks/04_add_behavior.ipynb)
- Week 5 — analysis & figures: [Open in Colab](https://colab.research.google.com/github/AmishI123/neuroscience-project/blob/main/notebooks/05_analysis.ipynb)

📄 **Written report:** [`docs/REPORT.md`](docs/REPORT.md) — the paper-style summary (application attachment).

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

Notebooks 1–4 are written and **verified end-to-end on the real dataset**.
Checkboxes below track your daughter *completing* each one.

- [x] Project set up
- [ ] Week 1 — Python + data exploration &nbsp;· `notebooks/01_python_and_data.ipynb`
- [ ] Week 2 — real Sensorium data exploration &nbsp;· `notebooks/02_real_data_exploration.ipynb`
- [ ] Week 3 — baseline encoding model (Model A) &nbsp;· `notebooks/03_baseline_model.ipynb`
- [ ] Week 4 — add behavior (Model B), compare &nbsp;· `notebooks/04_add_behavior.ipynb`
- [ ] Week 5 — analysis + figures &nbsp;· `notebooks/05_analysis.ipynb`
- [x] Week 6 — write-up &nbsp;· `docs/REPORT.md` + figures in `results/`

## Headline result (verified on mouse `static21067`, 8,372 V1 neurons)

Adding behavior improves neural prediction: mean test correlation **0.126 → 0.158
(+25%)**, ~90% of neurons improved. The gain comes entirely from **pupil/arousal**,
not running (this mouse rarely ran) — and the **arousal-sensitive neurons benefit
most** (+0.069). An honest, self-consistent finding.
