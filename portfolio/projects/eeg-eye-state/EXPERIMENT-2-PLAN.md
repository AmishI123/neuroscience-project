# Experiment 2: brain-wave bands over time (plan, written before running)

**Question.** Alpha waves (8–13 cycles a second) grow when eyes close. Does a model that sees how
strong each brain-wave band has been over the last second hold up across the recording better than
the first study's model, which sees only the raw readings at one moment?

**Why it matters for the story.** Chapter 3 found that a raw-reading model drifts to a coin flip
within two minutes. If band strength is steadier, a sensor might be more useful than chapter 3
suggests. If it also drifts, the design rule "ask, don't guess" stands on firmer ground.

## Fixed before running

- **Data:** the same UCI EEG Eye State recording (14 sensors, 14,980 readings, about 128 a second).
- **Broken readings:** capped first, at the 0.5th and 99.5th percentile of each fold's learning
  rows only, exactly as in the first study's check. Band strength is very sensitive to spikes.
- **Band strength:** for every reading, the last 128 readings (one second, looking back only) of
  each sensor, with a Hann window and a Fourier transform. The log of the average power in four bands:
  delta 1–4, theta 4–8, alpha 8–13 and beta 13–30 cycles a second. The first 127 readings have no full
  second behind them and are left out of every model, so all models are scored on the same rows.
- **Models** (the same simple model as the first study: standardised features, balanced logistic regression):
  1. *Raw readings* at that moment (the first study's model, on the same rows), as the comparison.
  2. *All four bands*, 56 features. **This is the main test.**
  3. *Alpha only*, 14 features.
- **Test:** five stretches forward in time (scikit-learn `TimeSeriesSplit`, 5 splits), learning
  only from earlier readings. Because one-second windows overlap, a gap of 128 readings is left between
  learning and testing in the main result. Results without the gap are also reported.
- **Score:** AUC (0.5 is a coin flip, 1.0 is always right), averaged over the five stretches.
- **Check:** eyes-open and eyes-closed labels scrambled 20 times (seed 20261110) with the same
  folds; the bands model should then score about 0.5.
- **What counts as "holds up better":** the all-bands average with the gap is above the raw-readings
  average with the gap, **and** no stretch is below 0.5. Anything else is reported as "did not hold up".

Nothing here is tuned after seeing results. If something has to change, the change and the reason go
in the report next to the original plan.
