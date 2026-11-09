# Shopping list — copy/paste search terms (Nov 2026)

Buy in this order. Prices are the ones in [`../builds/build-b-sweet-spot.json`](../builds/build-b-sweet-spot.json)
(2026-11-09). Search terms are written so they land on the right SKU rather than a lookalike.

## Priority 1 — the parts that decide how Minecraft feels

| # | Part | Search term | Target price | Notes |
|---|---|---|---|---|
| 1 | CPU | `Ryzen 7 9850X3D` | $484 | 96 MB L3, 120 W, AM5. Must be **9850X3D**, not 9800X3D/9700X. Boxed "without cooler" is fine. |
| 2 | RAM | `DDR5-6000 CL30 2x16GB EXPO` | $479.99 | 2 sticks only. Prefer kits explicitly listed as **AMD EXPO**, CL30 (not CL36/CL40). |
| 3 | GPU | `RX 9070 XT 16GB 3-fan` | $710–$760 | Any AIB is fine; pick the cheapest with 3 fans and a 2x8-pin or 12V-2x6 connector. Avoid 8 GB/12 GB variants. |
| 4 | SSD | `WD_BLACK SN850X 2TB` | $379.99 | Heatsink version not required (board has shields). Samsung 990 Pro 2 TB is the equal alternative at $389.99. |

## Priority 2 — platform and power

| # | Part | Search term | Target price | Notes |
|---|---|---|---|---|
| 5 | Motherboard | `Gigabyte B850 Eagle WiFi6E` | $189.99 | Needs: AM5, DDR5, PCIe 5.0 x16, 2x M.2, BIOS flashback. |
| 6 | PSU | `MSI MPG A1000GS ATX 3.1` | $109.99 | 1000 W, 80+ Gold, 12V-2x6 cable included. Corsair RM1000x is the alternative. |
| 7 | Case | `Lian Li Lancool 207` | $79.99 | Includes 4 fans. Lancool 217 ($119.99) if you want a 360 mm radiator later. |
| 8 | Cooler | `Thermalright Peerless Assassin 120 SE V2` | $34.99 | Must be the **SE V2** (AM5 bracket + 155 mm height). Arctic LF III Pro 360 ($94) only for Build A. |

## Priority 3 — nice to have

| # | Part | Search term | Target price |
|---|---|---|---|
| 9 | Monitor | `MSI MAG 272QP X24` (or `Gigabyte MO27Q2A`) | $394–$400 |
| 10 | Second SSD | `WD_BLACK SN850X 2TB` | $379.99 — buy later, NAND prices are climbing |

---

## If you can only buy part of it this month

1. **CPU + motherboard + RAM + PSU + case + cooler** first (~$1,160). The machine boots, and the
   integrated GPU on the 9850X3D runs vanilla Minecraft at 1080p — you can set up Bazzite, Prism
   Launcher and your modpack while you wait for GPU money.
2. **GPU** second ($730). This is where "good graphics" actually arrives.
3. **SSD** third ($380) — but note you need *something* to install the OS on, so in practice buy the
   SSD with the CPU or use any spare SATA/NVMe drive you already own.
4. **Monitor** last if you already have a display.

Buying the CPU now is the right call specifically because it is the only part currently *below* MSRP
($484 vs $499) while RAM, NAND and GPUs are all inflated. Do not wait on the CPU hoping for a drop.

---

## What to check at checkout

- [ ] CPU is `9850X3D` (8 cores), not `9850X` or `9800X3D`.
- [ ] RAM kit is **2 modules**, DDR5-6000, **CL30**, EXPO.
- [ ] GPU is **16 GB** and labeled `RX 9070 XT` (not `RX 9070` non-XT unless it is much cheaper).
- [ ] PSU is **ATX 3.1** with a **12V-2x6** cable in the box.
- [ ] Motherboard says **AM5** and **DDR5** (not AM4/DDR4 — B850E vs B550 confusion is common).
- [ ] Case spec sheet lists GPU clearance **≥ 330 mm**.
- [ ] Cooler lists **AM5** support and height **≤ 175 mm** for the Lancool 207.

Then re-run the checks in the repo:

```bash
python3 scripts/build_check.py --strict
python3 scripts/verify_repo.py
```
