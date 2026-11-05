"""Export the referendum section (Markdown) to claims/R22.jsonl with stable claim IDs.

usage: python3 tools/export_referendum.py --version 0.2.0 --as-of 2026-11-05 SECTION.md

Each bullet, numbered item, table row and paragraph in subsections 13.1-13.12 becomes one
claim. The self-check questions (13.5) and the model verdict (13.13, see panel/R22.json)
are not claims. IDs look like R22-08-14 (subsection at first export, sequence). When
claims/R22.jsonl already exists, a line that is the same or a light rewording
(similarity >= 0.6, same field) keeps its old ID. IDs are never reused.
"""
import argparse
import hashlib
import json
import re
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RACE = "R22"
H3 = re.compile(r"^### 13\.(\d+) (.+?)\s*$")
H4 = re.compile(r"^#### (.+?)\s*$")
REF = re.compile(r"^- \[([A-Z][A-Z0-9]*-\d+)\]\s*(.*)$")
TAG = re.compile(r"\[([A-Z][A-Z0-9]*-\d+)\]")
URL = re.compile(r"<(https?://[^>]+)>")
GRADE = re.compile(r"【([1-5N](?:-[ABC])?)】")
ITEM = re.compile(r"^\s*(?:[-*]|\d+\.)\s+(.*)$")
KEY = re.compile(r"主文|門檻|第 ?29 條|第 ?30 條|第 ?32 條|必要處置|理由書|意見書|改寫|修正動議|綁大選|中選會|地震|斷層|核廢|蘭嶼|事故|除役")
SKIP_SECTIONS = {5}


def norm(s):
    return re.sub(r"[\s\W_]+", "", TAG.sub("", s))


def parse(path):
    text = Path(path).read_text()
    text = re.sub(r"<!-- MOA22 BEGIN -->.*?<!-- MOA22 END -->", "", text, flags=re.S)
    body, _, refs = text.partition("<!-- REFS -->")
    refmap = {}
    for line in refs.splitlines():
        m = REF.match(line.strip())
        if m:
            u = URL.search(m.group(2))
            refmap[m.group(1)] = {"id": m.group(1), "title": URL.sub("", m.group(2)).strip(" .；"), "url": u.group(1) if u else ""}
    body = re.sub(r"\[\[#[^\]|]+\\?\|([^\]]+)\]\]", r"\1", body)
    items, sec, title, sub, header = [], 0, "", "", None
    para = []

    def flush():
        if para and sec and sec not in SKIP_SECTIONS:
            t = " ".join(para).strip()
            if t and not t.startswith("來源："):
                items.append((sec, title, sub, t))
        para.clear()

    for line in body.splitlines():
        m3, m4 = H3.match(line), H4.match(line)
        if m3 or m4 or not line.strip():
            flush()
            if m3:
                sec, title, sub, header = int(m3.group(1)), m3.group(2), "", None
            elif m4:
                sub, header = m4.group(1), None
            if not line.strip():
                header = header if header else None
            continue
        if not sec or sec in SKIP_SECTIONS:
            continue
        s = line.strip()
        if s.startswith("|"):
            flush()
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", s.strip("|"))]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            if header is None:
                header = cells
                continue
            items.append((sec, title, sub, "｜".join(f"{h}：{c}" for h, c in zip(header, cells) if c)))
            continue
        header = None
        if s.startswith(">"):
            s = re.sub(r"^>\s?(\[!\w+\][^\n]*)?", "", s).strip()
            if not s:
                continue
        m = ITEM.match(s)
        if m:
            flush()
            items.append((sec, title, sub, m.group(1).strip()))
        else:
            para.append(s)
    flush()
    return items, refmap


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True)
    ap.add_argument("--as-of", required=True)
    ap.add_argument("section")
    a = ap.parse_args()
    items, refmap = parse(a.section)
    out = ROOT / "claims" / f"{RACE}.jsonl"
    old = [json.loads(l) for l in out.read_text().splitlines() if l.strip()] if out.exists() else []
    used_ids = {c["id"] for c in old}
    taken, rows = set(), []
    for sec, title, sub, text in items:
        field = f"{title}／{sub}" if sub else title
        best, score = None, 0.0
        for c in old:
            if c["field"] != field or c["id"] in taken or c.get("retired_in"):
                continue
            r = SequenceMatcher(None, norm(text), norm(c["text"])).ratio()
            if r > score:
                best, score = c, r
        if best and score >= 0.6:
            cid = best["id"]
            revised = best.get("revised", 0) + (1 if norm(text) != norm(best["text"]) else 0)
        else:
            n = 1
            while f"{RACE}-{sec:02d}-{n:02d}" in used_ids:
                n += 1
            cid, revised = f"{RACE}-{sec:02d}-{n:02d}", 0
        used_ids.add(cid)
        taken.add(cid)
        refs = [refmap[t] for t in dict.fromkeys(TAG.findall(text)) if t in refmap]
        rows.append({
            "id": cid, "race": RACE, "section": f"13.{sec}", "field": field, "text": text,
            "grades": GRADE.findall(text), "key": bool(KEY.search(field + text)), "refs": refs,
            "text_sha256": hashlib.sha256(text.encode()).hexdigest()[:16],
            "revised": revised, "as_of": a.as_of, "version": a.version,
        })
    retired = [c for c in old if c["id"] not in taken]
    rows += [c if c.get("retired_in") else dict(c, retired_in=a.version) for c in retired]
    rows.sort(key=lambda r: (int(r["id"].split("-")[1]), int(r["id"].split("-")[2])))
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"{RACE}: {len(rows) - len(retired)} claims, {len(retired)} retired, {sum(r['key'] for r in rows)} key, "
          f"{sum(1 for r in rows if not r['refs'])} without refs")


if __name__ == "__main__":
    main()
