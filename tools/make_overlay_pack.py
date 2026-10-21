#!/usr/bin/env python3
"""make_overlay_pack.py - build the Talent Social on-screen graphics pack for CapCut (and the agent tier).

Usage: make_overlay_pack.py --out DIR --font TTF
         [--series "JOB SEARCH TIPS 101"] [--episode 02] [--name "Speaker Name"] [--topic "CAREER ADVICE"]
         [--headline "100+ APPLICATIONS.|ZERO REPLIES."] [--gold-word ZERO]
         [--tabs "STRATEGY,CV,STAND OUT"] [--points "FIX YOUR STRATEGY,FIX YOUR CV,STAND OUT"]
         [--checklist "A,B,C"] [--action "REWRITE YOUR CV FOR ONE ROLE"]
         [--cta "FOLLOW FOR PART 2"] [--keyword ROLES] [--skip-clips] [--skip-sounds] [--tmp DIR]

With only --out and --font every text has a sensible default and the whole pack is written.
Everything is 1080x1920, sRGB, transparent, and already positioned: the editor drops each file on the
overlay track at full frame. Nothing sits in the top 220 px, the bottom 380 px (y 1540+) or the right
140 px (x 940+); the script checks every PNG after writing it and exits 1 if one breaks the rule.

Writes under DIR (never inside the repo; media must stay out of git):
  stills/  brand-mark, series-bug, label, tabs-0..3, point-card-1..3, checklist-card (+ -step1, -step2),
           action-card, cta-card, comment-keyword-card, headline            (PNG)
  clips/   band-wipe, sting, cta-in                                          (.mov ProRes 4444 with alpha,
           plus a green-screen .mp4 fallback on #00FF00; the sting is opaque so its .mp4 has no green)
  sounds/  sting.wav, whoosh.wav, tick.wav   (synthesised with ffmpeg lavfi; mono 48 kHz; peak about -6 dBFS)
  CAPCUT-HOW-TO.md, manifest.json
Existing files in DIR with these names are overwritten; nothing else is touched or deleted.

Pillow draws every frame (this ffmpeg has no drawtext); ffmpeg only encodes and synthesises sound.
Colours come from IDENTITY.md: gold F5B533, charcoal 181E2A, off-white F4F1EA (placeholder, to confirm).
The Vetted purple is not used. Gold is used only for the one headline word, the active tab, the label's
topic line, the CTA button and the sting underline. The brand mark is text only until the real logo exists.
"""
import argparse, io, json, math, os, re, shutil, subprocess, sys, tempfile

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:
    sys.exit("make_overlay_pack.py: Pillow is missing. Use $STT_PYTHON or `pip install pillow`.")
try:
    import numpy as np
except ImportError:
    sys.exit("make_overlay_pack.py: numpy is missing. Use $STT_PYTHON or `pip install numpy`.")
try:
    from PIL import ImageCms
except ImportError:
    ImageCms = None

# ---------------------------------------------------------------- constants (IDENTITY.md)
W, H, FPS = 1080, 1920, 30
GOLD = (245, 181, 51)          # about F5B533, to confirm in Canva
CHAR = (24, 30, 42)            # about 181E2A, to confirm in Canva
OFFW = (244, 241, 234)         # F4F1EA placeholder, to confirm
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SAFE_X1, SAFE_Y0, SAFE_Y1 = 940, 220, 1540      # nothing at x >= 940, y < 220, y >= 1540
COL_L, COL_R = 60, 920                           # content column (keeps shadows inside x < 940)
COL_W = COL_R - COL_L
CX = (COL_L + COL_R) // 2                        # centre of the content column
TAIL_ALPHA = 12                                  # soft-shadow tails at or below this are zeroed outside the zone
FONT_DEFAULT = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_FALLBACK = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
SOUND_PEAK_DB = -6.0
CLIP_MB_TARGET = 3.0

FONT_PATH = FONT_DEFAULT


def die(msg):
    sys.exit(f"make_overlay_pack.py: {msg}")


def font(size):
    return ImageFont.truetype(FONT_PATH, int(round(size)))


_probe = ImageDraw.Draw(Image.new("L", (4, 4)))


def tlen(text, f):
    return _probe.textlength(text, font=f)


def ink(text, f, stroke=0):
    """(left, top, right, bottom) of the drawn ink relative to a baseline-left origin."""
    return _probe.textbbox((0, 0), text, font=f, anchor="ls", stroke_width=stroke)


def fit_size(texts, max_w, start, lo=16, stroke=0):
    """Largest font size at or below `start` where every text is at most max_w wide."""
    size = start
    while size > lo:
        f = font(size)
        if all(tlen(t, f) + 2 * stroke <= max_w for t in texts):
            return size
        size -= 1
    return lo


def canvas():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def paste(dst, layer, x, y):
    """alpha_composite `layer` onto `dst` at (x, y), cropping whatever falls outside."""
    x, y = int(x), int(y)
    l, t = max(0, -x), max(0, -y)
    r, b = min(layer.width, dst.width - x), min(layer.height, dst.height - y)
    if r > l and b > t:
        dst.alpha_composite(layer.crop((l, t, r, b)), (x + l, y + t))


def rgba(c, a=255):
    return tuple(c) + (a,)


def rrect(w, h, r, fill=None, outline=None, ow=0, ss=4):
    """Anti-aliased rounded rectangle (drawn 4x and shrunk)."""
    im = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, w * ss - 1, h * ss - 1), radius=r * ss, fill=fill,
                                         outline=outline, width=ow * ss)
    return im.resize((w, h), Image.LANCZOS)


