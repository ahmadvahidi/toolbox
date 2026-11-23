# TOOL ROUTER — job → the tool that has earned it

Every daily job we actually run, the tool that does it **now**, and the exact command. Read this
before picking a library; read `index.md` when the question is "is this thing good?" — this file only
answers "what do I reach for, and in what order".

Rules:
- The first column is the tool that already **ships** output on this box. Anything marked `consider`
  in the index is *not* in the chain until its trigger fires — the trigger is in
  `docs/INSTALL-LEDGER.md`.
- One tool per job, one fallback. A combination is listed only when the two pieces are actually wired
  to each other (a real recipe, not a wish).
- If a run shows the first choice failing twice for the environment (no GPU, missing key), move the job
  to the fallback and write the reason into the index `why` the same day.

## The routing table

| Job | First choice (ships today) | Fallback / when | Command or path |
|---|---|---|---|
| Vertical short from a trend/topic (DOPEAK) | our trend-short lane | AI Video Factory once provider keys exist | `/opt/data/scripts/run_trend_short.sh` |
| CS/tech short, ALGORHYTHM + IG | `cs-videos` uploader | repo-short lane (cron Wed/Sat) | `workspace/cs-videos/yt_uploader.py` |
| Narrated slideshow long-form | `faceless-youtube` pipeline | — | `workspace/faceless-youtube/` |
| Motion-graphics film (HTML → MP4) | `motionmaxxing` | film-toolpromo format file | `workspace/motionmaxxing/` + `team/formats/tool-promo-40s.md` |
| Physics / 3D B-roll clip | **MuJoCo** (212k steps/s, CPU) | Blender headless (`bpy` wheel) for real geometry | `workspace/physics-broll/render.py` |
| ASCII bumper / intro sting | **ascii.rest** + headless Chrome | none needed | `workspace/ascii-rest-demo/ascii_bumper.mjs` |
| Topic → full episode with approvals, cost ledger, Short | **AI Video Factory** `consider` — render+package verified, generation needs `FAL_KEY`/`GEMINI_API_KEY` + `ELEVENLABS_API_KEY` + agent | our own pipeline above, which needs no keys | `workspace/ai-video-factory` → `pnpm tx render-demo` |
| Keyframes / stylised stills | **huashu-art-motion** `consider` (~40 s/frame) | ClaudeAnimationBase `use` (19 s/frame) for motion, not stills | — |
| Thumbnail | our render + `video-thumbnail-design` skill | ASCII/typographic variant | `workspace/team/formats/` |
| Persian voice-over | `edge-tts` (fa-IR-FaridNeural) | ElevenLabs when a key exists | `/opt/data/home/.local/bin/edge-tts` |
| Subtitle quality gate | **srt-subtitle-quality-checker** (stdlib) | manual cue count | `skills` copy; ran 120 cues / 0 HIGH on ep01 |
| Prompt or asset sourcing | **prompts.chat** MCP (17 tools, no key) | `prompts-cli/pmcp.py search` | `workspace/prompts-cli/pmcp.py` |
| Clone a web app clean-room | **Replica skill** (11 skills, stdlib tools) | `clone-website` skill for a single page | `workspace/booking-clone` is the reference build |
| Read a page the plain fetch cannot | `browser_exec` + page JSON | `blocked-page-recovery` (r.jina.ai reader) | skill `web/blocked-page-recovery` |
| Download a post/reel | `yt-dlp` → browser for carousels | Instagram page-JSON fast path | `workspace/downloads/<id>/` |
| Local LLM for batch text | **llama.cpp** (2B at usable speed) | **colibri** / **Edge0** for big MoE, 6-11 tok/s | see entry `why` for measured tok/s |
| PDF / DOCX deliverable | `pdf`, `docx`, `persian-rtl-documents` skills | `branded-pdf-presentation` | `img2pdf` for slide-per-page |
| Code work by another agent | `claude-code` / `codex` / `opencode` skills | ECC `consider` — only the missing phase checklists | — |
| Network / VPN (Iran) | **usque** (WARP/MASQUE) | rVPN `consider` (needs a VPS) | skill `censorship-circumvention` |
| Remember / recall | `gabimaru-memory` SQLite+FTS5 | `toolbox` repo for tool verdicts | `workspace/gabimaru-memory/brief.py` |

## Combinations that are actually wired

These are chains, not lists — each one has produced a file on this box:

1. **Short, end to end (no keys):** topic → script (LLM) → `edge-tts` Persian/German voice →
   stills or B-roll (`physics-broll/render.py`, `motionmaxxing`) → ffmpeg cut with real motion →
   `srt-subtitle-quality-checker` gate → `post_guard` → uploader. This is the default money path.
2. **Episode with gates:** AI Video Factory for script/shot-plan/art *structure* + its audit and cost
   ledger — but only after the keys land; today its render half is what we borrow (packaging, audit,
   9:16 cut from the horizontal master).
3. **Fact-check a reel:** `yt-dlp` → Whisper (Groq) → frames → GitHub/HF/release APIs → `toolbox`
   entry. Four API calls turn "the caption says" into a verdict.
4. **Thumbnail:** art direction from a style pack / `code-animation-prompts` vocabulary → render at
   1280×720 → contrast pass (`replica-test` imgdiff) before upload.

## The daily loop (what "use it every day" means here)

- **05:10 UTC** — `toolbox daily refresh` re-reads stars/licence/last-push for all entries and pushes
  any numeric change. Numbers older than a day are a bug, not a memory.
- **During the day** — every content cron picks its tool from the table above; a tool that fails twice
  in the environment moves to its fallback and the reason lands in the index `why`.
- **When a `consider` tool's trigger fires** (a key arrives, a GPU exists, a client deliverable needs
  it) — it moves into the first column the same day it produces its first real output, and
  `docs/INSTALL-LEDGER.md` gets the verdict change.
- **Weekly** — `Weekly freshness audit` (Sun 04:00) flags reference files that pin a stale number;
  the router rows it invalidates get fixed in the same session.
