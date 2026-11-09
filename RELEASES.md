# Releases

Each release lists the SHA-256 hash of every published file. Check your copy with `shasum -a 256 -c SHA256SUMS` (macOS) or `sha256sum -c SHA256SUMS` (Linux). Each release is also a signed git tag.

## v0.4.0 — 2026-11-09

Taipei guide: a new rule for conduct in office (rubric.md 3.4 「問政行為」). The 2024-03-22 臨時會 quorum failure on the 剴剴 case lowers 民主 by 0.5 for the 24 candidates who were KMT caucus members at the time and absent at the count; this is a documented adjustment after the panel verdict, with no rerun (panel/adjustments.json). 首選 and 次選 are unchanged in every race. Two information layers that do not change any score: an optional 「我支持的市長候選人」 selector that tags each council candidate's public relation to that mayor candidate (align/taipei.jsonl), and party and political ties for the mayor candidates of 新北, 桃園, 臺中, 臺南 and 高雄 (align/mayors.jsonl). Both pages: clearer tap targets (folds, table rows, picker rows, grade and warning marks, source chips), and candidate links such as #d6-13. claims/*.jsonl are not re-exported for the new card lines. align/*.jsonl are hashed from this release on.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `8b085a0757beced5375adb36cabe8f56454aafa4a68217c17075d0ccbab591f9`

| File | SHA-256 |
|---|---|
| `guide.md` | `ac3976e4f9571b38612f8e1b90897177a406098d73770b35d8637cf6bd1bf4fe` |
| `index.html` | `7ee82bca9e6695886214d0cbac337f4727e596a8c5971d157f2748c09492a421` |
| `mayors.html` | `d56c185f8a8dae48895443a63d4db0c74cf0a92ab193bdd25136808ef0a7c2bc` |
| `rubric.md` | `d632be7ae2a51dd07804bb0c192997f497f5dc0d90a4efd6df352a0589b48c2c` |
| `rubric_r22.md` | `603c79a79fe20993fd7e50cb55b16117f3520cc1e4eaaf3b2166d28906c28166` |
| `VERIFY.md` | `6b258b552a3209ffc5c20b50213c29662ffca666ed2900179dc502b0b60a0ce1` |
| `claims/D1.jsonl` | `caeccd651de9b4c2a451c46e467d105c55b5ffe41bf3750f257c433520830031` |
| `claims/D2.jsonl` | `195c78c4b988265dc4fcb07a0f16160632282f4fed0f90342a4f8a79336900e1` |
| `claims/D3.jsonl` | `44094f3d62bf907d932e3c37dcf7d6f5edf76cf9968f464b5382d2230edb0bf4` |
| `claims/D4.jsonl` | `596cbdd009054548fd564ab42c4c4765b525479be8fa3a05da1f69045dd185b3` |
| `claims/D5.jsonl` | `52d38312e5cd6777ea4f668c02e827fd80f5604412bac46ecdd2aad6fcf4bcd7` |
| `claims/D6.jsonl` | `84afa83eaaf0b9ef6cf5f6dd3135cd1f18f59cb8e6bd215b78c57641091b8b5a` |
| `claims/D7.jsonl` | `fae83a474ad25916458d790545b29bbb113f5f530840613d2b81bc36c2267de3` |
| `claims/D8.jsonl` | `c60584cae423d1c8f5f9885e1a15450a307614071a9c2afbbb27bf1f97f5b41a` |
| `claims/M.jsonl` | `324d6079d81f1060b1617806d747b70d98b84229b6734e2809f0f89250103e4a` |
| `claims/R22.jsonl` | `6eeff34daf44626399a7d107e99d5e47a773e2c4ebcff2589934654bfd4ff448` |
| `panel/D1.json` | `e9911fa5797942ab7d92e4b655599df0b51bd8f431daa007d072528cea023ea0` |
| `panel/D2.json` | `8c07fd2209a78fe5bc3aed4f33c17d7ce09bc32b287e683c3d9ba7294ec444e6` |
| `panel/D3.json` | `f8bdd27301f38f2dd1ab5e988b977ea4ffb72590b1b04a95146ec9a67a099aeb` |
| `panel/D4.json` | `3fd5d67694bcae10b80d338421a9cde045ccdbf19c99a6ab3cf747a4fde972b4` |
| `panel/D5.json` | `40c8548f6f69af6e5b350f085edbffc0f20ec78036553f26210557840b3a0728` |
| `panel/D6.json` | `38db0e5823c81c6591922ddfd5998c0562e73ff86e7dfae12fd9e0d495b2e289` |
| `panel/D7-D8.json` | `3c669d808519beac9202f2a405505db2e2ef8a21d3dedf4105dd552842f3a726` |
| `panel/M.json` | `74eaf59e89d5fb607dd8227db80a51a2c05e2b060d9bba96ac188946969acf70` |
| `panel/R22.json` | `6e1199fed9a4eafa18845ac9c366cc2dda82094761ce9817c60a5a9390ad6f3a` |
| `panel/adjustments.json` | `864665ed5f54300afc374b794c72939c09e1d86b7a5b5dbe0913a0f9ec3d6a0c` |
| `align/mayors.jsonl` | `c2406b4916872d10ef365ad13c59071001d4f0367a7beebc2ea6bebef1466e17` |
| `align/taipei.jsonl` | `4e5faeb59e5d1ba05095cac41e39a90a67cc472e69b1574e14dd5a7b3ee6d707` |

