#!/usr/bin/env python3
"""Turn raw arXiv crawl output into the curated data/entries.json.

Keeps peer-reviewed papers (venue detected from arXiv comments), plus arXiv-only
papers whose *title* is about point clouds. De-duplicates by normalised title so
a paper that grew a conference version does not appear twice.

    python scripts/curate.py --raw data/arxiv_raw.json
    python scripts/curate.py --raw data/arxiv_raw.json --merge data/entries.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "entries.json")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl_arxiv import tag_of  # noqa: E402

CORE_VENUES = {
    "CVPR", "ICCV", "ECCV", "NeurIPS", "ICLR", "ICML", "AAAI", "IJCAI",
    "SIGGRAPH", "SIGGRAPH Asia", "ACM MM", "3DV", "WACV", "BMVC",
    "ICRA", "IROS", "RA-L", "TPAMI", "IJCV", "T-ITS", "TIP", "TVCG",
    "ISPRS", "TGRS", "PR",
}
PC_TITLE = re.compile(r"point cloud|point-cloud|lidar|gaussian splatting|3dgs", re.I)
# authors often drop the repo URL in the arXiv comment or the abstract
CODE_RE = re.compile(r"https?://(?:www\.)?github\.com/[\w.-]+/[\w.-]+", re.I)
MAX_TAGS = 4
MIN_YEAR = 2021          # 列表从 2021 年开始收录，更早的经典工作请看 DATASETS.md 与文末参考
MAX_YEAR = 2100


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", t.lower())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", required=True, nargs="+", help="one or more crawl output files")
    ap.add_argument("--merge", default=None)
    ap.add_argument("--out", default=DATA)
    ap.add_argument("--cap", type=int, default=0, help="optional cap on total entries")
    args = ap.parse_args()

    raw = []
    for path in args.raw:
        raw.extend(json.load(open(path, encoding="utf-8")))
    existing = json.load(open(args.merge, encoding="utf-8")) if args.merge else []

    entries, seen = [], set()
    for e in existing:  # keep already-curated entries verbatim
        k = norm_title(e["title"])
        if k and k not in seen:
            seen.add(k)
            entries.append(e)

    stats = Counter()
    for r in raw:
        k = norm_title(r["title"])
        if not k or k in seen:
            stats["dup"] += 1
            continue
        venue = r.get("venue")
        venue = venue if venue in CORE_VENUES else None
        if not venue and not PC_TITLE.search(r["title"]):
            stats["not_point_cloud"] += 1
            continue
        year = int(r["venue_year"]) if (venue and r.get("venue_year")) else int(r["published"][:4])
        if year < MIN_YEAR:
            stats["too_old"] += 1
            continue
        tags = tag_of(r["title"], r.get("abstract", ""))[:MAX_TAGS]
        note = "Workshop" if re.search(r"workshop", r.get("comment", ""), re.I) else ""
        m = CODE_RE.search(f"{r.get('comment', '')} {r.get('abstract', '')}")
        code = m.group(0).rstrip(".,;)") if m else ""
        entries.append({
            "title": r["title"],
            "year": year,
            "venue": venue or "arXiv",
            "arxiv": r["id"],
            "tags": tags,
            "code": code,
            "note": note,
        })
        seen.add(k)
        stats["kept"] += 1

    entries.sort(key=lambda e: (-int(e["year"]), e["venue"], e["title"].lower()))
    if args.cap:
        entries = entries[: args.cap]

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("[\n")
        f.write(",\n".join(" " + json.dumps(e, ensure_ascii=False, sort_keys=False) for e in entries))
        f.write("\n]\n")

    years = Counter(e["year"] for e in entries)
    venues = Counter(e["venue"] for e in entries)
    print(f"kept {stats['kept']}, dups {stats['dup']}, filtered {stats['not_point_cloud']} -> {len(entries)} total")
    print("by year:", dict(sorted(years.items(), reverse=True)))
    print("by venue:", venues.most_common(12))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
