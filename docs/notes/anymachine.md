# AnyMachine — reference note (filed 2026-11-21)

Filed from a forwarded reel (@githubsignals, 38 s, "Github Signals", https://www.instagram.com/reel/Df93yQrAacr/).
Everything below was verified against the repo and, for the Blender part, by running it here on this box.

## What it is

`apekshik/anymachine` — **not an app and not a tool you install.** It is a *method* plus the six worked runs
that produced it: reference images → parts breakdown → **one Python script** that builds geometry, materials,
UVs, texture bake, armature, skinning and animations in Blender, then check renders and a GLB/FBX verify pass.

| Verified on api.github.com (2026-11-21) | value |
|---|---|
| stars / forks | 908 / 101 |
| licence | MIT |
| created | 2026-11-04 |
| last push | 2026-11-17 (alive) |
| archived | no |
| repo size | 265 MB (536 MB cloned) |
| open issues | 3 |

Runs inside: `stilt` (30 m four-legged walker, 160 parts, 104-bone rig, three actions), `quadruped`, `spider`,
`laptop` (one hinge, 0–135°), `backpacks` (soft goods), `hardsurface` (helicopter, lifeboat, 12 equipment
pieces, 19 fixtures, 3 rifles — no joints). Status is stated plainly in the README: **"experiments… no
endpoint yet"**.

## Reel vs repo

The reel says it "takes a concept image and uses an AI agent to build a real 3D model… working hinges,
walking legs, soft materials… builds a physical simulation where every joint has a working range of motion".

- **True:** the model really is code. `stilt/build_stilt.py` is 2,190 lines and rebuilds the whole machine;
  `verify_glb.py` (137 lines) re-imports the export into an empty scene and reports what survived.
- **Overstated:** there is no physics engine and no runtime app. "Physical simulation" here means a rigged
  armature with animated actions, checked for parts passing through each other — not MuJoCo-style dynamics.
- **Missing from the reel:** the human steps. Someone picks the design and approves every reference set
  (concept → turnaround → single views → 28 close-up plates → parts breakdown) before any geometry exists.
  The references are the product; the script is the easy half.

## Verified here (this box, CPU only, no GPU, no Blender binary)

Blender **5.0.1** runs headless as a Python module — no system Blender needed:

```bash
uv venv --python 3.11 .venv && uv pip install --python .venv/bin/python bpy
# bpy needs the glvnd loader that is not in the base image; extract it once, no root:
cd /tmp && apt-get download libgl1 libglx0 libglvnd0
for d in libgl*.deb libglvnd0*.deb; do dpkg-deb -x $d <gl-dir>; done
LD_LIBRARY_PATH=<gl-dir>/usr/lib/x86_64-linux-gnu:/opt/data/local-sys/usr/lib/x86_64-linux-gnu .venv/bin/python build.py
```

- Cycles CPU still, 540×960, 16 samples: **~3 s**.
- `stilt/build_stilt.py` run unmodified: 65 unique parts built → **160 objects**, UV unwrap, texture bake,
  `stilt.glb` **35.8 MB**, `stilt.blend` **8.7 MB**, check renders written — under a minute of wall clock
  before the bake. Upstream used Blender 5.2, we ran 5.0.1: only a `use_nodes` DeprecationWarning.
- Workbench (the fast preview engine) does **not** start here — no GL context. Everything visual must be
  Cycles CPU, so animation cost has to be measured per second of footage before promising a daily lane.

Environment kept at `workspace/bpy-test` (venv + glvnd shims) and `workspace/anymachine` (shallow clone).

## Why it matters to us

1. **A 3D mechanism lane for the shorts.** "Why a knee needs two actuators", "what a hinge actually carries",
   "how a walker keeps four feet from sliding" — built from one script, so a change is a one-line edit and a
   rebuild, not a re-model. That is the format differentiation the channel is missing.
2. **The verification discipline is the transferable part.** Their checks are numbers, not opinions:
   0 overlaps across a joint sweep, min clearance 0.32 mm on the laptop hinge, 0.014 mm foot slip on the
   quadruped, joint ranges driven from the animation. Same shape as our motion gate and audio gate — a
   machine decides before a human looks.
3. **Stills are cheap today.** Product-style stills and turntables are seconds per frame on CPU; that alone
   is usable for thumbnails, B-roll and cover frames now.

## Measured: what a 3D mechanism short costs here (2026-11-21)

Built a two-plate hinge by script (`workspace/hinge-test/hinge.py`: base plate, three knuckles, pin, lid on an
empty pivot, 0-135 deg over 48 frames) and rendered it on CPU. Numbers, not estimates:

| Setting (540x960, Cycles CPU, OIDN denoise) | seconds / frame |
|---|---|
| 16 spp | 4.09 |
| 8 spp | 2.95 |
| 4 spp | 2.34 |
| 1 still, 540x960, 16 spp | ~3 s |

- 2 s clip (48 frames @ 24 fps, 8 spp) rendered end to end in **141 s** = 70 s of machine time per second of
  finished video, and the encode is instant (`hinge-2s.mp4`, 540x960).
- A 20 s short at 8 spp is therefore **~24 min**; at 4 spp **~19 min**. That is one short per machine per hour,
  which fits a daily lane next to the math renders.
- 540x960 is half of 1080x1920: either render 720x1280 at ~2x the time, or upscale (we have a
  video-super-resolution path). Do not promise full-res Cycles animation before that choice is made.

**EEVEE does not start on this box.** With the glvnd loader, the mesa DRI drivers extracted from Debian
(`libgl1-mesa-dri`) and `LIBGL_ALWAYS_SOFTWARE=1 GALLIUM_DRIVER=llvmpipe`, bpy still aborts with
"No OpenGL vendor detected / Couldn't find current GLX or EGL context". Cycles CPU is the only engine here.

**Blender 5.x API note:** `Action.fcurves` no longer exists (layered actions). Any script that walks fcurves to
set interpolation has to be rewritten; keyframe_insert with the default BEZIER is fine.

## Caveats

- 536 MB clone; the example assets (4K textures, videos, FBX) are the bulk and are not needed to run the method.
- Their scripts hardcode their own dimensions and part names — reusable as a template, not as a library.
- Bake is ~80 s per build and invalidates on any geometry change; `--reuse-bake` only while topology matches.
- The Stilt reference images were made with a paid image model (GPT Image 2.6 on fal). Our free route is
  Gemini stills, which will produce weaker close-up plates — expect simpler mechanisms first.

## Verdict: `consider`

Adopt the *method* now (references → parts breakdown → one build script → numeric checks → verify export),
start with one 15–20 s mechanism short from a laptop hinge (the simplest worked example), and measure Cycles
CPU render time per finished second before committing a slot. Not a dependency, not an app, no endpoint.