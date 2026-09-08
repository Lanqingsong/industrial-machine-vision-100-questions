from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "output" / "pdf"
SOURCE = ROOT / "tmp" / "pdfs" / "q51-q100-browser-render.pdf"
TARGET = PDF_DIR / "工业与机器视觉100问_Q51-Q100_第三版.pdf"
OLD_COVER = ROOT.parent / "open-source-book-Q1-Q60" / "output" / "pdf" / "工业与机器视觉100问_Q1-Q60_第三版_封面重制版.pdf"
TMP = ROOT / "tmp" / "pdfs"
COVER_OVERLAY = TMP / "q51-q100-cover-overlay.pdf"
INTRO = TMP / "q51-q100-intro.pdf"


def register_font() -> str:
    candidates = [Path(r"C:\Windows\Fonts\msyh.ttc"), Path(r"C:\Windows\Fonts\simhei.ttf")]
    for path in candidates:
        if path.exists():
            pdfmetrics.registerFont(TTFont("BookCN", str(path), subfontIndex=0))
            return "BookCN"
    return "Helvetica"


def make_front_matter(font: str) -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(COVER_OVERLAY), pagesize=(595.2756, 841.8898))
    c.setFont(font, 18)
    c.setFillColor(HexColor("#d6a63a"))
    c.drawString(52, 594, "Q51–Q100 发布分册")
    c.save()

    c = canvas.Canvas(str(INTRO), pagesize=(595.2756, 841.8898))
    c.setStrokeColor(HexColor("#d6a63a"))
    c.setLineWidth(3)
    c.line(52, 770, 150, 770)
    c.setFillColor(HexColor("#172b3c"))
    c.setFont(font, 28)
    c.drawString(52, 720, "关于本分册")
    c.setFillColor(HexColor("#5f7380"))
    c.setFont(font, 12)
    c.drawString(52, 684, "从成像判断开始，走到可运行、可验收的视觉系统")
    c.setFillColor(HexColor("#172b3c"))
    c.setFont(font, 12)
    paragraphs = [
        "本分册收录《工业与机器视觉100问》第51—100问，覆盖工业通信、实时控制、系统维护、",
        "算法工程、软件架构、部署和运行日志等内容。Q51—Q60 与 Q61—Q100 在同一目录和版式下连续编排。",
        "",
        "阅读说明",
        "本分册的题号书签与正文题号一一对应；图片保留统一版权水印；公式、代码和图注按正文顺序排版。",
        "工程参数仍需结合具体设备、现场风险评估和验收条件复核。",
    ]
    y = 620
    for line in paragraphs:
        if line == "":
            y -= 18
            continue
        if line == "阅读说明":
            c.setFillColor(HexColor("#d6a63a"))
            c.setFont(font, 16)
        else:
            c.setFillColor(HexColor("#172b3c"))
            c.setFont(font, 12)
        c.drawString(52, y, line)
        y -= 28 if line == "阅读说明" else 22
    c.setStrokeColor(HexColor("#b7c1c6"))
    c.setLineWidth(0.6)
    c.line(52, 55, 545, 55)
    c.setFillColor(HexColor("#5f7380"))
    c.setFont(font, 9)
    c.drawString(52, 35, "第三版")
    c.drawRightString(545, 35, "LanQS")
    c.save()


def footer_page(font: str, number: int) -> object:
    from io import BytesIO

    stream = BytesIO()
    c = canvas.Canvas(stream, pagesize=(595.2756, 841.8898))
    c.setStrokeColor(HexColor("#b7c1c6"))
    c.setLineWidth(0.6)
    c.line(52, 35, 545, 35)
    c.setFillColor(HexColor("#7b8b92"))
    c.setFont(font, 8)
    c.drawString(52, 20, "第三版")
    c.drawCentredString(298, 20, "LanQS｜工业与机器视觉100问｜Q51–Q100")
    c.drawRightString(545, 20, f"{number}")
    c.save()
    stream.seek(0)
    return PdfReader(stream).pages[0]


def main() -> None:
    font = register_font()
    make_front_matter(font)
    source = PdfReader(str(SOURCE))
    # The browser print can emit one empty leading page when the first heading
    # has a print break. Drop only leading pages with no text.
    while source.pages and not (source.pages[0].extract_text() or "").strip():
        del source.pages[0]
    old = PdfReader(str(OLD_COVER))
    cover = old.pages[0]
    cover.merge_page(PdfReader(str(COVER_OVERLAY)).pages[0])
    intro = PdfReader(str(INTRO)).pages[0]
    writer = PdfWriter()
    writer.add_page(cover)
    writer.add_page(intro)

    page_texts = [(page.extract_text() or "") for page in source.pages]
    starts: dict[int, int] = {}
    cursor = 0
    for number in range(51, 101):
        for index in range(cursor, len(page_texts)):
            if f"{number}." in page_texts[index] or re.search(rf"(?<!\d){number}(?!\d)", page_texts[index]):
                starts[number] = index
                cursor = index
                break

    for index, page in enumerate(source.pages):
        page.merge_page(footer_page(font, index + 1))
        writer.add_page(page)
    for number in range(51, 101):
        if number in starts:
            writer.add_outline_item(f"第{number}问", starts[number] + 2)
    writer.add_metadata({
        "/Title": "Industrial and Machine Vision 100 Questions - Q51-Q100 Third Edition",
        "/Author": "LanQS",
        "/Subject": "Q51-Q100 third edition release",
    })
    with TARGET.open("wb") as handle:
        writer.write(handle)
    print(f"pages={len(writer.pages)} bookmarks={len(starts)} missing={[n for n in range(51, 101) if n not in starts]}")


if __name__ == "__main__":
    main()
