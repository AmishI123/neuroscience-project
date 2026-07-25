# Project Plan — Does Behavior Help Predict the Brain?

*A joint neuroscience + AI research project.*
*Last updated: 2026-07-24*

---

## The one-sentence version

**Does knowing what a mouse is *doing* (running, arousal) help us predict what its
visual cortex is *doing* — better than using the image it sees alone?**

---

## Why this question matters

When a mouse looks at an image, neurons in its visual cortex fire. For decades,
scientists have tried to build "encoding models" that predict this firing from the
image on the screen. But the brain is not a camera: the *same* image produces
*different* neural responses depending on the animal's **internal state** — whether
it's running, alert, or drowsy. Two behavioral signals capture a lot of this state:

- **Running speed** (locomotion is known to boost visual-cortex activity)
- **Pupil size** (a proxy for arousal / alertness)

Our project tests, on real recorded data, whether adding these behavioral signals
makes our predictions of neural activity measurably better — and if so, **which
neurons benefit most, and whether running or arousal matters more.**

This is a real, open-flavored question in systems neuroscience, not a toy exercise.

---

## Hypothesis

Adding behavioral variables (running speed + pupil size) to a stimulus-only encoding
model will **increase prediction accuracy** (correlation between predicted and actual
neural responses on held-out data). We expect:

1. A measurable overall improvement.
2. The improvement to be **uneven** across neurons — some neurons are strongly
   state-modulated, others barely.
3. Running and pupil to contribute **different** amounts (an empirical question we'll test).

---

## The approach (and why it's the *right* one for us)

We answer the question with a **ridge-regression encoding model** built in
`scikit-learn`, not a deep neural network.

**Why ridge regression, not deep learning:**
- Linear / ridge encoding models are **standard, published methodology** in sensory
  neuroscience — this is not a shortcut, it's a legitimate tool.
- Every line is **understandable and explainable** — which matters far more than
  raw accuracy for a research application and interview.
- It runs fast, even on modest hardware.

The scientific *question* is identical to the ambitious deep-learning version; only
the *tool* is simpler and more transparent. That is a feature, not a compromise.

### The two models we compare

| Model | Inputs | What it tests |
|-------|--------|---------------|
| **A — Baseline** | Visual stimulus features only | How well can we predict neurons from the image alone? |
| **B — Extended** | Stimulus features **+ behavior** (running, pupil) | Does adding behavior improve the prediction? |

We compare **A vs. B** using prediction accuracy (correlation) on a held-out
**test set** the model never trained on. The *difference* is the result.

### Metrics
- **Primary:** mean correlation between predicted and actual responses across neurons.
- **Secondary:** per-neuron improvement (Model B − Model A), to see *which* neurons benefit.
- **Ablation:** stimulus+running vs. stimulus+pupil, to see *which behavior* matters more.

---

## Data

**Primary dataset:** the **Sensorium 2022** dataset (mouse primary visual cortex).
Chosen because it ships as clean numpy arrays — neural responses to natural images,
*plus* the behavioral variables (pupil size, change in pupil size, running speed) —
so we spend our time on the science, not on wrestling a messy data API.

**Backup dataset:** the **Allen Brain Observatory** (via the AllenSDK), which also
contains visual-cortex activity together with running and pupil data.

*Data files are large and are NOT committed to git (see `.gitignore`). Notebooks
document how to download them.*

---

## Deliverables (what we'll have at the end)

1. **Clean, commented notebooks** (`notebooks/`) that anyone can read and re-run.
2. **A short written report** (3–5 pages, in `application/`) with figures — this
   becomes the **portfolio attachment** for the application.
3. **Figures** (`results/`) — the key plots (A vs. B, per-neuron improvement, etc.).
4. **(Stretch) A poster** summarizing the project.

The project also *is* the learning journey — Python, data analysis, and ML on a real
scientific problem — which is itself part of the application story.

---

## 6-Week Timeline (tuned for: new to Python, ~6 weeks, Colab Pro available)

| Week | Goal | Concrete output |
|------|------|-----------------|
| **1** | Python + numpy basics **on real data**; load and explore the dataset. | `01_python_and_data.ipynb`; first plots of neural + behavior data. |
| **2** | Understand the data deeply; learn scikit-learn with a tiny "predict from behavior only" warm-up. | `02_first_model.ipynb`; understand train/test split. |
| **3** | Build **Model A** — the stimulus-only baseline encoding model. | `03_baseline_model.ipynb`; baseline accuracy number. |
| **4** | Build **Model B** — add behavior; compare A vs. B. | `04_add_behavior.ipynb`; the core result. |
| **5** | Analyses: which neurons improve most? running vs. pupil? Make figures. | `05_analysis.ipynb`; figures in `results/`. |
| **6** | Write the report; assemble the application attachment; (stretch) poster. | Report in `application/`. |

*Scope discipline: if we're behind, we cut analyses and the poster first — a clean
A-vs-B result with a clear writeup is the non-negotiable core.*

---

## How this maps to the application essays

- **"Hands-on / research experience"** → this project, described concretely.
- **"Previous coursework / learning"** → the self-directed Python + ML + neuroscience
  learning journey documented in the notebooks.
- **"Papers / posters" upload** → the report (and stretch poster).
- **Preferred research field** → Cognitive Science & Psychology and/or Computer Science.

---

## Open questions / decisions to revisit

- Exact image-feature representation for Model A (raw downsampled pixels + PCA vs. a
  fixed pretrained feature extractor as a provided preprocessing step). Decide in Week 3.
- Whether to include a small deep-learning comparison as a Week-6 stretch.
