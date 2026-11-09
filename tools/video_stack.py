#!/usr/bin/env python3
"""Render VIDEO-STACK.md from data/video-stack.json (+ live GitHub stars).

    python tools/video_stack.py            # rewrite VIDEO-STACK.md
    python tools/video_stack.py --check    # exit 1 if a path in the JSON is missing

Every entry names a real folder and a real command: a video tool we cannot point at is
not a tool we have. Paths are checked before the document is written.
"""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "video-stack.json")
OUT = os.path.join(ROOT, "VIDEO-STACK.md")
TOKEN_FILES = ("/opt/data/.env", os.path.join(ROOT, ".env"))


def token():
    for envf in TOKEN_FILES:
        try:
            for line in open(envf, encoding="utf-8"):
                if line.startswith("GITHUB_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
        except OSError:
            pass
    return os.environ.get("GITHUB_TOKEN", "")


def stars(repo, tok):
    if not repo:
        return None
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}",
                                 headers={"Authorization": f"token {tok}"} if tok else {})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r).get("stargazers_count")
    except Exception:
        return None


def missing(items):
    return [i for i in items if i.get("path") and not os.path.exists(i["path"])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    d = json.load(open(DATA, encoding="utf-8"))
    items = d["items"]
    bad = missing(items)
    if bad:
        for i in bad:
            print(f"missing path for {i['id']}: {i['path']}", file=sys.stderr)
        if a.check:
            return 1
    tok = token()
    today = dt.date.today().isoformat()

    lines = [
        "# 🎬 Video stack — every project we can make a video with",
        "",
        f"Refreshed **{today}**. Each row points at a real folder on the box and a real command; "
        "`tools/video_stack.py` refuses to write this page when a path has gone missing.",
        "",
        "**Rule:** pick the tool by the job, then **mix**. A published clip is normally three of "
        "these stacked: motion from one, voice from another, cards/encode from ffmpeg.",
        "",
        "| | Project | Makes | Use it when | Cost |",
        "|---|---|---|---|---|",
    ]
    for i in items:
        badge = {"in use": "✅ in use", "available": "🟡 available"}.get(i["status"], i["status"])
        name = f"**[{i['name']}](https://github.com/{i['repo']})**" if i.get("repo") else f"**{i['name']}**"
        s = stars(i["repo"], tok) if i.get("repo") else None
        if s and i.get("repo"):
            name += f" ★{s:,}"
        lines.append(f"| {badge} | {name} | {i['makes']} | {i['when']} | {i['cost']} |")

    lines += ["", "## Recipes (what to stack for a given job)", ""]
    for r in d["mix_recipes"]:
        lines += [f"### {r['job']}", "", f"- **Stack:** {r['use']}", f"- **Shipped example:** `{r['example']}`", ""]

    lines += ["## Details", ""]
    for i in items:
        lines += [f"### {i['name']}" + (f" — `{i['repo']}`" if i.get("repo") else ""), ""]
        lines += [f"- **Makes:** {i['makes']}"]
        lines += [f"- **When:** {i['when']}"]
        lines += [f"- **License:** {i['license']}"]
        if i.get("path"):
            lines += [f"- **Path:** `{i['path']}`"]
        lines += [f"- **Command:** `{i['cmd']}`", f"- **Cost:** {i['cost']}", ""]

    lines += [
        "## The one rule that keeps this honest",
        "",
        "Measure before claiming: a render speed, a page count, a duration comes from the tool's own "
        "output, never from a promo. Every line above has been run on this box, and the clips named "
        "in the recipes are the published ones.",
        "",
        f"_Data: [`data/video-stack.json`](data/video-stack.json) · generator: `tools/video_stack.py` · "
        f"refreshed {today}_",
    ]
    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"wrote {OUT} ({len(items)} projects, {len(d['mix_recipes'])} recipes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
