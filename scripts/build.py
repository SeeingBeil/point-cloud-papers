#!/usr/bin/env python3
"""Render README.md and per-topic pages from data/entries.json.

    python scripts/build.py            # regenerate everything
    python scripts/build.py --check    # CI: fail if committed output is stale

Never edit README.md by hand: it is generated. Edit data/entries.json instead.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "entries.json")
TAGS = os.path.join(ROOT, "data", "tags.json")
README = os.path.join(ROOT, "README.md")
TOPICS = os.path.join(ROOT, "docs", "topics")

REQUIRED = {"title", "year", "venue"}
VENUE_ORDER = [
    "CVPR", "ICCV", "ECCV", "NeurIPS", "ICLR", "ICML", "AAAI", "IJCAI",
    "SIGGRAPH", "SIGGRAPH Asia", "ACM MM", "3DV", "WACV", "BMVC",
    "ICRA", "IROS", "RA-L", "TPAMI", "IJCV", "T-ITS", "TIP", "TVCG",
    "ISPRS", "TGRS", "PR", "arXiv",
]


def load():
    entries = json.load(open(DATA, encoding="utf-8"))
    tags = json.load(open(TAGS, encoding="utf-8"))
    known = {t["id"] for t in tags["tags"]}
    problems = []
    for i, e in enumerate(entries):
        miss = REQUIRED - e.keys()
        if miss:
            problems.append(f"entry #{i} missing {sorted(miss)}: {e.get('title', '?')}")
            continue
        if not re.fullmatch(r"(19|20)\d{2}", str(e["year"])):
            problems.append(f"bad year {e['year']!r}: {e['title']}")
        bad = [t for t in e.get("tags", []) if t not in known]
        if bad:
            problems.append(f"unknown tag(s) {bad} in: {e['title']} (add to data/tags.json or fix spelling)")
        if e.get("arxiv") and not re.fullmatch(r"\d{4}\.\d{4,5}", e["arxiv"]):
            problems.append(f"bad arxiv id {e['arxiv']!r}: {e['title']}")
    return entries, tags, problems


def venue_rank(v: str) -> int:
    return VENUE_ORDER.index(v) if v in VENUE_ORDER else len(VENUE_ORDER)


def slug(tag_id: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", tag_id.lower()).strip("-")


def sort_key(e):
    return (-int(e["year"]), venue_rank(e["venue"]), e["venue"], e["title"].lower())


def link_for(e) -> str:
    if e.get("arxiv"):
        return f"https://arxiv.org/abs/{e['arxiv']}"
    return e.get("url", "")


def entry_line(e) -> str:
    title = e["title"].replace("[", "(").replace("]", ")")
    line = f"- [{title}]({link_for(e)})"
    bits = [f"`{t}`" for t in e.get("tags", [])]
    tail = []
    if e.get("code"):
        tail.append(f"[code]({e['code']})")
    if e.get("project"):
        tail.append(f"[project]({e['project']})")
    if e.get("note"):
        tail.append(e["note"])
    if bits and tail:
        line += " — " + " ".join(bits) + " — " + " ".join(tail)
    elif bits:
        line += " — " + " ".join(bits)
    elif tail:
        line += " — " + " ".join(tail)
    return line


def render_readme(entries, tags) -> str:
    by_year = defaultdict(list)
    for e in entries:
        by_year[int(e["year"])].append(e)
    for y in by_year:
        by_year[y].sort(key=sort_key)

    total = len(entries)
    with_code = sum(1 for e in entries if e.get("code"))
    years = sorted(by_year, reverse=True)
    tag_counts = Counter(t for e in entries for t in e.get("tags", []))
    tag_names = {t["id"]: t["name"] for t in tags["tags"]}

    L = []
    L += [
        "# Awesome Point Cloud Papers",
        "",
        "<p align=\"center\">",
        "  <b>点云论文索引 · 2021 年至今 · 每日自动更新</b><br>",
        "  <sub>Curated papers on 3D point clouds and LiDAR perception, 2021–present. Synced with arXiv.</sub>",
        "</p>",
        "",
        "[![Papers](https://img.shields.io/badge/papers-%d-blue)](#-papers)" % total,
        "[![With code](https://img.shields.io/badge/with_code-%d-brightgreen)](#-papers)" % with_code,
        "[![Datasets](https://img.shields.io/badge/datasets-index-orange)](DATASETS.md)",
        "[![Update](https://img.shields.io/badge/last_update-%s-lightgrey)](#)" % date.today().isoformat(),
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)",
        "",
        "> 本列表由 `scripts/build.py` 从 [`data/entries.json`](data/entries.json) 自动生成，**请勿直接编辑本文件**。",
        "> This README is generated. Add papers by editing `data/entries.json` (see [CONTRIBUTING.md](CONTRIBUTING.md)).",
        "",
        "## 目录 / Contents",
        "",
        "- [论文 / Papers](#-papers)",
        "- [按任务浏览 / Browse by task](#-browse-by-task)",
        "- [只看已发表 / Peer-reviewed only](docs/published.md)",
        "- [数据集 / Datasets](DATASETS.md)",
        "- [贡献 / Contributing](CONTRIBUTING.md)",
        "",
    ]

    # ---- browse by task ----
    L += ["## 按任务浏览 / Browse by task", "", "| 任务 | 篇数 | 列表 |", "|:--|--:|:--|"]
    for tid, n in tag_counts.most_common():
        if n < 3:
            continue
        L.append(f"| `{tid}` | {n} | [查看](docs/topics/{slug(tid)}.md) |")
    L += ["", "---", "", "## 论文 / Papers", ""]

    # ---- per year: the two newest years inline, older ones on their own page ----
    INLINE_YEARS = set(years[:2])
    for y in years:
        if y not in INLINE_YEARS:
            L += [f"### {y} <sub>({len(by_year[y])})</sub>", "",
                  f"→ [查看 {y} 年完整列表](docs/year/{y}.md)", ""]
            continue
        L += [f"### {y} <sub>({len(by_year[y])})</sub>", ""]
        by_venue = defaultdict(list)
        for e in by_year[y]:
            by_venue[e["venue"]].append(e)
        for v in sorted(by_venue, key=venue_rank):
            items = by_venue[v]
            L += [f"<details><summary><b>{v}</b> · {len(items)}</summary>", ""]
            for e in items:
                L.append(entry_line(e))
            L += ["", "</details>", ""]
        L.append("")

    L += [
        "---",
        "",
        f"### 更早年份 / Earlier years",
        "",
        " | ".join(f"[{y}](docs/year/{y}.md)" for y in years if y not in INLINE_YEARS),
        "",
        "## 说明 / Notes",
        "",
        f"- 共 **{total}** 篇（2021 年至今），其中 **{with_code}** 篇附带代码链接；年份为会议年份，纯 arXiv 为首次提交年份。",
        "- 收录范围：点云相关（检测、分割、配准、补全、分类、跟踪、SLAM、生成、压缩、预训练等），不限于单一子方向。",
        "- 2021 年前的经典工作未收录；数据集见 [DATASETS.md](DATASETS.md)（不受年份限制）。",
        "- 每日自动同步：[`.github/workflows/arxiv-sync.yml`](.github/workflows/arxiv-sync.yml)。",
        "- 灵感与对照：[zhulf0804/3D-PointCloud](https://github.com/zhulf0804/3D-PointCloud)（2024-08 起停更）。",
        "",
        "## License",
        "",
        "内容以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 发布，脚本以 MIT 发布。",
        "",
    ]
    return "\n".join(L)


def write_topics(entries, tags):
    os.makedirs(TOPICS, exist_ok=True)
    for f in os.listdir(TOPICS):
        os.remove(os.path.join(TOPICS, f))
    names = {t["id"]: t["name"] for t in tags["tags"]}
    buckets = defaultdict(list)
    for e in entries:
        for t in e.get("tags", []):
            buckets[t].append(e)
    rows = []
    for tid, items in sorted(buckets.items(), key=lambda kv: -len(kv[1])):
        items.sort(key=sort_key)
        L = [f"# {names.get(tid, tid)} · `{tid}`", "", f"共 **{len(items)}** 篇 · 返回 [索引](../../README.md#-browse-by-task)", "", "---", ""]
        cur = None
        for e in items:
            if e["year"] != cur:
                cur = e["year"]
                L += [f"## {cur}", ""]
            L.append(entry_line(e))
        L.append("")
        open(os.path.join(TOPICS, f"{slug(tid)}.md"), "w", encoding="utf-8").write("\n".join(L))
        rows.append((tid, len(items)))
    return rows


def write_year_pages(entries):
    """docs/year/<year>.md — full list for one year, grouped by venue."""
    outdir = os.path.join(ROOT, "docs", "year")
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        os.remove(os.path.join(outdir, f))
    by_year = defaultdict(list)
    for e in entries:
        by_year[int(e["year"])].append(e)
    for y in sorted(by_year, reverse=True):
        items = sorted(by_year[y], key=sort_key)
        by_venue = defaultdict(list)
        for e in items:
            by_venue[e["venue"]].append(e)
        L = [f"# {y}", "", f"共 **{len(items)}** 篇 · 返回 [索引](../../README.md#-papers)", "", "---", ""]
        for v in sorted(by_venue, key=venue_rank):
            L += [f"## {v} <sub>({len(by_venue[v])})</sub>", ""]
            for e in by_venue[v]:
                L.append(entry_line(e))
            L.append("")
        open(os.path.join(outdir, f"{y}.md"), "w", encoding="utf-8").write("\n".join(L))
    return len(by_year)


def write_published(entries):
    """docs/published.md — only peer-reviewed entries, grouped by venue, newest first."""
    pub = [e for e in entries if e["venue"] != "arXiv"]
    if not pub:
        return 0
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    by_venue = defaultdict(list)
    for e in pub:
        by_venue[e["venue"]].append(e)

    L = ["# 已正式发表 / Peer-reviewed only", "",
         f"共 **{len(pub)}** 篇（另有 {len(entries) - len(pub)} 篇为 arXiv 预印本，见 [README](../../README.md)）。",
         "按会议/期刊分组，组内按年份倒序。", "", "---", ""]
    for v in sorted(by_venue, key=lambda x: (-len(by_venue[x]), venue_rank(x))):
        items = sorted(by_venue[v], key=sort_key)
        L += [f"## {v} <sub>({len(items)})</sub>", ""]
        for e in items:
            L.append(f"- {e['year']} — " + entry_line(e)[2:])
        L.append("")
    open(os.path.join(ROOT, "docs", "published.md"), "w", encoding="utf-8").write("\n".join(L))
    return len(pub)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    entries, tags, problems = load()
    if problems:
        print(f"[!] {len(problems)} problem(s) in data/entries.json:", file=sys.stderr)
        for p in problems[:30]:
            print("  -", p, file=sys.stderr)
        if len(problems) > 30:
            print(f"  ... and {len(problems) - 30} more", file=sys.stderr)
        return 1

    readme = render_readme(entries, tags)
    if args.check:
        old = open(README, encoding="utf-8").read() if os.path.exists(README) else ""
        if old != readme:
            print("[!] README.md is stale. Run: python scripts/build.py", file=sys.stderr)
            return 1
        print("[ok] README.md is up to date")
        return 0

    open(README, "w", encoding="utf-8").write(readme)
    rows = write_topics(entries, tags)
    write_year_pages(entries)
    n_pub = write_published(entries)
    print(f"[ok] README.md: {len(entries)} papers, {len(rows)} topics, {n_pub} peer-reviewed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
