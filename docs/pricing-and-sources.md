# Pricing and sources — all data dated 2026-11-09

Every price in `builds/*.json` comes from the search results below (Tavily API, run on 2026-11-09).
Prices in this market move weekly and several sources are trackers rather than first-party store
pages, so **treat these as "what it costs this week", and re-check at checkout.**

Raw API responses are committed in [`../research/`](../research/) — file names map to the rows here.

---

## 1. CPUs

| Part | Price | Source | Notes |
|---|---|---|---|
| **Ryzen 7 9850X3D** | **$484.00** (Newegg, in stock) | [Newegg SKU](https://www.newegg.com/amd-ryzen-7-9850x3d-ryzen-7-9000-series-granite-ridge-socket-am5-desktop-processor/p/N82E16819113934) · [specs](https://www.techpowerup.com/cpu-specs/ryzen-7-9850x3d.c4301) · [Tom's review](https://www.tomshardware.com/pc-components/cpus/amd-ryzen-7-9850x3d-review) | 8C/16T, 96 MB L3, 4.7/5.6 GHz, 120 W, AM5. MSRP $499; launched 2026-01-29. Reviews: ~3–4% faster than 9800X3D in games, ~6–7% in single-thread. |
| Ryzen 7 9700X | $341.00 (Newegg) | [Newegg](https://www.newegg.com/amd-ryzen-7-9000-series-ryzen-7-9700x-granite-ridge-socket-am5-desktop-cpu-processor/p/N82E16819113843) | fallback; 32 MB L3 means a noticeable chunk-render penalty in MC. |
| Ryzen 5 9600X | $219.00 (Newegg) | [Newegg](https://www.newegg.com/amd-ryzen-5-9000-series-ryzen-5-9600x-granite-ridge-socket-am5-desktop-cpu-processor/p/N82E16819113844) | the "cut here if you must" option (saves $265, costs ~20–30% chunk-load speed). |
| Ryzen 9 9950X3D2 Dual Edition | $899 MSRP | [StorageReview](https://www.storagereview.com/review/amd-ryzen-9-9950x3d2-dual-edition-review-3d-v-cache-on-both-ccds) · [Ars Technica](https://arstechnica.com/gadgets/2026/04/amd-ryzen-9-9950x3d2-dual-edition-review-tons-of-cache-for-tons-of-dollars) | 16C, 208 MB, 200 W. Rejected: dual-CCD latency, no Minecraft benefit. |

## 2. Memory — the painful one

| Part | Price | Source | Notes |
|---|---|---|---|
| 32 GB (2x16) DDR5-6000 CL30 | **$479.99** | [DDR5 price index](https://tech-insider.org/ddr5-ram-prices-2026-pc-builders) · [Tom's RAM price index](https://www.tomshardware.com/pc-components/ram/ram-price-index-2026-lowest-price-on-ddr5-and-ddr4-memory-of-all-capacities) | lowest tracked 32 GB kit at Amazon on 2026-11-02; median across 22 listings $554.99. Up ~473% from the $72 all-time low. |
| 64 GB (2x32) DDR5-6000 CL30 | **$1,049.99** (Build A) | [PGrid 64 GB index](https://www.pgrid.app/us/advice/compare-64gb-ddr5-ram) (83 kits, from $929.99) · [Corsair kit](https://www.corsair.com/us/en/p/memory/cmk64gx5m2b6000z30/vengeance-64gb-2x32gb-ddr5-dram-6000mt-s-cl30-amd-expo-intel-xmp-memory-kit-cmk64gx5m2b6000z30) ($1,274.99) | $1,049.99 is a realistic mid-market figure for an EXPO 6000 CL30 kit; range is $930–$1,275. |

## 3. GPUs

| Part | Price | Source | Notes |
|---|---|---|---|
| **RX 9070 XT 16 GB** | **$729.99** (Build A/B) | [PC Guide deal](https://www.pcguide.com/deals/we-found-the-cheapest-rx-9070-xt-on-newegg-with-a-solid-deal-worth-talking-about-right-now) (XFX Swift $709.99, Oct 2026) · [Newegg listings](https://www.newegg.com/p/pl?d=rx+9070+xt) · [TechSpot Q4 2026 pricing](https://www.techspot.com/article/3192-gpu-pricing-q4-2026) | Street range $710–$950; AMD hiked Radeon prices twice in two months. 16 GB VRAM, 304 W. |
| RX 9060 XT 16 GB | $519.00 (Build C) | [price history](https://bestvaluegpu.com/history/new-and-used-rx-9060-xt-16gb-price-history-and-specs) | all-time low $419; flash sales as low as $339. 16 GB VRAM at the entry price is the point. |
| RTX 5080 | ~$2,200 (+120% over MSRP) | [TechRadar](https://www.techradar.com/computing/gpu/the-probability-is-extremely-high-that-nvidias-rumored-rtx-5080-super-has-been-delayed-and-with-gpu-prices-rocketing-upwards-the-future-looks-bleak) | Rejected on price. |
| RTX 5080 Super 24 GB | not buyable — delayed toward 2027 | [TechPowerUp](https://www.techpowerup.com/354315/nvidia-reportedly-moves-up-rtx-5080-24-gb-launch) | 3 GB GDDR7 pricing is the blocker. |
| RTX 5090 | $4,999 new / $5,000–$9,400 street | [TechPowerUp](https://www.techpowerup.com/354445/gpu-prices-up-again-in-october-rtx-5090-now-sells-for-262-over-msrp-worldwide) · [price history](https://bestvaluegpu.com/history/new-and-used-rtx-5090-price-history-and-specs) | Rejected: 6–7× the price, no Minecraft benefit. |

## 4. Everything else (storage, PSU, cooling, case, board, monitor)

| Part | Price | Source |
|---|---|---|
| WD_BLACK SN850X 2 TB | $379.99 | [Best NVMe SSDs 2026](https://www.newegg.com/insider/best-nvme-ssds-2026) · [SSD price trend](https://dropreference.com/en/blog/news/ssd-price-increase-2026-nand-flash-crisis) |
| Samsung 990 Pro 2 TB (alternative) | $389.99 | [NVMe round-up](https://spektova.com/tech/us/reviews/best-nvme-ssds-2026) |
| MSI MPG A1000GS 1000 W ATX 3.1 | $109.99 (was $169.99) | [Newegg PSU guide](https://www.newegg.com/insider/best-power-supplies-in-2026-for-every-build) · [HWBusters tier list](https://hwbusters.com/best_picks/best-atxv3-pcie5-ready-psus-picks-hardware-busters) |
| Arctic Liquid Freezer III Pro 360 | $94.00 | [Cooler ranking](https://dreaming3d.net/blogs/news/best-cpu-coolers-air-liquid-ranked-for-2026) |
| Thermalright Peerless Assassin 120 SE V2 | $34.99 | [Cooler ranking](https://dreaming3d.net/blogs/news/best-cpu-coolers-air-liquid-ranked-for-2026) · [9800X3D cooler guide](https://dropreference.com/en/blog/guide/best-cpu-cooler-ryzen-7-9800x3d-2026) |
| Lian Li Lancool 217 (380 mm GPU) | $119.99 | [Case round-up](https://www.newegg.com/insider/best-mid-tower-pc-cases-for-airflow-and-aesthetics-in-2026) · [TechRepublic](https://www.techrepublic.com/article/news-best-pc-cases-2026) |
| Lian Li Lancool 207 | $79.99 | same as above |
| Gigabyte B850 Eagle WiFi 6E | $189.99 | [Tom's best motherboards](https://www.tomshardware.com/best-picks/best-motherboards) · [PC Guide B850 picks](https://www.pcguide.com/motherboard/guide/best-b850) |
| MSI MAG X870 Tomahawk WiFi | $259.99 | [Tom's best motherboards](https://www.tomshardware.com/best-picks/best-motherboards) |
| MSI MAG 272QP X24 27" 1440p 240 Hz QD-OLED | $399.99 | [PCWorld](https://www.pcworld.com/article/3063618/msis-oled-monitor-drops-to-430-1440p-240hz-27-inches.html) · [RTINGS 1440p picks](https://www.rtings.com/monitor/reviews/best/1440p-gaming-monitors) |
| Gigabyte MO27Q2A 1440p 240 Hz OLED | $394.00 | [RTINGS 1440p picks](https://www.rtings.com/monitor/reviews/best/1440p-gaming-monitors) |
| Acer Nitro VG277U 1440p 180 Hz IPS | $269.00 | [RTINGS 1440p picks](https://www.rtings.com/monitor/reviews/best/1440p-gaming-monitors) |

---

## 5. Software / platform claims, with their sources

| Claim | Source |
|---|---|
| Bazzite 44 ships kernel 7.2 with Mesa 26.2.x and a new gaming stack | [Linuxiac on Bazzite 44](https://linuxiac.com/bazzite-linux-44-lands-with-kernel-7-2-new-gaming-stack-and-gui-updater) · [release notes](https://github.com/ublue-os/bazzite/releases) |
| RX 9070 XT keeps ~92% of Windows performance on Bazzite (~94% on CachyOS) | [RX 9070 XT vs RTX 5080 on Windows 11 vs Linux](https://en.gamegpu.com/news/zhelezo/sravnenie-proizvoditelnosti-rx-9070-xt-i-rtx-5080-v-windows-11-i-linux-v-2026-godu) · [GamersNexus: Linux GPU benchmarks on Bazzite](http://gamersnexus.net/gpus/rip-windows-linux-gpu-gaming-benchmarks-bazzite) |
| AMD is better than NVIDIA on Bazzite; NVIDIA shows driver regressions | GamersNexus above · [Bazzite forum thread](https://universal-blue.discourse.group/t/bazzite-graphics-performance-compared-to-windows/4143) · [NVIDIA Wayland crashes since driver 580](https://forums.developer.nvidia.com/t/random-crashes-on-wayland-since-driver-580-on-linux/345527) · [Bazzite #5086](https://github.com/ublue-os/bazzite/issues/5086) |
| Prism Launcher + Bazzite has a long-session memory-growth pattern — cap `-Xmx` | [bazzite issue #4145](https://github.com/ublue-os/bazzite/issues/4145) |
| Newest Sodium is incompatible with Iris on MC 26.3 (crashes) — pin versions | [IrisShaders issue #3265](https://github.com/IrisShaders/Iris/issues/3265) |
| Distant Horizons wants 6 GB+ VRAM; reduce "Distant Generation" for CPU relief | [Distant Horizons (Modrinth)](https://modrinth.com/project/uCdwusMi) · [DH settings guide](https://distanthorizonsguide.com/guides/distant-horizons-best-settings) |
| Heavy "All the Mods"-class packs want 12–16 GB allocated | [Connect Hosting RAM guide](https://connecthosting.net/blog/how-much-ram-modded-minecraft-server) · [2026 modpack RAM list](https://prismnodes.com/blog/best-minecraft-modpacks-2026) |
| Low-pause GC (ZGC) recommended for modded MC + Distant Horizons | [Distant Horizons (Modrinth)](https://modrinth.com/project/uCdwusMi) |
| "balzzite" ⇒ Bazzite | [bazzite.gg](https://bazzite.gg) · [Minecraft-on-Bazzite thread](https://github.com/ublue-os/bazzite/issues/4145) |

---

## 6. How to re-price this list later

```bash
export TAVILY_API_KEY=...            # any Tavily key
python3 scripts/tavily_search.py \
  --query "RX 9070 XT price Newegg in stock" --days 30 --n 5 --out research/reprice_gpu.json
```

Then edit the `price` field in `builds/*.json` and re-run `python3 scripts/build_check.py` — the
totals, PSU load and compatibility checks all recompute from those JSON files.