def shadow_under(dst, layer, x, y, sigma=6, dy=4, strength=0.45, times=1):
    pad = int(sigma * 4)
    a = Image.new("L", (layer.width + 2 * pad, layer.height + 2 * pad), 0)
    a.paste(layer.getchannel("A"), (pad, pad))
    a = a.filter(ImageFilter.GaussianBlur(sigma)).point(lambda v: int(v * strength))
    sh = Image.new("RGBA", a.size, (0, 0, 0, 0))
    sh.putalpha(a)
    for _ in range(times):
        paste(dst, sh, x - pad, y - pad + dy)


def text_layer(text, f, fill, stroke=0, stroke_fill=CHAR, pad=6):
    """RGBA layer with the text (colour taken from the mask, so edges stay clean on transparency).
    Returns (layer, dx, dy): the layer's top-left relative to the baseline-left origin."""
    l, t, r, b = ink(text, f, stroke)
    w, h = r - l + 2 * pad, b - t + 2 * pad
    ox, oy = pad - l, pad - t
    outer = Image.new("L", (w, h), 0)
    inner = Image.new("L", (w, h), 0)
    ImageDraw.Draw(outer).text((ox, oy), text, font=f, fill=255, anchor="ls", stroke_width=stroke)
    ImageDraw.Draw(inner).text((ox, oy), text, font=f, fill=255, anchor="ls")
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    if stroke:
        o = Image.new("RGBA", (w, h), rgba(stroke_fill, 0))
        o.putalpha(outer)
        lay.alpha_composite(o)
    i = Image.new("RGBA", (w, h), rgba(fill, 0))
    i.putalpha(inner)
    lay.alpha_composite(i)
    return lay, -ox, -oy


def put_text(dst, x, base, text, f, fill, stroke=0, stroke_fill=CHAR, shadow=False):
    lay, dx, dy = text_layer(text, f, fill, stroke, stroke_fill)
    if shadow:
        shadow_under(dst, lay, x + dx, base + dy, sigma=5, dy=4, strength=0.7, times=2)
    paste(dst, lay, x + dx, base + dy)


def put_text_centered(dst, cx, base, text, f, fill, **kw):
    put_text(dst, cx - tlen(text, f) / 2, base, text, f, fill, **kw)


def card(dst, x, y, w, h, r, fill, outline=None, ow=0, shadow=True):
    lay = rrect(w, h, r, fill=fill, outline=outline, ow=ow)
    if shadow:
        shadow_under(dst, lay, x, y)
    paste(dst, lay, x, y)


def check_icon(d, ticked):
    """A round tick box d px wide: white ring, or filled white with a charcoal tick."""
    ss = 4
    im = Image.new("RGBA", (d * ss, d * ss), (0, 0, 0, 0))
    g = ImageDraw.Draw(im)
    if ticked:
        g.ellipse((0, 0, d * ss - 1, d * ss - 1), fill=rgba(WHITE))
        pts = [(0.27, 0.53), (0.43, 0.69), (0.74, 0.34)]
        g.line([(px * d * ss, py * d * ss) for px, py in pts], fill=rgba(CHAR), width=int(d * ss * 0.12), joint="curve")
        for px, py in (pts[0], pts[2]):                       # round the line ends
            rr = d * ss * 0.06
            g.ellipse((px * d * ss - rr, py * d * ss - rr, px * d * ss + rr, py * d * ss + rr), fill=rgba(CHAR))
    else:
        g.ellipse((0, 0, d * ss - 1, d * ss - 1), outline=rgba(WHITE), width=int(d * ss * 0.09))
    return im.resize((d, d), Image.LANCZOS)


def wrap2(text, f, max_w):
    """Split text into at most two balanced lines no wider than max_w. None if it does not fit."""
    words = text.split()
    if tlen(text, f) <= max_w:
        return [text]
    best = None
    for k in range(1, len(words)):
        a, b = " ".join(words[:k]), " ".join(words[k:])
        m = max(tlen(a, f), tlen(b, f))
        if m <= max_w and (best is None or m < best[0]):
            best = (m, [a, b])
    return best[1] if best else None


# ---------------------------------------------------------------- stills
class Params:
    pass


def draw_brand(c):
    """Top-left chip 'Talent Social · powered by Vetted' at y 240. Text only (placeholder for the logo)."""
    f1, f2 = font(30), font(23)
    t1, t2 = "Talent Social", "  ·  powered by Vetted"
    padx, h, y = 26, 64, 240
    w = int(padx * 2 + tlen(t1, f1) + tlen(t2, f2))
    card(c, COL_L, y, w, h, 16, rgba(CHAR, 238))
    base = y + h // 2 + 11
    put_text(c, COL_L + padx, base, t1, f1, WHITE)
    put_text(c, COL_L + padx + tlen(t1, f1), base, t2, f2, OFFW)
    return y + h


