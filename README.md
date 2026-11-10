# Toolbox — everything Gabimaru has actually checked

A working inventory of tools, libraries and claims that came in through forwards, reels and
conversations — each one verified against the real repository, with a verdict for **this**
machine: a headless Linux box, 6 cores, 7 GB RAM, **no GPU**, running Hermes, Telegram bots and
a YouTube pipeline.

Numbers refreshed from `api.github.com` on **2026-11-10** by `tools/verify.py`.
Stars are a snapshot, not a quality score.

**Verdicts** — `use` shipped/installed · `consider` worth it, needs a decision · `watch` right tool, needs hardware we do not have · `park` useful to a human, useless on a server · `skip` we already do it better with code · `dead` repo gone or abandoned.

## Index

| | Tool | What it is | ★ | Licence | Last push |
|---|---|---|---:|---|---|
| ✅ in use | **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | CPU/GPU inference for GGUF models | 133,865 | MIT | 2026-11-10 |
| ✅ in use | **[MuJoCo](https://github.com/google-deepmind/mujoco)** | Google DeepMind physics engine (rigid bodies, contacts, actuators): robot sim and physical animation, Python bindings, Apache-2.0 | 17,015 | Apache-2.0 | 2026-11-10 |
| ✅ in use | **[ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase)** | Clawd character kit for p5.brush: 31 acted emotions, an 11s demo, ANIMATION_GUIDE | 2,811 | MIT | 2026-09-24 |
| ✅ in use | **[usque](https://github.com/Diniboy1123/usque)** | Open-source Cloudflare WARP MASQUE client | 1,529 | MIT | 2026-07-20 |
| ✅ in use | **[LivLiv Player](https://github.com/livliv-dev/player)** | 2.5D avatar player for the web: WebGL2, ~30KB core, lip sync + MediaPipe face tracking in-browser, VRM/PNGTuber support, 21 sample characters | 1,417 | Apache-2.0 | 2026-11-09 |
| ✅ in use | **[ascii.rest](https://github.com/bas3line/ascii)** | 240 animated ASCII pieces for the web, one <ascii-art> tag, MIT | 1,173 | MIT | 2026-11-08 |
| ✅ in use | **[code-animation-prompts](https://github.com/XiaoyeCodes/code-animation-prompts)** | 341 code-rendered animation styles with prompts | 893 | NOASSERTION | 2026-11-05 |
| 🟡 consider | **[ECC](https://github.com/affaan-m/ECC)** | 299k-star agent harness: 314 skills, 71 agents, 98 commands (plan→code→test→review) | 300,322 | MIT | 2026-11-09 |
| 🟡 consider | **[awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** | 57 runnable AI app folders (agents, RAG, voice): Streamlit demos, ~17.7k Python lines total, Apache-2.0 | 144,320 | Apache-2.0 | 2026-11-10 |
| 🟡 consider | **[Cal.com (cal.diy)](https://github.com/calcom/cal.diy)** | Self-hosted scheduling pages (Calendly alternative) | 49,870 | MIT | 2026-11-03 |
| 🟡 consider | **[huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Claude skill collection for hand-drawn and painterly motion | 6,633 | MIT | 2026-11-10 |
| 🟡 consider | **[AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)** | Long-form -> 9:16 shorts: faster-whisper transcription, LLM highlight ranking (OpenAI/Gemini), OpenCV face-tracking crop | 5,875 | MIT | 2026-11-09 |
| 🟡 consider | **[anidoodle](https://github.com/alexgreensh/anidoodle)** | Animated doodle/sketch skill for Claude | 1,543 | Apache-2.0 | 2026-11-05 |
| 🟡 consider | **[Masque Config Generator](https://github.com/DarknessShade/Masque-Generator)** | One-page generator for Xray WARP-over-MASQUE configs (P-256 keys) | 26 | MIT | 2026-11-03 |
| 👀 watch | **[VoiceStudio](https://github.com/debpalash/VoiceStudio)** | Local voice cloning and dubbing (ElevenLabs alternative) | 106,374 | AGPL-3.0 | 2026-11-10 |
| 👀 watch | **[AgentPilot](https://github.com/HKUDS/AgentPilot)** | 9B strategy model that picks the next move for a bigger agent, plus a skill workspace and an RSI benchmark arena | 7,983 | MIT | 2026-11-06 |
| 👀 watch | **[StableGen](https://github.com/sakalond/stablegen)** | Blender add-on: prompt to textured, rigged 3D character (TRELLIS.2 + SkinTokens + Marigold) | 1,633 | GPL-3.0 | 2026-11-04 |
| 👀 watch | **[Weight-Space Programming](https://github.com/RikiyaT/lm_understand-logs)** | MIT CSAIL experiment: an LLM edits another model's raw weights to fix reasoning loops | 1,172 | NOASSERTION | 2026-10-29 |
| 👀 watch | **[Avatar Creator (AVC Suite)](https://www.avcsuite.com/)** | Commercial Blender add-on: build / wrap / sync characters, convert AI meshes and retarget to MetaHuman or Genesis 9 | — | Commercial | 2026-10-14 |
| 🅿️ park | **[OpenCut](https://github.com/OpenCut-app/OpenCut)** | Browser timeline video editor (CapCut alternative) | 97,957 | MIT | 2026-09-24 |
| 🅿️ park | **[Plane](https://github.com/makeplane/plane)** | Self-hosted Jira/Linear alternative | 62,224 | AGPL-3.0 | 2026-11-09 |
| 🅿️ park | **[Chatwoot](https://github.com/chatwoot/chatwoot)** | Self-hosted Intercom alternative | 39,528 | NOASSERTION | 2026-11-10 |
| 🅿️ park | **[Cap](https://github.com/CapSoftware/Cap)** | Open-source Loom alternative for screen recording | 24,756 | NOASSERTION | 2026-11-10 |
| 🅿️ park | **[Dyad](https://github.com/dyad-sh/dyad)** | Local Lovable-style app builder | 22,251 | NOASSERTION | 2026-11-09 |
| 🅿️ park | **[TWP-CF](https://github.com/MHDLabs/TWP-CF)** | Telegram web proxy on Cloudflare Workers (MTProto over websocket) | 17 | GPL-3.0 | 2026-11-06 |
| 🅿️ park | **Muse-Glimmer-30B** | Apache-2.0 27.85B MoE GGUF, Q4_K_M 16.76 GB | — | — | — |
| 🅿️ park | **[Cinemap](https://github.com/cinemap.video (TapNow))** | 3D previs from text: build an editable set, keyframe props/actors, phone-as-camera via QR, then hand the clip to Seedance 2.5 as a camera reference | — | None | None |
| 🅿️ park | **[ClipUtils](https://github.com/cliputils.com)** | 32 browser tools: trim/compress/convert, remove music keeping the voice, auto subtitles, video translation/dubbing, TTS, HEIC/WebP conversion, background removal | — | None | None |
| ⏭️ skip | **[AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)** | Self-hosted Notion alternative | 78,602 | AGPL-3.0 | 2026-11-02 |
| ⏭️ skip | **[TwinDesk](https://github.com/inukaasith/twindesk)** | Share mouse, keyboard, files and clipboard across machines (KVM) | 3,849 | GPL-3.0 | 2026-11-09 |
| ⏭️ skip | **[FloMorphic getting-started](https://github.com/FloMorphic/getting-started)** | Low-code graph platform for agent pipelines, MCP + RAG + human oversight | 13 | Apache-2.0 | 2026-10-26 |
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
