# Native validation: waiting for working test environments

Recorded 2026-09-16 UTC. The full Android/iOS goal is not complete.
This record supersedes the older live-process notes in progress.md.

Update after the user could not supply hardware: hosted tests are prepared for
the existing private GitHub account, but upload/run approval is still pending.
Local WebKit now passes seven journey stages and fails full offline restart;
online recovery retains the saved notes. See `remote-testing-plan.md` and
`qa/webkit-journey.json`. The shared test-navigation helper was corrected; the
full Chromium regression has now finished successfully. All 288 source checks
have matching current hashes and no reported browser errors. The archive below
has been rebuilt and its extracted workflow passed after the test-helper change.
Neither source checks nor that archive approve native delivery.

## Hosted-run availability

The manual native workflow is present on this validation branch, but GitHub
does not expose it on the repository's default branch yet, and this branch has
no recorded workflow run. The workflow therefore needs to be merged or run
from a repository state where it is visible before an Android hosted journey or
Mac/iOS build can produce evidence. No workflow was dispatched from this
environment.

PR #2's existing repository check also confirms that hosted jobs are currently
blocked before starting because the GitHub account has a failed payment or
spending-limit problem. The check produced no test steps or product result.
Treat this as an infrastructure availability issue, not as a native pass or a
My Visit Notes failure.

## Verified

- All 288 web source checks pass with matching hashes.
- The expanded 229-file extracted web workflow passes, including Partly answered
  persistence, exact review export, private-note exclusion and offline reopening.
- Final web archive, manifest and passing verification receipt agree on SHA-256:
  `c70997f55e1221f9a26eb93ec364e05e09365394394575eaa735da01d6df6a5b`.
- Android compilation passes. The APK's 35 shared files match source and both
  native project folders. APK SHA-256:
  `cdc46a4cd09db5408b59d995aeb7b32ce41fe3ce087fb25036572e46bf2c988a`.
- The Android build was rerun from a clean environment declaration and passed;
  the bundle audit again found all 35 shared files identical.
- The native source audit also confirms the iOS custom bridge controller is the
  storyboard root and that the delegate, privacy declaration and app identity
  are included in the Xcode project. This does not compile Swift.
- The Android app declares no network permission: its production web files are
  bundled locally, and the app's save, transfer, share, clipboard and print
  paths do not require network access. This decision still needs confirmation
  during the native journey if a future feature adds an online destination.
- Simulated-native checks pass using the actual injected plugin interface.
  They do not prove native OS behavior.

## Android execution limit

Only one Android 34 emulator image is installed; no physical device is attached.
This account cannot read or write `/dev/kvm` and is not in the kvm group.
No host permissions were changed.

The read-only, unaccelerated emulator on port 5580 ran for about 50 minutes
without reporting completed boot. Its event log showed system processes 561,
828 and 1088 across repeated starts. Watchdog entries reported main-thread stalls
of 114 and 142 seconds. This is more than a shell observation timeout: Android
was restarting its system process during boot.

Stopped only that task-owned emulator through its console (`emu kill`). It used
`-read-only` and `-no-snapshot`, so the existing AVD was not updated. My Visit Notes
was never installed there; its journey runner stopped before installation at the
boot guard. Do not report any native journey step as passed.

## iOS execution limit

This is a Linux host with no Xcode or CocoaPods. The iOS project has not compiled
and has not run in a simulator. The Mac-only build script and separate manual
workflow are prepared, syntax-checked, and not remotely dispatched.

## What is needed to continue

1. An Android test phone or a working hardware-accelerated emulator. Run the
   dedicated-target journey, then the wider checks in acceptance.md: native
   import/export, clipboard, printing, offline restart, keyboard, privacy and
   installation updates. Keep fictional notes separate from anyone's real data.
2. A Mac with Xcode and CocoaPods. Run `scripts/build-ios.mjs`, address compilation
   errors if any, and execute the same complete journey in the simulator.

These environment requirements have recurred throughout the native work. The
completed web checks and Android compilation do not substitute for them. The
user has been asked which environments can be made available. No new account,
remote run, upload, host permission change or physical-device write was assumed.
