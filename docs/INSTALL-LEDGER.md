# Installed vs. recommended — 2026-11-22

Ahmad's rule: **take what we actually need and install/use it; whatever cannot be installed here goes on a
recommendation list, and it gets used once it can be.** This file is that ledger. `index.md` marks every
entry that is *not* installed with `[not installed]`; the verdict vocabulary is unchanged.

## Verdict → action

| Verdict | Meaning for this host | Action |
|---|---|---|
| `use` | installed and measured on a real box | nothing to do — this is the toolbox we run |
| `consider` | would pay, but needs a decision or a build step | install when a real use case shows up (see triggers) |
| `watch` | right tool, wrong hardware **here** | recommend only; use it on a GPU box when one exists |
| `park` / `skip` / `dead` | useless on a server / we do it better in code / gone | ignore |

## Ran and used today (2026-11-22)

- **Vork 0.6.1** — installed the Linux build at `/opt/data/workspace/vork-test`, `vork init` + `vork render --gpu cpu`
  produced a real still (61.5 s at 800x600 previs). Skill `media/vork-rendering`. Verdict moved to `watch`:
  one still is fine, but std/draft OOMs on 8 GB and the lavapipe image carries an artifact, so nothing
  watchable comes out of this host. **Trigger to revisit: a machine with an NVIDIA/AMD RTX-class GPU** (or the
  a CPU box with more RAM) — then it becomes the thumbnail/product-shot renderer.
- **AI-Youtube-Shorts-Generator** — already ran end to end on our own case-file ep01 (transcription 120
  segments in ~2 min, 2 shorts rendered, four breakages pinned). Moved to `use`: the reusable half is the
  highlight ranking, not its centre-crop.

## Ran and used today (2026-11-23)

- **AI Video Factory 0.6.8** (ersinkoc/AI-Video-Factory) — installed at `/opt/data/workspace/ai-video-factory`
  and ran the documented no-key path end to end: `render-demo` (3-shot synthetic episode) →
  `episode approve … preview` → `--only render` / `--only package` / `--only short`. Out came 1080p30
  9.8 s H.264+AAC, a 304 B `.srt`, a 1280x720 thumbnail and a 1080x1920 Short in ~2.5 min, with the
  repo's own video audit reporting 0 findings and $0.0000 agent cost. Verdict `consider`, **not** `use`:
  the generation stages need `FAL_KEY`/`GEMINI_API_KEY` + `ELEVENLABS_API_KEY` + a Claude/ACP agent and
  this box holds only `OPENROUTER_API_KEY`. **Trigger: one paid provider set + one episode we want to
  publish** — then run it against our faceless-youtube pipeline on the same topic and keep the cheaper
  per finished minute.

## Recommendation list — install when the trigger fires

| Tool | Verdict | Trigger / what installing it buys |
|---|---|---|
| Vork | `watch` | GPU box → code-deterministic 3D stills, thumbnails, product shots |
| ECC | `consider` | 314 skills; useful parts already imported (12 Hermes skills) — install only the missing phase checklists |
| awesome-llm-apps | `consider` | cloned already (163 MB); pick **one** app to productise with billing, not the collection |
| MoneyPrinterTurbo | `consider` | topic→9:16 video; needs provider keys, use for a client deliverable first |
| Cal.com (cal.diy) | `consider` | when IT work needs a booking link (domain + TLS + mail first) |
| huashu-art-motion | `consider` | hand-drawn/painterly keyframes; ~40 s/frame → keyframes only |
| anidoodle | `consider` | sketch illustration for shorts; install when a storyboard asks for it |
| Claude Blender Skills | `consider` | Blender via MCP; pairs with `blender-headless-render` on CPU |
| rVPN | `consider` | private VPN for the family; needs a VPS |
| Masque Config Generator | `consider` | WARP/MASQUE configs; the safe half (`usque`) is already in use |

## Rules that keep this honest

- A tool is `use` only after it ran on real input here — a README is not a verdict.
- Marking something `[not installed]` is not a downgrade: it is the difference between "we can" and "we do".
- Every new reel/repo gets a line in `index.md` **and** a row here if it is not installed.
