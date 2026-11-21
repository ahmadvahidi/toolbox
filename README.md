# Toolbox — everything Gabimaru has actually checked

A working inventory of tools, libraries and claims that came in through forwards, reels and
conversations — each one verified against the real repository, with a verdict for **this**
machine: a headless Linux box, 6 cores, 7 GB RAM, **no GPU**, running Hermes, Telegram bots and
a YouTube pipeline.

Numbers refreshed from `api.github.com` on **2026-11-21** by `tools/verify.py`.
Stars are a snapshot, not a quality score.

**Verdicts** — `use` shipped/installed · `consider` worth it, needs a decision · `watch` right tool, needs hardware we do not have · `park` useful to a human, useless on a server · `skip` we already do it better with code · `dead` repo gone or abandoned.

## Index

| | Tool | What it is | ★ | Licence | Last push |
|---|---|---|---:|---|---|
| ✅ in use | **[prompts.chat](https://github.com/f/prompts.chat)** | Open prompt + agent-skill library (2,916 prompts incl. 650 image and 89 video, 177 multi-file agent skills) with a stateless MCP endpoint and a Claude Code plugin | 178,083 | NOASSERTION | 2026-11-21 |
| ✅ in use | **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | CPU/GPU inference for GGUF models | 135,885 | MIT | 2026-11-21 |
| ✅ in use | **[colibri](https://github.com/JustVugg/colibri)** | C engine that streams MoE expert weights from NVMe, so 300B-1.5T models (GLM-5.2 744B, DeepSeek V4, Kimi K3) run on CPU-only machines; OpenAI/Anthropic API, dashboard, MCP server | 52,516 | Apache-2.0 | 2026-11-21 |
| ✅ in use | **[MuJoCo](https://github.com/google-deepmind/mujoco)** | Google DeepMind physics engine (rigid bodies, contacts, actuators): robot sim and physical animation, Python bindings, Apache-2.0 | 18,359 | Apache-2.0 | 2026-11-21 |
| ✅ in use | **[Edge0 (edge0-infer)](https://github.com/Edge0-AI/Edge0)** | Streaming MoE inference engine: 35B-A3B (Qwen3.6-35B-A3B, 4-bit) with expert weights on SSD, a trained prerouter and Recover-LoRA | 12,158 | Apache-2.0 | 2026-11-20 |
| ✅ in use | **[Replica skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app clean-room: recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy, with six stdlib-only Python tools | 10,168 | MIT | 2026-10-03 |
| ✅ in use | **[blender-skills](https://github.com/arjun988/blender-skills)** | 94 specialist Blender skills for Cursor, Claude Code, Kiro and Codex, plus an MCP route from blockout to engine export. | 4,505 | MIT | 2026-11-06 |
| ✅ in use | **[ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase)** | Clawd character kit for p5.brush: 31 acted emotions, an 11s demo, ANIMATION_GUIDE | 3,151 | MIT | 2026-09-24 |
| ✅ in use | **[LivLiv Player](https://github.com/livliv-dev/player)** | 2.5D avatar player for the web: WebGL2, ~30KB core, lip sync + MediaPipe face tracking in-browser, VRM/PNGTuber support, 21 sample characters | 1,611 | Apache-2.0 | 2026-11-18 |
| ✅ in use | **[usque](https://github.com/Diniboy1123/usque)** | Open-source Cloudflare WARP MASQUE client | 1,548 | MIT | 2026-07-20 |
| ✅ in use | **[code-animation-prompts](https://github.com/XiaoyeCodes/code-animation-prompts)** | 341 code-rendered animation styles with prompts | 1,358 | NOASSERTION | 2026-11-05 |
| ✅ in use | **[ascii.rest](https://github.com/bas3line/ascii)** | 240 animated ASCII pieces for the web, one <ascii-art> tag, MIT | 1,266 | MIT | 2026-11-15 |
| 🟡 consider | **[ECC](https://github.com/affaan-m/ECC)** | 299k-star agent harness: 314 skills, 71 agents, 98 commands (plan→code→test→review) | 307,944 | MIT | 2026-11-20 |
| 🟡 consider | **[awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** | 57 runnable AI app folders (agents, RAG, voice): Streamlit demos, ~17.7k Python lines total, Apache-2.0 | 145,235 | Apache-2.0 | 2026-11-18 |
| 🟡 consider | **[MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)** | Topic or keyword in, finished 9:16 video out: LLM script -> footage search keywords -> stock clips -> subtitles -> BGM -> render. WebUI plus HTTP API; provider-agnostic (many LLM keys, Pexels/Pixabay/Coverr or local material for footage). | 144,860 | MIT | 2026-11-21 |
| 🟡 consider | **[Cal.com (cal.diy)](https://github.com/calcom/cal.diy)** | Self-hosted scheduling pages (Calendly alternative) | 50,270 | MIT | 2026-11-13 |
| 🟡 consider | **[huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Claude skill collection for hand-drawn and painterly motion | 7,359 | MIT | 2026-11-18 |
| 🟡 consider | **[AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)** | Long-form -> 9:16 shorts: faster-whisper transcription, LLM highlight ranking (OpenAI/Gemini), OpenCV face-tracking crop | 6,376 | MIT | 2026-11-20 |
| 🟡 consider | **[anidoodle](https://github.com/alexgreensh/anidoodle)** | Animated doodle/sketch skill for Claude | 1,900 | Apache-2.0 | 2026-11-05 |
| 🟡 consider | **[rVPN](https://github.com/PDG-Global/rVPN-core)** | Stealth VPN protocol in Rust: TLS 1.3 + WebSocket transport, X3DH + Double Ratchet, pooled multiplexing, decoy website behind the endpoint | 269 | NOASSERTION | 2026-11-19 |
| 🟡 consider | **[Claude Blender Skills](https://github.com/mromidev/claude-blender-skills)** | MIT pack of 3 Blender film-production workflows (night FPV drone shot, forest scene, snowy-night short) with real Blender-Python scripts and a 127.0.0.1:9876 bridge an LLM drives | 173 | MIT | 2026-10-25 |
| 🟡 consider | **[Masque Config Generator](https://github.com/DarknessShade/Masque-Generator)** | One-page generator for Xray WARP-over-MASQUE configs (P-256 keys) | 36 | MIT | 2026-11-03 |
| 👀 watch | **[VoiceStudio](https://github.com/debpalash/VoiceStudio)** | Local voice cloning and dubbing (ElevenLabs alternative) | 115,544 | AGPL-3.0 | 2026-11-20 |
| 👀 watch | **[AgentPilot](https://github.com/HKUDS/AgentPilot)** | 9B strategy model that picks the next move for a bigger agent, plus a skill workspace and an RSI benchmark arena | 8,125 | MIT | 2026-11-12 |
| 👀 watch | **[StableGen](https://github.com/sakalond/stablegen)** | Blender add-on: prompt to textured, rigged 3D character (TRELLIS.2 + SkinTokens + Marigold) | 1,699 | GPL-3.0 | 2026-11-04 |
| 👀 watch | **[Weight-Space Programming](https://github.com/RikiyaT/lm_understand-logs)** | MIT CSAIL experiment: an LLM edits another model's raw weights to fix reasoning loops | 1,283 | NOASSERTION | 2026-10-29 |
| 👀 watch | **[InferSSD](https://github.com/wici-ai/inferssd)** | Streams MoE experts from SSD so models far larger than RAM/VRAM run on ordinary machines. Built on llama.cpp, standard GGUF, browser chat + OpenAI-compatible API. Runs DeepSeek-V4.1-Flash-1017 (763B total), Muse-Spark-Open (816B), Qwen3.6-35B-A3B, Gemma4 E4B. | 1,276 | Apache-2.0 | 2026-11-20 |
| 👀 watch | **[MiniMax H3 integrations](https://github.com/MiniMax-AI/awesome-minimax-h3-integration)** | Community index for MiniMax H3, a video model that generates up to 15 s clips at up to 2K with NATIVE stereo audio. Two variants: FL2VA (0-2 keyframe images) and Ref2VA (up to 9 images, 3 clips of 2-15 s, 3 audio clips, 12 files total). Lists checkpoints down to NF4 that run from 8 GB VRAM via DiffSynth-Studio, plus Apple-Silicon engines (h3.c, Draw Things, mlx-serve). | 587 | none | 2026-11-12 |
| 👀 watch | **[Avatar Creator (AVC Suite)](https://www.avcsuite.com/)** | Commercial Blender add-on: build / wrap / sync characters, convert AI meshes and retarget to MetaHuman or Genesis 9 | — | Commercial | 2026-10-14 |
| 🅿️ park | **[OpenCut](https://github.com/OpenCut-app/OpenCut)** | Browser timeline video editor (CapCut alternative) | 99,049 | MIT | 2026-09-24 |
| 🅿️ park | **[Plane](https://github.com/makeplane/plane)** | Self-hosted Jira/Linear alternative | 62,878 | AGPL-3.0 | 2026-11-20 |
| 🅿️ park | **[Chatwoot](https://github.com/chatwoot/chatwoot)** | Self-hosted Intercom alternative | 40,270 | NOASSERTION | 2026-11-20 |
| 🅿️ park | **[Cap](https://github.com/CapSoftware/Cap)** | Open-source Loom alternative for screen recording | 25,353 | NOASSERTION | 2026-11-21 |
| 🅿️ park | **[Dyad](https://github.com/dyad-sh/dyad)** | Local Lovable-style app builder | 22,339 | NOASSERTION | 2026-11-20 |
| 🅿️ park | **[TWP-CF](https://github.com/MHDLabs/TWP-CF)** | Telegram web proxy on Cloudflare Workers (MTProto over websocket) | 21 | GPL-3.0 | 2026-11-11 |
| 🅿️ park | **Muse-Glimmer-30B** | Apache-2.0 27.85B MoE GGUF, Q4_K_M 16.76 GB | — | — | — |
| 🅿️ park | **[Cinemap](https://github.com/cinemap.video (TapNow))** | 3D previs from text: build an editable set, keyframe props/actors, phone-as-camera via QR, then hand the clip to Seedance 2.5 as a camera reference | — | None | None |
| 🅿️ park | **[ClipUtils](https://github.com/cliputils.com)** | 32 browser tools: trim/compress/convert, remove music keeping the voice, auto subtitles, video translation/dubbing, TTS, HEIC/WebP conversion, background removal | — | None | None |
| ⏭️ skip | **[AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)** | Self-hosted Notion alternative | 79,285 | AGPL-3.0 | 2026-11-15 |
| ⏭️ skip | **[TwinDesk](https://github.com/inukaasith/twindesk)** | Share mouse, keyboard, files and clipboard across machines (KVM) | 4,333 | GPL-3.0 | 2026-11-18 |
| ⏭️ skip | **[FloMorphic getting-started](https://github.com/FloMorphic/getting-started)** | Low-code graph platform for agent pipelines, MCP + RAG + human oversight | 13 | Apache-2.0 | 2026-11-21 |
| ⏭️ skip | **[tree-of-neuron](https://github.com/fermow/tree-of-neuron)** | Interactive 47-milestone history of neuroscience | 4 | none | 2026-10-15 |
| ⚰️ dead | **OpenSEO (claim)** | Supposed free Semrush alternative from the same carousel | — | — | — |
| ⚰️ dead | **OpenWhispr (claim)** | Supposed open-source Wispr Flow dictation app | — | — | — |

## How this stays current

```bash
python3 tools/verify.py          # refresh stars/licence/last-push, rewrite this file
python3 tools/verify.py --push   # same, then commit and push if anything moved
```

A cron job runs that every morning, so the table is never more than a day old and this file
never has to live in an agent's context to stay true.

## Adding an entry

Append an object to `data/tools.json`:

```json
{"name": "…", "repo": "owner/name", "what": "one line", "verdict": "park",
 "why": "why it does or does not change what we do", "date": "2026-11-04",
 "tags": ["video", "gpu"]}
```

`repo` may be omitted for things that are not on GitHub (a model on Hugging Face, a claim from a
reel). `why` is the part that matters: the verdict without a reason rots into folklore.
