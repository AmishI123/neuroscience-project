# Neuroscience Lab mobile demo

This is a project-specific, responsive mobile experience built from the copied
Neurocomms and Neurodivergent interaction patterns: one focused task per screen,
large tap targets, explicit progress, plain-language result cards, and visible
scope limits.

It covers both portfolio studies:

- mouse visual cortex: stimulus-only versus behavior-augmented prediction;
- EEG eye state: pointwise baseline versus causal temporal context.

The “Print research card” control turns the selected result into a compact
presentation/application handout. It contains no participant data and makes no
clinical inference.

## Native path

`native/` is a Capacitor wrapper based on the copied Neurocomms mobile
configuration pattern. Its deterministic build copies the reviewed demo into a
Capacitor `dist/` directory. The Android debug APK build is verified; iOS build
and physical-device/runtime acceptance remain explicitly open in
`native/acceptance.md`.
