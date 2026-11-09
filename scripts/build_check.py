#!/usr/bin/env python3
"""Validate and price the PC builds in builds/*.json.

Checks are the ones that actually bite in a real build:
  * CPU socket matches motherboard socket
  * memory type matches the board, stick count fits the slots, and AM5 gets a 2-stick warning
  * GPU length / cooler height / radiator fit inside the case
  * M.2 drives fit the available M.2 slots
  * PSU wattage has >=30% headroom over the estimated peak wall draw
  * high-TDP GPUs get the 12V-2x6 / ATX 3.1 warning

Usage:
    python3 scripts/build_check.py            # human readable
    python3 scripts/build_check.py --markdown # table for the README
    python3 scripts/build_check.py --strict   # non-zero exit on any hard error
"""
from __future__ import annotations

import argparse
import glob
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD_GLOB = str(ROOT / "builds" / "*.json")

# Estimated fixed overhead (board, fans, RAM, drives, pumps) in watts.
PLATFORM_OVERHEAD_W = 60
# AM5 boards lose memory stability with 4 DIMMs populated; Minecraft is latency sensitive.
AM5_MAX_STICKS_FAST = 2


def load_builds() -> list[dict]:
    builds = []
    for path in sorted(glob.glob(BUILD_GLOB)):
        with open(path) as fh:
            build = json.load(fh)
        build["_path"] = path
        builds.append(build)
    if not builds:
        sys.exit(f"no build files matched {BUILD_GLOB}")
    return builds


def peak_draw_w(parts: dict) -> int:
    return parts["cpu"]["peak_w"] + parts["gpu"]["tdp_w"] + PLATFORM_OVERHEAD_W


def cost(parts: dict) -> float:
    return sum(p["price"] for p in parts.values())


def fmt(amount: float) -> str:
    return f"${amount:,.2f}"


def validate(build: dict) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for a single build."""
    errors: list[str] = []
    warnings: list[str] = []
    parts = build["parts"]
    cpu, mobo, ram = parts["cpu"], parts["motherboard"], parts["memory"]
    gpu, case, psu = parts["gpu"], parts["case"], parts["psu"]
    cooler = parts["cooler"]

    # --- socket / platform -------------------------------------------------
    if cpu["socket"] != mobo["socket"]:
        errors.append(f"CPU socket {cpu['socket']} != motherboard socket {mobo['socket']}")
    if ram["type"] != mobo["ram_type"]:
        errors.append(f"RAM type {ram['type']} != motherboard RAM type {mobo['ram_type']}")
    if ram["sticks"] > mobo["dimm_slots"]:
        errors.append(f"{ram['sticks']} memory sticks but only {mobo['dimm_slots']} DIMM slots")
    if cpu["socket"] == "AM5" and ram["sticks"] > AM5_MAX_STICKS_FAST:
        warnings.append(
            f"{ram['sticks']} DIMMs on AM5 forces a lower memory clock; 2 sticks (one per channel) is faster"
        )
    if cpu["socket"] == "AM5" and ram["speed_mts"] > 6400:
        warnings.append("above DDR5-6400 on AM5 usually drops the fabric out of 1:1 mode - slower in game")

    # --- physical fit ------------------------------------------------------
    if gpu["length_mm"] > case["max_gpu_mm"]:
        errors.append(f"GPU is {gpu['length_mm']} mm but the case takes {case['max_gpu_mm']} mm")
    if cooler["type"] == "air":
        if cooler.get("height_mm", 0) > case["max_cooler_mm"]:
            errors.append(
                f"air cooler is {cooler['height_mm']} mm tall, case limit is {case['max_cooler_mm']} mm"
            )
    elif cooler["type"] == "aio":
        if cooler.get("radiator_mm", 0) > 360:
            warnings.append("radiator larger than 360 mm - confirm the case's mount dimensions")
        if case["max_cooler_mm"] < 100:
            warnings.append("verify radiator clearance in this case before buying")

    # --- storage -----------------------------------------------------------
    if 1 > mobo["m2_slots"]:
        errors.append("no free M.2 slot for the SSD")

    # --- power -------------------------------------------------------------
    peak = peak_draw_w(parts)
    headroom_pct = (psu["wattage"] - peak) / peak * 100
    if psu["wattage"] < peak:
        errors.append(f"PSU {psu['wattage']} W is below the estimated {peak} W peak draw")
    elif headroom_pct < 30:
        warnings.append(
            f"only {headroom_pct:.0f}% PSU headroom ({psu['wattage']} W vs {peak} W peak); aim for 30%+"
        )
    if not psu.get("atx_31") and gpu["tdp_w"] >= 300:
        warnings.append("300 W+ GPU without an ATX 3.1 / 12V-2x6 PSU risks transient-trip shutdowns")

    # --- sensible pairing for this workload -------------------------------
    if gpu["vram_gb"] < 12:
        warnings.append("under 12 GB VRAM will thrash with 128x packs + Distant Horizons + shaders")
    if ram["capacity_gb"] < 32:
        warnings.append("under 32 GB cannot hold a 10-16 GB modpack heap plus the desktop")
    if cpu.get("l3_mb", 0) < 32 and cpu["socket"] == "AM5":
        warnings.append("small L3 hurts Minecraft chunk rendering; an X3D part is worth the premium")
    return errors, warnings


def render(builds: list[dict], markdown: bool) -> int:
    hard_failures = 0
    rows = []
    for build in builds:
        parts = build["parts"]
        errors, warnings = validate(build)
        total = cost(parts)
        periph = sum(p["price"] for p in build.get("peripherals", {}).values())
        peak = peak_draw_w(parts)
        util = peak / parts["psu"]["wattage"] * 100
        rows.append((build, total, periph, peak, util, errors, warnings))
        if errors:
            hard_failures += 1
        if markdown:
            continue

        status = "ERROR" if errors else ("WARN" if warnings else "OK")
        print("=" * 80)
        print(build["name"])
        print(f"  file       : {pathlib.Path(build['_path']).name}")
        print(f"  price date : {build['price_date']}")
        print(f"  target     : {build['target']}")
        print("  " + "-" * 76)
        for key, part in parts.items():
            print(f"  {key:<12} {part['name']:<52} {fmt(part['price']):>10}")
        print("  " + "-" * 76)
        print(f"  {'TOTAL':<12} {'':<52} {fmt(total):>10}")
        if periph:
            print(f"  {'+ extras':<12} {'':<52} {fmt(periph):>10}  -> {fmt(total + periph)} all-in")
        print(f"  peak draw {peak} W | PSU load at peak {util:.0f}% of {parts['psu']['wattage']} W | {status}")
        for warn in warnings:
            print(f"    WARN  {warn}")
        for err in errors:
            print(f"    ERROR {err}")

    if markdown:
        print("| Build | CPU | GPU | RAM | SSD | Tower total | Peak draw | PSU load |")
        print("|---|---|---|---|---|---|---|---|")
        for build, total, periph, peak, util, errors, warnings in rows:
            p = build["parts"]
            label = build["name"].split("\u2014")[0].strip()
            print(
                f"| {label} | {p['cpu']['name']} | {p['gpu']['name']} | {p['memory']['name']} "
                f"| {p['storage']['name']} | {fmt(total)} | {peak} W | {util:.0f}% |"
            )
    return hard_failures


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--markdown", action="store_true", help="print a README-ready table")
    ap.add_argument("--strict", action="store_true", help="exit non-zero on hard errors")
    args = ap.parse_args()

    builds = load_builds()
    failures = render(builds, args.markdown)
    print(f"\n{len(builds)} build(s) loaded, {failures} with hard errors.")
    if failures and args.strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
