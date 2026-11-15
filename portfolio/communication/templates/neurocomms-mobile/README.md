# My Visit Notes for Android and iOS

Status: implementation in progress. This is the mobile project for the visit app.
Read the [delivery checklist and remaining proof](acceptance.md), then use the
[native acceptance runbook](NATIVE-ACCEPTANCE-RUNBOOK.md) when an Android device
and Mac/iPhone are available.
The downloadable web archive includes these status documents only. Native build
commands require the full repository checkout, including this project's source
and package files; that web archive is not an Android or iOS distribution.
The existing `communication-tool/android` and `communication-tool/ios` projects
belong to Phrase Studio.

The shared application is in `../product-specs/my-visit-notes`. `npm run build`
copies an explicit list of application files and records their hashes. There is
no hosted start URL: Capacitor packages the files inside the app.

Run `npm ci`, `npm run build`, then `npx cap add android` or `npx cap add ios`
once to create a missing platform. Run `npm run sync` after source changes.
Open a platform using `npm run android` or `npm run ios`.

For a local Android build, set `ANDROID_HOME` and `ANDROID_SDK_ROOT` to the
Android SDK directory, and put the JDK `bin` directory on `PATH`. The build
does not change the repository or create a machine-specific `local.properties`
file. The hosted workflow supplies these values through its Android setup step.

The initial shell is not ready for distribution. Native backup export, clipboard,
printing, Back behavior, app background privacy, keyboard layout, saved data after
restart and installation updates must be checked before delivery. iOS compilation
and simulator checks require macOS with Xcode. Browser tests do not prove these
native behaviors.

On a Mac, run `npm ci` then `node scripts/build-ios.mjs`. The script builds the
unsigned simulator app, checks its identity, privacy declaration and every
packaged web file, and writes `ios/App/build/visit-build-evidence.json`. It fails
on Linux without attempting a build. The separate manual GitHub workflow
`Check My Visit Notes iOS build` runs the same check; it has not been dispatched
or verified here. Neither compilation nor that report replaces the required
simulator journey. See [current evidence](progress.md).
