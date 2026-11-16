#!/usr/bin/env python3
"""Crawl arXiv for point-cloud papers and emit structured JSON records.

Used both to bootstrap the repo (large --max) and by the daily GitHub Action
(small --max, --since 3d) that opens a PR with newly published papers.

Usage:
    python scripts/crawl_arxiv.py --out data/arxiv_raw.json --max 1600
    python scripts/crawl_arxiv.py --out new.json --max 40 --since 2025-01-01 --merge data/entries.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

API = "https://export.arxiv.org/api/query"
NS = {
    "a": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# Queries are OR-ed together and de-duplicated by arXiv id.
QUERIES = [
    'all:"point cloud"',
    'all:"point clouds"',
    'ti:"point cloud"',
    'abs:"LiDAR" AND cat:cs.RO',
    'abs:"3D object detection" AND abs:"point"',
    'abs:"point cloud" AND cat:cs.GR',
]

KEEP_CATS = {"cs.CV", "cs.RO", "cs.GR", "cs.LG", "cs.AI", "eess.IV"}

# Historic backfill only needs the two broadest queries; the daily sync uses all.
QUERIES_CORE = QUERIES[:2]

# Venue detection from arXiv comment / journal_ref, e.g.
#   "Accepted by CVPR 2025" / "ICCV 2025 Camera Ready" / "Published in TPAMI"
VENUES = [
    (r"\bCVPR(?:\s*(?:20)?(\d{2}))?\b", "CVPR"),
    (r"\bICCV(?:\s*(?:20)?(\d{2}))?\b", "ICCV"),
    (r"\bECCV(?:\s*(?:20)?(\d{2}))?\b", "ECCV"),
    (r"\bNeurIPS\b|\bNIPS\b", "NeurIPS"),
    (r"\bICLR\b", "ICLR"),
    (r"\bICML\b", "ICML"),
    (r"\bAAAI(?:\s*(?:20)?(\d{2}))?\b", "AAAI"),
    (r"\bIJCAI\b", "IJCAI"),
    (r"\bACM\s*MM\b|\bACM Multimedia\b", "ACM MM"),
    (r"\bSIGGRAPH\s*Asia\b", "SIGGRAPH Asia"),
    (r"\bSIGGRAPH\b", "SIGGRAPH"),
    (r"\b3DV\b", "3DV"),
    (r"\bWACV\b", "WACV"),
    (r"\bBMVC\b", "BMVC"),
    (r"\bICRA\b", "ICRA"),
    (r"\bIROS\b", "IROS"),
    (r"\bRA-?L\b|\bRobotics and Automation Letters\b", "RA-L"),
    (r"\bTPAMI\b", "TPAMI"),
    (r"\bIJCV\b", "IJCV"),
    (r"\bT-?ITS\b|\bTITS\b", "T-ITS"),
    (r"\bTVCG\b", "TVCG"),
    (r"\bTIP\b", "TIP"),
    (r"\bISPRS\b", "ISPRS"),
    (r"\bTGRS\b", "TGRS"),
    (r"\bPattern Recognition\b", "PR"),
]

# keyword -> tag, checked against title + abstract (case-insensitive)
TAG_RULES = [
    ("registration", r"\bregist(?:er|ration|ering)\b|\bpoint cloud alignment\b", "any"),
    ("segmentation", r"\bsegment(?:ation|ing)?\b|\bpanoptic\b", "any"),
    ("detection", r"\bdetect(?:ion|or|ing)\b", "any"),
    ("completion", r"\bcompletion\b|\bpoint cloud completion\b", "any"),
    ("classification", r"\bclassification\b|\bshape retrieval\b", "any"),
    ("tracking", r"\btrack(?:ing|er)\b", "any"),
    ("slam", r"\bSLAM\b|\bvisual odometry\b", "any"),
    ("localization", r"\blocali[sz]ation\b|\bplace recognition\b", "any"),
    ("generation", r"\bgenerat(?:ion|ive|or)\b|\bdiffusion model\b", "any"),
    ("reconstruction", r"\breconstruct(?:ion|ing)\b|\bsurface reconstruction\b", "any"),
    ("nerf", r"\bNeRF\b|\bneural radiance\b", "any"),
    ("gaussian-splatting", r"\bGaussian splatting\b|\b3DGS\b", "any"),
    ("self-supervised", r"\bself-supervised\b|\bcontrastive learning\b|\bmasked autoencoder\b", "any"),
    ("compression", r"\bcompress(?:ion|ed)?\b", "any"),
    ("upsampling", r"\bupsampl(?:ing|e)\b|\bsuper-?resolution\b|\bpoint cloud densif", "any"),
    ("denoising", r"\bdenois(?:ing|e)\b|\bnoise removal\b", "any"),
    ("normal estimation", r"\bnormal estimation\b|\bnormals?\b.*\bestimat", "any"),
    ("scene flow", r"\bscene flow\b", "any"),
    ("autonomous driving", r"\bautonomous driving\b|\bself-driving\b", "any"),
    ("monocular", r"\bmonocular\b", "any"),
    ("BEV", r"\bBEV\b|\bbird'?s-eye-view\b", "any"),
    ("open-vocabulary", r"\bopen-?vocabulary\b|\bzero-?shot\b", "any"),
    ("pre-training", r"\bpre-?train(?:ing|ed)?\b|\bfoundation model\b", "title"),
    ("occupancy prediction", r"\boccupanc(?:y|ies) prediction\b|\bsemantic scene completion\b", "title"),
    ("vision-language", r"\bvision-language\b|\bLLM\b|\bVLM\b|\blanguage-grounded\b", "title"),
    ("multi-modal", r"\bmulti-?modal\b|\bLiDAR-camera\b|\bcamera-LiDAR\b|\bradar\b", "title"),
    ("anomaly detection", r"\banomaly detection\b|\bdefect\b", "title"),
    ("domain adaptation", r"\bdomain adaptation\b|\bdomain gap\b", "title"),
    ("robustness", r"\brobust(?:ness)?\b|\badversarial\b|\bcorruption\b", "title"),
    ("efficiency", r"\befficien(?:t|cy)\b|\breal-?time\b|\blight-?weight\b|\bpruning\b|\bquantiz", "title"),
    ("dataset", r"\bdataset\b|\bbenchmark\b", "title"),
]


def build_query(base: str, date_from: str | None, date_to: str | None) -> str:
    """Wrap a query with an arXiv submittedDate range, e.g.
    submittedDate:[202101010000 TO 202112312359]
    """
    if not date_from and not date_to:
        return base
    lo = (date_from or "20150101").replace("-", "") + "0000"
    hi = ((date_to or "20301231").replace("-", "")) + "2359"
    return f'({base}) AND submittedDate:[{lo} TO {hi}]'


def fetch(query: str, start: int, max_results: int, sort: str) -> str:
    params = {
        "search_query": query,
        "start": str(start),
        "max_results": str(max_results),
        "sortBy": sort,
        "sortOrder": "descending",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "point-cloud-papers/1.0"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            if attempt == 3:
                raise
            print(f"  retry {attempt + 1}: {e}", file=sys.stderr)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError("unreachable")


def parse_venue(text: str):
    if not text:
        return None, None
    for pat, name in VENUES:
        m = re.search(pat, text, re.I)
        if m:
            yy = next((g for g in m.groups() if g), None) if m.groups() else None
            year = f"20{yy}" if yy else None
            return name, year
    return None, None


def tag_of(title: str, abstract: str = ""):
    """Keyword tagger. Patterns marked \"title\" must match the title."""
    tags = []
    for tag, pat, scope in TAG_RULES:
        hay = title if scope == "title" else f"{title} {abstract}"
        if re.search(pat, hay, re.I):
            tags.append(tag)
    return tags[:6]


