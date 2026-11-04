"""Check ledger contributions: append-only rule, line schema, and verbatim-quote check.

usage:
  python3 tools/check_ledger.py --base origin/main [--actor NAME --owner NAME] [--no-fetch]
  python3 tools/check_ledger.py --files ledger/2026-11-05_alice_gpt-5.6-sol.jsonl [--no-fetch]

Exit code 1 only for rule or schema errors. A quote that cannot be found is reported
("check by hand") but does not fail the run: some official sites block automated fetches.
Writes a Markdown report to $GITHUB_STEP_SUMMARY when set, else to stdout.
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = re.compile(r"^ledger/\d{4}-\d{2}-\d{2}_[A-Za-z0-9-]{1,39}_[a-z0-9.\-]{2,60}\.jsonl$")
VERDICTS = {"確認", "推翻", "更新", "查無", "新增"}
GRADE = re.compile(r"^([1-5]-[ABC]|N(-[ABC])?)$")
CLAIM_ID = re.compile(r"^(M|D[1-8])-\d{2}-\d{2}$")
NEW_ID = re.compile(r"^(M|D[1-8])-\d{2}-N\d{2,3}$")
REQUIRED = ["claim", "verdict", "grade", "url", "quote", "checked_at", "model", "tool", "contributor"]
PROTECTED = ("claims/", "VERIFY.md", "rubric.md", "guide.md", "RELEASES.md", "SHA256SUMS", "tools/", ".github/")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140 Safari/537.36"


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def changed(base):
    rows = []
    for line in git("diff", "--name-status", "--no-renames", f"{base}...HEAD").splitlines():
        st, _, path = line.partition("\t")
        rows.append((st[0], path))
    return rows


def claim_ids():
    ids = set()
    for p in (ROOT / "claims").glob("*.jsonl"):
        for l in p.read_text().splitlines():
            if l.strip():
                ids.add(json.loads(l)["id"])
    return ids


def norm(s):
    return re.sub(r"[\s\W_]+", "", unicodedata.normalize("NFKC", html.unescape(s)))


def fetch(url):
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "page"
        r = subprocess.run(["curl", "-s", "-L", "-m", "30", "-A", UA, "-o", str(f), "-w", "%{http_code} %{content_type}", url],
                           capture_output=True, text=True)
        code, _, ctype = (r.stdout or "000 ").partition(" ")
        if not f.exists():
            return code, ""
        raw = f.read_bytes()
        if raw[:4] == b"%PDF" or "pdf" in ctype:
            t = subprocess.run(["pdftotext", "-layout", str(f), "-"], capture_output=True, text=True).stdout
        else:
            t = raw.decode("utf-8", "ignore")
            t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
            t = re.sub(r"<[^>]+>", " ", t)
        return code, t


def quote_status(quote, text):
    q, t = norm(quote), norm(text)
    if not q:
        return "no-quote", 0.0
    if q in t:
        return "exact", 1.0
    best, step = 0.0, max(1, len(q) // 4)
    for i in range(0, max(1, len(t) - len(q) + 1), step):
        r = SequenceMatcher(None, q, t[i:i + len(q)]).ratio()
        best = max(best, r)
        if best > 0.95:
            break
    return ("fuzzy" if best >= 0.8 else "missing"), round(best, 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    ap.add_argument("--files", nargs="*")
    ap.add_argument("--actor", default="")
    ap.add_argument("--owner", default="")
    ap.add_argument("--no-fetch", action="store_true")
    a = ap.parse_args()
    errors, report = [], []
    files = list(a.files or [])
    if a.base:
        is_owner = a.actor and a.actor == a.owner
        for st, path in changed(a.base):
            if path.startswith("ledger/") and path != "ledger/README.md":
                if st != "A":
                    errors.append(f"`{path}`: ledger files are append-only (status {st}). Add a new file instead.")
                elif path.endswith(".jsonl"):
                    files.append(path)
            elif path.startswith(PROTECTED) and not is_owner:
                errors.append(f"`{path}`: only the maintainer changes this file. Put your findings in a new ledger file.")
    ids = claim_ids()
    seen = set()
    for fp in files:
        if not NAME.match(fp):
            errors.append(f"`{fp}`: name must be ledger/YYYY-MM-DD_<github-handle>_<model-slug>.jsonl")
        for n, line in enumerate((ROOT / fp).read_text().splitlines(), 1):
            if not line.strip():
                continue
            where = f"`{fp}` line {n}"
            try:
                r = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append(f"{where}: not valid JSON ({e.msg})")
                continue
            miss = [k for k in REQUIRED if not str(r.get(k, "")).strip()]
            if miss:
                errors.append(f"{where}: missing {', '.join(miss)}")
                continue
            if r["verdict"] not in VERDICTS:
                errors.append(f"{where}: verdict must be one of {', '.join(sorted(VERDICTS))}")
            if not GRADE.match(r["grade"].strip("【】")):
                errors.append(f"{where}: grade must look like 5-A, 4-C or N")
            cid = r["claim"]
            if r["verdict"] == "新增":
                if not NEW_ID.match(cid):
                    errors.append(f"{where}: a 新增 line needs a new id like D3-05-N01")
            elif cid not in ids:
                errors.append(f"{where}: claim id {cid} does not exist in claims/")
            if r["verdict"] != "查無":
                if not r["url"].startswith("https://") and not r["url"].startswith("http://"):
                    errors.append(f"{where}: url must be a full http(s) URL")
                if len(r["quote"]) > 80:
                    errors.append(f"{where}: quote must be at most 80 characters")
            if (cid, r["url"]) in seen:
                errors.append(f"{where}: duplicate claim + url in this contribution")
            seen.add((cid, r["url"]))
            if r["verdict"] == "查無" or a.no_fetch:
                report.append((cid, r["verdict"], r["grade"], r["url"], "-", "not fetched" if a.no_fetch else "n/a", r["model"]))
                continue
            url = re.sub(r"[?&]utm_source=[^&]+", "", r["url"])
            code, text = fetch(url)
            st, score = quote_status(r["quote"], text) if text else ("unfetched", 0.0)
            label = {"exact": "pass", "fuzzy": f"pass (similar {score})"}.get(st, f"check by hand ({st})")
            report.append((cid, r["verdict"], r["grade"], url, code, label, r["model"]))
    out = ["## Ledger check", ""]
    if errors:
        out += ["### Errors (must fix)", ""] + [f"- {e}" for e in errors] + [""]
    if report:
        out += ["### Quote check", "", "| claim | verdict | grade | HTTP | result | model | URL |", "|---|---|---|---|---|---|---|"]
        out += [f"| {c} | {v} | {g} | {h} | {s} | {m} | {u[:80]} |" for c, v, g, u, h, s, m in report]
        passed = sum(1 for x in report if x[5].startswith("pass"))
        out += ["", f"{passed} of {len(report)} lines passed the quote check. Lines marked 'check by hand' need a maintainer to open the page."]
    if not errors and not report:
        out.append("No ledger contributions in this change.")
    text = "\n".join(out) + "\n"
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write(text)
    print(text)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
