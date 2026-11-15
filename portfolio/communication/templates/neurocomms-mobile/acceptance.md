# My Visit Notes: what is ready and what still needs proof

Status: not ready for native delivery. Android builds. iOS has not been built.
Passing browser tests does not mean a phone app works correctly.

Use [NATIVE-ACCEPTANCE-RUNBOOK.md](NATIVE-ACCEPTANCE-RUNBOOK.md) for the
step-by-step Android and iPhone test record. This checklist explains the scope;
the runbook is the copyable test sheet.

The goal is one complete appointment journey on the web, Android and iPhone.
The existing Phrase Studio app remains a separate product.

## Delivery checklist

| Requirement | Evidence so far | Still needed |
| --- | --- | --- |
| Separate Android and iOS apps | Both projects use `org.myvisitnotes.app`. Android debug build passed. The 35 shared app files match the APK and both project folders. | Build and inspect the iOS simulator app. |
| Clear, usable phone screens | Browser checks cover 320px screens, larger text, keyboard navigation, rotation and reduced screen height. | Real software keyboard, cutouts, system text size and rotation on each native platform. |
| Prepare, use, review and continue a visit | Shared logic and browser tests cover these steps. The previously broken “Partly answered” save has a recovery-history regression test. | Complete the whole journey in each native app. |
| Reopen saved work without a connection | Browser restart/offline checks passed. Native files are packaged locally. | Save, close the native process, disable network access, reopen and compare the saved words. |
| Backups, transfer, deliberate sharing, copy and print | Native export/copy/print paths are implemented. Simulated native tests check exact selected output and errors. | Use real file pickers, destinations, clipboard and print sheets. Restore exported files into a separate test installation. |
| Back, interruptions, updates and recovery | Android Back and background covers are implemented. Slow export cleanup no longer delays the event handlers. Android backup is disabled. | Verify Back, interruption snapshots, unsaved work, recovery and app updates on native platforms. Review iOS device-backup behavior. |
| Installable files and an honest report | Android debug APK exists; build and package checks passed. This report lists the gaps. | Native runtime evidence, iOS build/runtime evidence and physical-device checks when devices are available. |

## The native journey that must pass

Use fictional notes in a dedicated test installation. Do not clear an existing
installation with someone's notes to make a test pass.

1. Prepare three questions, a private preparation note and a request for what
   helps during the appointment. Save, close the app and reopen it.
2. Choose one question to show. Confirm that the other questions and private
   notes are not visible. Put the app in the background and inspect the app
   switcher. Return: shown words must remain concealed until deliberately shown.
3. Use Back with the keyboard open, while showing words, inside a dialog and
   from the visit screen. None of these actions may erase unfinished work.
4. Record every supported question outcome, including “Partly answered.” Add a
   personal answer note and a next step. Save, restart and compare the words.
5. Prepare a follow-up message. Keep it as a draft, reopen it, edit it and review
   its exact output. Creating or sharing a message must not mark it sent or done.
6. Prepare the next appointment from selected unfinished items. The original
   visit must stay unchanged. Personal notes must not be copied by default.
7. Export a backup and a transfer file. Cancel one attempt; finish another. Open
   the chosen destination and confirm the file is there. Restore it elsewhere
   and compare saved visits, preparation, drafts and links to earlier items.
8. Copy and print selected output. Inspect the clipboard and actual print/PDF
   result. Only the reviewed words may appear. Cancel and retry both operations.
9. Disable network access and restart the app. Repeat saving and reopening.
   Simulate a failed save: the latest words must remain visible with a clear
   failure message, and retry must not duplicate records.
10. Install an updated build over the same test installation without clearing
    data. Saved visits, drafts and recovery must still work. Keep the original
    and updated build identities with the result.

Record each step separately for Android and iOS: build hash, OS version, device
or simulator, exact result, and any failure. Do not replace a failed step with
a smaller successful check.

## Where the evidence lives

- [Progress and live test handles](progress.md)
- [Build instructions](README.md)
- `scripts/android-journey.mjs`: installation, saving, clipboard, Back and restart
  checks; its output explicitly lists the wider journey steps it does not test.
- `scripts/build-ios.mjs`: Mac-only compilation and packaged-file checks, not a
  simulator journey. Its manual workflow has not been run here.
- `../product-specs/my-visit-notes/qa/`: browser and logic results. Use their
  pass/fail entries and file hashes; old green reports are not current approval.

No participant sessions are required for this engineering goal. These checks
do not establish clinical benefit or suitability for a particular person.