## v0.3.1 — 2026-11-07

Search: a result whose snippet shows a court or prosecution record (判決確定, 起訴) now comes right after name matches, on both pages. 不起訴, 未起訴, 非起訴 and sentences that report an absence or an acquittal do not count. When the search word appears several times, the snippet shows the first place with such a record. Content and scores are unchanged from v0.3.0.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `2a3aa13fa69923d4456896388c458aa2c0398602ab40de62434179ac7cfb0f1b`

| File | SHA-256 |
|---|---|
| `guide.md` | `4f3a997b74e17ae41f0c5afab5454aaf61e96508ae0834960761987e85037057` |
| `index.html` | `c4ab3fca7fa81b070496bf8c8f803716b6f3b6ac669b33e51743a33641c2b4d9` |
| `mayors.html` | `8e31cca20bb78538003b842ac8410b786a52bd9436d0e625ae6fefcd8f37ab77` |
| `rubric.md` | `a893504f2751880d5fc46094aef12d9469e8abe73df71156fc3e14d217ff261a` |
| `rubric_r22.md` | `603c79a79fe20993fd7e50cb55b16117f3520cc1e4eaaf3b2166d28906c28166` |
| `VERIFY.md` | `6b258b552a3209ffc5c20b50213c29662ffca666ed2900179dc502b0b60a0ce1` |
| `claims/D1.jsonl` | `caeccd651de9b4c2a451c46e467d105c55b5ffe41bf3750f257c433520830031` |
| `claims/D2.jsonl` | `195c78c4b988265dc4fcb07a0f16160632282f4fed0f90342a4f8a79336900e1` |
| `claims/D3.jsonl` | `44094f3d62bf907d932e3c37dcf7d6f5edf76cf9968f464b5382d2230edb0bf4` |
| `claims/D4.jsonl` | `596cbdd009054548fd564ab42c4c4765b525479be8fa3a05da1f69045dd185b3` |
| `claims/D5.jsonl` | `52d38312e5cd6777ea4f668c02e827fd80f5604412bac46ecdd2aad6fcf4bcd7` |
| `claims/D6.jsonl` | `84afa83eaaf0b9ef6cf5f6dd3135cd1f18f59cb8e6bd215b78c57641091b8b5a` |
| `claims/D7.jsonl` | `fae83a474ad25916458d790545b29bbb113f5f530840613d2b81bc36c2267de3` |
| `claims/D8.jsonl` | `c60584cae423d1c8f5f9885e1a15450a307614071a9c2afbbb27bf1f97f5b41a` |
| `claims/M.jsonl` | `324d6079d81f1060b1617806d747b70d98b84229b6734e2809f0f89250103e4a` |
| `claims/R22.jsonl` | `6eeff34daf44626399a7d107e99d5e47a773e2c4ebcff2589934654bfd4ff448` |
| `panel/D1.json` | `e9911fa5797942ab7d92e4b655599df0b51bd8f431daa007d072528cea023ea0` |
| `panel/D2.json` | `8c07fd2209a78fe5bc3aed4f33c17d7ce09bc32b287e683c3d9ba7294ec444e6` |
| `panel/D3.json` | `f8bdd27301f38f2dd1ab5e988b977ea4ffb72590b1b04a95146ec9a67a099aeb` |
| `panel/D4.json` | `3fd5d67694bcae10b80d338421a9cde045ccdbf19c99a6ab3cf747a4fde972b4` |
| `panel/D5.json` | `40c8548f6f69af6e5b350f085edbffc0f20ec78036553f26210557840b3a0728` |
| `panel/D6.json` | `38db0e5823c81c6591922ddfd5998c0562e73ff86e7dfae12fd9e0d495b2e289` |
| `panel/D7-D8.json` | `3c669d808519beac9202f2a405505db2e2ef8a21d3dedf4105dd552842f3a726` |
| `panel/M.json` | `74eaf59e89d5fb607dd8227db80a51a2c05e2b060d9bba96ac188946969acf70` |
| `panel/R22.json` | `6e1199fed9a4eafa18845ac9c366cc2dda82094761ce9817c60a5a9390ad6f3a` |

