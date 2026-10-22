#!/usr/bin/env python3
"""brand_cards.py - draw the on-screen cards in the Talent Social brand (Pillow, transparent PNGs).

Usage: brand_cards.py spec.json out_dir
spec keys (all optional):
  "headline": {"setup": ["Words the speaker said", "in their own order."], "payoff": "Their own words."}
  "watermark": "talentsocial.network"                     small, quiet, bottom-left (hide it while a glass card is up)
  "lower":    {"name": "Speaker Name", "role": "ROLE, COMPANY"}   lower third, left aligned
  "lowers":   {"a": {...}, "b": {...}}                      several lower thirds: lower-a.png, lower-b.png
  "glass":    {"yulia": {"type": "name", "name": "...", "role": "..."}, "end": {"type": "outro", "title": "Talent Social", "line": "talentsocial.network"}}
                                                             liquid-glass cards: glass-<id>.png, glass-<id>.mask.png, glass-<id>.json (x, y, w, h);
                                                             the assembler blurs the real picture behind them
  "cta":      {"text": "RSVP · THU 29 OCT · WESTLANDS"}  square gold button, bottom-left
  "points":   [["1", "Know your strategy"], ...]          numbered step lines, one PNG each (step-1.png ...)
  "number":   {"from": "1 week", "to": "2 days"}          big before / after numbers
Writes headline.png, watermark.png, lower.png, cta.png, step-N.png, number.png (1080x1920, RGBA).
Look: Inter Tight SemiBold setup, a gold payoff (Didot Italic on macOS), left aligned at a 92 px margin,
a soft warm-black gradient behind text (no boxes), nothing in the top 220 px, the right 140 px or the bottom 480 px.
The values come from brand.py. Run with $STT_PYTHON (Pillow).
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand
from PIL import Image, ImageDraw, ImageFilter

W, H = 1080, 1920
MX = 92                      # left margin (matches the team's confirmed layout)
RIGHT = 940                  # nothing right of this
TOP = 240                    # nothing above 220; the eyebrow sits at 240
BOTTOM = 1440                # keep text above the caption and button zone (bottom 25%)


def canvas():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def scrim(img, y0, y1, strength=190, top_soft=True):
    """Warm-black gradient behind text so it reads on any shot: soft at both ends, strongest in the middle. No boxes."""
    import math
    n = y1 - y0
    g = Image.new("L", (1, n))
    for i in range(n):
        t = i / max(1, n - 1)
        g.putpixel((0, i), int(strength * math.sin(math.pi * t) ** 0.7))
    band = Image.new("RGBA", (W, n), brand.rgb(brand.INK, 255))
    band.putalpha(g.resize((W, n)))
    img.alpha_composite(band, (0, y0))


def curly(t):
    """Typographic apostrophes and quotes (Pillow here has no kerning, and straight quotes space badly in Didot)."""
    return t.replace("'", "\u2019").replace('"', "\u201d")


def shadowed(img, xy, text, font, fill, blur=8, dy=4, alpha=170, tracking=0, stroke=0):
    """Draw text over a soft drop shadow (shadow first, then the text). Optional letter tracking in px. Returns end x."""
    text = curly(text)
    x, y = xy
    chars = list(text) if tracking else [text]
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    probe = ImageDraw.Draw(img)
    cx = x
    for ch in chars:
        sd.text((cx, y + dy), ch, font=font, fill=(0, 0, 0, alpha))
        cx += probe.textlength(ch, font=font) + tracking
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(img)
    cx = x
    for ch in chars:
        d.text((cx, y), ch, font=font, fill=fill, stroke_width=stroke, stroke_fill=fill)
        cx += d.textlength(ch, font=font) + tracking
    return cx


def fit(text_lines, face, max_w, start, lo=40):
    text_lines = [curly(t) for t in text_lines]
    probe = ImageDraw.Draw(Image.new("L", (4, 4)))
    size = start
    while size > lo:
        f = face(size)
        if all(probe.textlength(t, font=f) <= max_w for t in text_lines):
            return size
        size -= 2
    return lo


def glow(img, strength=1.0):
    """Soft warm-black glow behind whatever is drawn (same as the captions' halo), instead of a gradient block."""
    import kinetic_captions as ktc
    return ktc.halo(img)


def headline(spec):
    """Setup lines in off-white, then the payoff line in gold, over a soft glow. Sits at 30% of the frame height."""
    img = canvas()
    setup = spec["setup"]; pay = spec.get("payoff", "")
    max_w = RIGHT - MX
    size = fit(setup, lambda s: brand.inter(s, 600), max_w, 92)
    f = brand.inter(size, 600)
    lh = int(size * 1.08)
    top = int(H * spec.get("y", 0.30))
    y = top
    for line in setup:
        shadowed(img, (MX, y), line, f, brand.rgb(brand.OFFWHITE, 255), tracking=-size * 0.02)
        y += lh
    if pay:
        pf_size = fit([pay], lambda s: brand.payoff(s), max_w, int(size * 1.12))
        shadowed(img, (MX, y + int(size * 0.02)), pay, brand.payoff(pf_size), brand.rgb(brand.GOLD_VIDEO, 255), stroke=brand.payoff_stroke(2))
    return glow(img)


def watermark(text):
    """A small, quiet site address at the bottom-left, above y 1440. Low opacity, no glow, nowhere near the faces."""
    img = canvas()
    f = brand.inter(22, 600)
    shadowed(img, (MX, 1402), text, f, brand.rgb(brand.OFFWHITE, 150), blur=4, dy=1, alpha=150, tracking=1.4)
    return img



def bottom_gradient(img, y0=1010, y1=1460, strength=215):
    """Ramp from clear (y0) to strength (y1), then hold to the bottom edge, like the platform's own shading."""
    n = H - y0
    g = Image.new("L", (1, n))
    for i in range(n):
        t = min(1.0, i / max(1, y1 - y0))
        g.putpixel((0, i), int(strength * (t * t * (3 - 2 * t))))
    band = Image.new("RGBA", (W, n), brand.rgb(brand.INK, 255))
    band.putalpha(g.resize((W, n)))
    img.alpha_composite(band, (0, y0))


def lower(spec):
    img = canvas()
    name, role = spec["name"], spec.get("role", "")
    size = fit([name], lambda s: brand.inter(s, 600), RIGHT - MX, 56)
    fn, fr = brand.inter(size, 600), brand.inter(24, 600)
    y0 = 1318                    # clear of the caption band (55 to 70%) and above the bottom 25%
    bottom_gradient(img)
    ImageDraw.Draw(img).rectangle([MX, y0 + 14, MX + 4, y0 + 14 + size + 44], fill=brand.rgb(brand.GOLD, 255))
    shadowed(img, (MX + 24, y0), name, fn, brand.rgb(brand.OFFWHITE, 255))
    if role:
        shadowed(img, (MX + 24, y0 + size + 18), role, fr, brand.rgb(brand.GOLD_VIDEO, 255), blur=4, dy=2, tracking=3.4)
    return img


def cta(spec):
    """Square gold button in the site's style, left aligned, above the bottom 25% zone."""
    img = canvas()
    text = spec["text"]
    f = brand.inter(34, 700)
    d = ImageDraw.Draw(img)
    tw = d.textlength(text, font=f) + len(text) * 2.6
    w, h = int(tw + 64), 84
    x0, y0 = MX, 1318
    if x0 + w > RIGHT:
        f = brand.inter(28, 700); tw = d.textlength(text, font=f) + len(text) * 2.2; w = int(tw + 56)
    bottom_gradient(img, 1100, 1480, 190)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([x0, y0 + 6, x0 + w, y0 + h + 6], fill=(0, 0, 0, 120))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(img)
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=brand.rgb(brand.GOLD_VIDEO, 255))
    tx = x0 + 32
    for ch in text:
        d.text((tx, y0 + (h - f.size) // 2 - 3), ch, font=f, fill=brand.rgb(brand.ON_GOLD, 255))
        tx += d.textlength(ch, font=f) + (2.6 if f.size >= 34 else 2.2)
    return img


def step(num, title):
    img = canvas()
    f1, f2 = brand.inter(22, 600), brand.inter(46, 600)
    y = 470
    scrim(img, y - 70, y + 150, 150)
    shadowed(img, (MX, y), f"{num}", brand.payoff(64), brand.rgb(brand.GOLD, 255), blur=4)
    shadowed(img, (MX + 64, y + 8), title, f2, brand.rgb(brand.OFFWHITE, 255), blur=5)
    return img


def number(spec):
    img = canvas()
    a, b = spec["from"], spec["to"]
    size = fit([a, b], lambda s: brand.inter(s, 700), RIGHT - MX - 40, 190, lo=80)
    f = brand.inter(size, 700)
    top0 = int(H * spec.get("y", 0.27))
    shadowed(img, (MX, top0), a, f, brand.rgb(brand.MUTED, 255))
    d = ImageDraw.Draw(img)
    d.rectangle([MX, top0 + size * 0.52, MX + ImageDraw.Draw(img).textlength(curly(a), font=f), top0 + size * 0.52 + 8],
                fill=brand.rgb(brand.OFFWHITE, 255))
    shadowed(img, (MX, top0 + int(size * 1.18)), b, brand.payoff(size * 1.04), brand.rgb(brand.GOLD_VIDEO, 255), stroke=brand.payoff_stroke(2))
    return glow(img)


def _rr_mask(size, r):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=r, fill=255)
    return m


def _diag(size, a0, a1, flip=False):
    """Diagonal alpha ramp (top-left a0 -> bottom-right a1) as an L image."""
    import numpy as np
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w]
    t = (xx / max(1, w - 1) + yy / max(1, h - 1)) / 2
    if flip:
        t = 1 - t
    return Image.fromarray((a0 + (a1 - a0) * t).clip(0, 255).astype("uint8"), "L")


