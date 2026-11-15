# Essay 5: Hands-on research (limit 375, max 3 examples)

Current draft. The source of truth is `final_drafts.md` in https://github.com/AmishI123/neuroscience-project/tree/main/application. Written from her own submitted answers; she should edit anything that does not sound like her.

---

I have not been part of a formal lab program yet, but I have done computational research on public biological datasets. Each project taught me something different about how to trust a result.

**1. Mouse visual cortex.** I did most of this project myself, with advice and guidance from my father, who has a software background. Using public recordings from thousands of neurons in mouse visual cortex, I asked whether a mouse's behavior, meaning pupil size and running, improves predictions of its neural activity beyond the image it saw. Adding behavior raised held-out prediction accuracy from 0.126 to 0.158 in the first mouse, and the result held in two more mice (0.154 to 0.203, and 0.143 to 0.191). Pupil-linked arousal helped all three, while running helped by very different amounts. I then tried to break the result. Shuffling behavior across trials erased the gain, and dropping any one mouse left it positive. That taught me a convincing result needs tests built to make it fail. It shows prediction, not cause, and three mice are not a population.

**2. Alzheimer's brain imaging.** Using a public imaging dataset, I built logistic regression and random forest classifiers to separate healthy scans from Alzheimer's scans. The random forest did much better, which told me a simple linear boundary was missing real structure. Preprocessing took more effort than the modeling.

**3. Sleep health data.** I wanted to know whether common claims about stress or steps held up in real data, starting from my own sleep habits. I ran correlations and trained a linear regression and a decision tree to predict sleep duration. Stress and age both correlated with sleep, but age also correlated with stress, so I read about confounding variables before trusting either.

These projects drew me toward molecular neuroscience, because the questions I care about, like how memory breaks down in Alzheimer's or what changes in neurons when a brain's state shifts, need experimental biology at the cellular level. Through ASDRP I want lab experience and mentorship, and to pair wet-lab work with the computational skills I have built.
