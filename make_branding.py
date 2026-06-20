r"""Generate the site's branding images in the Qhawarina palette:
 - og-image.png (1200x630): name card for Google/social previews
 - favicon set + apple-touch-icon: CC monogram
Run from the site root. Overwrites the placeholder purple images.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ST = Path(r"D:\Investigacion\cesarchavezp29.github.io\static")
CREAM = (250, 246, 236)
NAVY = (26, 44, 84)
MAROON = (122, 31, 43)
GOLD = (183, 132, 40)
MUTED = (93, 99, 120)
F = r"C:\Windows\Fonts"


def font(name, size):
    return ImageFont.truetype(str(Path(F) / name), size)


def w(draw, text, fnt):
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0]


# ---------- og-image 1200x630 ----------
img = Image.new("RGB", (1200, 630), CREAM)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 18, 630], fill=MAROON)              # left accent bar
d.rectangle([0, 0, 1200, 10], fill=NAVY)               # thin top band
x = 96
d.text((x, 120), "UNIVERSITY OF CHICAGO", font=font("georgiab.ttf", 26), fill=GOLD)
# name (auto-fit to width)
name = "Carlos César Chávez Padilla"
fs = 80
while True:
    fn = font("georgiab.ttf", fs)
    if w(d, name, fn) <= 1200 - x - 70 or fs <= 52:
        break
    fs -= 2
d.text((x, 170), name, font=font("georgiab.ttf", fs), fill=NAVY)
d.rectangle([x, 180 + fs + 18, x + 150, 180 + fs + 24], fill=MAROON)   # maroon rule
yy = 180 + fs + 52
d.text((x, yy), "Development Economist", font=font("georgia.ttf", 40), fill=NAVY)
d.text((x, yy + 58), "Center for Economics of Human Development", font=font("georgia.ttf", 30), fill=MUTED)
d.text((x, 548), "cesarchavezp29.github.io", font=font("georgiab.ttf", 28), fill=MAROON)
img.save(ST / "og-image.png")
print("wrote og-image.png", img.size)

# ---------- favicon: CC monogram ----------
def monogram(px):
    im = Image.new("RGB", (px, px), NAVY)
    dd = ImageDraw.Draw(im)
    dd.rectangle([0, 0, px - 1, px - 1], outline=GOLD, width=max(2, px // 32))
    fnt = font("georgiab.ttf", int(px * 0.56))
    txt = "CC"
    b = dd.textbbox((0, 0), txt, font=fnt)
    tw, th = b[2] - b[0], b[3] - b[1]
    dd.text(((px - tw) / 2 - b[0], (px - th) / 2 - b[1]), txt, font=fnt, fill=CREAM)
    return im

big = monogram(512)
big.save(ST / "apple-touch-icon.png")
monogram(32).save(ST / "favicon-32x32.png")
monogram(16).save(ST / "favicon-16x16.png")
big.save(ST / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("wrote favicon set + apple-touch-icon (CC monogram)")
