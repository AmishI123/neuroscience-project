# Neuroscience Lab mobile builds

`neuroscience-lab-debug.apk` is a debug Android build produced from the
committed Capacitor project. It is a reviewer/development artifact, not a store
release. Its SHA-256 checksum is recorded in `native/acceptance.md`.

The iOS project is generated under `native/ios/`, but an iOS build requires
macOS/Xcode and has not been claimed here.

> **Update, November 2026:** the phone tour was rebuilt as the five chapters of *From neurons to next steps*. The Android app is now rebuilt by GitHub Actions (`.github/workflows/phone-tour-android.yml`) whenever the tour changes, and the current SHA-256 is in `communication/projects/neuroscience-mobile/releases/SHA256.txt`. The checksum above belongs to the earlier build.
