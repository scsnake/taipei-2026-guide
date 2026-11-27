# Releases

Each release lists the SHA-256 hash of every published file. Check your copy with `shasum -a 256 -c SHA256SUMS` (macOS) or `sha256sum -c SHA256SUMS` (Linux). Each release is also a signed git tag.

## v0.6.9 — 2026-11-27

Add a folded 投票小提醒 box to index.html, mayors.html and council.html: one vote per ballot, valid and invalid ballots per the CEC's illustrated rules, how to fold the ballot (a mirror imprint from folding stays valid), and a link to the CEC PDF. tools/add_ballot.py keeps the box on rebuilt pages.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `2074958671d17ad935d884fd195414abe8a71ba12237ad9af412ccc96c94e62e`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `0b584a4c662fb6d80664bd9e8fa3d504b80ba2241e0e0fa153edbea56064b8f3` |
| `mayors.html` | `73f2e9659e8321dbc0528cade0915f208ce52874a245db20c30134f7d568d92f` |
| `council.html` | `080cfdb001f5ef6ba91be0201902e46b3b496d0be68d06d243b3d536ef5efbbf` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/cyi_candidates.json` | `c634de68b0da6c2d4f397a5b71b5f083d81349bb660549ebeed7ef67e818d736` |
| `council/cyi_records.json` | `67bf03396d28cfc94b8124097be00d4198a6869e5d05baf3cde8894a257d14fc` |
| `council/cyq_candidates.json` | `e6cf3ce136c73bf1381d67392115e7102bc79964588a9e0f1c143b512d6f76fc` |
| `council/cyq_records.json` | `6b19ac485689766dd400af54b08b48f1763942ffc14da8d82c06b792ecbe67c1` |
| `council/hsq_candidates.json` | `2867ab51fcef7273504668817d4394496bb894bcbb6409342d72f87b3a2a2980` |
| `council/hsq_records.json` | `02101f4e987a49043a9177352744a336169bd6161c6b1e2414dad11a9689c336` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/hua_candidates.json` | `cc40237421c34b1bf0a8369cb244c70a3807f4858327028f8405eb0883b9b2a7` |
| `council/hua_records.json` | `6560b658d68bf5fbdd68d3bc5c528ab220149cbbc6068d99d912a5ca1dbfc501` |
| `council/ila_candidates.json` | `cf3420c0e1581018c20a190153a32ceddf0c722b9770804dcee51d2b126988ea` |
| `council/ila_records.json` | `fef87a20b7ee839bfa12e6eddbe9879179869f9be0f1844d890311057f52af53` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/mia_candidates.json` | `a4875af36df92e30b48f3428a29d28d1c8e38ae4e97f8b08ed5de733089a1466` |
| `council/mia_records.json` | `9b4a2043a6ec3c249a480c5513ed32de919cfab3d7972683d84eb6f2ab0ba4ec` |
| `council/nan_candidates.json` | `00b5b24a5caf4538a75cad04b8115f2452254a42c7d8bfa9e692cf40b0c4171b` |
| `council/nan_records.json` | `a725960384347eee8aaeaad0c4fc48cfcf2cddcadba18cad148c84a965f67112` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.8 — 2026-11-27

council.html adds 宜蘭縣 (59 candidates, 11 records; 1 marked as inferred identity). Seventeen 縣市, 211 records. 宜蘭縣 review: GPT-6 Luna (medium) plus Claude Sonnet 5.5; disputes decided by Claude Opus 5.5.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `99540b82cf0350ae62b535cdd09aad92b8f05f9dccd4eaa101a72c9d1c5eaa8f`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `98e6a6dc9ef443aca27d7cf6ae048a259b657c9e9b2784b13bf7b0325036ccde` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/cyi_candidates.json` | `c634de68b0da6c2d4f397a5b71b5f083d81349bb660549ebeed7ef67e818d736` |
| `council/cyi_records.json` | `67bf03396d28cfc94b8124097be00d4198a6869e5d05baf3cde8894a257d14fc` |
| `council/cyq_candidates.json` | `e6cf3ce136c73bf1381d67392115e7102bc79964588a9e0f1c143b512d6f76fc` |
| `council/cyq_records.json` | `6b19ac485689766dd400af54b08b48f1763942ffc14da8d82c06b792ecbe67c1` |
| `council/hsq_candidates.json` | `2867ab51fcef7273504668817d4394496bb894bcbb6409342d72f87b3a2a2980` |
| `council/hsq_records.json` | `02101f4e987a49043a9177352744a336169bd6161c6b1e2414dad11a9689c336` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/hua_candidates.json` | `cc40237421c34b1bf0a8369cb244c70a3807f4858327028f8405eb0883b9b2a7` |
| `council/hua_records.json` | `6560b658d68bf5fbdd68d3bc5c528ab220149cbbc6068d99d912a5ca1dbfc501` |
| `council/ila_candidates.json` | `cf3420c0e1581018c20a190153a32ceddf0c722b9770804dcee51d2b126988ea` |
| `council/ila_records.json` | `fef87a20b7ee839bfa12e6eddbe9879179869f9be0f1844d890311057f52af53` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/mia_candidates.json` | `a4875af36df92e30b48f3428a29d28d1c8e38ae4e97f8b08ed5de733089a1466` |
| `council/mia_records.json` | `9b4a2043a6ec3c249a480c5513ed32de919cfab3d7972683d84eb6f2ab0ba4ec` |
| `council/nan_candidates.json` | `00b5b24a5caf4538a75cad04b8115f2452254a42c7d8bfa9e692cf40b0c4171b` |
| `council/nan_records.json` | `a725960384347eee8aaeaad0c4fc48cfcf2cddcadba18cad148c84a965f67112` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.7 — 2026-11-27