def records(xml_text: str):
    root = ET.fromstring(xml_text)
    for e in root.findall("a:entry", NS):
        aid_url = e.findtext("a:id", "", NS)
        m = re.search(r"abs/([0-9.]+)v?\d*", aid_url)
        if not m:
            continue
        aid = m.group(1)
        title = re.sub(r"\s+", " ", e.findtext("a:title", "", NS)).strip()
        summary = re.sub(r"\s+", " ", e.findtext("a:summary", "", NS)).strip()
        published = e.findtext("a:published", "", NS)
        comment = (e.findtext("arxiv:comment", "", NS) or "").strip()
        journal = (e.findtext("arxiv:journal_ref", "", NS) or "").strip()
        cats = [c.get("term") for c in e.findall("a:category", NS) if c.get("term")]
        primary = ""
        pc = e.find("arxiv:primary_category", NS)
        if pc is not None:
            primary = pc.get("term", "")
        venue, vyear = parse_venue(f"{comment} {journal}")
        yield {
            "id": aid,
            "title": title,
            "url": f"https://arxiv.org/abs/{aid}",
            "pdf": f"https://arxiv.org/pdf/{aid}",
            "published": published[:10],
            "year": published[:4],
            "comment": comment,
            "journal": journal,
            "venue": venue,
            "venue_year": vyear,
            "primary": primary,
            "categories": cats,
            "tags": tag_of(title, summary),
            "abstract": summary[:400],
        }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--max", type=int, default=1600, help="per-query cap of results to scan")
    ap.add_argument("--since", default=None, help="YYYY-MM-DD lower bound on published date")
    ap.add_argument("--date-from", default=None, help="YYYY-MM-DD, arXiv submittedDate range lower bound")
    ap.add_argument("--date-to", default=None, help="YYYY-MM-DD, arXiv submittedDate range upper bound")
    ap.add_argument("--merge", default=None, help="existing entries JSON to avoid duplicates")
    ap.add_argument("--query-set", choices=["full", "core"], default="full")
    ap.add_argument("--sort", choices=["submittedDate", "relevance"], default="submittedDate",
                    help="relevance covers a whole year; submittedDate follows recency")
    ap.add_argument("--sleep", type=float, default=3.0)
    args = ap.parse_args()

    since = args.since
    if since and since.endswith("d"):
        days = int(since[:-1])
        since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")

    seen_ids, seen_titles = set(), set()
    if args.merge:
        for r in json.load(open(args.merge, encoding="utf-8")):
            seen_ids.add(r["id"])
            seen_titles.add(r["title"].lower())

    out, page = [], 200
    queries = QUERIES_CORE if args.query_set == "core" else QUERIES
    for base in queries:
        q = build_query(base, args.date_from, args.date_to)
        print(f"query: {q}", file=sys.stderr)
        start = 0
        while start < args.max:
            n = min(page, args.max - start)
            try:
                xml = fetch(q, start, n, args.sort)
            except Exception as e:  # noqa: BLE001
                print(f"  abort query after error: {e}", file=sys.stderr)
                break
            got = 0
            for r in records(xml):
                got += 1
                if r["id"] in seen_ids:
                    continue
                if since and r["published"] < since:
                    continue
                if not (set(r["categories"]) & KEEP_CATS):
                    continue
                if not re.search(r"point cloud|LiDAR|point-based|point set", r["title"] + " " + r["abstract"], re.I):
                    continue
                if r["title"].lower() in seen_titles:
                    continue
                seen_ids.add(r["id"])
                seen_titles.add(r["title"].lower())
                out.append(r)
            print(f"  start={start} got={got} kept_total={len(out)}", file=sys.stderr)
            if got < n:
                break
            start += n
            time.sleep(args.sleep)
        time.sleep(args.sleep)

    out.sort(key=lambda r: r["published"], reverse=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"wrote {len(out)} records -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
