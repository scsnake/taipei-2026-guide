# Claims

One file per race: `M` (mayor), `D1`–`D6` (council districts), `D7` and `D8` (indigenous districts), and `R22` (national referendum case 22).
Each line is one claim, exported from the guide by `tools/export_claims.py`.

| Field | Meaning |
|---|---|
| `id` | Stable id `<race>-<ballot no>-<seq>`. It stays the same when the text is lightly reworded. Ids are never reused. |
| `candidate_no`, `candidate`, `party`, `status` | Ballot number, name, party, incumbent or newcomer |
| `field` | Profile field, for example 背景, 主要政見, 爭議、法律與金錢事項, 兩岸指標 |
| `text` | The claim in zh-TW, with local source tags like `[D3-57]` |
| `grades` | Evidence grades found in the text (`5-B`, …); `（舊標記）` marks an old-style grade not yet converted |
| `key` | `true` for crime, money, PRC ties or democracy conduct: check these first |
| `refs` | The sources cited in the text: tag, title, URL |
| `text_sha256` | First 16 hex digits of the SHA-256 of `text` |
| `revised` | How many releases changed this claim's text |
| `as_of`, `version` | Data date and release version of this export |
| `retired_in` | Set when the claim was removed from the guide in that version; the line is kept for history |

## Referendum case 22 (`R22.jsonl`)

Exported by `tools/export_referendum.py` from guide section 13 (13.1–13.12). Each bullet, numbered item, table row and paragraph is one claim. The self-check questions (13.5) and the model verdict (13.13, see `panel/R22.json`) are not claims.

- `id` is `R22-<subsection>-<seq>`, for example `R22-09-14`. The subsection number is fixed at first export, so it can differ from the section number in a later guide.
- `section` is the subsection in this release; `field` is its title, with the H4 title after `／`.
- There are no candidate fields. Lines labeled （推論） or （估算） are the guide's own inference or estimate, not sourced facts.

