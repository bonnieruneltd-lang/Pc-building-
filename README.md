# The Bazzite Modded-Minecraft Machine (Nov 2026)

A parts list, a compatibility-validated bill of materials, and a setup guide for one specific
job: **heavily modded Minecraft with good graphics** (Iris shaders + 128x resource packs +
Distant Horizons) running on **Bazzite**, the Linux gaming distro.

> Reading of the request: "balzzite" = **Bazzite** (bazzite.gg), "moded good graphic Minecraft"
> = modded Java Edition with shader packs. If you actually meant a modpack or game called
> "Balzzite", tell me and I will re-target the list — every number here is generated from
> `builds/*.json`, so swapping parts is a 30-second edit.

All prices were researched with the Tavily API on **2026-11-09** and are reproduced with sources in
[`docs/pricing-and-sources.md`](docs/pricing-and-sources.md). The raw search responses are kept in
[`research/`](research/) so every claim is traceable.

---

## 1. The builds

| | Build A — Flagship | Build B — Sweet Spot ⭐ | Build C — X3D-First Value |
|---|---|---|---|
| CPU | Ryzen 7 9850X3D | Ryzen 7 9850X3D | Ryzen 7 9850X3D |
| Cooler | Arctic LF III Pro 360 | Peerless Assassin 120 SE V2 | Peerless Assassin 120 SE V2 |
| Board | MSI MAG X870 Tomahawk WiFi | Gigabyte B850 Eagle WiFi 6E | Gigabyte B850 Eagle WiFi 6E |
| RAM | 64 GB (2x32) DDR5-6000 CL30 | 32 GB (2x16) DDR5-6000 CL30 | 32 GB (2x16) DDR5-6000 CL30 |
| GPU | RX 9070 XT 16 GB | RX 9070 XT 16 GB | RX 9060 XT 16 GB |
| SSD | WD_BLACK SN850X 2 TB | WD_BLACK SN850X 2 TB | WD_BLACK SN850X 2 TB |
| PSU | MSI MPG A1000GS 1000 W ATX 3.1 | same | same |
| Case | Lian Li Lancool 217 | Lian Li Lancool 207 | Lian Li Lancool 207 |
| **Tower total** | **$3,227.94** | **$2,488.93** | **$2,277.94** |
| + 1440p 240 Hz monitor | $399.99 → $3,627.93 | $394.00 → $2,882.93 | $269.00 → $2,546.94 |
| Peak draw / PSU load | 526 W / 53% | 526 W / 53% | 382 W / 38% |

**Buy Build B.** It is the point where spending more stops buying Minecraft frames. Build A only
makes sense if you also host a server for friends, keep 3 modpack instances open, or run 128x
resource packs at 4K. Build C is the "I want the X3D feel but the GPU budget is gone" option.

Ready-to-paste search terms for every part, plus a buy-in-stages plan, are in
[`docs/shopping-list.md`](docs/shopping-list.md).

Verify any of it yourself:

```bash
python3 scripts/build_check.py            # full bill of materials, wattage, warnings
python3 scripts/build_check.py --markdown # the table above
python3 scripts/build_check.py --strict   # fails loudly on an incompatible/mismatched part
```

The checker enforces socket/chipset match, DDR5 vs board, DIMM count, GPU length and cooler height
against the case, M.2 slots, ≥30% PSU headroom, ATX 3.1 on 300 W+ GPUs, and the
"you need VRAM/RAM for this workload" minimums.

---

## 2. Why these parts (the Minecraft performance model)

Minecraft is not a normal game benchmark, and that changes the whole parts list:

1. **The main thread is the frame limiter.** One thread does world tick, entity AI, block updates
   and chunk meshing. That thread is also cache-hungry — which is why **3D V-Cache** chips are
   disproportionately fast in Minecraft. The Ryzen 7 9850X3D (96 MB L3, 5.6 GHz boost, $484) is the
   fastest gaming CPU you can buy in Nov 2026; reviews put it ~3–4% ahead of the 9800X3D in games
   and ~6–7% ahead in single-thread. In *modded* Minecraft the gap is bigger than in esports titles,
   because mods add per-tick work and chunk churn.
2. **Mods multiply the tick cost.** A 200+ mod pack (All the Mods-class) wants **12–16 GB of heap**
   for the game alone, on top of Bazzite, a browser and the shader compiler. That is why 32 GB is
   the floor and 64 GB is the comfort pick — not because Minecraft "uses" 64 GB.
3. **Shaders turn it into a real GPU load.** Iris + a modern pack (Complementary, Photon, Solas,
   Rethinking Voxels) is a deferred renderer: it wants VRAM bandwidth and capacity, especially when
   you combine it with **Distant Horizons** (LOD terrain, 6+ GB VRAM recommended) and 128x textures.
4. **The GPU ceiling is absurd right now.** RTX 5090 street price is **$5,000+** and the RTX 5080 is
   ~**$2,200** (120% over MSRP) because of the AI-driven memory shortage; the 5080 Super (24 GB) is
   reportedly delayed toward 2027. Paying 6–10× for a card that Minecraft can't fully use is the
   single worst move available. The **RX 9070 XT 16 GB at ~$730** is the best Minecraft-shaders
   value in this market.
5. **Bazzite runs AMD better than Windows-adjacent vendors.** Independent Bazzite benchmarks put
   RDNA4 at ~92–94% of its Windows performance under Mesa/RADV, while NVIDIA on Wayland/Bazzite has
   been the source of regressions and crashes. Same money, fewer driver adventures → **AMD GPU**.
