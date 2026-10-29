# DSH Android v139 — isolated build and validation

This is a **public source-only staging repository** for DSH v139. It is not the original Android host project and it does **not** currently produce a usable APK.

## Security boundary
- Never commit APK/DEX, recovered proprietary host code, diagnostics, cookies, API keys, P12/JKS, passwords, or real user data.
- GitHub Actions initially run **without any signing credentials**. Signing the original `com.dsh.android` APK with its fixed certificate should preferably happen on a trusted local machine after privacy and host integration gates pass.
- A passing JVM/D8 workflow is **not** proof of Android ART compatibility, no unauthorized diagnostics upload, profile isolation, preservation of app data, or install/upgrade safety.
- Current phone v138 remains unchanged. No release APK is authorized.

## Input status
The source-only P5/P6 packages remain outside this public repository pending a file-by-file licensing and secret audit. P6 does not contain the complete Gradle host project. A final APK requires a verified original host integration and controlled signing step.

## CI
The workflow `.github/workflows/source-gates.yml` checks the public staging tree and records explicit blocked gates. When approved source files are added, it may run static Java/Node tests and Android D8 (no network diagnostics sent). **No production signing or deployment.**

## Expected identity for future private release validation
- Application ID: `com.dsh.android`
- Installed baseline: `versionCode=138`
- New release: `versionCode>138`
- Required signing certificate SHA-256: `90072b7de43e96999be92d99869ce5e5b7639b5f2449417b99a1790831b60ff8`

This documentation is a safeguard, not evidence that an APK has been built.
