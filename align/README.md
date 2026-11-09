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

# Mayor candidates and parties (5 major cities)

`mayors.jsonl` holds the public evidence behind the 「與政黨及政治人物的關係」 list on the mayor cards in `mayors.html`.
It covers 新北 (`nwt`), 桃園 (`tao`), 臺中 (`txg`), 臺南 (`tnn`) and 高雄 (`khh`). Other counties have no list yet.
This list is information only: it does not change any score or recommendation.

| Field | Meaning |
|---|---|
| `race`, `no`, `name` | Race code, ballot number, mayor candidate |
| `tie`, `tie_type` | The party, person or faction; `party`, `person` or `faction` |
| `relation` | `support` or `oppose` (conflict, criticism, distance) |
| `kind` | `nominate`, `endorse`, `rally`, `split`, `faction`, `statement`, `distance` |
| `level` | `明確` (official record, 2+ outlets, or a direct quote or clear description in one outlet) or `傾向` (all other items, and all faction items) |
| `date`, `text`, `sources` | As above |

Limits:
- A candidate with no line is 「未見」: no report was found. It does not mean there is no tie.
- Each source page was fetched and checked to name both the candidate and the tie.
- Items that rested only on a search summary or on an event announcement were removed.