## v0.3.0 — 2026-11-07

Draft. New page `mayors.html`: all 22 mayor and county magistrate races (21 with checked profiles and panel verdicts; 臺北 links to the Taipei guide). Taipei D4 panel rerun under the base-5 rule (首選 and 次選 unchanged). Two new ranking rules in `rubric.md` 3.4 and 3.5: a candidate with only base scores is never tagged 首選 or 次選, and a final violent conviction means 不列入推薦 with a warning on the card.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `0f2c9a4bb3407b7f91d9ae89e19b87aa9522f3e7954df1d4806e419b24abb037`

| File | SHA-256 |
|---|---|
| `guide.md` | `4f3a997b74e17ae41f0c5afab5454aaf61e96508ae0834960761987e85037057` |
| `index.html` | `c46feed29b9bd33c17e2b3dcd3a98a655a98ea553db58f7253236fcbee033048` |
| `mayors.html` | `01fd4c5abb8fdbfa66fe4e9827596461790807be35bb88468d040625c7565d0d` |
| `rubric.md` | `a893504f2751880d5fc46094aef12d9469e8abe73df71156fc3e14d217ff261a` |
| `rubric_r22.md` | `603c79a79fe20993fd7e50cb55b16117f3520cc1e4eaaf3b2166d28906c28166` |
| `VERIFY.md` | `6b258b552a3209ffc5c20b50213c29662ffca666ed2900179dc502b0b60a0ce1` |
| `claims/D1.jsonl` | `caeccd651de9b4c2a451c46e467d105c55b5ffe41bf3750f257c433520830031` |
| `claims/D2.jsonl` | `195c78c4b988265dc4fcb07a0f16160632282f4fed0f90342a4f8a79336900e1` |
| `claims/D3.jsonl` | `44094f3d62bf907d932e3c37dcf7d6f5edf76cf9968f464b5382d2230edb0bf4` |
| `claims/D4.jsonl` | `596cbdd009054548fd564ab42c4c4765b525479be8fa3a05da1f69045dd185b3` |
| `claims/D5.jsonl` | `52d38312e5cd6777ea4f668c02e827fd80f5604412bac46ecdd2aad6fcf4bcd7` |
| `claims/D6.jsonl` | `84afa83eaaf0b9ef6cf5f6dd3135cd1f18f59cb8e6bd215b78c57641091b8b5a` |
| `claims/D7.jsonl` | `fae83a474ad25916458d790545b29bbb113f5f530840613d2b81bc36c2267de3` |
| `claims/D8.jsonl` | `c60584cae423d1c8f5f9885e1a15450a307614071a9c2afbbb27bf1f97f5b41a` |
| `claims/M.jsonl` | `324d6079d81f1060b1617806d747b70d98b84229b6734e2809f0f89250103e4a` |
| `claims/R22.jsonl` | `6eeff34daf44626399a7d107e99d5e47a773e2c4ebcff2589934654bfd4ff448` |
| `panel/D1.json` | `e9911fa5797942ab7d92e4b655599df0b51bd8f431daa007d072528cea023ea0` |
| `panel/D2.json` | `8c07fd2209a78fe5bc3aed4f33c17d7ce09bc32b287e683c3d9ba7294ec444e6` |
| `panel/D3.json` | `f8bdd27301f38f2dd1ab5e988b977ea4ffb72590b1b04a95146ec9a67a099aeb` |
| `panel/D4.json` | `3fd5d67694bcae10b80d338421a9cde045ccdbf19c99a6ab3cf747a4fde972b4` |
| `panel/D5.json` | `40c8548f6f69af6e5b350f085edbffc0f20ec78036553f26210557840b3a0728` |
| `panel/D6.json` | `38db0e5823c81c6591922ddfd5998c0562e73ff86e7dfae12fd9e0d495b2e289` |
| `panel/D7-D8.json` | `3c669d808519beac9202f2a405505db2e2ef8a21d3dedf4105dd552842f3a726` |
| `panel/M.json` | `74eaf59e89d5fb607dd8227db80a51a2c05e2b060d9bba96ac188946969acf70` |
| `panel/R22.json` | `6e1199fed9a4eafa18845ac9c366cc2dda82094761ce9817c60a5a9390ad6f3a` |

