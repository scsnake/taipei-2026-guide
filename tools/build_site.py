"""Copy the built guide page into the repo as index.html, as a standalone document.

The guide is built as a claude.ai artifact body (it starts at <title>). claude.ai adds
the document skeleton when it publishes, so the built file has no doctype, charset or
viewport. A plain web server, a downloaded copy, or an archive copy needs them.

The artifact links to the other site pages by their full GitHub Pages address, because a
relative link does not work inside claude.ai. The repo copy uses relative links instead,
so the pages also link to each other in a local copy, a fork or an archive copy.

Usage: python3 tools/build_site.py PATH/TO/guide.html [OUT_NAME]
       OUT_NAME defaults to index.html (for example: mayors.html for the mayors page).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEAD = (
    "<!doctype html>\n"
    '<html lang="zh-Hant-TW">\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
)
PAGES = "https://scsnake.github.io/taipei-2026-guide/"
SITE_LINK = re.compile(r'href="' + re.escape(PAGES) + r'([A-Za-z0-9_-]+\.html(?:#[^"]*)?)"')


def main(src, name="index.html"):
    body = Path(src).read_text(encoding="utf-8")
    low = body.lstrip()[:200].lower()
    if low.startswith("<!doctype") or "<meta charset" in low:
        sys.exit(f"{src} already has a document head; copy it as it is")
    if not low.startswith("<title>"):
        sys.exit(f"{src} does not start with <title>; is it the built guide?")
    if "/" in name or not name.endswith(".html"):
        sys.exit(f"{name}: give a plain .html file name in the repo root")
    out = ROOT / name
    body, n = SITE_LINK.subn(r'href="\1"', body)
    out.write_text(HEAD + body, encoding="utf-8")
    print(f"{out.name}: {out.stat().st_size // 1024} KiB, {n} site link(s) made relative")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(*sys.argv[1:])
