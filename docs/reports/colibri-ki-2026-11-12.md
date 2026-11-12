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
glm-5.3 419 GB good · **glm-5.2 (744B) 429 GB good** (only 9.9 GB must stay in RAM) ·
inkling 514 GB needs 120 GB RAM · mimo-v2.6-pro 564 GB needs 54 GB RAM · kimi-k3 1.5 T needs 1594 GB disk.

GLM-5.2 download started on the same box: 429 GB at a measured 38.5 MB/s (ETA ~3 h at 08:10 UTC).
Its benchmark is appended to the PDF when it completes.

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
