# Essay 5 — Hands-on science / lab research experience (limit: 375 words, max 3 examples)

> **DRAFT to personalize.** Example 1 (our project) is written for you and is truthful.
> Add examples 2–3 if you have them (a school lab, summer program, science fair, etc.).
> Being honest that this was a joint project with your father is the right call — ASDRP
> values integrity, and a self-started project is impressive regardless. ≈ 300 words;
> you have room to add more.

---

**1. Predicting neural activity from behavior (independent project, collaborating with
my father).** This is the project I've worked on most closely. My father has a software
background, and together we set out to test whether a mouse's behavior helps predict how
its visual-cortex neurons respond to images.

My specific tasks: I learned Python and its scientific libraries (numpy, scikit-learn)
from scratch, then loaded Sensorium 2022 recordings — thousands of visual-cortex
neurons across roughly 6,000 trials per animal, along with pupil size and running speed.
I first explored the data and measured how neural activity related to behavior. Pupil
linked to the prediction improvement in both evaluated animals, while the running
contribution varied; in the first mouse, running appeared on only about 5% of trials.

I then built two prediction models using ridge regression: a baseline using only the
image the mouse saw, and an extended model that also included behavior. I evaluated both
on held-out test trials by correlating predicted and actual responses. Adding behavior
raised mean prediction accuracy from 0.126 to 0.158 in the first mouse and from 0.154
to 0.203 in a second mouse. Using an ablation, I found that pupil-linked arousal
improved both animals, while movement contributed differently across them. The
replication strengthened the predictive claim without turning it into a causal claim.

What I accomplished: a complete, reproducible analysis — documented in notebooks and a
short write-up — answering a real question (internal state improves models of visual
cortex) using transparent methods I can fully explain. Most importantly, I learned to
let the data change my mind.

**2. [Other hands-on experience — what you did, with whom, your tasks, what you
accomplished.]**

**3. [Another example, if you have one.]**
