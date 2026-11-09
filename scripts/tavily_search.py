#!/usr/bin/env python3
"""Tiny Tavily helper used to research PC parts for this build.

Usage:
    python3 scripts/tavily_search.py --query "best cpu for modded minecraft" \
        --out research/cpu.json [--depth advanced] [--n 6]

The API key can be supplied via the TAVILY_API_KEY environment variable.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

API_URL = "https://api.tavily.com/search"


def search(query: str, n: int = 6, depth: str = "basic", topic: str = "general",
           days: int | None = None, retries: int = 3) -> dict:
    key = os.environ.get("TAVILY_API_KEY")
    if not key:
        sys.exit("TAVILY_API_KEY is not set")
    payload = {
        "api_key": key,
        "query": query,
        "search_depth": depth,
        "topic": topic,
        "max_results": n,
        "include_answer": True,
        "include_raw_content": False,
    }
    if days:
        payload["days"] = days
    body = json.dumps(payload).encode()
    last = None
    for attempt in range(retries):
        req = urllib.request.Request(
            API_URL, data=body, headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            time.sleep(2 * (attempt + 1))
    raise SystemExit(f"search failed for {query!r}: {last}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", required=True)
    ap.add_argument("--out")
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--depth", default="basic")
    ap.add_argument("--days", type=int)
    args = ap.parse_args()

    result = search(args.query, n=args.n, depth=args.depth, days=args.days)
    blob = json.dumps(result, indent=2)
    if args.out:
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        with open(args.out, "w") as fh:
            fh.write(blob)
    print(blob[:4000])


if __name__ == "__main__":
    main()
