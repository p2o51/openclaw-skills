---
name: apk-device-compatibility
description: Analyze and adapt Android APK manufacturer/model restrictions for non-vendor devices, including Huawei apps on Pixel. Use for device-gate diagnosis, minimal compatibility patches, rebuilding, signing and new-version adaptation. Preserve normal account, payment, subscription and DRM authorization; do not assume every app is patchable.
---

# APK device compatibility

Match the requested scope: inspect for diagnosis requests; implement for patch/build requests. Answer in the user's language and lead with the verified outcome.

## Identify the input

- Obtain an authorized original APK from the user or a verified source. Preserve it unchanged. Record source/date, size and SHA-256. Compare hashes rather than assuming different stores or languages mean different builds.
- Inspect package, versionName/versionCode, minSdk/targetSdk, ABIs, manifest dependencies and certificate using Android SDK tools. Verify with apksigner; certificate names alone do not prove authenticity.
- Distinguish standalone APK, incomplete base APK, split set and native HarmonyOS HAP/APP by contents. Removing a device gate cannot convert a HarmonyOS application to Android.
- When extracting from a connected Android device, confirm its serial and discovered package. Run `adb -s SERIAL shell pm path PACKAGE` and collect every returned base/split path. Do not assume the Huawei Music package name.
- Establish target device/OS, exact failure stage/message, and relevant HMS/account-region state. Never request passwords or tokens; let the user perform real login.
- Separate installation failure, launch rejection, missing vendor APIs, signature failures, server restrictions and regional content differences.

## Trace the gate

- Read repository AGENTS.md and build instructions. Pin patch/tool versions and inspect existing source before reuse. Read references/huawei.md for Huawei targets.
- Use JADX for inspection and smali or a supported patch framework for bytecode edits. Trace the rejection string/resource to its callers and the branch that exits.
- Inspect all callers of a shared device helper. Prefer changing the narrow rejection branch over globally forcing a manufacturer helper true: other callers may select vendor-only login or system services.
- Classify missing dependencies as optional with fallback, required runtime, privileged permission or hardware capability. A boolean change supplies none of these.
- Diagnose re-signing failures from logs/code. Adapt an app-local integrity check only where necessary for this compatibility change and separable from content authorization. Preserve real login, TLS verification, payment, subscriptions and DRM; do not extract media keys or spoof entitlements.

## Build reproducibly

- Work in an isolated branch/directory, preserving original files and unrelated work. Publish patch sources/instructions, not proprietary APKs, decompiled trees, user data or signing keys.
- Prefer versioned Morphe/ReVanced patches where supported; otherwise use reproducible apktool/smali edits. Check local help or current official docs before generating commands.
- Constrain patches by package/version and structural fingerprints. Assert expected match counts and original instructions; fail on missing or ambiguous matches. Never reuse obfuscated names or native offsets blindly.
- For native changes, verify ABI, instruction boundaries and expected bytes. Avoid unexplained bulk replacements.
- Preserve the package name by default. Renaming may break OAuth, providers and service bindings; test it as a separate variant.
- Record input hash, patch revision, tool versions and exact changes. Rebuild, align before signing, and sign with a user-controlled key outside the repository. Reuse it for future compatible upgrades.
- Explain signature conflicts when replacing an official install. Do not uninstall applications or erase user data without explicit authorization.

## Verify

- Check APK structure, intended package/version/ABIs, alignment and `apksigner verify --verbose --print-certs`. Compare intended changes and confirm the original is untouched.
- With an authorized test device, verify installation, cold start, removal of the rejection, permissions, login/logout and relevant features. Redact tokens, account identifiers and unrelated personal data from logs.
- For music, test local user-owned audio first, then normally authorized streaming, background playback, media controls and Bluetooth where relevant. A working splash screen does not prove playback works.
- Report artifact inspection, build, signature verification, installation, launch and feature tests as separate statuses. Mark unperformed runtime checks pending.
- For content differences, compare like-for-like clients and change one variable at a time. A native HarmonyOS app is not a same-APK control. Treat account-region/service-routing explanations as hypotheses until demonstrated.
- Deliver the requested build if produced, checksum, reproducible patch source, tested version/device and remaining limitations. Revalidate fingerprints and relevant regressions on each update; never promise future compatibility.

## GitHub handoff

When requested, prepare a clean skill/patch-only change. Use a specified repository or a clearly relevant established skills repository. Read its instructions and structure first. If the destination is unclear, complete the files before asking for it. Verify remote contents after upload. Saving a personal skill does not itself publish it to GitHub.
