from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "docs" / "chapters"
TEMP_DOC = CHAPTERS / "q51-q100-release.md"


def extract_questions(path: Path, start: int, end: int) -> list[str]:
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^#{1,2} 第(\d+)问[：　 ].*$", text))
    sections: list[str] = []
    for index, match in enumerate(matches):
        number = int(match.group(1))
        if not start <= number <= end:
            continue
        section_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append(text[match.start():section_end].strip())
    return sections


def main() -> None:
    sources = [
        (CHAPTERS / "chapter-03-q41-q55.md", 51, 55),
        (CHAPTERS / "chapter-04-q56-q60.md", 56, 60),
        (CHAPTERS / "chapter-05-q61-q70.md", 61, 70),
        (CHAPTERS / "chapter-06-q71-q80.md", 71, 80),
        (CHAPTERS / "chapter-07-q81-q90.md", 81, 90),
        (CHAPTERS / "chapter-08-q91-q100.md", 91, 100),
    ]
    sections: list[str] = []
    for path, start, end in sources:
        sections.extend(extract_questions(path, start, end))
    numbers = [int(re.match(r"#{1,2} 第(\d+)问", section).group(1)) for section in sections]
    expected = list(range(51, 101))
    if numbers != expected:
        raise SystemExit(f"question sequence mismatch: {numbers}")
    header = (
        "# 《工业与机器视觉100问》Q51–Q100\n\n"
        "> 发布范围：Q51–Q100。Q51–Q60 为老仓库已有正文，本次纳入正式发布；Q61–Q100 为新增正文。\n\n"
        "---\n\n"
    )
    TEMP_DOC.write_text(header + "\n\n---\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"wrote {TEMP_DOC} with {len(sections)} questions")


if __name__ == "__main__":
    main()