def glass_card(spec):
    """Liquid-glass card. Returns (full-frame RGBA with tint, rim, highlight and text; rect-sized L mask; rect dict).
    The assembler blurs the real picture behind the rect and cuts it with the mask, so the glass is truly translucent."""
    kind = spec.get("type", "name")
    pad_x, pad_y, r = 54, 34, 46
    if kind == "outro":
        l1, l2 = spec.get("title", "Talent Social"), spec.get("line", "talentsocial.network")
        f1, f2 = brand.inter(60, 700), brand.inter(36, 600)
        tr1, tr2 = 0, 0.6
    else:
        l1, l2 = spec["name"], spec.get("role", "")
        size = fit([l1], lambda s: brand.inter(s, 700), 800 - 2 * pad_x, 64)
        f1, f2 = brand.inter(size, 700), brand.inter(26, 600)
        tr1, tr2 = 0, 4.0
    probe = ImageDraw.Draw(Image.new("L", (4, 4)))
    w1 = probe.textlength(curly(l1), font=f1)
    w2 = sum(probe.textlength(ch, font=f2) + tr2 for ch in curly(l2)) if l2 else 0
    w = int(max(w1, w2) + 2 * pad_x)
    a1 = f1.size
    a2 = f2.size if l2 else 0
    h = int(pad_y * 2 + a1 * 1.05 + (a2 * 1.35 if l2 else 0))
    x, y = MX, 1440 - h - 8 if kind != "outro" else 1440 - h - 8
    img = canvas()
    # soft shadow under the card
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sh.paste((0, 0, 0, 120), (x, y + 12), _rr_mask((w, h), r))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(20)))
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    # glass tint: lighter at the top, clearer at the bottom
    tint = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    grad = Image.new("L", (1, h))
    for i in range(h):
        grad.putpixel((0, i), int(52 - 34 * i / max(1, h - 1)))
    tint.putalpha(grad.resize((w, h)))
    card.alpha_composite(tint)
    # specular blob top-left, clipped to the card
    blob = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(blob).ellipse([-w * 0.15, -h * 0.9, w * 0.55, h * 0.45], fill=(255, 255, 255, 70))
    card.alpha_composite(blob.filter(ImageFilter.GaussianBlur(16)))
    # rim light: bright top-left to faint bottom-right, plus a warm edge bottom-right
    rim = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(rim).rounded_rectangle([1, 1, w - 2, h - 2], radius=r - 1, outline=(255, 255, 255, 255), width=3)
    rim.putalpha(Image.fromarray((__import__("numpy").array(rim.getchannel("A"), dtype="float32") * __import__("numpy").array(_diag((w, h), 0.95, 0.22), dtype="float32") / 255).astype("uint8"), "L"))
    card.alpha_composite(rim)
    warm = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(warm).rounded_rectangle([1, 1, w - 2, h - 2], radius=r - 1, outline=brand.rgb(brand.GOLD_VIDEO, 255), width=2)
    warm.putalpha(Image.fromarray((__import__("numpy").array(warm.getchannel("A"), dtype="float32") * __import__("numpy").array(_diag((w, h), 0.0, 0.55), dtype="float32") / 255).astype("uint8"), "L"))
    card.alpha_composite(warm)
    inner = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(inner).rounded_rectangle([6, 6, w - 7, h - 7], radius=r - 6, outline=(255, 255, 255, 34), width=2)
    card.alpha_composite(inner)
    # clip everything to the rounded card
    card.putalpha(Image.fromarray((__import__("numpy").array(card.getchannel("A"), dtype="float32") * __import__("numpy").array(_rr_mask((w, h), r), dtype="float32") / 255).astype("uint8"), "L"))
    img.alpha_composite(card, (x, y))
    # text
    ty = y + pad_y - 2
    shadowed(img, (x + pad_x, ty), l1, f1, brand.rgb(brand.OFFWHITE, 255), blur=5, dy=2, alpha=120, tracking=tr1)
    if l2:
        shadowed(img, (x + pad_x, ty + int(a1 * 1.12)), l2, f2, brand.rgb(brand.GOLD_VIDEO if kind != "outro" else brand.OFFWHITE, 255),
                 blur=4, dy=2, alpha=110, tracking=tr2)
    return img, _rr_mask((w, h), r), {"x": x, "y": y, "w": w, "h": h, "r": r}


