#!/usr/bin/env python3
"""Repo self-check: keeps the docs honest about the JSON builds.

Run after any price edit:

    python3 scripts/verify_repo.py

It asserts that
  1. every builds/*.json has the required keys,
  2. the totals quoted in README.md match the JSON to the cent,
  3. every relative markdown link in the docs points at a real file,
  4. every markdown file has balanced code fences.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED_PART_KEYS = {
    "cpu": ["name", "price", "socket", "tdp_w", "peak_w"],
    "cooler": ["name", "price", "type"],
    "motherboard": ["name", "price", "socket", "ram_type", "dimm_slots", "m2_slots"],
    "memory": ["name", "price", "type", "capacity_gb", "sticks", "speed_mts"],
    "gpu": ["name", "price", "vram_gb", "tdp_w", "length_mm"],
    "storage": ["name", "price"],
    "psu": ["name", "price", "wattage"],
    "case": ["name", "price", "max_gpu_mm", "max_cooler_mm"],
}
failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def check_builds() -> list[dict]:
    builds = []
    for path in sorted(ROOT.glob("builds/*.json")):
        build = json.loads(path.read_text())
        for key in ("id", "name", "currency", "price_date", "target", "parts"):
            if key not in build:
                fail(f"{path.name}: missing top-level key {key!r}")
        for part, keys in REQUIRED_PART_KEYS.items():
            if part not in build.get("parts", {}):
                fail(f"{path.name}: missing part {part!r}")
                continue
            for key in keys:
                if key not in build["parts"][part]:
                    fail(f"{path.name}: {part} missing {key!r}")
        builds.append((path.name, build))
    return builds


def check_totals(builds) -> None:
    readme = (ROOT / "README.md").read_text()
    for name, build in builds:
        total = sum(p["price"] for p in build["parts"].values())
        if f"${total:,.2f}" not in readme:
            fail(f"README.md does not contain the computed tower total for {name}: ${total:,.2f}")
        extras = sum(p["price"] for p in build.get("peripherals", {}).values())
        if extras:
            combo = total + extras
            if f"${combo:,.2f}" not in readme:
                fail(f"README.md does not contain the all-in total for {name}: ${combo:,.2f}")


def check_links() -> None:
    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for md in list(ROOT.glob("*.md")) + list(ROOT.glob("docs/*.md")) + list(ROOT.glob("research/*.md")):
        text = md.read_text()
        for target in link_re.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            rel = target.split("#")[0]
            if not rel:
                continue
            resolved = (md.parent / rel).resolve()
            if not resolved.exists():
                fail(f"{md.relative_to(ROOT)}: dead relative link -> {target}")
        if text.count("```") % 2 != 0:
            fail(f"{md.relative_to(ROOT)}: unbalanced code fences")


def main() -> None:
    builds = check_builds()
    check_totals(builds)
    check_links()
    if failures:
        print(f"{len(failures)} problem(s):")
        for msg in failures:
            print("  -", msg)
        sys.exit(1)
    print(f"OK: {len(builds)} builds, totals in README match JSON, all relative links resolve.")


if __name__ == "__main__":
    main()
