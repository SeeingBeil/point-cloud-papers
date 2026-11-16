#!/usr/bin/env python3
"""Probe every arXiv / code / project link in data/entries.json.

    python scripts/check_links.py                 # report only
    python scripts/check_links.py --fail          # exit 1 when dead links found
    python scripts/check_links.py --only-code     # only repository links

arXiv 对高频请求会限流，默认并发较低并带重试。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "entries.json")
UA = {"User-Agent": "Mozilla/5.0 (compatible; point-cloud-papers link checker)"}


def probe(url: str) -> tuple[str, int | None, str]:
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers=UA)
            with urllib.request.urlopen(req, timeout=25) as r:
                return url, r.status, ""
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405, 429):
                return url, e.code, str(e.reason)
        except Exception as e:  # noqa: BLE001
            if method == "GET":
                return url, None, type(e).__name__
    return url, None, "unreachable"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fail", action="store_true")
    ap.add_argument("--only-code", action="store_true")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--out", default="link-report.md")
    args = ap.parse_args()

    entries = json.load(open(DATA, encoding="utf-8"))
    urls: set[str] = set()
    for e in entries:
        if e.get("code"):
            urls.add(e["code"])
        if not args.only_code:
            if e.get("arxiv"):
                urls.add(f"https://arxiv.org/abs/{e['arxiv']}")
            if e.get("project"):
                urls.add(e["project"])

    urls = sorted(urls)
    print(f"checking {len(urls)} links with {args.jobs} workers...", file=sys.stderr)
    bad = []
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        for url, status, err in ex.map(probe, urls):
            if status is None or status >= 400:
                bad.append((url, status, err))

    with open(os.path.join(ROOT, args.out), "w", encoding="utf-8") as f:
        f.write(f"# Link report\n\n检查 {len(urls)} 个链接，失效 {len(bad)} 个。\n\n")
        if bad:
            f.write("| URL | status | error |\n|:--|--:|:--|\n")
            for url, status, err in sorted(bad):
                f.write(f"| {url} | {status or '-'} | {err} |\n")

    print(f"{len(bad)} dead of {len(urls)}")
    for url, status, err in bad[:20]:
        print(f"  {status or '-':>4}  {url}  {err}")
    return 1 if (bad and args.fail) else 0


if __name__ == "__main__":
    raise SystemExit(main())
