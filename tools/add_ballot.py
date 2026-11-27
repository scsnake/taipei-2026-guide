"""Add the folded 投票小提醒 box (valid and invalid ballots, folding) to the site pages.

The box goes right after the page header (the lede) of each page, between <!--BALLOT-->
markers. Running this again removes the old box and adds it again after the header.
The content follows the CEC's illustrated rules (公職人員選舉選舉票有效與無效之認定圖例).

Usage: python3 tools/add_ballot.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ("index.html", "mayors.html", "council.html")
BEGIN, END = "<!--BALLOT-->", "<!--/BALLOT-->"
ANCHOR = "</header>"
PDF = "https://web.cec.gov.tw/api/file/24caf042-5dbf-48c3-95d7-578267385332.pdf"

BLOCK = f"""{BEGIN}
  <details class="panel" id="ballot">
    <summary>投票小提醒：有效票、無效票與摺票</summary>
    <div class="md">
      <p>官方完整圖例（有效票 28 例、無效票 27 例）：<a href="{PDF}" target="_blank" rel="noopener noreferrer">中選會〈公職人員選舉選舉票有效與無效之認定圖例〉PDF ↗</a></p>

      <h4>每張選票只圈一位</h4>
      <p>市長、縣市議員、里長各領一張選票，每張只能圈選一位候選人。議員選舉區即使有多個席次，每位選民也只有一票，由得票最高者依席次當選（另有婦女保障名額）。原住民選民投原住民選舉區，同樣只有一票。</p>

      <h4>有效票的基本原則</h4>
      <p>使用選舉委員會製備的圈選工具，圈在一位候選人的欄位內，只要<b>能辨別圈選何人</b>，就是有效票。依中選會圖例，下列情形仍然有效：</p>
      <ul>
        <li>圈印部分壓到欄位格線、選票邊緣，或兩位候選人之間的共用空間，但仍能辨別圈選何人。</li>
        <li>圈印只印出一部分。</li>
        <li>在同一位置重複蓋印，或蓋後移動形成兩圈。</li>
        <li>摺票時印泥反印到選票其他位置，能辨別是摺票造成的反印。</li>
        <li>手指沾到印泥留下痕跡，但看不出是按指印，也不是符號。</li>
      </ul>

      <h4>常見的無效票</h4>
      <ul>
        <li>圈選兩位以上，或完全沒有圈選。</li>
        <li>圈在共用空間且圈印超出格線，無法辨別圈選何人。</li>
        <li>圈選後塗改，或另行圈選。</li>
        <li>簽名、蓋章、按指印、寫任何文字或畫符號。</li>
        <li>撕破選票任何一角，或污染到無法辨別。</li>
        <li>不用選舉委員會製備的圈選工具（例如自己的筆或印章），或不用選舉委員會製發的選票。</li>
      </ul>

      <h4>擔心摺票時印泥沾到別的欄位？</h4>
      <p>中選會圖例有效票第 22 例：「因疊折反印之圈選痕跡，能辨別係摺票時所疊折反印者，應屬有效票。」反印的圈印是左右顛倒的，開票時可以分辨，所以不必為此重新處理選票。</p>
      <p>以下是本站整理的做法，不是中選會規定：</p>
      <ol>
        <li>圈選時垂直按下一次，不要旋轉或拖動圈選章。</li>
        <li>圈好後稍等幾秒，讓印泥稍乾再摺。</li>
        <li>圈選面朝內摺起，依選票原有摺痕或選務人員指示摺疊，避免他人看到圈選內容。</li>
        <li>直接投入票匭。</li>
      </ol>
      <p>不要做的事：</p>
      <ul>
        <li>不要為了蓋掉反印而補蓋、塗抹或在選票上寫字；塗改與加記號會使選票無效。</li>
        <li>不要用手指去擦印泥；看起來像按指印的痕跡會使選票無效。</li>
        <li>不要把圈選內容給他人看，也不要拍攝選票。除執行公務外，手機或具攝影功能的器材須關閉電源才能帶進投票所（選罷法第 65 條）。</li>
      </ul>

    </div>
  </details>
{END}
"""


def run(quiet=False):
    for name in PAGES:
        p = ROOT / name
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        if BEGIN in t:
            a, b = t.index(BEGIN), t.index(END) + len(END)
            a = t.rfind("\n", 0, a) + 1
            b = t.find("\n", b) + 1
            while t[b:b + 1] == "\n":
                b += 1
            t = t[:a] + t[b:]
        if ANCHOR not in t:
            sys.exit(f"{name}: no page header to put the box after")
        i = t.index(ANCHOR) + len(ANCHOR)
        t = t[:i] + "\n  " + BLOCK.strip() + t[i:]
        p.write_text(t, encoding="utf-8")
        if not quiet:
            print(f"{name}: ballot box added")


if __name__ == "__main__":
    run()
