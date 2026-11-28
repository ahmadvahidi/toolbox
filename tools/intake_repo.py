#!/usr/bin/env python3
"""intake_repo — document a forwarded repo in index.md the moment it arrives.

    python3 tools/intake_repo.py <owner/name> [--verdict watch] [--note "why"] [--commit]

Pulls GitHub metadata (stars, licence, last push, archived), appends ONE line in the same
format as every other entry, and optionally commits. The point: a forwarded repo must not
depend on someone remembering to write it up later — the earlier backlog (150 forwarded items
on disk, 20 notes) is what forgetting looks like.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.md"
VERDICTS = {"use", "consider", "watch", "park", "skip", "dead"}


def gh(path: str) -> dict:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        for line in Path("/opt/data/.env").read_text().splitlines():
            if line.startswith("GITHUB_TOKEN="):
                token = line.split("=", 1)[1].strip().strip('"')
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Accept": "application/vnd.github+json",
                 **({"Authorization": f"Bearer {token}"} if token else {})})
    return json.load(urllib.request.urlopen(req, timeout=30))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", help="owner/name")
    ap.add_argument("--verdict", default="watch", choices=sorted(VERDICTS))
    ap.add_argument("--note", default="")
    ap.add_argument("--commit", action="store_true")
    a = ap.parse_args()

    repo = a.repo.strip().removeprefix("https://github.com/").strip("/")
    d = gh(f"repos/{repo}")
    lic = (d.get("license") or {}).get("spdx_id") or "no licence"
    flags = []
    if d.get("archived"):
        flags.append("ARCHIVED")
    if not d.get("license"):
        flags.append("NO LICENCE")
    meta = (f"{d['stargazers_count']:,} stars, {lic}, created {d['created_at'][:10]}, "
            f"pushed {d['pushed_at'][:10]}")
    if flags:
        meta += " · " + ", ".join(flags)

    note = a.note or (d.get("description") or "").strip()[:220]
    line = (f"- `{a.verdict:<8}` **{repo.split('/')[-1]}** — {note} · {repo} · "
            f"Meta {meta} (checked {date.today().isoformat()}).")

    text = INDEX.read_text(encoding="utf-8")
    if repo.lower() in text.lower():
        print(f"already documented: {repo}")
        return 0
    INDEX.write_text(text.rstrip("\n") + "\n" + line + "\n", encoding="utf-8")
    print("added:", line[:160])

    if a.commit:
        subprocess.run(["git", "-C", str(ROOT), "add", "index.md"], check=True)
        subprocess.run(["git", "-C", str(ROOT), "-c", "user.name=Gabimaru",
                        "-c", "user.email=gabimaru@dopeak.local", "commit",
                        "-qm", f"index: intake {repo} ({a.verdict})"], check=True)
        print("committed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
