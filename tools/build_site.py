"""Copy the built guide page into the repo as index.html, as a standalone document.

The guide is built as a claude.ai artifact body (it starts at <title>). claude.ai adds
the document skeleton when it publishes, so the built file has no doctype, charset or
viewport. A plain web server, a downloaded copy, or an archive copy needs them.

Usage: python3 tools/build_site.py PATH/TO/guide.html
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEAD = (
    "<!doctype html>\n"
    '<html lang="zh-Hant-TW">\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
)


def main(src):
    body = Path(src).read_text(encoding="utf-8")
    low = body.lstrip()[:200].lower()
    if low.startswith("<!doctype") or "<meta charset" in low:
        sys.exit(f"{src} already has a document head; copy it as it is")
    if not low.startswith("<title>"):
        sys.exit(f"{src} does not start with <title>; is it the built guide?")
    out = ROOT / "index.html"
    out.write_text(HEAD + body, encoding="utf-8")
    print(f"{out.name}: {out.stat().st_size // 1024} KiB")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
