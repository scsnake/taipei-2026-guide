"""Write SHA256SUMS and add a release entry to RELEASES.md.

usage: python3 tools/release.py VERSION "short note"
Then commit, and tag: git tag -s vVERSION -m "VERSION"
"""
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["guide.md", "index.html", "rubric.md", "rubric_r22.md", "VERIFY.md"]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(version, note):
    paths = ([ROOT / f for f in FILES if (ROOT / f).exists()] + sorted((ROOT / "claims").glob("*.jsonl"))
             + sorted((ROOT / "panel").glob("*.json")))
    sums = [(sha(p), p.relative_to(ROOT).as_posix()) for p in paths]
    (ROOT / "SHA256SUMS").write_text("".join(f"{h}  {n}\n" for h, n in sums))
    n_claims = sum(1 for p in (ROOT / "claims").glob("*.jsonl") for l in p.read_text().splitlines()
                   if l.strip() and not json.loads(l).get("retired_in"))
    n_ledger = sum(1 for p in (ROOT / "ledger").glob("*.jsonl") for l in p.read_text().splitlines() if l.strip())
    today = dt.date.today().isoformat()
    entry = [f"## v{version} — {today}", "", note, "", f"- Claims: {n_claims} (active). Ledger lines: {n_ledger}.",
             f"- SHA-256 of SHA256SUMS: `{sha(ROOT / 'SHA256SUMS')}`", "", "| File | SHA-256 |", "|---|---|"]
    entry += [f"| `{n}` | `{h}` |" for h, n in sums] + [""]
    rel = ROOT / "RELEASES.md"
    head = "# Releases\n\nEach release lists the SHA-256 hash of every published file. Check your copy with `shasum -a 256 -c SHA256SUMS` (macOS) or `sha256sum -c SHA256SUMS` (Linux). Each release is also a signed git tag.\n\n"
    old = rel.read_text()[len(head):] if rel.exists() and rel.read_text().startswith(head) else ""
    rel.write_text(head + "\n".join(entry) + "\n" + old)
    print(f"v{version}: {len(sums)} files hashed, {n_claims} claims, {n_ledger} ledger lines")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")