def check_safe(img, name):
    """Fail loudly if text (bright pixels, not the dark gradient) sits in the top 220 px or the right 140 px."""
    import numpy as np
    arr = np.array(img)
    bright = (arr[..., 3] > 40) & (arr[..., :3].max(axis=2) > 90)
    if bright[:220].any() or bright[:, RIGHT + 8:].any():
        sys.exit(f"brand_cards.py: {name} has text in a safe zone (top {int(bright[:220].sum())} px, right {int(bright[:, RIGHT + 8:].sum())} px).")


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    spec = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    made = {}
    if spec.get("headline"):
        made["headline"] = headline(spec["headline"])
    if spec.get("watermark"):
        made["watermark"] = watermark(spec["watermark"])
    if spec.get("lower"):
        made["lower"] = lower(spec["lower"])
    for key, sp in (spec.get("glass") or {}).items():         # liquid-glass cards: glass-<key>.png + .mask.png + .json
        gi, gm, gr = glass_card(sp)
        check_safe(gi, f"glass-{key}")
        gi.save(os.path.join(out, f"glass-{key}.png")); gm.save(os.path.join(out, f"glass-{key}.mask.png"))
        json.dump(gr, open(os.path.join(out, f"glass-{key}.json"), "w"))
        print(os.path.join(out, f"glass-{key}.png"))
    for key, sp in (spec.get("lowers") or {}).items():       # several speakers: lower-<key>.png
        made[f"lower-{key}"] = lower(sp)
    if spec.get("cta"):
        made["cta"] = cta(spec["cta"])
    for i, (n, t) in enumerate(spec.get("points", []), 1):
        made[f"step-{i}"] = step(n, t)
    if spec.get("number"):
        made["number"] = number(spec["number"])
    for k, im in made.items():
        check_safe(im, k)
        im.save(os.path.join(out, k + ".png"))
        print(os.path.join(out, k + ".png"))


if __name__ == "__main__":
    main()
