#!/usr/bin/env python3
"""Daily refresh of the toolbox: live GitHub numbers, regenerated README, optional push.

    python3 tools/verify.py              # refresh + rewrite README/index, report
    python3 tools/verify.py --push       # ...and commit+push if anything changed
"""
import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "tools.json")
VERDICT_ORDER = ["use", "consider", "watch", "park", "skip", "dead"]
BADGE = {"use": "✅ in use", "consider": "🟡 consider", "watch": "👀 watch",
         "park": "🅿️ park", "skip": "⏭️ skip", "dead": "⚰️ dead"}


def token():
    p = os.environ.get("GITHUB_TOKEN")
    if p:
        return p
    for envf in ("/opt/data/.env", os.path.join(ROOT, ".env")):
        try:
            for line in open(envf, encoding="utf-8"):
                if line.startswith("GITHUB_TOKEN="):
                    return line.split("=", 1)[1].strip()
        except OSError:
            pass
    return None


def gh(path, tok):
    req = urllib.request.Request("https://api.github.com" + path,
                                 headers={"User-Agent": "gabimaru-toolbox",
                                          "Accept": "application/vnd.github+json",
                                          **({"Authorization": "Bearer " + tok} if tok else {})})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"__404__": True}
        return {"__error__": f"HTTP {e.code}"}
    except Exception as e:  # noqa: BLE001
        return {"__error__": str(e)}


def refresh(data, tok):
    changed = []
    for t in data["tools"]:
        repo = t.get("repo")
        if not repo:
            continue
        d = gh(f"/repos/{repo}", tok)
        if d.get("__404__"):
            if t.get("status") != "gone":
                t["status"], _ = "gone", changed.append(f"{repo}: 404")
            continue
        if "__error__" in d:
            print(f"  ! {repo}: {d['__error__']}")
            continue
        new = {
            "stars": d.get("stargazers_count"),
            "forks": d.get("forks_count"),
            "license": (d.get("license") or {}).get("spdx_id") or "none",
            "pushed": (d.get("pushed_at") or "")[:10],
            "archived": bool(d.get("archived")),
        }
        old = {k: t.get(k) for k in new}
        diff = {k: (old[k], v) for k, v in new.items()
                if k in ("stars", "license", "pushed", "archived") and old[k] not in (None, v)}
        if diff:
            changed.append(f"{repo}: " + ", ".join(f"{k} {a}→{b}" for k, (a, b) in diff.items()))
        t.update(new)
    data["checked"] = dt.date.today().isoformat()
    return changed


def render(data):
    tools = sorted(data["tools"], key=lambda t: (VERDICT_ORDER.index(t["verdict"])
                                                 if t["verdict"] in VERDICT_ORDER else 9,
                                                 -(t.get("stars") or 0)))
    rows = []
    for t in tools:
        name = f"**[{t['name']}](https://github.com/{t['repo']})**" if t.get("repo") else f"**{t['name']}**"
        stars = f"{t['stars']:,}" if t.get("stars") else "—"
        rows.append(f"| {BADGE.get(t['verdict'], t['verdict'])} | {name} | {t.get('what', '')} | "
                    f"{stars} | {t.get('license', '—')} | {t.get('pushed', '—')} |")

    readme = [
        "# Toolbox — everything Gabimaru has actually checked\n",
        "A working inventory of tools, libraries and claims that came in through forwards, reels and\n"
        "conversations — each one verified against the real repository, with a verdict for **this**\n"
        "machine: a headless Linux box, 6 cores, 7 GB RAM, **no GPU**, running Hermes, Telegram bots and\n"
        "a YouTube pipeline.\n",
        f"Numbers refreshed from `api.github.com` on **{data['checked']}** by `tools/verify.py`.\n"
        "Stars are a snapshot, not a quality score.\n",
        "**Verdicts** — `use` shipped/installed · `consider` worth it, needs a decision · `watch` right tool, "
        "needs hardware we do not have · `park` useful to a human, useless on a server · `skip` we already do "
        "it better with code · `dead` repo gone or abandoned.\n",
        "## Index\n",
        "| | Tool | What it is | ★ | Licence | Last push |",
        "|---|---|---|---:|---|---|",
        *rows,
        "\n## How this stays current\n",
        "```bash\npython3 tools/verify.py          # refresh stars/licence/last-push, rewrite this file\n"
        "python3 tools/verify.py --push   # same, then commit and push if anything moved\n```\n",
        "A cron job runs that every morning, so the table is never more than a day old and this file\n"
        "never has to live in an agent's context to stay true.\n",
        "## Adding an entry\n",
        "Append an object to `data/tools.json`:\n",
        "```json\n"
        '{"name": "…", "repo": "owner/name", "what": "one line", "verdict": "park",\n'
        ' "why": "why it does or does not change what we do", "date": "2026-11-04",\n'
        ' "tags": ["video", "gpu"]}\n'
        "```\n",
        "`repo` may be omitted for things that are not on GitHub (a model on Hugging Face, a claim from a\n"
        "reel). `why` is the part that matters: the verdict without a reason rots into folklore.\n",
    ]
    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write("\n".join(readme))

    idx = ["# index — one line per entry\n",
           f"checked {data['checked']}\n"]
    for t in tools:
        idx.append(f"- `{t['verdict']:<8}` **{t['name']}** — {t.get('what','')}"
                   + (f" · {t.get('repo')}" if t.get("repo") else "")
                   + f" · {t.get('why','')}")
    open(os.path.join(ROOT, "index.md"), "w", encoding="utf-8").write("\n".join(idx) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    data = json.load(open(DATA, encoding="utf-8"))
    changed = refresh(data, token())
    json.dump(data, open(DATA, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    render(data)

    if changed:
        print(f"{len(changed)} change(s):")
        for c in changed:
            print("  ~", c)
    else:
        print("no changes")
    print(f"{len(data['tools'])} entries, checked {data['checked']}")

    if a.push and changed:
        subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
        subprocess.run(["git", "-c", "user.name=toolbox-bot",
                        "-c", "user.email=bot@dopeak.dev",
                        "commit", "-qm", f"refresh: {data['checked']} ({len(changed)} changes)"],
                       cwd=ROOT, check=True)
        tok = token()
        url = f"https://x-access-token:{tok}@github.com/ahmadvahidi/toolbox.git"
        r = subprocess.run(["git", "push", "-q", url, "HEAD:main"], cwd=ROOT)
        print("pushed" if r.returncode == 0 else "push failed")
        return 0 if r.returncode == 0 else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
