#!/usr/bin/env python3
"""Add one paper (or many) to data/entries.json by arXiv id / URL or GitHub repo.

    python scripts/add.py 2312.10035
    python scripts/add.py https://arxiv.org/abs/2312.10035
    python scripts/add.py 2312.10035 --code https://github.com/pointcept/pointtransformerv3 --tags segmentation detection

Re-runs scripts/build.py afterwards unless --no-build is given.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "entries.json")
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl_arxiv import parse_venue, tag_of  # noqa: E402


def arxiv_id(raw: str) -> str | None:
    m = re.search(r"(\d{4}\.\d{4,5})", raw)
    return m.group(1) if m else None


def fetch(aid: str) -> dict:
    url = f"https://export.arxiv.org/api/query?id_list={aid}"
    req = urllib.request.Request(url, headers={"User-Agent": "point-cloud-papers/1.0"})
    xml = None
    last = ""
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                xml = r.read().decode("utf-8", "replace")
            break
        except urllib.error.HTTPError as exc:
            last = f"HTTP {exc.code}"
            # 429 = throttled; back off much harder, it usually clears in seconds
            time.sleep(5 * (attempt + 1) if exc.code != 429 else 15 * (attempt + 1))
        except Exception as exc:  # noqa: BLE001
            last = type(exc).__name__
            time.sleep(3 * (attempt + 1))
    if xml is None:
        raise SystemExit(
            f"无法从 arXiv 获取 {aid}（{last}）。\n"
            "  多半是触发了 arXiv 的限流（429）：等 1-2 分钟再试；\n"
            "  如果是批量添加，建议改用 python scripts/crawl_arxiv.py 并加大 --sleep。"
        )
    root = ET.fromstring(xml)
    e = root.find("a:entry", NS)
    if e is None:
        raise SystemExit(f"arXiv id not found: {aid}")
    title = re.sub(r"\s+", " ", e.findtext("a:title", "", NS)).strip()
    if title.lower() == "error":
        raise SystemExit(f"arXiv returned an error for id: {aid}")
    published = e.findtext("a:published", "", NS)
    comment = (e.findtext("arxiv:comment", "", NS) or "").strip()
    journal = (e.findtext("arxiv:journal_ref", "", NS) or "").strip()
    summary = re.sub(r"\s+", " ", e.findtext("a:summary", "", NS)).strip()
    venue, vyear = parse_venue(f"{comment} {journal}")
    return {
        "title": title,
        "year": int(vyear or published[:4]),
        "venue": venue or "arXiv",
        "arxiv": aid,
        "tags": tag_of(f"{title} {summary}"),
        "code": "",
        "note": "",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("papers", nargs="+", help="arXiv id or URL")
    ap.add_argument("--code", default="", help="code repository URL")
    ap.add_argument("--project", default="", help="project page URL")
    ap.add_argument("--tags", nargs="*", default=None, help="override auto-detected tags")
    ap.add_argument("--note", default="")
    ap.add_argument("--no-build", action="store_true")
    args = ap.parse_args()

    entries = json.load(open(DATA, encoding="utf-8"))
    have = {e.get("arxiv") for e in entries if e.get("arxiv")}
    added = 0
    for raw in args.papers:
        aid = arxiv_id(raw)
        if not aid:
            print(f"skip (not an arXiv id): {raw}", file=sys.stderr)
            continue
        if aid in have:
            print(f"skip (already listed): {aid}")
            continue
        e = fetch(aid)
        if args.tags:
            e["tags"] = args.tags
        if args.code:
            e["code"] = args.code
        if args.project:
            e["project"] = args.project
        if args.note:
            e["note"] = args.note
        entries.append(e)
        have.add(aid)
        added += 1
        print(f"added: {e['year']} {e['venue']} — {e['title'][:70]}")
        time.sleep(1)

    entries.sort(key=lambda e: (-int(e["year"]), e["venue"], e["title"].lower()))
    with open(DATA, "w", encoding="utf-8") as f:
        f.write("[\n")
        f.write(",\n".join(" " + json.dumps(e, ensure_ascii=False) for e in entries))
        f.write("\n]\n")

    print(f"{added} added, {len(entries)} total")
    if not args.no_build:
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build.py")], check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
