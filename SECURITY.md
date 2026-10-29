# Security policy

The repository is PUBLIC. Never commit signing keys, passwords, GitHub tokens,
real diagnostic bundles, authentic host APK/DEX files, cookies, or raw logs.

**Do not add DSH signing credentials to GitHub Actions yet.** The Android CI
smoke job runs entirely without secrets. The identity that signs an installed
com.dsh.android application should stay under local control.

If cloud signing is considered later, first audit the public workflow and
repository access, restrict manual triggering and environment access, protect
branches, and define a rotation/revocation response. Public GitHub repository
Secrets are encrypted, but they can still be exposed by a workflow edited by
someone who gains write access.

Do not publish a DSH APK until all native and Node diagnostic sending paths,
host UI integration, ART loading, and data preservation have independent evidence.
