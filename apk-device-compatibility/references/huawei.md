# Petal Maps reference

## Petal Maps historical case

Upstream: https://github.com/andersonlucasg3/PetalMaps-NonHuawei

The previously inspected v1.3.4 workflow targeted `com.huawei.maps.app` version `4.7.0.322(001)`, versionCode 40700322. Original size: 86,868,406 bytes. Original SHA-256:

`b55133d89beeadad36ceadebddd521e30dba9f13530fa1dfee41335df9d15bbd`

This identifies a historical input, not the current latest version or an independent authenticity guarantee. An AppGallery-exported original and a third-party original had this identical hash.

Upstream forced `up2.g(Context)` true to bypass the launch gate. That helper also affected login selection, requiring separate Account Picker/WebView fallback changes. The workflow handled app-local re-signing detection in `SecurityDetect.irpj()` in `libaegissec.so`. Inspect pinned upstream source before reuse; these are not universal Huawei symbols.

Build/sign success did not prove every map service worked. China map tiles and Japanese transit remained unresolved in the Android case. Do not claim a China-region account fixes them, the patch caused them, or every Petal Maps edition lacks Japanese transit. The native HarmonyOS edition was a different comparison subject.

## Reproduce the recorded build

Use upstream tag `v1.3.4` as the historical baseline; verify its resolved revision and current build instructions before execution. The recorded workflow used Morphe desktop 1.12.0 with the original APK identified above.

The recorded enabled patches were Manufacturer Check Bypass, Anti-Repack Bypass, Huawei Login Fix, AccountPicker WebView force, and Main activity orientation fix. These labels describe the recorded functions; list the actual bundle patches to obtain exact current names before invoking the CLI. Package-name changing was disabled.

Build the patch bundle using the pinned project's documented build task, list its contents, apply only the intended patches, align/sign and verify the output. Keep the signing key private and stable. Inspect all build scripts before execution; do not assume platform-specific paths work in the current environment.

For a new Maps version, first compare the input version/hash and inspect whether upstream supports it. Revalidate each fingerprint and each ABI's native patch. If the same supported original hash is supplied again, explain that it is the same source build rather than claiming a new domestic edition. Do not apply the historical native patch to a different binary without analysis.

The historical build was produced and signed; the user reported using the modified app. This is not a comprehensive runtime or navigation test. Missing China tiles and Japanese transit remained unresolved. Do not treat an outdated coverage page as proof of current behavior across all editions.

## Official tool references

- APK Analyzer: https://developer.android.com/tools/apkanalyzer
- Signing: https://developer.android.com/tools/apksigner
- Alignment: https://developer.android.com/tools/zipalign
- JADX: https://github.com/skylot/jadx
- Apktool: https://apktool.org/docs/

Use current documentation or installed-tool help for syntax. Tool availability does not prove that an app can be adapted.