## v0.2.0 — 2026-11-05

Draft. All candidate profiles have the full fact-check (GPT-5.6 Sol), and the model panel has scored all 9 races (`panel/`). New: national referendum case 22 (核電) — guide section 13, 239 claims in `claims/R22.jsonl`, the approved criteria in `rubric_r22.md`, and the panel verdict with its decision map in `panel/R22.json`. Case 22 result under the criteria: 證據不足以分出 (default total −2.8; W1 −4.8; W2 +1.2). The 2026 選舉公報 is not yet online.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `3d305c47b5bff83f89ffe9e3207143cbf9f4e782934f57a0ff6280501d134ab3`

| File | SHA-256 |
|---|---|
| `guide.md` | `55d7914079e8aceededfc6e882d74eb42f65cffc9a989496b0e171d7d80628d0` |
| `rubric.md` | `873bebf2bd95462bd2ef44afc5203d38376d0f232171aff8252ddb7cc8b75aa6` |
| `rubric_r22.md` | `603c79a79fe20993fd7e50cb55b16117f3520cc1e4eaaf3b2166d28906c28166` |
| `VERIFY.md` | `6b258b552a3209ffc5c20b50213c29662ffca666ed2900179dc502b0b60a0ce1` |
| `claims/D1.jsonl` | `caeccd651de9b4c2a451c46e467d105c55b5ffe41bf3750f257c433520830031` |
| `claims/D2.jsonl` | `195c78c4b988265dc4fcb07a0f16160632282f4fed0f90342a4f8a79336900e1` |
| `claims/D3.jsonl` | `44094f3d62bf907d932e3c37dcf7d6f5edf76cf9968f464b5382d2230edb0bf4` |
| `claims/D4.jsonl` | `596cbdd009054548fd564ab42c4c4765b525479be8fa3a05da1f69045dd185b3` |
| `claims/D5.jsonl` | `52d38312e5cd6777ea4f668c02e827fd80f5604412bac46ecdd2aad6fcf4bcd7` |
| `claims/D6.jsonl` | `84afa83eaaf0b9ef6cf5f6dd3135cd1f18f59cb8e6bd215b78c57641091b8b5a` |
| `claims/D7.jsonl` | `fae83a474ad25916458d790545b29bbb113f5f530840613d2b81bc36c2267de3` |
| `claims/D8.jsonl` | `c60584cae423d1c8f5f9885e1a15450a307614071a9c2afbbb27bf1f97f5b41a` |
| `claims/M.jsonl` | `324d6079d81f1060b1617806d747b70d98b84229b6734e2809f0f89250103e4a` |
| `claims/R22.jsonl` | `6eeff34daf44626399a7d107e99d5e47a773e2c4ebcff2589934654bfd4ff448` |
| `panel/D1.json` | `e9911fa5797942ab7d92e4b655599df0b51bd8f431daa007d072528cea023ea0` |
| `panel/D2.json` | `8c07fd2209a78fe5bc3aed4f33c17d7ce09bc32b287e683c3d9ba7294ec444e6` |
| `panel/D3.json` | `f8bdd27301f38f2dd1ab5e988b977ea4ffb72590b1b04a95146ec9a67a099aeb` |
| `panel/D4.json` | `8c5199f2c417513c9499069e11ced71c4783dc2f89f7ea4ed54e4a2e614c0ce2` |
| `panel/D5.json` | `40c8548f6f69af6e5b350f085edbffc0f20ec78036553f26210557840b3a0728` |
| `panel/D6.json` | `38db0e5823c81c6591922ddfd5998c0562e73ff86e7dfae12fd9e0d495b2e289` |
| `panel/D7-D8.json` | `3c669d808519beac9202f2a405505db2e2ef8a21d3dedf4105dd552842f3a726` |
| `panel/M.json` | `74eaf59e89d5fb607dd8227db80a51a2c05e2b060d9bba96ac188946969acf70` |
| `panel/R22.json` | `6e1199fed9a4eafa18845ac9c366cc2dda82094761ce9817c60a5a9390ad6f3a` |