council.html adds 花蓮縣 (55 candidates, 10 records; 2 marked as inferred identity). Sixteen 縣市, 200 records. 花蓮縣 review: GPT-6 Luna (medium) plus Claude Sonnet 5.5; disputes decided by Claude Opus 5.5.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `f2450df644c7bca2f5b86ddeadea0a019bb9e8ffa88e63c5ef5134ef5891a99b`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `e0e45043aea35deafefe29d77368bc9d5620010e303f235cf5636a53fd84b682` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/cyi_candidates.json` | `c634de68b0da6c2d4f397a5b71b5f083d81349bb660549ebeed7ef67e818d736` |
| `council/cyi_records.json` | `67bf03396d28cfc94b8124097be00d4198a6869e5d05baf3cde8894a257d14fc` |
| `council/cyq_candidates.json` | `e6cf3ce136c73bf1381d67392115e7102bc79964588a9e0f1c143b512d6f76fc` |
| `council/cyq_records.json` | `6b19ac485689766dd400af54b08b48f1763942ffc14da8d82c06b792ecbe67c1` |
| `council/hsq_candidates.json` | `2867ab51fcef7273504668817d4394496bb894bcbb6409342d72f87b3a2a2980` |
| `council/hsq_records.json` | `02101f4e987a49043a9177352744a336169bd6161c6b1e2414dad11a9689c336` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/hua_candidates.json` | `cc40237421c34b1bf0a8369cb244c70a3807f4858327028f8405eb0883b9b2a7` |
| `council/hua_records.json` | `6560b658d68bf5fbdd68d3bc5c528ab220149cbbc6068d99d912a5ca1dbfc501` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/mia_candidates.json` | `a4875af36df92e30b48f3428a29d28d1c8e38ae4e97f8b08ed5de733089a1466` |
| `council/mia_records.json` | `9b4a2043a6ec3c249a480c5513ed32de919cfab3d7972683d84eb6f2ab0ba4ec` |
| `council/nan_candidates.json` | `00b5b24a5caf4538a75cad04b8115f2452254a42c7d8bfa9e692cf40b0c4171b` |
| `council/nan_records.json` | `a725960384347eee8aaeaad0c4fc48cfcf2cddcadba18cad148c84a965f67112` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.6 — 2026-11-27

council.html adds 苗栗縣 (56 candidates, 10 records). Fifteen 縣市, 190 records. 苗栗縣 review: GPT-6 Luna (medium) plus Claude Sonnet 5.5; disputes decided by Claude Opus 5.5.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `4d4ade4cab794f49354ba12e690c740c9c0a0cfc4e3b71aae8d871c1560240cb`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `6dff269d84edd9dd92f1899f4752aaa58b214e51d68bf53339bcceffbdb04b1a` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/cyi_candidates.json` | `c634de68b0da6c2d4f397a5b71b5f083d81349bb660549ebeed7ef67e818d736` |
| `council/cyi_records.json` | `67bf03396d28cfc94b8124097be00d4198a6869e5d05baf3cde8894a257d14fc` |
| `council/cyq_candidates.json` | `e6cf3ce136c73bf1381d67392115e7102bc79964588a9e0f1c143b512d6f76fc` |
| `council/cyq_records.json` | `6b19ac485689766dd400af54b08b48f1763942ffc14da8d82c06b792ecbe67c1` |
| `council/hsq_candidates.json` | `2867ab51fcef7273504668817d4394496bb894bcbb6409342d72f87b3a2a2980` |
| `council/hsq_records.json` | `02101f4e987a49043a9177352744a336169bd6161c6b1e2414dad11a9689c336` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/mia_candidates.json` | `a4875af36df92e30b48f3428a29d28d1c8e38ae4e97f8b08ed5de733089a1466` |
| `council/mia_records.json` | `9b4a2043a6ec3c249a480c5513ed32de919cfab3d7972683d84eb6f2ab0ba4ec` |
| `council/nan_candidates.json` | `00b5b24a5caf4538a75cad04b8115f2452254a42c7d8bfa9e692cf40b0c4171b` |
| `council/nan_records.json` | `a725960384347eee8aaeaad0c4fc48cfcf2cddcadba18cad148c84a965f67112` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.5 — 2026-11-27

council.html adds 新竹縣 (68 candidates, 10 records; 1 marked as inferred identity). Fourteen 縣市, 180 records. 新竹縣 review: GPT-6 Luna (medium) plus Gemini 4 Neon, or Claude Sonnet 5.5 where Gemini was rate-limited; disputes decided by Claude Opus 5.5.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `fffe9f3b70e20fa3533d5597c6413efd728988130e8f830fbf4dfe1d80784fd0`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `50e2a13e5467ce8762f58b86992fb1b70c3f8e42cb0de8c8390d00420e930760` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/cyi_candidates.json` | `c634de68b0da6c2d4f397a5b71b5f083d81349bb660549ebeed7ef67e818d736` |
| `council/cyi_records.json` | `67bf03396d28cfc94b8124097be00d4198a6869e5d05baf3cde8894a257d14fc` |
| `council/cyq_candidates.json` | `e6cf3ce136c73bf1381d67392115e7102bc79964588a9e0f1c143b512d6f76fc` |
| `council/cyq_records.json` | `6b19ac485689766dd400af54b08b48f1763942ffc14da8d82c06b792ecbe67c1` |
| `council/hsq_candidates.json` | `2867ab51fcef7273504668817d4394496bb894bcbb6409342d72f87b3a2a2980` |
| `council/hsq_records.json` | `02101f4e987a49043a9177352744a336169bd6161c6b1e2414dad11a9689c336` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/nan_candidates.json` | `00b5b24a5caf4538a75cad04b8115f2452254a42c7d8bfa9e692cf40b0c4171b` |
| `council/nan_records.json` | `a725960384347eee8aaeaad0c4fc48cfcf2cddcadba18cad148c84a965f67112` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.4 — 2026-11-27

council.html adds 嘉義市 (37 candidates, 3 records). Thirteen 縣市, 170 records. 嘉義市: Claude Sonnet 5.5 and GPT-6 Luna search; GPT-6 Luna (medium) plus Gemini 4 Neon review; disputes decided by Claude Opus 5.5.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `ee0a8290db16ad790c33790e6f48de1fcde2bb4cf836d220c198bdb927c00565`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `767edad8ff6efe2e6e71d843c341d855e4cfdc60ec867bfc21f4b1118eae3118` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/cyi_candidates.json` | `c634de68b0da6c2d4f397a5b71b5f083d81349bb660549ebeed7ef67e818d736` |
| `council/cyi_records.json` | `67bf03396d28cfc94b8124097be00d4198a6869e5d05baf3cde8894a257d14fc` |
| `council/cyq_candidates.json` | `e6cf3ce136c73bf1381d67392115e7102bc79964588a9e0f1c143b512d6f76fc` |
| `council/cyq_records.json` | `6b19ac485689766dd400af54b08b48f1763942ffc14da8d82c06b792ecbe67c1` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/nan_candidates.json` | `00b5b24a5caf4538a75cad04b8115f2452254a42c7d8bfa9e692cf40b0c4171b` |
| `council/nan_records.json` | `a725960384347eee8aaeaad0c4fc48cfcf2cddcadba18cad148c84a965f67112` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.3 — 2026-11-27

council.html adds 嘉義縣 (52 candidates, 9 records; 3 court records marked as inferred identity, not officially confirmed). Twelve 縣市, 167 records. 嘉義 review: GPT-6 Luna (medium) plus Gemini 4 Neon; disputes decided by Claude Opus 5.5.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `45ddb5d87315659bf96e9b395f6b121a4674275b6961d661d0477078f149d762`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `19a182730702207642d56273bb04853819d33061374f27cd4654e1ac3445bee5` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/cyq_candidates.json` | `e6cf3ce136c73bf1381d67392115e7102bc79964588a9e0f1c143b512d6f76fc` |
| `council/cyq_records.json` | `6b19ac485689766dd400af54b08b48f1763942ffc14da8d82c06b792ecbe67c1` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/nan_candidates.json` | `00b5b24a5caf4538a75cad04b8115f2452254a42c7d8bfa9e692cf40b0c4171b` |
| `council/nan_records.json` | `a725960384347eee8aaeaad0c4fc48cfcf2cddcadba18cad148c84a965f67112` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.2 — 2026-11-27

council.html adds 南投縣 (61 candidates, 10 records). Eleven 縣市, 158 records. 南投 review: GPT-6 Luna (medium) plus Gemini 4 Neon; disputes decided by Claude Opus 5.5. Each record now names the models that reviewed it, and the page signature names the second-search models.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `6feab7b304e6468a487688f8e53370486e9946da9eef2aec59f257508cf05b18`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `6f1e4438f4f7f759696426158d84e164ab15c63b86a8ba939c4aa86f5d427c68` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/nan_candidates.json` | `00b5b24a5caf4538a75cad04b8115f2452254a42c7d8bfa9e692cf40b0c4171b` |
| `council/nan_records.json` | `a725960384347eee8aaeaad0c4fc48cfcf2cddcadba18cad148c84a965f67112` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.1 — 2026-11-27

