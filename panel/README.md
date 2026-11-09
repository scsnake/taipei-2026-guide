# Panel verdicts

One file per race: the structured verdict of the model panel, as written by the moderator.
The full reasoning (scores, disagreements, sensitivity, limits) is in `guide.md` section 12 (candidates) and 13.13 (referendum case 22).

| Field | Meaning |
|---|---|
| `race` | `M`, `D1`–`D6`, `D7-D8` (one debate for both indigenous districts), `R22` (national referendum case 22) |
| `completed` | Date the debate finished |
| `moderator`, `debaters`, `rounds` | Models and settings of the debate |
| `rubric` | The criteria the panel had to apply: `rubric.md` for candidates, `rubric_r22.md` for the referendum |
| `verdict` | The moderator's JSON block, unchanged |
| `decision_map` | `R22` only: totals, weight and probability break-even points, and the voter-type table, recomputed from the verdict |

## Adjustments after the verdict

`adjustments.json` lists score changes applied after a verdict, without a rerun, under a rule added later (rubric.md 3.4 問政行為). It gives the event, the sources, and each candidate's value before and after. The verdict files themselves stay unchanged.

The rankings and the referendum result follow stated criteria and weights. They are not endorsements.
