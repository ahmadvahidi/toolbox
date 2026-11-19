# InferSSD — reference note (filed 2026-11-19)

Filed from a forwarded reel (@reporadarai, README-scroll promo, 38 s). Everything below was verified
against the repo, not read off the reel.

## What it is

`wici-ai/inferssd` — a C/C++ inference engine that **streams mixture-of-experts (MoE) weights from SSD**,
so a model that does not fit in RAM or VRAM still runs. It is built on `llama.cpp`, takes standard
**GGUF** files, ships a browser chat and an **OpenAI-compatible API**.

| Verified on api.github.com | value |
|---|---|
| stars | 1,235 |
| licence | Apache-2.0 |
| created | 2026-10-22 |
| last push | 2026-11-19 (alive, shipping) |
| archived | no |

Models it runs (from its own README): **DeepSeek-V4.1-Flash-1017** (763B total / 8–16B active),
**Muse-Spark-Open** (816B / 42B active), **Qwen3.6-35B-A3B**, **Gemma4 E4B**. Quantisations include
Q4_K_M, Q8_0, MXFP4 routed experts, plus community NVFP4/INT4 builds.

## Why it matters to us (not as our engine)

It benchmarks itself **head-to-head against Colibri** — the engine we already documented and shipped a
short about (`JustVugg/colibri`, toolbox entry, carded as `demo-colibri/`). That makes it:

1. a direct technical competitor to the stack we recommend on our own channel, and
2. the one topic where **we hold first-hand numbers for one side** of the comparison instead of
   repeating a reel.

## Hardware reality — the reason it is `watch`, not `use`

Every published benchmark row is a GPU box or a large unified-memory Mac:

| Hardware | CPU | GPU | Memory | SSD |
|---|---|---|---|---|
| MacBook Pro | Apple M5 Max (18) | 40-core | 48 GB unified | 2 TB internal |
| RTX 5060 Ti | Intel Core 3 100U (6) | RTX 5060 Ti | 8 GB + 16 GB VRAM | 2 TB PCIe 4 |
| RTX 5090 | Intel Core Ultra 5 230F (10) | RTX 5090 | 32 GB + 32 GB VRAM | 2 TB PCIe 5 |
| DGX Spark | NVIDIA GB10 (20) | Blackwell | 128 GB unified | 4 TB PCIe 5 |

Headline number from the reel, in context: **164.5 tok/s prefill** is the RTX 5090 row. Our box is
**6 cores / 7 GB RAM / no GPU** — below every row. The 763B model is out of reach by an order of
magnitude, not by a tuning step.

Realistic ceiling on this machine, extrapolating from the weakest published row (MacBook, 2.87 tok/s
decode on a 763B model): well under 1 tok/s. Not a production engine for us.

## What we would actually do with it (when hardware changes)

1. **A GPU with ≥8 GB VRAM** puts the RTX 5060 Ti row in reach: 75 tok/s prefill, 2.55 tok/s decode on
   the 763B model. At that point it is worth a real trial against Colibri on the same GGUF, same prompt,
   same 4K/256-token protocol the repo publishes.
2. **A 35B-class model on CPU** is the only near-term use: `Qwen3.6-35B-A3B` at ~3 B active is in the
   same class Edge0 and Colibri already handle on this box, so any trial must beat them on the same
   machine or it is not worth the install.
3. Install path for that trial: build from source (`llama.cpp` toolchain is already on the box), point
   `--model` at a GGUF, use the OpenAI-compatible endpoint, and measure with the repo's own protocol
   (decode over tokens 129–256 after a 4K prompt) so the numbers are comparable to its tables.

## Content angle (the best position for it right now)

**"Two engines, one SSD"** — a 30-40 s ALGORHYTHM short comparing InferSSD with Colibri, where we can
say from our own measurements what Colibri did on our box, and quote InferSSD's own table for the rest.
That honesty is the differentiator: the reel says "763B on less RAM" with no mention that every row
needs a GPU.

Do not produce it until the comparison can be run on identical hardware, or the short becomes the same
reel with a different logo.

## Traps

- **`763B params` is not `763B in RAM`.** The trick is SSDs, and the SSD must be fast (PCIe 4/5, or the
  internal NVMe); a SATA disk turns this into a slideshow.
- **Active vs total parameters.** Read "8–16B active" as the compute cost; the 763B is only the
  storage footprint.
- **Benchmark protocol matters.** The published numbers are prefill AND decode on a 4K prompt with
  256 output tokens, decode measured over tokens 129–256. Comparing a fresh short-prompt run against
  those tables is how a false verdict gets published.
- **The reel's watermarks and caption are not independent evidence.** It is a README scroll; every
  number in it comes from the repo's own tables.
