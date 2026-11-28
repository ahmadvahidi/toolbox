#!/usr/bin/env python3
"""toolbox_daily_use.py — picks the day's toolbox tool and turns it into a real artifact.

The owner's standing order (2026-11-23): every tool in the toolbox is used in its slot —
each one at its own time, in the best place or the best combination — and the result is stored
and commented, so all sides of a video carry evidence.

Rotation: one tool per day from the `use` verdicts, advanced deterministically by date, so the
same tool is not used twice until the list is exhausted.

    python3 toolbox_daily_use.py plan           # today's tool + what to produce (no work)
    python3 toolbox_daily_use.py run [--dry]    # do it, append to state.json, print a summary
"""
import argparse
import datetime as dt
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "data", "tools.json")
STATE = os.path.join(ROOT, "data", "daily-use.json")
KIT = "/opt/data/workspace/codevember-kit"
PY_SKILLS = "/opt/data/skills/.venv/bin/python"

# tool name -> concrete, verifiable unit of work on this box
JOBS = {
    "blender-skills": {
        "what": "one vertical 720x1280 Cycles render from a real bpy scene (hero prop, 3-point light)",
        "cmd": [PY_SKILLS, os.path.join(ROOT, "tools", "jobs", "blender_skills.py"),
                "--out", os.path.join(ROOT, "out", "blender-{date}.png")],
        "topic_cycle": ["hero-prop"],
    },
    "Codevember 2026": {
        "what": "one clean 1080x1920 plate from today's scene",
        "cmd": [PY_SKILLS, f"{KIT}/codevember_capture.py", "{scene}", "--still", "--t0", "12",
                "--out", f"{KIT}/out/{{date}}-{{scene}}.png"],
        "scene_cycle": True,
    },
    "llama.cpp": {
        "what": "local-model sanity run (prompt -> answer) proving the stack still answers",
        "cmd": None,
    },
    "prompts.chat": {
        "what": "search the prompt library for the day's topic and save the best 5",
        "cmd": [PY_SKILLS, "/opt/data/workspace/prompts-cli/pmcp.py",
                "search", "{topic}", "-n", "5"],
        # topic rotates with the date, same idea as the Codevember scenes
        "topic_cycle": ["cinematic lighting", "code animation", "product photography",
                        "explainer video", "youtube thumbnail"],
        "save": os.path.join(ROOT, "data", "notes", "prompts-{date}.md"),
    },
}


def load_tools():
    d = json.load(open(TOOLS))
    return d["tools"]


def pick(today):
    cands = [t["name"] for t in load_tools() if t.get("verdict") == "use"]
    if not cands:
        return None
    idx = today.toordinal() % len(cands)
    return cands[idx]


def scene_for(today):
    """Cycle the 23 Codevember scenes by day number, so the plate rotates."""
    st = os.path.join(KIT, "state.json")
    if not os.path.exists(st):
        return None
    scenes = sorted(json.load(open(st))["scenes"], key=lambda s: s["day"])
    if not scenes:
        return None
    have = [s for s in scenes if (s.get("gif_bytes") or 0) > 0]
    pick = have[today.toordinal() % len(have)]
    return pick["id"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["plan", "run"])
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    today = dt.date.today()
    name = pick(today)
    job = JOBS.get(name or "", None)
    print(f"{today} => {name}")
    if not name:
        sys.exit("no 'use' tools in the index")
    if not job:
        print("  no wired job for this tool yet: record it, do not fake a run")
        return 0
    cmd = job["cmd"]
    if cmd and job.get("scene_cycle"):
        scene = scene_for(today)
        if not scene:
            sys.exit("codevember-kit has no material yet (run codevember_material.py sync)")
        cmd = [c.replace("{scene}", scene).replace("{date}", today.isoformat()) for c in cmd]
        os.makedirs(os.path.join(KIT, "out"), exist_ok=True)
    if cmd and job.get("topic_cycle"):
        cyc = job["topic_cycle"]
        topic = cyc[today.toordinal() % len(cyc)]
        cmd = [c.replace("{topic}", topic).replace("{date}", today.isoformat()) for c in cmd]
    else:
        topic = "-"
    print("  what:", job["what"])
    print("  cmd :", " ".join(cmd) if cmd else "(not runnable here)")
    if a.mode == "plan" or not cmd:
        return 0
    if a.dry:
        return 0
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout.strip()[-600:] or r.stderr.strip()[-600:])
    rec = {"date": today.isoformat(), "tool": name, "what": job["what"],
           "cmd": cmd, "rc": r.returncode,
           "out": cmd[-1] if cmd else None}
    if job.get("save") and r.returncode == 0:
        # the run only counts if it leaves something readable behind
        path = job["save"].replace("{date}", today.isoformat()).replace("{topic}", topic)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(f"# {name} — {today.isoformat()}\n\n"
                     f"topic: `{topic}` · query: `{' '.join(cmd)}`\n\n"
                     f"```\n{r.stdout.strip()}\n```\n")
        rec["out"] = path
        print("  saved:", path)
    hist = json.load(open(STATE)) if os.path.exists(STATE) else []
    hist.append(rec)
    json.dump(hist, open(STATE, "w"), indent=1)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
