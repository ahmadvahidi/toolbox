#!/usr/bin/env python3
"""Check that every path named in docs/TOOL-ROUTER.md still exists.

The router says "job -> the tool that has earned it, with the command that runs it". A row pointing
at a deleted directory is worse than no row: the next session follows it and finds nothing. Runs from
the daily refresh; prints one line, plus the missing rows if any.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "TOOL-ROUTER.md"
BASES = [Path("/opt/data"), Path("/opt/data/workspace"), Path("/opt/data/skills")]

def resolve(token: str):
    if any(c in token for c in "<>…*"):
        return None  # placeholder, not a literal path
    if token.startswith("/"):
        return Path(token.rstrip("/"))
    if "/" not in token:
        return None
    cand = [Path(b) / token.rstrip("/") for b in [ROOT] + BASES]
    return next((c for c in cand if c.exists()), cand[0])

def main() -> int:
    if not DOC.exists():
        print("router: docs/TOOL-ROUTER.md missing")
        return 1
    text = DOC.read_text()
    tokens = sorted(set(re.findall(r"`([^`\s]+)`", text)))
    checked, missing = 0, []
    for t in tokens:
        if not re.search(r"\.(sh|py|mjs|js|ts|json|md)$|/$|^/[a-z]", t):
            continue
        p = resolve(t)
        if p is None:
            continue
        checked += 1
        if not p.exists():
            missing.append(t)
    print(f"router: {checked} paths, {len(missing)} missing")
    for m in missing:
        print(f"  ✗ {m}")
    return 1 if missing else 0

if __name__ == "__main__":
    sys.exit(main())
