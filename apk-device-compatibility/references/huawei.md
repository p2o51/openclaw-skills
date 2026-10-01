# Huawei targets

## Petal Maps historical case

Upstream: https://github.com/andersonlucasg3/PetalMaps-NonHuawei

The previously inspected v1.3.4 workflow targeted `com.huawei.maps.app` version `4.7.0.322(001)`, versionCode 40700322. Original size: 86,868,406 bytes. Original SHA-256:

`b55133d89beeadad36ceadebddd521e30dba9f13530fa1dfee41335df9d15bbd`

This identifies a historical input, not the current latest version or an independent authenticity guarantee. An AppGallery-exported original and a third-party original had this identical hash.

Upstream forced `up2.g(Context)` true to bypass the launch gate. That helper also affected login selection, requiring separate Account Picker/WebView fallback changes. The workflow handled app-local re-signing detection in `SecurityDetect.irpj()` in `libaegissec.so`. Inspect pinned upstream source before reuse; these are not universal Huawei symbols.

Build/sign success did not prove every map service worked. China map tiles and Japanese transit remained unresolved in the Android case. Do not claim a China-region account fixes them, the patch caused them, or every Petal Maps edition lacks Japanese transit. The native HarmonyOS edition was a different comparison subject.

## Huawei Music: not yet validated

No Huawei Music APK has been analyzed for this skill. Do not advertise a working Music patch. Establish its actual package/version, signature, channel and failure first.

Investigate manufacturer checks, framework calls, required shared libraries, signature-level permissions, account/HMS login and native ABI support. Distinguish launch gates from privileged services or Huawei audio hardware dependencies. Preserve normal paid-content authorization.

## Official tool references

- APK Analyzer: https://developer.android.com/tools/apkanalyzer
- Signing: https://developer.android.com/tools/apksigner
- Alignment: https://developer.android.com/tools/zipalign
- JADX: https://github.com/skylot/jadx
- Apktool: https://apktool.org/docs/

Use current documentation or installed-tool help for syntax. Tool availability does not prove that an app can be adapted.
