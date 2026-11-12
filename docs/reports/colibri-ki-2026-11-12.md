# colibri on the ki home box — measured 2026-11-12

PDF: `docs/reports/colibri-ki-2026-11-12.pdf` · raw data: `data/colibri-ki.json`

## What was tested

`JustVugg/colibri` v2.1.0 (Apache-2.0, C) on the ki home box: Ubuntu 26.04.1, Intel i5-10500T
(6C/12T, 2.3-3.8 GHz), 30 GB RAM, SSD, no GPU. Built from source with gcc 15.2
(`make -C c portable`, then the per-family engine with `ARCH=native`).

## Measured (Qwen3.6-35B-A3B, int4/gs64, 23 GB, served on 127.0.0.1:8000/v1, temperature 0)

| prompt | tokens in | tokens out | TTFT | decode tok/s | tokens/min | disk read |
|---|---|---|---|---|---|---|
| short_en | 31 | 45 | 0.717 s | 11.56 | 585.7 | 54 MB |
| german | 32 | 62 | 0.530 s | 11.57 | 631.6 | 54 MB |
| long_en | 34 | 160 | 0.766 s | 11.46 | 651.7 | 156 MB |

RSS 14.5-14.9 GB, MemAvailable fell 16.3 -> 15.5 GB. The model is fully resident in RAM, so the
vendor's "6.0 tok/s on CPU" is conservative here: measured **11.5 tok/s** (1.9x) on 12 threads with
a 30 GB RAM cache.

## Fit (the tool's own `setup --list` on that box: 32.8 GB RAM seen, 753 GB free)

qwen36-35b 23 GB good · qwen3-coder-30b 19 GB good · deepseek-v4-flash-reap 85 GB good ·
deepseek-v4-flash 167 GB good · mimo-v2.6-flash 172 GB tight · qwen38-flash-next 186 GB good ·
glm-5.3 419 GB good · **glm-5.2 (744B) 429 GB good** (the tool puts 11.9 GB of dense weights in RAM) ·
inkling 514 GB needs 120 GB RAM · mimo-v2.6-pro 564 GB needs 54 GB RAM · kimi-k3 1.5 T needs 1594 GB disk.

GLM-5.2 was then downloaded and measured for real - see the next section. "good" means *it fits and it
starts*, not *it is fast*.

## Measured (GLM-5.2, 744B, int4, 429 GB on disk, served on 127.0.0.1:8000/v1, temperature 0)

Download finished 2026-11-12 11:15 UTC: 429 GB in **3.23 h** at an average **36.9 MB/s**, resumable.
Engine: `python3 c/coli serve --model ~/colibri-models/glm-5.2 --port 8000` (model id `glm-5.2-colibri`,
32768 ctx, KV16 latent, MTP speculation draft=1). Placement on 30 GB: dense part **11.9 GB in RAM**,
expert cache auto-capped to **2 slots/layer** (21.5 MB avg x 76 layers) plus a 0.5 GB pinned hot set.

| prompt | tokens in | tokens out | TTFT | decode tok/s | tokens/min | total | disk read |
|---|---|---|---|---|---|---|---|
| short_en | 24 | 33 | 281.96 s | 0.03 | 1.4 | 1378.8 s | 617 GB |
| german | 26 | 48 | 272.28 s | 0.03 | 1.7 | 1671.6 s | 1330 GB |
| long_en | 28 | 48 | 323.27 s | 0.03 | 1.5 | 1863.1 s | 2129 GB |

RSS 17.5-18.4 GB, MemAvailable 12.7 -> 12.0 GB. Bench run with `COLI_MAX_TOKENS=48` because 744B on
this CPU decodes at ~0.03 tok/s (each prompt took 23-31 min end to end).

Verdict: **the 744B model really runs on a 30 GB no-GPU box, and it is not usable interactively** - one
token every ~33 seconds, TTFT ~4.7 min, and the expert cache is too small to help: the three requests
read 617 GB / 1330 GB / 2129 GB from the SSD, i.e. ~19 GB of disk traffic per generated token (2.2 TB
total, ~5 full passes over the 429 GB model). The reel's claim "744B on an ordinary PC" is true as a
statement about *running*, false as a statement about *using*. The same box does 11.5 tok/s on a
35B-A3B - 380x faster - so 35B is the interactive choice and 744B is a demo/overnight-batch choice.

## Install (Ubuntu)

```bash
sudo apt install -y git python3 build-essential
git clone --depth 1 https://github.com/JustVugg/colibri ~/colibri-moe/colibri
cd ~/colibri-moe/colibri
make -C c portable -j$(nproc)
python3 c/coli setup --list                 # what fits this machine, no download
python3 c/coli setup --model qwen36-35b --yes
curl -s http://127.0.0.1:8000/v1/models
```

Benchmark script: `/opt/data/workspace/colibri-moe/bench_api.py` (stdlib only; reads
`/proc/<pid>/io` and RSS; streams with `stream_options.include_usage`).

German edition of the same report: `docs/reports/colibri-ki-2026-11-12-de.pdf` (2 pages, LTR, same numbers).
