# Council candidates and mayor candidates (Taipei)

`taipei.jsonl` holds the public evidence behind the 「與市長候選人的關係」 layer in `index.html`.
One line is one evidence item. The rule is in `rubric.md` 3.4. This layer is information only: it does not change any score or recommendation.

| Field | Meaning |
|---|---|
| `race`, `no`, `name` | Council district (`d1`–`d8`), ballot number, name |
| `mayor` | The 2026 Taipei mayor candidate the item is about |
| `relation` | `support` or `oppose` |
| `kind` | `endorse`, `rally`, `joint`, `statement`, `council`, `distance` |
| `level` | `明確` (official record, 2+ outlets, or a direct quote or clear description in one outlet) or `傾向` (all other items, and all council acts) |
| `date` | Date of the act, when the source gives it |
| `text` | What was done or said (zh-TW) |
| `sources` | News or official pages. No social media, no forums, no polls |

Limits:
- A candidate with no line is 「未見」: no report was found. It does not mean there is no relation.
- Same party alone is not evidence.
- Most items rest on one outlet. Each source page was checked to name both people; the claims themselves were not all re-read in full.
