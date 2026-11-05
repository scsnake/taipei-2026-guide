# Contributing

## Add a re-check (most contributions)

1. Run your agent with [VERIFY.md](VERIFY.md).
2. Save the result as one new file: `ledger/YYYY-MM-DD_<github-handle>_<model-slug>.jsonl`.
3. Read every line. You are responsible for what you submit.
4. Sign your commit (`git commit -S`). Open a pull request.
5. CI runs `tools/check_ledger.py`:
   - It rejects the pull request if it changes or deletes any existing ledger file, or changes files that only the maintainer may change.
   - It rejects lines with a missing field, an unknown claim id, or a wrong grade format.
   - It fetches each URL and searches the page for your quote. "check by hand" is not a failure: some official sites block automated fetches.
6. A maintainer reviews the result. Accepted lines go into the next release. Rejected lines stay in the ledger with the review note, so the history stays complete.

## Rules

- Public records only. No private data, no rumours, no opinions.
- Presumption of innocence: write the exact legal status (偵查中, 起訴, 一審有罪（未確定）, 判決確定, 不起訴, 無罪).
- A claim about a crime, money, or PRC ties needs a source that you opened yourself, with a verbatim quote.
- Family members appear only if they are a party to the same case, and the text must say that the candidate is not a defendant.
- Do not rank or endorse candidates in the ledger.

## What only the maintainer changes

`claims/`, `panel/`, `guide.md`, `rubric.md`, `rubric_r22.md`, `VERIFY.md`, `RELEASES.md`, `SHA256SUMS`, `tools/` and `.github/`. The maintainer applies accepted ledger lines to the claims, exports the guide again, and writes a new signed release.

## Local check

```bash
python3 tools/check_ledger.py --files ledger/<your-file>.jsonl
```
