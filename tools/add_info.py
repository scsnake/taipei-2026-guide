"""Add the maintainer's notes in additions.md to the candidate cards.

Each line under "## 資料" in additions.md is one note:
    候選人 | YYYY-MM-DD | 內容 | https://source
候選人 is a name or a card code (mayor-3, d6-9, khh-5).

The notes go into index.html and mayors.html as a JSON block plus a small
script that shows them in a 補充資料 box on each card. The block sits
between <!--ADDITIONS--> markers, so running this again replaces it.
SHA256SUMS is updated for the two pages.

Usage:
  python3 tools/add_info.py            check additions.md and update the pages
  python3 tools/add_info.py --check    also open each source URL
  python3 tools/add_info.py --list     print card codes and names
"""
import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "additions.md"
PAGES = ("index.html", "mayors.html")
BAN = ("facebook.com", "fb.com", "instagram.com", "threads.net", "threads.com", "x.com", "twitter.com",
       "youtube.com", "youtu.be", "tiktok.com", "line.me", "ptt.cc", "dcard.tw", "disp.cc",
       "mobile01.com", "wikipedia.org", "telegram.org", "t.me")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140 Safari/537.36"
BEGIN, END = "<!--ADDITIONS-->", "<!--/ADDITIONS-->"
DATA = re.compile(r'<script id="data" type="application/json">(.*?)</script>', re.S)

STYLE = """<style>
.addn{margin:10px 0;padding:8px 10px;border-left:3px solid var(--line,#999);font-size:.88rem}
.addn h4{margin:0 0 4px;font-size:.85rem;color:var(--muted,#666)}
.addn ul{margin:0;padding:0;list-style:none}
.addn li{margin:0 0 6px;line-height:1.6;overflow-wrap:anywhere}
.addn .d{color:var(--muted,#666);margin-right:6px;font-variant-numeric:tabular-nums}
</style>"""

SCRIPT = """<script>
(() => {
  const N = JSON.parse(document.getElementById("additions").textContent);
  const box = items => {
    const d = document.createElement("div"); d.className = "addn";
    const h = document.createElement("h4"); h.textContent = "補充資料（維護者補充，不影響評分）"; d.append(h);
    const ul = document.createElement("ul");
    for (const it of items) {
      const li = document.createElement("li");
      const s = document.createElement("span"); s.className = "d"; s.textContent = it.date; li.append(s);
      li.append(document.createTextNode(it.text + " "));
      const a = document.createElement("a"); a.href = it.url; a.target = "_blank";
      a.rel = "noopener noreferrer nofollow"; a.textContent = "來源 ↗"; li.append(a);
      ul.append(li);
    }
    d.append(ul); return d;
  };
  let busy = false;
  const apply = () => {
    busy = false;
    for (const [id, items] of Object.entries(N)) {
      const card = document.getElementById(id);
      if (!card || card.querySelector(".addn")) continue;
      const fold = card.querySelector("details.bul");
      fold ? fold.before(box(items)) : card.append(box(items));
    }
  };
  const later = () => { if (!busy) { busy = true; requestAnimationFrame(apply); } };
  new MutationObserver(later).observe(document.body, {childList: true, subtree: true});
  later();
})();
</script>"""


def cards():
    """{card code: (page, element id, name)} from the data block of each page."""
    out = {}
    for page in PAGES:
        m = DATA.search((ROOT / page).read_text(encoding="utf-8"))
        if not m:
            sys.exit(f"{page}: no data block")
        for r in json.loads(m.group(1))["races"]:
            for c in r.get("candidates", []):
                out[f"{r['id']}-{c['no']}"] = (page, f"{r['id']}-c{c['no']}", c["name"])
    return out


