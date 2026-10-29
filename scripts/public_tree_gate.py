#!/usr/bin/env python3
"""Public-repository leak gate. This does not prove source safety or app security."""
import json
import pathlib
import re
import subprocess
import sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
def run(*args):
    return subprocess.check_output(args, cwd=ROOT, text=True).splitlines()
paths = [pathlib.Path(p) for p in run("git", "ls-files")]
bad_ext = {".apk",".aab",".dex",".p12",".pfx",".jks",".keystore",".pem",".key",".zip",".db",".sqlite",".sqlite3"}
bad_names = {"local.properties",".env"}
bad_segments = {"inputs","secrets","diagnostics"}
violations = []
for p in paths:
    if p.suffix.lower() in bad_ext or p.name.lower() in bad_names or any(s.lower() in bad_segments for s in p.parts):
        violations.append(f"forbidden-path:{p}")
    if not (ROOT/p).is_file():
        violations.append(f"missing:{p}")
        continue
    raw = (ROOT/p).read_bytes()
    if (b"-----BEGIN" + b" PRIVATE KEY-----") in raw or (b"-----BEGIN" + b" ENCRYPTED PRIVATE KEY-----") in raw:
        violations.append(f"private-key-marker:{p}")
    if re.search(rb"ghp_[a-zA-Z0-9]{20}|github_pat_[a-zA-Z0-9_]{20}|AKIA[0-9A-Z]{16}",raw):
        violations.append(f"token-pattern:{p}")
result = {"public_tree_gate":"FAIL" if violations else "PASS","tracked_files":len(paths),
 "violations":violations,
 "native_host_integrated":"NOT_VERIFIED","diagnostic_egress_closed":"NOT_VERIFIED",
 "apk_built":"NO","signing_certificate_verified":"NOT_VERIFIED",
 "art_verified":"NOT_VERIFIED","phone_accepted":"NOT_VERIFIED"}
(ROOT/"out").mkdir(exist_ok=True)
(ROOT/"out"/"gate-report.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
if violations: sys.exit(1)
