from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "output" / "pdf"
SOURCE = PDF_DIR / "q51-q100-release-test.pdf"
TARGET = PDF_DIR / "工业与机器视觉100问_Q51-Q100_老仓库标准合并发布稿.pdf"


def main() -> None:
    reader = PdfReader(str(SOURCE))
    writer = PdfWriter()
    target_w, target_h = 595.2756, 841.8898  # A4 in points
    page_starts: dict[int, int] = {}
    page_texts: list[str] = []
    for page_index, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        page_texts.append(text)
        old_w, old_h = float(page.mediabox.width), float(page.mediabox.height)
        scale = min((target_w - 28) / old_w, (target_h - 34) / old_h)
        tx = (target_w - old_w * scale) / 2
        ty = (target_h - old_h * scale) / 2
        page.add_transformation(Transformation().scale(scale).translate(tx, ty))
        page.mediabox = RectangleObject((0, 0, target_w, target_h))
        page.cropbox = RectangleObject((0, 0, target_w, target_h))
        writer.add_page(page)

    # Locate the question markers in order. The source PDF may contain mojibake
    # for Chinese headings, so use the numeric marker and never move backward.
    cursor = 0
    for number in range(51, 101):
        token = str(number)
        for page_index in range(cursor, len(page_texts)):
            text = page_texts[page_index]
            if f"{number}." in text or re.search(rf"(?<!\d){token}(?!\d)", text):
                page_starts[number] = page_index
                cursor = page_index
                break

    writer.add_metadata({
        "/Title": "工业与机器视觉100问 Q51-Q100 合并发布稿",
        "/Author": "兰青松（LanQS）",
        "/Subject": "Q51-Q100；Q51-Q60纳入正式发布，Q61-Q100新增内容",
        "/Keywords": "工业视觉,机器视觉,Q51-Q100,出版发布稿",
    })
    for number in range(51, 101):
        page_index = page_starts.get(number)
        if page_index is not None:
            writer.add_outline_item(f"第{number}问", page_index)
    with TARGET.open("wb") as handle:
        writer.write(handle)
    missing = [n for n in range(51, 101) if n not in page_starts]
    print(f"pages={len(reader.pages)} bookmarks={len(page_starts)} missing={missing}")


if __name__ == "__main__":
    main()
