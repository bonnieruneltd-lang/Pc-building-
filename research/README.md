# Research provenance

Raw Tavily API responses collected on **2026-11-09** with `scripts/tavily_search.py`. Nothing in the
docs is invented: each file backs one or more claims in `README.md`, `docs/pricing-and-sources.md`
and `docs/bazzite-setup.md`.

| File | Query | What it establishes |
|---|---|---|
| `q01_balzzite.json` | "balzzite minecraft" | "balzzite" resolves to Bazzite, the Linux gaming OS |
| `q02_bazzite.json` | "bazzite modded minecraft gaming pc" | Bazzite + Prism Launcher is the normal Minecraft path on Linux |
| `q03_balzzite2.json` | "balzzite mod minecraft curseforge modrinth" | rules out a modpack named "balzzite" |
| `q10_cpu.json` | best CPU for modded MC | cache/single-thread guidance, X3D preference |
| `q11_gpu.json` | best GPU for MC shaders 2026 | 9070 XT vs 5080 value + Linux performance retention |
| `q12_bazzite_hw.json` | Bazzite AMD vs NVIDIA | AMD objectively better, NVIDIA worse on Bazzite |
| `q20_9950x3d2.json` | 9950X3D2 specs/price | $899, 16C, 208 MB — considered and rejected |
| `q21_9850x3d.json` | 9850X3D specs | 8C/16T, 96 MB L3, 120 W, $499 MSRP, Jan-2026 launch |
| `q22_ddr5.json` | DDR5 prices Nov 2026 | 32 GB $479.99 median $554.99, +473% vs low |
| `q30_gpus.json` | RTX 50 Super lineup | 5080 Super / 5070 Ti Super rumored 24 GB, delayed |
| `q31_gpu_prices.json` | RX 9070 XT price Nov 2026 | $710–$950 range, AMD price hikes |
| `q32_ssd.json` | best SSD for gaming 2026 | NAND shortage, 2 TB pricing up 80–150% |
| `q40_5090.json` | RTX 5090 street price | $4,999–$9,400 — the "do not buy" data point |
| `q41_bazzite_nvidia.json` | Bazzite NVIDIA status | driver regressions, Wayland instability |
| `q42_dh.json` | Distant Horizons VRAM | 6 GB recommended, 10 GB heap caution |
| `q50_9850_price.json` | 9850X3D in-stock price | $484 Newegg in stock on 2026-11-09 |
| `q51_64gb.json` | 64 GB DDR5-6000 CL30 price | $929.99–$1,274.99 |
| `q52_mobo.json` | best B850 2026 | B850 Eagle / X870 Tomahawk pricing |
| `q60_9070xt.json` | 9070 XT Newegg | $709.99 XFX Swift deal, $949.99+ listings |
| `q61_ssd_price.json` | 2 TB NVMe price Nov 2026 | SN850X $379.99, 990 Pro $389.99 |
| `q62_psu.json` | best 1000 W ATX 3.1 PSU | MSI MPG A1000GS $109.99 |
| `q70_5070tis.json` | 5070 Ti Super availability | not officially priced/available |
| `q71_9850_mc.json` | 9850X3D review data | +3–4% games, +6–7% single-thread vs 9800X3D |
| `q72_mc_tuning.json` | modded MC JVM/settings | ZGC, 6–8 GB vs 12–16 GB heap guidance |
| `q80_case.json` | best PC case 2026 | Lancool 217 $119.99, Lancool 207 ~$80 |
| `q81_cooler.json` | best cooler for 9850X3D | Peerless Assassin $35, LF III Pro 360 $94 |
| `q82_mcversion.json` | Minecraft 26.3 modding | version scheme + Sodium/Iris incompatibility |
| `q90_bazzite_rel.json` | Bazzite 44 release | kernel 7.2, Mesa 26.2.x, GUI updater |
| `q91_modpack.json` | ATM-class pack RAM | 12–16 GB allocation |
| `q92_monitor.json` | 1440p 240 Hz OLED prices | $394–$549, MSI 272QP X24 at $400 |
| `q93_5080s.json` | RTX 5080 Super status | delayed, 5080 at ~$2,200 |
| `q94_budget.json` | 9060 XT 16 GB price | $519 new, low $419 |
| `q95_midcpu.json` | 9600X / 9700X price | $219 / $341 on Newegg |

Reproduce any of them:

```bash
export TAVILY_API_KEY=...
python3 scripts/tavily_search.py --query "your query" --n 6 --out research/new.json
```
