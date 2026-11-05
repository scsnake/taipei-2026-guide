# Taipei 2026 voter guide: open claims for re-verification

台北市 2026-11-28 市長與市議員選舉的候選人資料，以及同日投票的全國性公投第 22 案（核電）。每一項事實都拆成一條可單獨查證的「主張」（claim），附證據等級與來源。歡迎用你自己的 AI 代理重新查證，並把結果提交到 `ledger/`。

> **Status: draft (v0.2.0).** All candidate profiles have the full fact-check, and the model panel has scored every race and referendum case 22. The 2026 election bulletin (選舉公報) is not yet online, so some platforms are still incomplete. Do not cite this guide as final until a release says so in [RELEASES.md](RELEASES.md).

## What is here

| Path | What it is |
|---|---|
| `guide.md` | The full guide (zh-TW): candidate profiles, method, model panel, referendum case 22, counterarguments, references. |
| `claims/<race>.jsonl` | One line per claim, with a stable id, the zh-TW text, the evidence grade 【L-S】, and its sources. Races: `M` mayor, `D1`–`D6` council districts, `D7` and `D8` indigenous districts, `R22` referendum case 22. |
| `rubric.md` | The method: evidence grades, the cross-strait scale, and the value criteria. |
| `rubric_r22.md` | The criteria for referendum case 22: scenarios, net-effect scoring, weights, rules. |
| `panel/` | The model panel's structured verdict for each race and for case 22, with the case 22 decision map. |
| `VERIFY.md` | A prompt that you give to your own AI agent to re-verify claims. |
| `ledger/` | Append-only re-check results from contributors. Never edited, only added to. |
| `RELEASES.md`, `SHA256SUMS` | Each release with the SHA-256 hash of every published file. |
| `tools/` | Scripts: export claims, check ledger files, write release hashes. |

## How to re-verify

1. Download the latest release. Check the hashes: `shasum -a 256 -c SHA256SUMS`.
2. Give [VERIFY.md](VERIFY.md) and the `claims/` files to an agent that can search the web.
3. Read its output. Remove anything you cannot stand behind.
4. Submit it as a new file in `ledger/` through a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## How the guide was made

- Research and writing: Claude Opus 5.5.
- Fact-check: GPT-5.6 Sol (Codex CLI, live web search). Every returned quote is fetched from the cited page and matched automatically.
- Scoring panel (cross-strait scale, criteria-based ranking, and referendum case 22): Claude Fable 5.1 (moderator), GPT-6.1 Sol and Gemini 4 Argon (debaters).
- The questions and criteria came from the human maintainer, who reviews every release.

The ranking and the referendum result follow stated criteria and weights. They are not endorsements. The weights are a value choice; `rubric.md` and `rubric_r22.md` show them, so you can apply your own.

## How history is protected

- Every change is a signed git commit. Use `git log` and `git blame` to see who changed what, and when.
- `main` accepts changes only through reviewed pull requests. Force-pushes are off.
- Ledger files are append-only. CI rejects a pull request that changes or deletes one. A correction is a new line.
- Each release is a signed tag, with SHA-256 hashes in `RELEASES.md`. A copy of each release goes to the Internet Archive.
- A bad change can be undone with `git revert`, or by rebuilding from the last good tag.

## Corrections and right of reply

Candidates and their teams can ask for a correction or add a reply. Open an issue with the label `reply` and give the claim id and a source. Replies from the person concerned are added to the claim, next to the accusation.

## License

Text and data: [CC BY 4.0](LICENSE). Scripts in `tools/`: [MIT](LICENSE-CODE).
