from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1] / "docs" / "chapters" / "images"
TARGETS = [ROOT / f"Q{number}" for number in range(61, 101)]
TEXT = "LanQS｜工业与机器视觉100问"
TEXT_EXTRA = "B站搜索：飒飒青屿"
FONT_PATH = r"C:\Windows\Fonts\simhei.ttf"


font_cache: dict[int, ImageFont.FreeTypeFont] = {}
files = sorted(
    path
    for folder in TARGETS
    for path in folder.rglob("*")
    if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
)

for path in files:
    with Image.open(path) as original:
        image = original.convert("RGBA")
        width, height = image.size
        size = max(18, round(width * 0.017))
        if size not in font_cache:
            font_cache[size] = ImageFont.truetype(FONT_PATH, size)
        font = font_cache[size]

        overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)
        margin = max(12, round(width * 0.012))

        box = draw.textbbox((0, 0), TEXT, font=font)
        draw.text(
            (width - (box[2] - box[0]) - margin, margin),
            TEXT,
            font=font,
            fill=(100, 110, 120, 42),
        )

        extra_box = draw.textbbox((0, 0), TEXT_EXTRA, font=font)
        draw.text(
            (
                width - (extra_box[2] - extra_box[0]) - margin,
                height - (extra_box[3] - extra_box[1]) - margin,
            ),
            TEXT_EXTRA,
            font=font,
            fill=(100, 110, 120, 42),
        )

        result = Image.alpha_composite(image, overlay).convert("RGB")
        if path.suffix.lower() in {".jpg", ".jpeg"}:
            result.save(path, quality=95, optimize=True)
        else:
            result.save(path, optimize=True)

print(f"watermarked_images={len(files)}")