def parse(cmap):
    names = {}
    for code, (_, _, name) in cmap.items():
        names.setdefault(name, []).append(code)
        first = re.split(r"[\s（(]", name)[0]
        if first != name:
            names.setdefault(first, []).append(code)
    lines = SRC.read_text(encoding="utf-8").split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "## 資料") + 1
    except StopIteration:
        sys.exit("additions.md: no '## 資料' heading")
    notes, errors = [], []
    for n, line in enumerate(lines[start:], start + 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        parts = [p.strip() for p in s.split("|")]
        where = f"additions.md:{n}"
        if len(parts) != 4:
            errors.append(f"{where}: need 4 fields separated by |, found {len(parts)}")
            continue
        who, day, text, url = parts
        code = who if who in cmap else None
        if not code:
            hits = sorted(set(names.get(who, [])))
            if len(hits) == 1:
                code = hits[0]
            elif hits:
                errors.append(f"{where}: {who} matches {', '.join(hits)}; write the card code")
                continue
            else:
                errors.append(f"{where}: no candidate or card code '{who}' (see --list)")
                continue
        try:
            if date.fromisoformat(day) > date.today():
                errors.append(f"{where}: date {day} is in the future")
        except ValueError:
            errors.append(f"{where}: date must be YYYY-MM-DD, got '{day}'")
        if not 4 <= len(text) <= 400:
            errors.append(f"{where}: text must be 4 to 400 characters")
        if not re.match(r"https?://[^\s|<>\"]+$", url):
            errors.append(f"{where}: source must be one http(s) URL")
        elif any(re.search(r"(^|[./])" + re.escape(b) + r"(/|$)", re.sub(r"^https?://", "", url).split("?")[0] + "/") for b in BAN):
            errors.append(f"{where}: social media, forums and Wikipedia are not accepted as sources")
        notes.append({"code": code, "line": n, "date": day, "text": text, "url": url})
    return notes, errors


def check_urls(notes):
    bad = []
    for x in notes:
        r = subprocess.run(["curl", "-s", "-L", "-m", "40", "-A", UA, "-o", "/dev/null", "-w", "%{http_code}", x["url"]],
                           capture_output=True, text=True)
        code = r.stdout.strip() or "no answer"
        print(f"  line {x['line']}: HTTP {code}  {x['url']}")
        if not code.startswith(("2", "3")):
            bad.append(f"additions.md:{x['line']}: source returned HTTP {code}; open it by hand")
    return bad


def block(items):
    data = json.dumps(items, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'{BEGIN}\n{STYLE}\n<script id="additions" type="application/json">{data}</script>\n{SCRIPT}\n{END}\n'


def apply(page, items):
    """Put the notes for one page into it (or remove the block when there are none)."""
    p = ROOT / page
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"\n?" + re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?", "", t, flags=re.S)
    if items:
        t = t + "\n" + block(items)
    p.write_text(t, encoding="utf-8")


def update_sums():
    p = ROOT / "SHA256SUMS"
    lines = p.read_text(encoding="utf-8").splitlines()
    out = []
    for l in lines:
        h, name = l.split("  ", 1)
        if name in PAGES:
            h = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        out.append(f"{h}  {name}")
    p.write_text("\n".join(out) + "\n", encoding="utf-8")


def run(check=False, quiet=False):
    cmap = cards()
    notes, errors = parse(cmap)
    if check:
        errors += check_urls(notes)
    if errors:
        sys.exit("\n".join(errors) + f"\n{len(errors)} problem(s); nothing changed")
    per_page = {page: {} for page in PAGES}
    for x in sorted(notes, key=lambda x: x["date"], reverse=True):
        page, el, _ = cmap[x["code"]]
        per_page[page].setdefault(el, []).append({k: x[k] for k in ("date", "text", "url")})
    for page in PAGES:
        apply(page, per_page[page])
    update_sums()
    if not quiet:
        for x in notes:
            print(f"  {x['code']:8} {cmap[x['code']][2]}  {x['date']}  {x['text'][:30]}")
        print(f"{len(notes)} note(s) on {sum(len(v) for v in per_page.values())} card(s); pages and SHA256SUMS updated")


if __name__ == "__main__":
    args = set(sys.argv[1:])
    if args - {"--check", "--list"}:
        sys.exit(__doc__)
    if "--list" in args:
        for code, (page, _, name) in cards().items():
            print(f"{code:8} {name}  ({page})")
    else:
        run(check="--check" in args)