council.html adds 新竹市 (56 candidates, 8 records). Ten 縣市, 148 records. Same checks as v0.6.0: source text match, GPT-6.1 Terra plus Gemini 4 Neon review, disputes decided by Claude Opus 5.5.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `ff4394d2bb71aa0eda6cf7beac4ca8d6843df25f9651cb2487f08fb6a8ecd117`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `e408149267bd9c6776d81f0ab37e093d4989fe3424494dd25b68a53a932ebc2e` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/hsz_candidates.json` | `f96ee60a327f451559390e5033978ee50c86053fe074da1c18167fead87c2682` |
| `council/hsz_records.json` | `61544234df889b829ed49f67e79f39c02ac5f81f545bb07e4601fe0e7dc7957b` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.6.0 — 2026-11-27

New page council.html (縣市議員候選人紀錄): no scores; only major negative records (前科、起訴、官方處分) and major contributions for 縣市議員 candidates outside Taipei. Nine 縣市: 新北、桃園、臺中、臺南、高雄、彰化、雲林、屏東、基隆 (140 records). Each record was checked against its source text and reviewed by GPT-6.1 Terra plus Gemini 4 Neon or Claude Sonnet 5.5; disputes were decided by Claude Opus 5.5. 2026-11-27 status refresh of 11 open cases, and 6 records restored with an identity note (two marked as inferred, not officially confirmed). All pages show the page update time (台灣時間).

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `a48dda7775f074bbaf2061600077a1d373fe7ab7969dcc7836db6ea2e8e43d46`

| File | SHA-256 |
|---|---|
| `guide.md` | `c07736f947c94a8b9c43612f83ba91173e6931e18f148b7fd7020f659ea0b833` |
| `index.html` | `4555edf9046f97b1f8bd60ae5ae580f0b3d9012f6afe07abcd99302b29a9e399` |
| `mayors.html` | `c422c87854b34fb62f69c488baac4a2da83e78eac37fb48e4142b4d5f7dee1e2` |
| `council.html` | `0ced9cabeffe41b3fac48b985711638ef496f6ff5b8e13a62c255bc2f69f81fe` |
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
| `council/chc_candidates.json` | `be6e07192938beb025e7ae2caefbbcfa9a4c38c0b230c452e7df8f3ad967ced5` |
| `council/chc_records.json` | `4130cdf4e3b9a56e2458ad59b0464e1de0fe1758023c1bc57bd8bc06f50d6c1a` |
| `council/kee_candidates.json` | `e2d65a55683b9e3a4f9d6327f89c6559234065c2608decee09790639d6497ca5` |
| `council/kee_records.json` | `97187b5759a3c0e4d04f330df3764f7136683164484c53e1078de14d7d085705` |
| `council/khh_candidates.json` | `beecc94cd0345ac30c9bfcfe08a50af318503af6770f3a5dcd18e7bb9feabea9` |
| `council/khh_records.json` | `f33aac0246270bed011ac9ba8b03e16ab9a4c969534bde5f68a284921a1762ae` |
| `council/ntpc_candidates.json` | `89e67e217dbdeba597653b110b28aa29afb45ea58d5c7a63da4cd0509bbe63bd` |
| `council/ntpc_records.json` | `e9131dbca30eff3fc422c895f53b8a64866658beec5ce86885cbec04d369f6f1` |
| `council/pif_candidates.json` | `c18b3a2d7874170318e5c20c4aad6b0ca3776a68c2ca66e817ab91d0bb01bfe7` |
| `council/pif_records.json` | `fe955c53cc80e1b97cab9404da8a9f68fa7e5940ffbe045c248f414aa89a5eae` |
| `council/tnn_candidates.json` | `d795aec209b9a12515af63588524930dc77b68fe04c6ddd546af4dc6be71cd4c` |
| `council/tnn_records.json` | `c1d7023e2009d35c152c0c2ad0d8a35c965a8d2fef392b7a892bb06d0c632270` |
| `council/txg_candidates.json` | `30081a6937a964d88dd85723f45f9af1a8fd9441db84448d76b7822d2f846e13` |
| `council/txg_records.json` | `8af423ca90d8821df1c854bf3f7038a09a52e709f5b717c0c6704ca550a14eec` |
| `council/tyc_candidates.json` | `3c8832db2d7af965ff80b2c7b63b0d2da59fad184d7e8843cf180ef481deaa8f` |
| `council/tyc_records.json` | `822131389545d7af51f766d7988a49c603616b417b5e00179c0780b1b8d68f53` |
| `council/yun_candidates.json` | `04fc7402cdf2d9e0799f0167782550667ce24dedbe32f2a5b15972b3cfb4692e` |
| `council/yun_records.json` | `e4c7ca571659f5c5fb29cd1d137f679a0b48d8d3ebb66ae5c5fe7659e84bc467` |

## v0.5.0 — 2026-11-17

Both pages: a closed 選舉公報與查核 fold on every candidate card (103 Taipei cards, 75 cards in 21 county mayor races). It shows the 具結情形 as printed in the 2026 bulletin, 學歷 and 經歷 lines marked ✓ / ✗ / ? (✓ only when a fetched source page names the candidate and holds the quote; ✗ only after a hand check against an official or primary source), the official 政見 text, and QR code URLs decoded from the bulletin. 政見評估, with no score effect: 超出職權 (hand-reviewed against 憲法 §107 and 地方制度法 §18–19), cost estimates for cash promises from 內政部戶政司 open data, 言行對照 with checked sources, and quoted cross-strait wording. New: additions.md and tools/add_info.py for dated maintainer notes on cards. Scores, 首選 and 次選 are unchanged. claims/*.jsonl are not re-exported for the bulletin data.

- Claims: 1269 (active). Ledger lines: 0.
- SHA-256 of SHA256SUMS: `b175c13196ed6b435d899998b8ccd9149b78b5487b23d8d5431583723ddfcfc7`

| File | SHA-256 |
|---|---|
| `guide.md` | `ac3976e4f9571b38612f8e1b90897177a406098d73770b35d8637cf6bd1bf4fe` |
| `index.html` | `1016e14e22d9c7000cee0d09bda5b254bc72fd4ff7c4c4dc3066dfc3739c4bb6` |
| `mayors.html` | `16d9ca92e29a7dd91fbbb87ec7b76bf9200969a7ba8aa50fe93e22c7beef644d` |
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

