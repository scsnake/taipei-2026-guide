# Ledger

Append-only re-check results. One file per contribution, named
`YYYY-MM-DD_<github-handle>_<model-slug>.jsonl`. Never edit or delete a file here: CI rejects it.
A correction is a new line in a new file that points to the same claim id.

Line format (one JSON object per line):

| Field | Required | Meaning |
|---|---|---|
| `claim` | yes | A claim id from `claims/` (for example `D3-05-03`), or a new id `D3-05-N01` with verdict 新增 |
| `verdict` | yes | 確認, 推翻, 更新, 查無 or 新增 |
| `grade` | yes | Evidence grade, for example `5-A`, `4-C`, `N` (see `rubric.md`) |
| `url` | yes | The page you opened (`-` for 查無) |
| `quote` | yes | Verbatim text from that page, at most 60 Chinese characters (`-` for 查無) |
| `page_date` | no | Date on the page, `YYYY-MM-DD` |
| `archive` | no | An Internet Archive snapshot of the page |
| `checked_at` | yes | ISO 8601 time with time zone |
| `note` | no | At most 40 characters, zh-TW: what changed, or the new status |
| `model` | yes | Model name and effort, self-reported |
| `tool` | yes | App or CLI and its version |
| `contributor` | yes | `github:<handle>` of the human who submits the file |
