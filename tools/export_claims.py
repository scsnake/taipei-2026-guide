"""Export candidate profile sections (Markdown) to claims/<race>.jsonl with stable claim IDs.

usage: python3 tools/export_claims.py --version 0.1.0 --as-of 2026-11-04 SECTION.md[:RACE[:START:END]] ...

Each bullet line in a candidate block becomes one claim. IDs look like D3-05-03
(race, ballot number, sequence). When claims/<race>.jsonl already exists, a line that
is the same or a light rewording (similarity >= 0.6, same candidate and field) keeps
its old ID; new lines get the next free sequence number. IDs are never reused.
"""
import argparse
import hashlib
import json
import re
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
H4 = re.compile(r"^#### (\d+)\. (.+?)（(.+)）\s*$")
FIELD = re.compile(r"^- \*\*(.+?)：\*\*\s*(.*)$")
SUB = re.compile(r"^\s{2,}- (.*)$")
REF = re.compile(r"^- \[([A-Z][A-Z0-9]*-\d+)\]\s*(.*)$")
TAG = re.compile(r"\[([A-Z][A-Z0-9]*-\d+)\]")
URL = re.compile(r"<(https?://[^>]+)>")
GRADE = re.compile(r"【([1-5N](?:-[ABC])?)】")
OLD = {"事實": "5", "強推論": "4", "弱推論": "3", "事實後推翻": "1", "無據": "N"}
OLDTAG = re.compile(r"【(" + "|".join(OLD) + r")】")
KEY = re.compile(r"起訴|判決|判處|判刑|一審|二審|有罪|無罪|不起訴|緩起訴|偵查|搜索|交保|收押|告訴|告發|提告|誹謗|賄|貪污|圖利|詐|洗錢|背信|獻金|助理費|回扣|國安|共諜|間諜|滲透|統戰|國台辦|台辦|海峽論壇|中共|赴中|雙城論壇|統一|台獨|九二共識|一中|境外|罷免|國會改革|選舉")


def norm(s):
    return re.sub(r"[\s\W_]+", "", TAG.sub("", s))


def parse(path, start=None, end=None):
    text = Path(path).read_text()
    body, _, refs = text.partition("<!-- REFS -->")
    refmap = {}
    for line in refs.splitlines():
        m = REF.match(line.strip())
        if m:
            u = URL.search(m.group(2))
            refmap[m.group(1)] = {"id": m.group(1), "title": URL.sub("", m.group(2)).strip(" .；"), "url": u.group(1) if u else ""}
    if start:
        a = body.index(start)
        b = body.index(end) if end else len(body)
        body = body[a:b]
    items, cand, field = [], None, None
    for line in body.splitlines():
        m = H4.match(line)
        if m:
            meta = m.group(3).split("；")
            cand = {"no": int(m.group(1)), "name": m.group(2).strip(), "party": meta[0], "status": "；".join(meta[1:])}
            field = None
            continue
        if cand is None:
            continue
        if line.startswith("### ") or line.startswith("## "):
            cand = None
            continue
        f = FIELD.match(line)
        s = SUB.match(line)
        if f:
            field = f.group(1)
            if f.group(2).strip():
                items.append((cand, field, f.group(2).strip()))
        elif s and field:
            items.append((cand, field, s.group(1).strip()))
    return items, refmap


def grades(t):
    g = GRADE.findall(t)
    g += [OLD[x] + "（舊標記）" for x in OLDTAG.findall(t)]
    return g


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True)
    ap.add_argument("--as-of", required=True)
    ap.add_argument("sections", nargs="+")
    a = ap.parse_args()
    for spec in a.sections:
        parts = spec.split(":")
        path, race = parts[0], parts[1] if len(parts) > 1 else Path(parts[0]).stem
        start = parts[2] if len(parts) > 2 else None
        end = parts[3] if len(parts) > 3 and parts[3] else None
        items, refmap = parse(path, start, end)
        out = ROOT / "claims" / f"{race}.jsonl"
        old = [json.loads(l) for l in out.read_text().splitlines() if l.strip()] if out.exists() else []
        used_ids = {c["id"] for c in old}
        taken = set()
        rows = []
        for cand, field, text in items:
            key = (cand["no"], field)
            best, score = None, 0.0
            for c in old:
                if (c["candidate_no"], c["field"]) != key or c["id"] in taken or c.get("retired_in"):
                    continue
                r = SequenceMatcher(None, norm(text), norm(c["text"])).ratio()
                if r > score:
                    best, score = c, r
            if best and score >= 0.6:
                cid = best["id"]
                revised = best.get("revised", 0) + (1 if norm(text) != norm(best["text"]) else 0)
            else:
                n = 1
                while f"{race}-{cand['no']:02d}-{n:02d}" in used_ids:
                    n += 1
                cid = f"{race}-{cand['no']:02d}-{n:02d}"
                revised = 0
            used_ids.add(cid)
            taken.add(cid)
            refs = [refmap[t] for t in dict.fromkeys(TAG.findall(text)) if t in refmap]
            rows.append({
                "id": cid, "race": race, "candidate_no": cand["no"], "candidate": cand["name"],
                "party": cand["party"], "status": cand["status"], "field": field,
                "text": text, "grades": grades(text), "key": bool(KEY.search(field + text)),
                "refs": refs, "text_sha256": hashlib.sha256(text.encode()).hexdigest()[:16],
                "revised": revised, "as_of": a.as_of, "version": a.version,
            })
        retired = [c for c in old if c["id"] not in taken]
        for c in retired:
            rows.append(c if c.get("retired_in") else dict(c, retired_in=a.version))
        rows.sort(key=lambda r: (r["candidate_no"], r["id"]))
        out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        print(f"{race}: {len(rows) - len(retired)} claims, {len(retired)} retired, {sum(r['key'] for r in rows)} key")


if __name__ == "__main__":
    main()