def draw_bug(c, top, series, episode):
    """Series bug directly under the brand mark: off-white chip, charcoal text."""
    text = f"{series} · EP {episode}".upper()
    size = fit_size([text], COL_W - 44, 25)
    f = font(size)
    padx, h = 22, 50
    w = int(tlen(text, f) + 2 * padx)
    y = top + 12
    card(c, COL_L, y, w, h, 12, rgba(OFFW, 245))
    put_text(c, COL_L + padx, y + h // 2 + int(size * 0.36), text, f, CHAR)
    return y + h


def draw_tabs(c, top, tabs, active):
    """Three progress tabs under the bug. Active tab gold, the others outlined. active is 0 (none) or 1..3."""
    labels = [f"{i + 1} {t}".upper() for i, t in enumerate(tabs)]
    gap, padx, h = 12, 22, 58
    size = 26
    while size > 14:
        f = font(size)
        total = sum(tlen(t, f) + 2 * padx for t in labels) + gap * (len(labels) - 1)
        if total <= COL_W:
            break
        size -= 1
    f = font(size)
    x, y = COL_L, top + 14
    for i, t in enumerate(labels):
        w = int(tlen(t, f) + 2 * padx)
        if i + 1 == active:
            card(c, x, y, w, h, 14, rgba(GOLD))
            colour = CHAR
        else:
            card(c, x, y, w, h, 14, rgba(CHAR, 150), outline=rgba(WHITE), ow=3)
            colour = WHITE
        put_text(c, x + padx, y + h // 2 + int(size * 0.36), t, f, colour)
        x += w + gap
    return y + h


def make_headline(p):
    c = canvas()
    lines = [l.strip().upper() for l in p.headline.split("|") if l.strip()]
    if not 1 <= len(lines) <= 2:
        die("--headline takes one or two lines separated by '|'.")
    stroke = 5
    size = min(fit_size(lines, COL_W - 2 * stroke, 118, stroke=stroke), 118)
    f = font(size)
    gold = re.sub(r"[^\w+%]", "", p.gold_word.upper()) if p.gold_word else ""
    used_gold = False
    lh = int(size * 1.14)
    block_h = lh * len(lines)
    top = int(H * 0.275 - block_h / 2)
    space = tlen(" ", f)
    for li, line in enumerate(lines):
        words = line.split()
        total = sum(tlen(w, f) for w in words) + space * (len(words) - 1)
        x = CX - total / 2
        base = top + li * lh + int(size * 0.88)
        for w in words:
            is_gold = (not used_gold) and gold and re.sub(r"[^\w+%]", "", w) == gold
            used_gold = used_gold or bool(is_gold)
            put_text(c, x, base, w, f, GOLD if is_gold else WHITE, stroke=stroke, shadow=True)
            x += tlen(w, f) + space
    if gold and not used_gold:
        print(f"warning: --gold-word '{p.gold_word}' not found in the headline; no gold word drawn.", file=sys.stderr)
    return c


def make_label(p):
    c = canvas()
    name, topic = p.name, p.topic
    padx, padt = 30, 16
    fn = font(fit_size([name], COL_W - 2 * padx, 48))
    ft = font(fit_size([topic], COL_W - 2 * padx, 30))
    w = int(max(tlen(name, fn), tlen(topic, ft)) + 2 * padx)
    w = min(w, COL_W)
    y = int(H * 0.72)
    h = 127
    card(c, COL_L, y, w, h, 14, rgba(CHAR, 242))
    put_text(c, COL_L + padx, y + padt + 42, name, fn, WHITE)
    put_text(c, COL_L + padx, y + padt + 42 + 42, topic, ft, GOLD)
    assert y + h <= int(H * 0.79) + 1, "label card leaves the 72 to 79% band"
    return c


def make_point_card(p, n):
    c = canvas()
    title = p.points[n - 1].upper()
    chip_w, chip_h, m = 104, 80, 14
    h = chip_h + 2 * m
    size = fit_size([title], COL_W - (m + chip_w + 26 + 34), 50)
    f = font(size)
    w = int(m + chip_w + 26 + tlen(title, f) + 34)
    y = 480
    card(c, COL_L, y, w, h, 18, rgba(OFFW, 247))
    paste(c, rrect(chip_w, chip_h, 12, fill=rgba(CHAR)), COL_L + m, y + m)
    fn = font(46)
    put_text_centered(c, COL_L + m + chip_w / 2, y + m + chip_h // 2 + 16, f"#{n}", fn, WHITE)
    put_text(c, COL_L + m + chip_w + 26, y + h // 2 + int(size * 0.36), title, f, CHAR)
    return c


def make_checklist(p, ticked):
    c = canvas()
    lines = [s.upper() for s in p.checklist]
    size = fit_size(lines, COL_W - 36 - 50 - 24 - 36, 46)
    f = font(size)
    box, row, padx, pady = 50, 86, 36, 26
    w = int(padx + box + 24 + max(tlen(s, f) for s in lines) + padx)
    h = pady * 2 + row * len(lines)
    x, y = COL_L, 700
    card(c, x, y, w, h, 20, rgba(CHAR, 240))
    for i, s in enumerate(lines):
        ry = y + pady + i * row
        paste(c, check_icon(box, i < ticked), x + padx, ry + (row - box) // 2)
        put_text(c, x + padx + box + 24, ry + row // 2 + int(size * 0.36), s, f, WHITE)
    return c


def make_action(p):
    c = canvas()
    pad = 36
    head = "THIS WEEK:"
    text = p.action.upper()
    size = 52
    while True:
        f = font(size)
        lines = wrap2(text, f, COL_W - 2 * pad)
        if lines or size <= 28:
            break
        size -= 2
    lines = lines or [text]
    fh = font(32)
    lh = int(size * 1.2)
    w = int(max([tlen(head, fh)] + [tlen(l, f) for l in lines]) + 2 * pad)
    h = pad + 36 + 14 + lh * len(lines) + pad - 8
    x, y = COL_L, 700
    card(c, x, y, w, h, 20, rgba(OFFW, 247))
    put_text(c, x + pad, y + pad + 26, head, fh, CHAR)
    for i, l in enumerate(lines):
        put_text(c, x + pad, y + pad + 36 + 14 + i * lh + int(size * 0.9), l, f, CHAR)
    return c


def cta_pill(c, parts, bottom=1500):
    """Gold pill, bottom edge at `bottom` (above y 1540). parts = list of (text, is_keyword)."""
    padx, h = 54, 124
    texts = [t for t, _ in parts]
    size = 62
    while size > 24:
        f = font(size)
        total = sum(tlen(t, f) for t in texts) + (len(parts) - 1) * 22 + (2 * 22 if any(k for _, k in parts) else 0)
        if total + 2 * padx <= 800:
            break
        size -= 1
    f = font(size)
    kw_pad = 22
    widths = [tlen(t, f) + (2 * kw_pad if k else 0) for t, k in parts]
    w = int(sum(widths) + 22 * (len(parts) - 1) + 2 * padx)
    x, y = int(CX - w / 2), bottom - h
    card(c, x, y, w, h, h // 2, rgba(GOLD), shadow=True)
    cx = x + padx
    base = y + h // 2 + int(size * 0.36)
    for (t, k), wd in zip(parts, widths):
        if k:
            ch = int(size * 1.5)
            paste(c, rrect(int(wd), ch, ch // 3, fill=rgba(CHAR)), cx, y + (h - ch) // 2)
            put_text(c, cx + kw_pad, base, t, f, WHITE)
        else:
            put_text(c, cx, base, t, f, CHAR)
        cx += wd + 22
    return c


def make_cta(p):
    return cta_pill(canvas(), [(p.cta.upper(), False)])


def make_keyword(p):
    return cta_pill(canvas(), [("COMMENT", False), (p.keyword.upper(), True)])


def build_stills(p):
    s = {}
    c = canvas(); draw_brand(c); s["brand-mark"] = c
    c = canvas(); draw_bug(c, 240 + 64, p.series, p.episode); s["series-bug"] = c
    s["label"] = make_label(p)
    for k in range(4):                                   # tabs-0 = all outlined (before point 1)
        c = canvas()
        draw_tabs(c, draw_bug(canvas(), 240 + 64, p.series, p.episode), p.tabs, k)
        s[f"tabs-{k}"] = c
    for n in (1, 2, 3):
        s[f"point-card-{n}"] = make_point_card(p, n)
    s["checklist-card-step1"] = make_checklist(p, 1)
    s["checklist-card-step2"] = make_checklist(p, 2)
    s["checklist-card"] = make_checklist(p, 3)
    s["action-card"] = make_action(p)
    s["cta-card"] = make_cta(p)
    s["comment-keyword-card"] = make_keyword(p)
    s["headline"] = make_headline(p)
    return s


def srgb_profile():
    if ImageCms is None:
        return None
    try:
        return ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
    except Exception:
        return None


def finalize_safe(img, name):
    """Zero the invisible soft-shadow tails that fall outside the safe band; fail on anything real."""
    arr = np.array(img)
    outside = np.ones(arr.shape[:2], bool)
    outside[SAFE_Y0:SAFE_Y1, 0:SAFE_X1] = False
    a = arr[..., 3]
    if a[outside].max() > TAIL_ALPHA:
        ys, xs = np.nonzero((a > TAIL_ALPHA) & outside)
        die(f"{name}: visible pixels outside the safe zones (x {xs.min()}-{xs.max()}, y {ys.min()}-{ys.max()}).")
    arr[outside] = 0
    return Image.fromarray(arr, "RGBA")


def check_png(path):
    """Independent re-read of the saved file. Returns (corner_alpha_ok, bbox, violations)."""
    im = Image.open(path)
    arr = np.array(im.convert("RGBA"))
    a = arr[..., 3]
    ys, xs = np.nonzero(a > 0)
    bbox = (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())) if len(xs) else None
    bad = int(((a > 0) & ((np.arange(H)[:, None] < SAFE_Y0) | (np.arange(H)[:, None] >= SAFE_Y1)
                          | (np.arange(W)[None, :] >= SAFE_X1))).sum())
    corners = all(a[y, x] == 0 for y in (0, H - 1) for x in (0, W - 1))
    return corners, bbox, bad, im.size, im.mode


# ---------------------------------------------------------------- ffmpeg helpers
def ffmpeg(*args):
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *args]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        die("ffmpeg failed: " + " ".join(cmd[:12]) + " ...\n" + r.stderr[-800:])


def require_ffmpeg():
    for t in ("ffmpeg", "ffprobe"):
        if shutil.which(t) is None:
            die(f"{t} is not installed or not on PATH.")
    enc = subprocess.run(["ffmpeg", "-hide_banner", "-encoders"], capture_output=True, text=True).stdout
    for e in ("prores_ks", "libx264", "pcm_s16le"):
        if e not in enc:
            die(f"this ffmpeg has no {e} encoder.")


COLOUR_VF = "scale=in_range=full:out_range=limited:out_color_matrix=bt709:flags=accurate_rnd+full_chroma_int"
COLOUR_TAGS = ["-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"]


def encode_alpha(seq_dir, out_mov):
    ffmpeg("-framerate", str(FPS), "-i", os.path.join(seq_dir, "f_%03d.png"),
           "-vf", COLOUR_VF + ",format=yuva444p10le", "-c:v", "prores_ks", "-profile:v", "4444",
           "-alpha_bits", "8", "-qscale:v", "9", "-vendor", "apl0", *COLOUR_TAGS, out_mov)


def encode_green(seq_dir, out_mp4, n, tmp):
    gdir = os.path.join(tmp, "green_" + os.path.basename(out_mp4))
    os.makedirs(gdir, exist_ok=True)
    for i in range(1, n + 1):
        im = Image.open(os.path.join(seq_dir, f"f_{i:03d}.png")).convert("RGBA")
        bg = Image.new("RGBA", im.size, rgba(GREEN))
        bg.alpha_composite(im)
        bg.convert("RGB").save(os.path.join(gdir, f"f_{i:03d}.png"))
    ffmpeg("-framerate", str(FPS), "-i", os.path.join(gdir, "f_%03d.png"),
           "-vf", COLOUR_VF + ",format=yuv420p", "-c:v", "libx264", "-preset", "slow", "-crf", "12",
           "-movflags", "+faststart", *COLOUR_TAGS, out_mp4)


def save_seq(frames, seq_dir):
    os.makedirs(seq_dir, exist_ok=True)
    for i, fr in enumerate(frames, 1):
        fr.save(os.path.join(seq_dir, f"f_{i:03d}.png"))


# ---------------------------------------------------------------- clips
def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


def ease_out_back(t, s=1.6):
    t -= 1
    return 1 + (s + 1) * t ** 3 + s * t ** 2


def wipe_frames(n=9, slope=0.30, band=1800):
    """Gold diagonal band. Enters from the left, fully covers the frame at the middle frame, leaves right."""
    ys, xs = np.mgrid[0:H, 0:W].astype(np.float32)
    u = xs + slope * ys
    umax = W + slope * H
    p0, p1 = -band - 20.0, umax + 20.0
    frames = []
    for i in range(n):
        s = (i + 0.5) / n
        e = 0.5 - 0.5 * math.cos(math.pi * s)
        p = p0 + (p1 - p0) * e
        a = np.clip(u - p + 0.5, 0, 1) * np.clip(p + band - u + 0.5, 0, 1)
        arr = np.zeros((H, W, 4), np.uint8)
        arr[..., 0], arr[..., 1], arr[..., 2] = GOLD
        arr[..., 3] = (a * 255 + 0.5).astype(np.uint8)
        frames.append(Image.fromarray(arr, "RGBA"))
    return frames


def sting_frames(dur=1.2):
    n = int(round(dur * FPS))
    word, tag = "Talent Social", "powered by Vetted"
    size = fit_size([word], 760, 112)
    f, ft = font(size), font(38)
    wl, wdx, wdy = text_layer(word, f, WHITE, pad=10)
    tl, tdx, tdy = text_layer(tag, ft, OFFW, pad=10)
    gw, gh = 820, 380
    base_y = 150                                  # wordmark baseline inside the group
    uy, uh = base_y + 34, 14
    ww = tlen(word, f)
    wx = (gw - ww) / 2
    frames = []
    for i in range(n):
        t = i / FPS
        bg = Image.new("RGBA", (W, H), rgba(CHAR))
        grp = Image.new("RGBA", (gw, gh), (0, 0, 0, 0))
        paste(grp, wl, wx + wdx, base_y + wdy)
        up = min(1, max(0, (t - 0.20) / 0.20))
        if up > 0:
            uw = int(ww * ease_out_cubic(up))
            if uw > 0:
                paste(grp, rrect(uw, uh, 4, fill=rgba(GOLD)), int(wx), uy)
        ta = min(1, max(0, (t - 0.40) / 0.15))
        if ta > 0:
            tg = tl.copy()
            tg.putalpha(tg.getchannel("A").point(lambda v: int(v * ta)))
            paste(grp, tg, int((gw - tlen(tag, ft)) / 2 + tdx), uy + uh + 56 + tdy)
        if t < 0.05:
            vis, sc = 0.0, 1.0
        elif t < 0.25:
            k = (t - 0.05) / 0.20
            vis, sc = min(1.0, k * 4), 0.6 + 0.4 * ease_out_back(k)
        elif t < 0.95:
            vis, sc = 1.0, 1.0
        elif t < 1.10:
            k = (t - 0.95) / 0.15
            vis, sc = 1 - k, 1 + 0.06 * k
        else:
            vis, sc = 0.0, 1.0
        if vis > 0:
            g = grp
            if abs(sc - 1) > 1e-3:
                g = grp.resize((max(1, int(gw * sc)), max(1, int(gh * sc))), Image.LANCZOS)
            if vis < 1:
                g.putalpha(g.getchannel("A").point(lambda v: int(v * vis)))
            paste(bg, g, CX_FULL - g.width // 2, SAFE_MID - g.height // 2 + 20)
        frames.append(bg)
    return frames


CX_FULL = W // 2
SAFE_MID = (SAFE_Y0 + SAFE_Y1) // 2


def cta_in_frames(cta_img, slide=8, hold=0):
    frames = []
    for i in range(slide):
        t = ease_out_cubic((i + 1) / slide)
        fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        moved = cta_img.copy()
        moved.putalpha(moved.getchannel("A").point(lambda v, k=min(1, t * 1.7): int(v * k)))
        fr.alpha_composite(moved.crop((0, 1200, W, 1620)), (0, 1200 + int((1 - t) * 170)))
        frames.append(fr)
    frames += [cta_img] * hold
    return frames


def build_clips(p, stills, out, tmp, report):
    cdir = os.path.join(out, "clips")
    os.makedirs(cdir, exist_ok=True)
    jobs = [("band-wipe", wipe_frames(), True),
            ("sting", sting_frames(), False),
            ("cta-in", cta_in_frames(stills["cta-card"], hold=0), True)]
    for name, frames, has_alpha in jobs:
        seq = os.path.join(tmp, "seq_" + name)
        save_seq(frames, seq)
        mov = os.path.join(cdir, name + ".mov")
        encode_alpha(seq, mov)
        entry = {"file": f"clips/{name}.mov", "frames": len(frames), "seconds": round(len(frames) / FPS, 3),
                 "mb": round(os.path.getsize(mov) / 1e6, 2)}
        green = os.path.join(cdir, (name + "-green.mp4") if has_alpha else (name + ".mp4"))
        encode_green(seq, green, len(frames), tmp)
        entry["fallback"] = f"clips/{os.path.basename(green)}"
        entry["fallback_mb"] = round(os.path.getsize(green) / 1e6, 2)
        report["clips"][name] = entry
        for key in ("mb", "fallback_mb"):
            if entry[key] > CLIP_MB_TARGET:
                print(f"note: {name} {key} {entry[key]} MB is over the {CLIP_MB_TARGET} MB target.", file=sys.stderr)


# ---------------------------------------------------------------- sounds
def render_sound(out_wav, inputs, graph, tmp):
    """Render to a temp wav, measure the peak, then write the final file at SOUND_PEAK_DB."""
    raw = os.path.join(tmp, "raw_" + os.path.basename(out_wav))
    args = []
    for i in inputs:
        args += ["-f", "lavfi", "-i", i]
    ffmpeg(*args, "-filter_complex", graph, "-map", "[out]", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", raw)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", raw, "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr)
    if not m:
        die("could not measure sound peak.")
    gain = SOUND_PEAK_DB - float(m.group(1))
    ffmpeg("-i", raw, "-af", f"volume={gain:.2f}dB", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", out_wav)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", out_wav, "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    return float(re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr).group(1))


def build_sounds(out, tmp, report):
    sdir = os.path.join(out, "sounds")
    os.makedirs(sdir, exist_ok=True)
    sr = "s=48000"
    # sting: rising chirp 300 -> 900 Hz over 0.40 s (with an octave above), then a soft low hit at 0.40 s
    rise = ("aevalsrc='(0.5*sin(2*PI*(300*t+750*t*t))+0.15*sin(4*PI*(300*t+750*t*t)))"
            "*(0.25+0.75*t/0.4)*lt(t,0.4)':" + sr + ":d=1.2")
    hit = ("aevalsrc='(0.9*sin(2*PI*(95+80*exp(-t*20))*t)*exp(-t*6.5)+0.35*sin(2*PI*660*t)*exp(-t*11))'"
           ":" + sr + ":d=0.8")
    g = ("[1]adelay=400[h];[0][h]amix=inputs=2:normalize=0:duration=longest,"
         "afade=t=in:d=0.004,afade=t=out:st=0.95:d=0.25[out]")
    peaks = {"sting.wav": render_sound(os.path.join(sdir, "sting.wav"), [rise, hit], g, tmp)}
    # whoosh: pink noise through six band-pass filters whose levels peak in turn, low to high
    bands = [400, 700, 1200, 2000, 3400, 5600]
    parts = ["[0]asplit=6" + "".join(f"[a{i}]" for i in range(6))]
    for i, fq in enumerate(bands):
        c0 = 0.04 + 0.04 * i
        parts.append(f"[a{i}]bandpass=f={fq}:width_type=q:w=1.2,asetnsamples=n=64:p=0,"
                     f"volume='exp(-pow((t-{c0:.2f})/0.05,2))':eval=frame[b{i}]")
    parts.append("".join(f"[b{i}]" for i in range(6)) +
                 "amix=inputs=6:normalize=0,afade=t=in:d=0.03,afade=t=out:st=0.2:d=0.1[out]")
    noise = f"anoisesrc=color=pink:amplitude=1:{sr}:d=0.3:seed=7"
    peaks["whoosh.wav"] = render_sound(os.path.join(sdir, "whoosh.wav"), [noise], ";".join(parts), tmp)
    # tick: 50 ms damped click
    tick = (f"aevalsrc='(sin(2*PI*2400*t)+0.4*sin(2*PI*4800*t))*exp(-t*95)*min(1,t/0.001)':{sr}:d=0.05")
    peaks["tick.wav"] = render_sound(os.path.join(sdir, "tick.wav"), [tick], "[0]afade=t=out:st=0.045:d=0.005[out]", tmp)
    report["sounds"] = {k: {"file": f"sounds/{k}", "peak_dbfs": v} for k, v in peaks.items()}


# ---------------------------------------------------------------- how-to
HOWTO = """# CapCut how-to: Talent Social overlay pack

One page for the editor. **Status:** the files were checked by script (size, transparency, safe zones, sound levels).
The CapCut steps below were **not** tried in CapCut by the person who built this pack. Each one is marked
{{NEEDS_VERIFICATION in CapCut}}. If a step does not match your app, tell the pack owner.

## What is in the pack
- `stills/` transparent PNGs, 1080x1920. Each graphic is already in its right place on the frame.
- `clips/` `band-wipe.mov`, `sting.mov`, `cta-in.mov` (transparent). Backup: `band-wipe-green.mp4`, `cta-in-green.mp4` (green background) and `sting.mp4` (solid card, no green).
- `sounds/` `sting.wav`, `whoosh.wav`, `tick.wav`. These are **placeholder** sounds until a designed sting exists.
- The brand mark is **text only** (a placeholder) until the real logo file exists.

## Import {{NEEDS_VERIFICATION in CapCut}}
- **Desktop:** project 9:16 (1080x1920). Media > Import, pick the whole `stills`, `clips` and `sounds` folders' files.
- **Phone:** copy the files to the phone first. PNGs and MOVs must keep their transparency; sending them through a chat app can flatten them, so use AirDrop, cable or a drive. Add them with Overlay > Add overlay (PNG and MOV) and Audio > Sounds > Your sounds or Extract/Device (WAV).

## Put each one on the overlay track at full frame {{NEEDS_VERIFICATION in CapCut}}
Drag the file onto a track **above** the video. Leave scale at 100% and position at 0, 0. Do not resize or move it: the position is built in, and moving it breaks the safe zones. On phone, an overlay may open smaller than the frame; pinch it out to fill the frame, then check it lines up with the screen edges.
Use five overlay tracks: **A** brand-mark, **B** series-bug, **C** tabs, **D** cards (headline, label, point, checklist, action, CTA: one at a time), **E** the clips (sting and band wipe).

## Advice episode: order and timing (58 s cut)
These are the times in `formats/advice-episode.md`. If the sting lands later than 3.0 s (its first sentence ends at 6 s, say), push every time after it by the same amount.

| When (s) | Put this | Track | Sound |
|---|---|---|---|
| 0.0 to the sting | `headline.png` | D | none |
| first sentence ends (about 3.0), 1.2 s long | `sting.mov` | E | `sting.wav` starting at the same moment |
| 4.2 to 7.2 | `label.png` | D | none |
| 4.2 to end | `brand-mark.png`; `series-bug.png` | A; B | none |
| 5.0 to 10.0 | `tabs-0.png` (all outlined) | C | none |
| 10.0 to 22.0 / 22.0 to 34.0 / 34.0 to 46.0 | `tabs-1.png` / `tabs-2.png` / `tabs-3.png` (that tab is gold) | C | none |
| 10.0, 22.0, 34.0 (0.3 s each) | `band-wipe.mov`. Make the cut in the video 0.15 s into the clip, when the whole frame is gold | E | `whoosh.wav` starting with the clip |
| start of each point, 2.5 s | `point-card-1.png`, `point-card-2.png`, `point-card-3.png` | D | none |
| inside a point, 3 s, as the speaker names the items | `checklist-card-step1.png`, then `-step2`, then `checklist-card.png` (all ticked) | D | none |
| 46.0 to 54.0 | `action-card.png` | D | none |
| 55.0 to 58.0 (held 3 s) | `cta-in.mov` (slides up in 0.27 s) then `cta-card.png` for the rest. Or just `cta-card.png` | D | none |

Only one card on screen at a time on track D; the wipe on track E may overlap a card. A comment-keyword CTA (`comment-keyword-card.png`) is used only when a named person will send the replies; otherwise use `cta-card.png`.

## Talk clip (`formats/talk-clip.md`, 20 to 45 s)
Make the pack with `--topic` set to the speaker's role exactly as the speaker form gives it, and `--cta` to the follow line.

| When (s) | Put this |
|---|---|
| 0.0 to the label | `headline.png` (the speaker's own words) |
| 5.0 to 8.0, at the first full sentence after the hook | `label.png` (name over role) |
| 5.0 to end | `brand-mark.png` |
| last 3 s | `cta-card.png` (held 3 s) |

The sting is optional in a talk clip: use `sting.mov` + `sting.wav` only if the hook ends at a sentence break. At most one `whoosh.wav`.

## Sounds
Voice stays first. `sting.wav` goes with the sting, `whoosh.wav` with each band wipe, nothing else. `tick.wav` is **not** used by default: IDENTITY section 8 allows only the sting and the whoosh. Use it on checklist ticks only if the pack owner says yes. Add music in the app at upload, not in this project. Keep the sound peaks as they are (about -6 dBFS); the final mix is mastered to -14 LUFS later.

## If the transparent clip does not work: green backup {{NEEDS_VERIFICATION in CapCut}}
Use `band-wipe-green.mp4` or `cta-in-green.mp4` on the overlay track, select the clip and find the Chroma key tool (desktop: Video > Cutout > Chroma key; phone: Cutout > Chroma key). Pick the green with the colour picker (it is #00FF00), then raise the intensity until the green is gone. A thin green edge may remain on the gold; lower the shadow or raise the intensity a little. `sting.mp4` is a solid card and needs no key.

## Before you export
Nothing in the top 220 px, the bottom 380 px or the right 140 px. One CTA, held 3 s. Pack text in this build: series "{series} - EP {episode}", headline "{headline}", tabs {tabs}, CTA "{cta}".
"""


def write_howto(p, out):
    txt = (HOWTO.replace("{series}", p.series).replace("{episode}", p.episode)
           .replace("{headline}", p.headline.replace("|", " / "))
           .replace("{tabs}", ", ".join(f'"{t}"' for t in p.tabs)).replace("{cta}", p.cta))
    with open(os.path.join(out, "CAPCUT-HOW-TO.md"), "w", encoding="utf-8") as fh:
        fh.write(txt)


# ---------------------------------------------------------------- main
def split_list(s, n, label, exact=False):
    items = [x.strip() for x in s.split(",") if x.strip()]
    if (exact and len(items) != n) or (not exact and not 1 <= len(items) <= n):
        die(f"{label} needs {'exactly ' if exact else 'up to '}{n} comma-separated items, got {len(items)}.")
    return items


def main():
    global FONT_PATH
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="output folder, outside the repo")
    ap.add_argument("--font", default=FONT_DEFAULT, help="heavy sans TTF (Poppins ExtraBold when you have it)")
    ap.add_argument("--series", default="JOB SEARCH TIPS 101")
    ap.add_argument("--episode", default="02")
    ap.add_argument("--name", default="Speaker Name", help="spelled as its owner spells it; not forced to caps")
    ap.add_argument("--topic", default="CAREER ADVICE", help="topic, or the speaker's role for a talk clip")
    ap.add_argument("--headline", default="100+ APPLICATIONS.|ZERO REPLIES.", help="one or two lines split with |")
    ap.add_argument("--gold-word", default="ZERO")
    ap.add_argument("--tabs", default="STRATEGY,CV,STAND OUT")
    ap.add_argument("--points", default="FIX YOUR STRATEGY,FIX YOUR CV,STAND OUT")
    ap.add_argument("--checklist", default=None, help="up to 3 lines; default = --points")
    ap.add_argument("--action", default="REWRITE YOUR CV FOR ONE ROLE", help="up to 8 words")
    ap.add_argument("--cta", default="FOLLOW FOR PART 2")
    ap.add_argument("--keyword", default="ROLES", help="word for the comment-keyword card")
    ap.add_argument("--skip-clips", action="store_true")
    ap.add_argument("--skip-sounds", action="store_true")
    ap.add_argument("--tmp", default=None, help="folder for temporary frames (default: system temp)")
    if len(sys.argv) == 1:
        ap.print_help()
        sys.exit(1)
    a = ap.parse_args()

    fp = os.path.expanduser(a.font)
    if not os.path.isfile(fp):
        for alt in (FONT_DEFAULT, FONT_FALLBACK):
            if os.path.isfile(alt):
                print(f"warning: font not found: {fp}; using {alt}", file=sys.stderr)
                fp = alt
                break
        else:
            die(f"font not found: {fp}")
    FONT_PATH = fp
    try:
        ImageFont.truetype(FONT_PATH, 20)
    except OSError as e:
        die(f"cannot open font {FONT_PATH}: {e}")

    p = Params()
    p.series, p.episode, p.name, p.topic = a.series, a.episode, a.name, a.topic
    p.headline, p.gold_word, p.cta, p.keyword, p.action = a.headline, a.gold_word, a.cta, a.keyword, a.action
    p.tabs = split_list(a.tabs, 3, "--tabs", exact=True)
    p.points = split_list(a.points, 3, "--points", exact=True)
    p.checklist = split_list(a.checklist, 3, "--checklist") if a.checklist else p.points
    for t in p.points + p.checklist:
        if len(t.split()) > 4:
            print(f"warning: '{t}' is longer than 4 words; the format page says 1 to 3 (cards) and 4 (checklist).", file=sys.stderr)
    if len(a.action.split()) > 8:
        print("warning: --action is longer than 8 words.", file=sys.stderr)

    out = os.path.abspath(os.path.expanduser(a.out))
    probe = out
    while True:                                   # media must never go in a git repo
        if os.path.exists(os.path.join(probe, ".git")):
            die(f"--out is inside a git repo ({probe}). Media must stay out of the repo; choose another folder.")
        if os.path.dirname(probe) == probe:
            break
        probe = os.path.dirname(probe)
    os.makedirs(out, exist_ok=True)
    if not (a.skip_clips and a.skip_sounds):
        require_ffmpeg()

    report = {"font": FONT_PATH, "stills": {}, "clips": {}, "sounds": {}, "violations": []}
    sdir = os.path.join(out, "stills")
    os.makedirs(sdir, exist_ok=True)
    icc = srgb_profile()
    stills = build_stills(p)
    for name, img in stills.items():
        img = finalize_safe(img, name)
        stills[name] = img
        path = os.path.join(sdir, name + ".png")
        kw = {"icc_profile": icc} if icc else {}
        img.save(path, optimize=True, **kw)
        corners, bbox, bad, size, mode = check_png(path)
        report["stills"][name] = {"file": f"stills/{name}.png", "size": list(size), "mode": mode,
                                  "corner_alpha_zero": corners, "ink_bbox": bbox, "pixels_in_unsafe_zones": bad,
                                  "srgb_profile": bool(icc)}
        if bad or not corners or size != (W, H):
            report["violations"].append(name)

    with tempfile.TemporaryDirectory(prefix="overlay_pack_", dir=a.tmp) as tmp:
        if not a.skip_clips:
            build_clips(p, stills, out, tmp, report)
        if not a.skip_sounds:
            build_sounds(out, tmp, report)
    write_howto(p, out)
    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1)

    print(f"{len(report['stills'])} stills, {len(report['clips'])} clips, {len(report['sounds'])} sounds -> {out}")
    if report["violations"]:
        print("SAFE-ZONE / TRANSPARENCY FAIL: " + ", ".join(report["violations"]), file=sys.stderr)
        sys.exit(1)
    print("safe-zone check: all stills inside x<940, 220<=y<1540, corners transparent.")


if __name__ == "__main__":
    main()