## v0.1.0 — 2026-11-04

Draft. Candidate profiles for the mayor and 8 council races. MAYOR, D1 and D2 have the full GPT-5.6 Sol fact-check; D3–D6, D7 and D8 are in progress. The model panel's scores are not in this release.

- Claims: 936 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `9a785773c0954553ee8054349996c8f728a2d8d6111372dfb3161cfde9f404cb`

| File | SHA-256 |
|---|---|
| `guide.md` | `4d6cb3901776890d1246f5ca596695259cdb6639c3210e9eba06df7a5a90d304` |
| `rubric.md` | `85ec92029e4e872f381f2b9ccb8c3c5dc16fca052d1f192acbd3c14206b434a2` |
| `VERIFY.md` | `1c6b1ab734447eaca7b1c452e7b36add588ed991314a74f72a087880ff9cf917` |
| `claims/D1.jsonl` | `2c31aff31ab81456e73c903adc57edd5c026c21f9077b3cc385c9fa1151cebe3` |
| `claims/D2.jsonl` | `235a6f3c471b64142c0245af23dd9276f062d11bcda3c0b1e6b64d7ab0c73238` |
| `claims/D3.jsonl` | `47ae1806c61db03384ecc15d32a1f05dda43795019d61cce65f98979549e28eb` |
| `claims/D4.jsonl` | `88367a417f622e032354ebb462e406addfbbfc519815d15a841eab3f412f6b6f` |
| `claims/D5.jsonl` | `94d8975e68a5ee37a2bcc2085506fb5dd3406ebb05517066d978d71efa74567b` |
| `claims/D6.jsonl` | `c9f43f7a13c2c5a5c50b4741326845605bf4d8ee2614a3922dfdcc03adbf61e9` |
| `claims/D7.jsonl` | `2a4618861333e83af9101ad71f0bb844d55292f59859932f667ca681937fb334` |
| `claims/D8.jsonl` | `ad0e1fe09a562444bac7a32be90337dda49442f0aaf4bd992a363dada98a496c` |
| `claims/M.jsonl` | `04f759f9076dea7bbba2eade01c23b9ce5f9ea12cf6968d2e05e1d558396997b` |

