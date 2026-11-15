# Reproducibility checklist

## Mouse visual-cortex study

- [x] Public repository with six notebooks
- [x] Dataset source documented in the report
- [x] Training-only preprocessing described
- [x] Baseline and behavior-augmented models defined
- [x] Held-out evaluation reported
- [x] Replication across two additional mice (three evaluated animals total)
- [x] Core dependency manifest added (`neuroscience-project/requirements.txt`)
- [x] Automated clean-environment run from that manifest
- [x] Descriptive within-animal bootstrap intervals (population-level CI remains open)
- [x] Descriptive animal-level gain summary without pooling neurons
- [x] Behavior-shuffle negative control (20 permutations per animal)

## EEG eye-state study

- [x] Public UCI dataset downloaded and provenance documented
- [x] Raw ARFF file retained in `data/raw/`
- [x] Chronological split specified in code and report
- [x] Baseline and extension implemented
- [x] Held-out metrics saved in `results/metrics.json`
- [x] Negative result documented rather than discarded
- [x] Five-fold forward-chaining blocked cross-validation analysis (additional recordings remain open)
- [x] Project dependency manifest (`projects/eeg-eye-state/requirements.txt`)
- [x] Clean-environment analysis run documented
- [x] Five-fold forward-chaining blocked analysis
- [x] Pre-specified exploratory temporal-window sweep (3/9/30/90 samples)
- [x] Global label-shuffle negative control (20 permutations per EEG model)

## Communication artifacts

- [x] Interactive HTML explainers
- [x] Mobile interaction specifications
- [x] Working responsive mobile research demo
- [x] Capacitor native wrapper scaffolded
- [x] Android debug APK build verified
- [x] Android/iOS device acceptance runbook documented
- [ ] iOS build and Android/iOS device acceptance execution
- [x] Presentation outlines
- [x] Video scripts
- [x] Scope and limitations notes
- [ ] Recorded final videos
- [x] Final exported ASDRP PDF packet
