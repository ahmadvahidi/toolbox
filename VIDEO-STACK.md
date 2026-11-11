# 🎬 Video stack — every project we can make a video with

Refreshed **2026-11-11**. Each row points at a real folder on the box and a real command; `tools/video_stack.py` refuses to write this page when a path has gone missing.

**Rule:** pick the tool by the job, then **mix**. A published clip is normally three of these stacked: motion from one, voice from another, cards/encode from ffmpeg.

| | Project | Makes | Use it when | Cost |
|---|---|---|---|---|
| ✅ in use | **[MuJoCo B-roll](https://github.com/google-deepmind/mujoco)** ★17,569 | real physics B-roll (domino chain, tower collapse, pendulum, collisions) and full mixes: physics + avatar + caption cards | a claim needs motion you cannot film — saturation, cascades, damping, impact | CPU only, ~2-3 min per 12 s at 720x1280 |
| ✅ in use | **[LivLiv Player (talking avatar)](https://github.com/livliv-dev/player)** ★1,483 | 2.5D character that speaks with lip-sync, no face, no GPU | the video needs a presenter or a character voice instead of a narrator | ~5 frames/s on CPU; a 12 s clip ≈ 3 min |
| ✅ in use | **Gabimaru PNGTuber** | our own masked-ninja avatar frames (closed/open/blink) + monologue renders | channel identity videos, intros, in-character pieces | CPU; 2:19 clip ≈ 7 min |
| ✅ in use | **Aesthetic notes shorts** | handwritten-notebook math explainers (TTS + notes page + motion + music) | math/education topic with a visual derivation | CPU, a few minutes; 127 renders to date |
| ✅ in use | **ALGORHYTHM CS shorts** | computer-science shorts with diagrams, code and narration | CS concept, system behaviour, algorithm intuition | CPU; 533 renders to date |
| ✅ in use | **faceless-youtube pipeline** | the main long/short pipeline: script → TTS → scenes → motion → upload | standard DOPEAK output; anything that must end up published | CPU; 88 renders to date |
| ✅ in use | **[Manim CE](https://github.com/ManimCommunity/manim)** ★42,413 | mathematical animation with exact geometry (3Blue1Brown style) | the idea IS the geometry: circles, limits, transforms, graphs | CPU, slow; keep scenes under ~20 s |
| 🟡 available | **Animation styles library** | 13 coded motion styles (kinetic type, grid, glitch...) as JS samples | the video needs a look, not a simulation — pick a style and drive it with our text | browser render, seconds per frame |
| 🟡 available | **[ClaudeAnimationBase (p5.brush)](https://github.com/JohnHeibel/ClaudeAnimationBase)** ★2,875 | hand-drawn character acting (31 emotions) and soft painted stills | a mascot must emote, or a thumbnail needs a painted look | ~18 s per 1280px still; full video ~19 s per frame — nightly only |
| ✅ in use | **CASE FILE longform** | documentary-style long episodes (evidence boards, maps, timelines) | a story with documents, dates and a verdict | long render, run twice a week |
| 🟡 available | **microduck-short** | short assembly from clips + audio (one build.py) | you already have footage and only need the cut | seconds |
| ✅ in use | **ffmpeg** | encode, concat, mux audio, burn cards, loudnorm, loop, trim | always — it is the last step of every pipeline above | seconds per clip |
| 🟡 available | **[AI Shorts Generator (long -> 9:16)](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)** ★5,944 | whisper transcript + LLM highlight ranking + auto-cropped vertical shorts from one long video | talking-head / interview footage only — the auto crop is centre/face based and cuts text off our kinetic-type longforms | 8.5 min source: ~2 min transcribe + ~3 min rank/render on CPU |
| ✅ in use | **[Replica skill (app teardown / clone)](https://github.com/Jakeschincariol/replica-skill)** ★8,866 | the 'how this app really works' video format (recon map, screen inventory, data model drawn as cards) and the working clone that the video points at | a reel/blog claims 'clone any app' or 'build this in a weekend' — prove or disprove it with a real parity score on screen | CPU, seconds — stdlib only, no keys |
| ✅ in use | **[Edge0 — 35B on 3 GB RAM](https://github.com/Edge0-AI/Edge0)** ★9,691 | on-screen proof that a 35B MoE decodes in 3 GB of RAM: terminal run, tok/s counter, RSS readout, SSD read counter | a reel claims 'runs a huge model on your phone/laptop' and we want to prove or disprove it with our own hardware | CPU only; 6 tok/s on i5-10500T; 42 GB disk for the assets |

## Recipes (what to stack for a given job)

### Character + physics + cards (the full mix)

- **Stack:** MuJoCo scene as background, Gabimaru PNGTuber (transparent frames) bottom-right with mouth from the VO envelope, drawtext cards on the VO timeline, one ffmpeg pass
- **Shipped example:** `physics-broll/out/gabimaru-physics-de.mp4 — 32.7 s, 3 layers, German VO`

### Concept that needs motion (queues, collapse, damping)

- **Stack:** physics-broll for the motion + faceless-youtube for narration/music + ffmpeg drawtext for the key line
- **Shipped example:** `out/queue-collapse-de.mp4 — 3 scenes, 33 s, German VO, 4 caption cards`

### A tool/repo review

- **Stack:** terminal cards (short_llmapps.py pattern) + real screen evidence, never stock b-roll
- **Shipped example:** `out/llmapps-de.mp4 — 144,280 stars, 57 apps, the audit line`

### Math derivation

- **Stack:** math-notes for the page, Manim when the geometry must move exactly
- **Shipped example:** `notes_v27_short.mp4`

### Presenter / in-character

- **Stack:** gabimaru-avatar or LivLiv for the face, faceless-youtube for the bed, captions from the VO envelope
- **Shipped example:** `gabimaru-de-long.mp4`

### App-teardown short (claim -> proof -> number)

- **Stack:** 5 s claim card, 8 s recon map (screens/flows/data model as text cards), 12 s real tool output (parity score + missing list), 8 s the built screen as B-roll, CTA. Numbers come from parity.py/imgdiff.py, never invented.
- **Shipped example:** `workspace/booking-clone — parity 79.0/100, 14/14 must-haves, 4/4 tests`

### Claim-check short: '35B in 3 GB' 

- **Stack:** 3 s cover claim, 5 s what a MoE is (two cards), 12 s real terminal: prefill timer, decode speed ticking, RSS from /usr/bin/time, 6 s the same model answering in Persian, CTA. Numbers from our own run, never the reel's.
- **Shipped example:** `ki box 2026-11-11 — 6.07 tok/s, TTFT 6.39 s, peak RSS 3.09 GB, 42.3% expert hit rate`

## Details

### MuJoCo B-roll — `google-deepmind/mujoco`

- **Makes:** real physics B-roll (domino chain, tower collapse, pendulum, collisions) and full mixes: physics + avatar + caption cards
- **When:** a claim needs motion you cannot film — saturation, cascades, damping, impact
- **License:** Apache-2.0
- **Path:** `/opt/data/workspace/physics-broll`
- **Command:** `python render.py --scene tower ... && python build_mix.py`
- **Cost:** CPU only, ~2-3 min per 12 s at 720x1280

### LivLiv Player (talking avatar) — `livliv-dev/player`

- **Makes:** 2.5D character that speaks with lip-sync, no face, no GPU
- **When:** the video needs a presenter or a character voice instead of a narrator
- **License:** Apache-2.0 (core) / samples non-commercial
- **Path:** `/opt/data/workspace/avatar-video`
- **Command:** `see skill livliv-avatar-video (stage.html + env.json + CDP capture)`
- **Cost:** ~5 frames/s on CPU; a 12 s clip ≈ 3 min

### Gabimaru PNGTuber

- **Makes:** our own masked-ninja avatar frames (closed/open/blink) + monologue renders
- **When:** channel identity videos, intros, in-character pieces
- **License:** ours
- **Path:** `/opt/data/workspace/avatar-gabimaru`
- **Command:** `python make_frames.py && python render_video.py`
- **Cost:** CPU; 2:19 clip ≈ 7 min

### Aesthetic notes shorts

- **Makes:** handwritten-notebook math explainers (TTS + notes page + motion + music)
- **When:** math/education topic with a visual derivation
- **License:** ours
- **Path:** `/opt/data/workspace/math-videos`
- **Command:** `python aesthetic_notes.py out/notes_vNN_short.mp4  (subject gate runs first)`
- **Cost:** CPU, a few minutes; 127 renders to date

### ALGORHYTHM CS shorts

- **Makes:** computer-science shorts with diagrams, code and narration
- **When:** CS concept, system behaviour, algorithm intuition
- **License:** ours
- **Path:** `/opt/data/workspace/cs-videos`
- **Command:** `see run_cs_shorts.sh (cron) / build scripts in the folder`
- **Cost:** CPU; 533 renders to date

### faceless-youtube pipeline

- **Makes:** the main long/short pipeline: script → TTS → scenes → motion → upload
- **When:** standard DOPEAK output; anything that must end up published
- **License:** ours
- **Path:** `/opt/data/workspace/faceless-youtube`
- **Command:** `see PLAYBOOK.md (the operating contract) and pipeline_v3.py`
- **Cost:** CPU; 88 renders to date

### Manim CE — `ManimCommunity/manim`

- **Makes:** mathematical animation with exact geometry (3Blue1Brown style)
- **When:** the idea IS the geometry: circles, limits, transforms, graphs
- **License:** MIT
- **Path:** `/opt/data/workspace/manim-test`
- **Command:** `manim -pqh scene.py Scene (local-sys libs + TEXMFCNF needed)`
- **Cost:** CPU, slow; keep scenes under ~20 s

### Animation styles library

- **Makes:** 13 coded motion styles (kinetic type, grid, glitch...) as JS samples
- **When:** the video needs a look, not a simulation — pick a style and drive it with our text
- **License:** mixed (see INDEX.md)
- **Path:** `/opt/data/workspace/animation-styles`
- **Command:** `see STYLES.md / dopeak_15s.mp4 reference render`
- **Cost:** browser render, seconds per frame

### ClaudeAnimationBase (p5.brush) — `JohnHeibel/ClaudeAnimationBase`

- **Makes:** hand-drawn character acting (31 emotions) and soft painted stills
- **When:** a mascot must emote, or a thumbnail needs a painted look
- **License:** MIT
- **Path:** `/opt/data/workspace/claude-anim-base`
- **Command:** `node render.mjs --stills=3.0 --w=1280 --soft-gl --chrome=$CHROME_HEADLESS`
- **Cost:** ~18 s per 1280px still; full video ~19 s per frame — nightly only

### CASE FILE longform

- **Makes:** documentary-style long episodes (evidence boards, maps, timelines)
- **When:** a story with documents, dates and a verdict
- **License:** ours
- **Path:** `/opt/data/workspace/case-file`
- **Command:** `see cron_brief.md + motion_pass.py`
- **Cost:** long render, run twice a week

### microduck-short

- **Makes:** short assembly from clips + audio (one build.py)
- **When:** you already have footage and only need the cut
- **License:** ours
- **Path:** `/opt/data/workspace/microduck-short`
- **Command:** `python build.py`
- **Cost:** seconds

### ffmpeg

- **Makes:** encode, concat, mux audio, burn cards, loudnorm, loop, trim
- **When:** always — it is the last step of every pipeline above
- **License:** LGPL/GPL
- **Path:** `/usr/bin`
- **Command:** `ffmpeg -framerate 24 -i f%04d.png -i vo.mp3 -vf format=yuv420p -c:v libx264 -crf 20 -shortest out.mp4`
- **Cost:** seconds per clip

### AI Shorts Generator (long -> 9:16) — `Anil-matcha/AI-Youtube-Shorts-Generator`

- **Makes:** whisper transcript + LLM highlight ranking + auto-cropped vertical shorts from one long video
- **When:** talking-head / interview footage only — the auto crop is centre/face based and cuts text off our kinetic-type longforms
- **License:** MIT
- **Path:** `/opt/data/workspace/ai-shorts-gen`
- **Command:** `GEMINI_API_KEY=... LLM_PROVIDER=gemini python main.py <file> --mode local --num-clips 2`
- **Cost:** 8.5 min source: ~2 min transcribe + ~3 min rank/render on CPU

### Replica skill (app teardown / clone) — `Jakeschincariol/replica-skill`

- **Makes:** the 'how this app really works' video format (recon map, screen inventory, data model drawn as cards) and the working clone that the video points at
- **When:** a reel/blog claims 'clone any app' or 'build this in a weekend' — prove or disprove it with a real parity score on screen
- **License:** MIT
- **Path:** `/opt/data/skills/replica`
- **Command:** `python3 /opt/data/skills/replica/replica-diff/parity.py <project>/replica/features.csv`
- **Cost:** CPU, seconds — stdlib only, no keys

### Edge0 — 35B on 3 GB RAM — `Edge0-AI/Edge0`

- **Makes:** on-screen proof that a 35B MoE decodes in 3 GB of RAM: terminal run, tok/s counter, RSS readout, SSD read counter
- **When:** a reel claims 'runs a huge model on your phone/laptop' and we want to prove or disprove it with our own hardware
- **License:** Apache-2.0
- **Path:** `/opt/data/workspace/edge0`
- **Command:** `ssh ki 'cd ~/edge0/edge0-infer && ./build/cpu/bin/edge0-infer run --model ~/edge0-assets/assets-35b --device cpu --user "..." --max-tokens 80'  # build lives on ki:~/edge0, assets on ki:~/edge0-assets`
- **Cost:** CPU only; 6 tok/s on i5-10500T; 42 GB disk for the assets

## The one rule that keeps this honest

Measure before claiming: a render speed, a page count, a duration comes from the tool's own output, never from a promo. Every line above has been run on this box, and the clips named in the recipes are the published ones.

_Data: [`data/video-stack.json`](data/video-stack.json) · generator: `tools/video_stack.py` · refreshed 2026-11-11_
