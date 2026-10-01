---
name: apk-device-compatibility
description: Adapt the Android edition of Petal Maps (com.huawei.maps.app) for non-Huawei devices. Use for reproducing the PetalMaps-NonHuawei workflow, inspecting manufacturer gates, fixing related login compatibility, rebuilding/signing and evaluating newer Maps APKs. Scope is Petal Maps only; regional map and transit availability require separate verification.
---

# Petal Maps on non-Huawei devices

Keep the existing skill identifier for compatibility with installed references. Work only on the Android edition of Petal Maps; do not extend this workflow to unrelated Huawei apps or native HarmonyOS packages.

Match the requested scope: inspect for diagnosis requests; implement for patch/build requests. Answer in the user's language and lead with the verified outcome.

## Identify the input

- Obtain an authorized original APK from the user or a verified source. Preserve it unchanged. Record source/date, size and SHA-256. Compare hashes rather than assuming different stores or languages mean different builds.
- Inspect package, versionName/versionCode, minSdk/targetSdk, ABIs, manifest dependencies and certificate using Android SDK tools. Verify with apksigner; certificate names alone do not prove authenticity.
- Distinguish standalone APK, incomplete base APK, split set and native HarmonyOS HAP/APP by contents. Removing a device gate cannot convert a HarmonyOS application to Android.
- When extracting from a connected Android device, confirm its serial and discovered package. Run `adb -s SERIAL shell pm path PACKAGE` and collect every returned base/split path. Require the inspected package to be `com.huawei.maps.app` before applying the Maps patches.
- Establish target device/OS, exact failure stage/message, and relevant HMS/account-region state. Never request passwords or tokens; let the user perform real login.
- Separate installation failure, launch rejection, missing vendor APIs, signature failures, server restrictions and regional content differences.

## Trace the gate

- Read repository AGENTS.md and build instructions. Pin patch/tool versions and inspect existing source before reuse. Read references/huawei.md for the pinned Maps precedent and unresolved service limitations.
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
- For Maps, test map tiles, location, place search, route planning, navigation voice and login separately. Check the user's target country. Record China map rendering and Japanese transit as separate feature checks; launch success proves neither.
- Report artifact inspection, build, signature verification, installation, launch and feature tests as separate statuses. Mark unperformed runtime checks pending.
- For content differences, compare like-for-like clients and change one variable at a time. A native HarmonyOS app is not a same-APK control. Treat account-region/service-routing explanations as hypotheses until demonstrated.
- Deliver the requested build if produced, checksum, reproducible patch source, tested version/device and remaining limitations. Revalidate fingerprints and relevant regressions on each update; never promise future compatibility.

## GitHub handoff

When requested, prepare a clean skill/patch-only change. Use a specified repository or a clearly relevant established skills repository. Read its instructions and structure first. If the destination is unclear, complete the files before asking for it. Verify remote contents after upload. Saving a personal skill does not itself publish it to GitHub.
