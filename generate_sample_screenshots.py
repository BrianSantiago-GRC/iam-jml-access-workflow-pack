from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap


BASE_DIR = Path(__file__).parent
OUT_DIR = BASE_DIR / "screenshots"
OUT_DIR.mkdir(exist_ok=True)


def load_font(size: int):
    candidates = [
        Path("C:/Windows/Fonts/consola.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def wrap_lines(content: str, width: int = 120) -> list[str]:
    lines: list[str] = []
    for line in content.splitlines():
        if not line.strip():
            lines.append("")
            continue
        lines.extend(textwrap.wrap(line, width=width) or [""])
    return lines


def render(title: str, lines: list[str], output: Path) -> None:
    width = 1800
    padding = 48
    line_height = 34
    title_height = 58
    height = padding * 2 + title_height + (max(1, len(lines)) * line_height)

    img = Image.new("RGB", (width, height), color=(16, 22, 32))
    draw = ImageDraw.Draw(img)
    title_font = load_font(34)
    body_font = load_font(23)

    draw.text((padding, padding), title, fill=(220, 232, 250), font=title_font)
    y = padding + title_height
    for line in lines:
        draw.text((padding, y), line, fill=(232, 240, 250), font=body_font)
        y += line_height

    img.save(output)


def main() -> None:
    files = [
        ("JML Workflow", "JML_WORKFLOW.md", "01-jml-workflow.png"),
        ("Access Request Form Template", "ACCESS_REQUEST_FORM_TEMPLATE.md", "02-access-request-form-template.png"),
        ("Access Approval Matrix", "ACCESS_APPROVAL_MATRIX.md", "03-access-approval-matrix.png"),
        ("Offboarding Checklist", "OFFBOARDING_CHECKLIST.md", "04-offboarding-checklist.png"),
        ("Risk Notes", "RISK_NOTES.md", "05-risk-notes.png"),
    ]

    for title, source, output in files:
        content = (BASE_DIR / source).read_text(encoding="utf-8")
        render(title, wrap_lines(content), OUT_DIR / output)


if __name__ == "__main__":
    main()