6. **AM5 + two DIMMs.** DDR5-6000 CL30 in two sticks keeps the fabric at 1:1. Four sticks on AM5
   drops to ~4800–5200 MT/s and adds latency, which is exactly what Minecraft hates. So: 2x16 or
   2x32, never 4x16.

---

## 3. What I deliberately did *not* put in the list

| Tempting part | Why not |
|---|---|
| **RTX 5090** ($5,000+) | 6–7× the price of the 9070 XT for a workload that is CPU-bound half the time. Terrible on Bazzite per current Linux driver reports. |
| **RTX 5080 / 5070 Ti Super** | 5080 is ~$2,200 (+120% over MSRP); the 5080 Super 24 GB is delayed toward 2027. Not buyable at a sane price today. |
| **Ryzen 9 9950X3D2** ($899, 16C, 208 MB) | Two CCDs means cross-CCD latency for game threads; you gain nothing over a single-CCD 9850X3D in Minecraft. Buy it only if you also run a dedicated server + stream encode on the same box. |
| **DDR5-8000 / 4-DIMM 64 GB** | 1:1 fabric breaks, latency rises, and Minecraft gets slower. 6000 CL30, 2 sticks. |
| **PCIe 5.0 SSD** | Minecraft loads thousands of small files; random latency and DRAM cache matter, sequential Gen5 speed does not. SN850X 2 TB is the value pick. |
| **1200 W PSU** | 526 W peak load; 1000 W ATX 3.1 at $110 is already oversized and future-proof. |
| **360 mm AIO in Build B/C** | A 120 W single-CCD X3D chip is fine on a $35 Peerless Assassin. |

---

## 4. Buy-vs-wait, November 2026 (read this before you order)

This is a historically bad moment for three of the nine parts:

- **DDR5:** 32 GB kits bottomed at ~$72; a 32 GB DDR5-6000 kit is now **~$480**, 64 GB kits start
  around **$930–$1,050**. Prices roughly doubled since Sept 2025 on AI demand. → Buy the RAM you can
  live with *now* (32 GB, 2 sticks) rather than "waiting"; there is no relief in the visible window,
  and adding a second identical 2x16 kit later gives you 64 GB *if* you re-buy the same SKU.
- **NAND/SSD:** up 80–150% year over year; a 2 TB SN850X is ~$380 vs ~$140 historically. → Do not
  buy a 4 TB drive for future-proofing. Buy 2 TB now, archive old worlds to a cheap SATA/HDD.
- **GPUs:** AMD raised Radeon prices twice in two months; the 9070 XT has ranged **$710–$950** for
  the same card. → Buy the cheapest 3-fan 9070 XT you can find at ≤$760, and check Black Friday
  flyers first (the 9060 XT 16 GB has already dipped to $339–$419 in flash sales, which would drop
  Build C under $2,100).
- **CPU:** the 9850X3D is *in stock at $484* (below its $499 MSRP). This is the one part that is
  currently a good deal. Buy it first — it is also the part that decides how the machine feels.

If you only have budget for one thing this month: **CPU first, RAM second, GPU third.**

---

## 5. Build-day checklist (AM5 + Bazzite specific)

1. **Flash the BIOS before first Windows-free boot.** Both boards support BIOS flashback from USB;
   X870/B850 launch BIOSes are rough with 9000-series X3D parts. Update, then clear CMOS.
2. **Install one SSD in M2_1** (CPU-attached slot) — that is the PCIe 5.0 x4 slot; the drive runs at
   Gen4 and that is fine.
3. **Seat the two RAM sticks in A2/B2** (slots 2 and 4). First POST on AM5 does memory training and
   can take 60–120 s with no video. Do not panic, do not power-cycle.
4. **Enable EXPO** in BIOS (DDR5-6000 CL30), set **fTPM on** (needed by some launchers/anticheat),
   enable **Resizable BAR** (AMD calls it Smart Access Memory), and leave **PBO on Auto** — the X3D
   part already boosts to spec and hand-tuning costs stability in a modded pack.
5. **Boot the Bazzite installer in UEFI mode**, and pick the *desktop* image (KDE or GNOME) rather
   than the Deck image — you want a normal desktop for Prism Launcher and mod file management.
6. Then follow [`docs/bazzite-setup.md`](docs/bazzite-setup.md) for the launcher, JVM flags, and
   Sodium/Iris/Distant Horizons tuning that actually produces the "good graphics" result.

---

## 6. Expected result

With Build A or B, shader-heavy 1440p is comfortable and Distant Horizons at long LOD distances is
usable; the frame limiter moves from the CPU to the shader pack as you push render distance and
resolution up. With Build C, keep the shader preset one notch lower and Distant Horizons at a
moderate LOD radius. Exact FPS depends far more on the pack, the render distance and the shader
preset than on the parts, so tune in this order: **render distance → shader preset → resource pack
resolution → Distant Horizons LOD radius.** Full tuning walkthrough in
[`docs/bazzite-setup.md`](docs/bazzite-setup.md).

---

## Repo layout

```
README.md                       this file
builds/build-a-flagship.json    machine-readable bill of materials (A)
builds/build-b-sweet-spot.json  machine-readable bill of materials (B)  <- recommended
builds/build-c-x3d-first.json   machine-readable bill of materials (C)
scripts/build_check.py          compatibility + wattage + pricing validator
scripts/tavily_search.py        the research harness used to price everything
docs/bazzite-setup.md           OS + Prism Launcher + Sodium/Iris/DH tuning
docs/shopping-list.md           copy/paste search terms and a buy-in-stages plan
docs/pricing-and-sources.md     every price, dated, with its source URL
research/*.json                 raw Tavily responses (provenance)
scripts/verify_repo.py          asserts the docs' totals match the JSON
```
