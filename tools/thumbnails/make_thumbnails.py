"""Generate the standard post thumbnails, one per category ("track").

Every thumbnail uses the same layout: a solid colour panel on the left with a
two-line label and an icon, and abstract art on the right. Output goes to
assets/img/thumbnails/<slug>.png, where <slug> is the category name as Hugo
urlizes it (e.g. "Digital Forensics" -> digital-forensics; avoid "&" in category
names, Hugo slugs "Identity & Access" as identity--access). Posts pick their
thumbnail from their first category (layouts/partials/functions/feature-image.html).

Run from the repo root:  py tools/thumbnails/make_thumbnails.py
Needs Pillow and the Windows Arial Bold font (C:\\Windows\\Fonts\\arialbd.ttf).

To add a track: add an entry to TRACKS, drop art (474x528) in art/ and a white
icon with transparency in icons/ (or reuse existing ones), then re-run.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parents[1] / "assets" / "img" / "thumbnails"
FONT = r"C:\Windows\Fonts\arialbd.ttf"

W, H = 816, 528
PANEL_W = 342
FONT_SIZE = 61          # 44px cap height, matching the original thumbnails
LABEL_TOPS = (48, 123)  # cap-top of line 1 and line 2
ICON_BOX = 150
ICON_CENTER = (PANEL_W // 2, 330)

# slug: (label lines, panel colour, icon, art)
TRACKS = {
    "incident-response": (("Incident", "Response"), (108, 0, 0), "incident-response", "incident-response"),
    "digital-forensics": (("Digital", "Forensics"), (103, 53, 149), "digital-forensics", "digital-forensics"),
    "identity-and-access": (("Identity", "& Access"), (0, 84, 89), "identity-and-access", "identity-and-access"),
    "mitigation": (("Mitigation",), (194, 27, 113), "mitigation", "mitigation"),
    "industry-trends": (("Industry", "Trends"), (0, 17, 50), "industry-trends", "industry-trends"),
}


def padlock_icon(size=150):
    """White padlock, drawn at 4x and downsampled for smooth edges."""
    s = 4
    im = Image.new("L", (size * s, size * s), 0)
    d = ImageDraw.Draw(im)
    u = size * s / 150
    # shackle
    d.arc([38 * u, 6 * u, 112 * u, 86 * u], 180, 360, fill=255, width=int(16 * u))
    d.rectangle([38 * u, 44 * u, 54 * u, 72 * u], fill=255)
    d.rectangle([96 * u, 44 * u, 112 * u, 72 * u], fill=255)
    # body
    d.rounded_rectangle([18 * u, 66 * u, 132 * u, 146 * u], radius=int(14 * u), fill=255)
    # keyhole
    d.ellipse([63 * u, 86 * u, 87 * u, 110 * u], fill=0)
    d.polygon([(68 * u, 104 * u), (82 * u, 104 * u), (86 * u, 128 * u), (64 * u, 128 * u)], fill=0)
    alpha = im.resize((size, size), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    out.putalpha(alpha)
    return out


def teal_art(src):
    """Recolour an art panel to the Identity & Access teal by hue rotation."""
    hsv = Image.open(src).convert("RGB").convert("HSV")
    h, s, v = hsv.split()
    h = h.point(lambda x: (x - 45) % 256)  # blue (~170) -> teal (~125)
    return Image.merge("HSV", (h, s, v)).convert("RGB")


def ensure_sources():
    icon = ROOT / "icons" / "identity-and-access.png"
    if not icon.exists():
        padlock_icon().save(icon)
    art = ROOT / "art" / "identity-and-access.png"
    if not art.exists():
        teal_art(ROOT / "art" / "industry-trends.png").save(art)


def render(lines, colour, icon_name, art_name):
    im = Image.new("RGB", (W, H), colour)
    im.paste(Image.open(ROOT / "art" / f"{art_name}.png").convert("RGB").resize((W - PANEL_W, H)), (PANEL_W, 0))
    d = ImageDraw.Draw(im)

    size = FONT_SIZE
    font = ImageFont.truetype(FONT, size)
    while max(d.textlength(t, font=font) for t in lines) > PANEL_W - 40:
        size -= 1
        font = ImageFont.truetype(FONT, size)
    cap_top = font.getbbox("H", anchor="ls")[1]
    tops = LABEL_TOPS if len(lines) == 2 else ((LABEL_TOPS[0] + LABEL_TOPS[1]) // 2,)
    for text, top in zip(lines, tops):
        d.text((PANEL_W // 2, top - cap_top), text, font=font, fill="white", anchor="ms")

    icon = Image.open(ROOT / "icons" / f"{icon_name}.png").convert("RGBA")
    scale = ICON_BOX / max(icon.size)
    icon = icon.resize((round(icon.width * scale), round(icon.height * scale)), Image.LANCZOS)
    im.paste(icon, (ICON_CENTER[0] - icon.width // 2, ICON_CENTER[1] - icon.height // 2), icon)
    return im


def main():
    ensure_sources()
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, spec in TRACKS.items():
        path = OUT / f"{slug}.png"
        render(*spec).save(path, optimize=True)
        print("wrote", path.relative_to(ROOT.parents[1]))


if __name__ == "__main__":
    main()
