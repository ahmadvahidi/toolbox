#!/usr/bin/env python3
"""intake_backlog — turn the 150 un-noted downloads into toolbox entries, 10 a day.

Scans /opt/data/workspace/downloads/*/ for a repo URL (NOTES.md, url file, caption json),
skips anything already in index.md, and appends up to N entries per run with a `watch`
verdict. A `watch` entry says: captured, metadata pulled, not evaluated yet — which is the
honest state, and better than an empty folder nobody will ever open again.

    python3 tools/intake_backlog.py --limit 10 --commit
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/opt/data/workspace/toolbox-repo")
DOWN = Path("/opt/data/workspace/downloads")
INDEX = ROOT / "index.md"
REPO_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
SKIP = {"features", "topics", "about", "pricing", "login", "join", "sponsors",
        "settings", "orgs", "apps", "marketplace", "repos"}


def candidates() -> list[str]:
    seen, out = set(), []
    for d in sorted(DOWN.iterdir()):
        if not d.is_dir():
            continue
        for f in d.rglob("*"):
            if f.is_file() and f.stat().st_size < 800_000 and f.suffix.lower() in {
                    ".md", ".txt", ".json", ".html", ".srt"}:
                try:
                    txt = f.read_text(errors="ignore")
                except OSError:
                    continue
                for m in REPO_RE.finditer(txt):
                    owner, name = m.group(1).lower(), m.group(2).lower().rstrip(".")
                    if owner in SKIP or len(name) < 2:
                        continue
                    slug = f"{owner}/{name}".replace(".git", "")
                    if slug in seen:
                        continue
                    seen.add(slug)
                    out.append(slug)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--commit", action="store_true")
    a = ap.parse_args()

    index = INDEX.read_text(encoding="utf-8").lower()
    todo = [r for r in candidates() if r not in index]
    print(f"backlog: {len(todo)} repos not in index; handling {min(a.limit, len(todo))} now")
    done = 0
    for repo in todo[:a.limit]:
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "intake_repo.py"), repo,
                            "--verdict", "watch",
                            "--note", "forwarded by Ahmad, captured from the download backlog; "
                                      "metadata only, not evaluated yet"],
                           capture_output=True, text=True)
        if r.returncode == 0 and "added:" in r.stdout:
            done += 1
            print(" ", r.stdout.strip()[:110])
    print(f"added {done}")
    if a.commit and done:
        subprocess.run(["git", "-C", str(ROOT), "add", "index.md"], check=True)
        subprocess.run(["git", "-C", str(ROOT), "-c", "user.name=Gabimaru",
                        "-c", "user.email=gabimaru@dopeak.local", "commit", "-qm",
                        f"index: backlog intake, {done} repos from forwarded downloads"],
                       check=True)
        print("committed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
