# Essay 5: Hands-on / lab research experience (limit 375 words, max 3 examples)

> Replaces the earlier draft. Keeps her original three projects (sleep, Alzheimer's, mouse)
> and credits the collaboration honestly, so it matches `docs/REPORT.md`.
> Fill the one [bracket] with what she did versus what her father helped with. ~335 words.

---

I have not been part of a formal lab program yet, but I have done computational research on public biological datasets. Each project taught me something different about how to trust a result.

**1. Sleep health data.** I wanted to know whether common claims about stress or steps held up in real data, starting from my own sleep habits. In Python I ran correlations, plotted the relationships, and trained a linear regression and a decision tree to predict sleep duration. Stress and age both correlated with sleep, but age also correlated with stress, so I read about confounding variables before trusting either.

**2. Alzheimer's brain imaging.** Using a public imaging dataset, I built logistic regression and random forest classifiers to separate healthy scans from Alzheimer's scans. The random forest did much better, which told me a simple linear boundary was missing real structure. Preprocessing took more effort than the modeling.

**3. Mouse visual cortex (with my father).** My father has a software background, and we worked on this project together. [Describe exactly what she did and what he helped with.] Using public recordings from thousands of neurons in mouse visual cortex, I asked whether a mouse's behavior, meaning pupil size and running, improves predictions of its neural activity beyond the image it saw. Adding behavior raised held-out prediction accuracy from 0.126 to 0.158 in the first mouse, and the result held in two more mice (0.154 to 0.203 and 0.143 to 0.191). Pupil-linked arousal helped all three, while running helped by very different amounts, so the pattern repeated while its parts varied.

I also tested whether the result could be an accident. Shuffling behavior across trials erased the gain, and dropping any one mouse left it positive. I learned that a convincing result needs tests built to make it fail. It is a predictive result, not a causal one, and three mice are not a population.

These projects drew me toward molecular neuroscience, because the questions I care about, like how memory breaks down in Alzheimer's, need experimental biology at the cellular level. Through ASDRP I want lab experience and mentorship, and to pair wet-lab work with the computational skills I have built.
