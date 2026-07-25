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
from scratch, then loaded the Sensorium 2022 dataset — recordings of 8,372 neurons
across roughly 6,000 trials, along with the mouse's pupil size and running speed. I first
explored the data and measured how each neuron's activity related to behavior, and found
that arousal (pupil) tracked neural activity while running did not — because the mouse
ran in only 5% of trials.

I then built two prediction models using ridge regression: a baseline using only the
image the mouse saw, and an extended model that also included behavior. I evaluated both
on held-out test trials by correlating predicted and actual responses. Adding behavior
raised mean prediction accuracy from 0.126 to 0.158 — about 25% — and improved roughly
90% of neurons. Using an ablation, I showed the improvement came entirely from arousal,
not movement, and that the arousal-sensitive neurons benefited most.

What I accomplished: a complete, reproducible analysis — documented in notebooks and a
short write-up — answering a real question (internal state improves models of visual
cortex) using transparent methods I can fully explain. Most importantly, I learned to
let the data change my mind.

**2. [Other hands-on experience — what you did, with whom, your tasks, what you
accomplished.]**

**3. [Another example, if you have one.]**
