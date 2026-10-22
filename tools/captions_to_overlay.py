#!/usr/bin/env python3
"""captions_to_overlay.py - draw captions as transparent PNGs (Pillow) plus an ffconcat list.

Usage: captions_to_overlay.py <captions.srt|transcript.json> <out_dir> --font <ttf>
         [--size 64] [--y 0.62] [--gold E2B05A] [--emphasis words.txt] [--style brand|classic] [--weight 600]
         [--width 1080] [--height 1920] [--max-seconds S]

Writes out_dir/cap_0001.png ..., blank.png, overlay.ffconcat and overlay.json (band position).
Each PNG is a full-width band; burn_captions.py overlays it at the y in overlay.json.
Rules: 2 to 5 words per chunk, sentence case as transcribed, white text with a thin charcoal edge and a soft shadow,
at most one gold word per chunk (a word from --emphasis, else a number word), centred at --y of the height.
This ffmpeg has no subtitles/drawtext filter, which is why captions are drawn here.
"""
import argparse, json, os, re, sys

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import brand
except ImportError:
    sys.exit("captions_to_overlay.py: Pillow is missing. Use $STT_PYTHON or `pip install pillow`.")

NUMBER_WORDS = {"hundred", "hundreds", "thousand", "thousands", "million", "billion", "percent"}
MIN_WORDS, MAX_WORDS = 2, 5
SAFE_SIDE = 140 / 1080          # right safe zone, applied on both sides so text stays centred


def srt_time(s):
    h, m, rest = s.strip().split(":")
    sec, ms = rest.replace(",", ".").split(".")
    return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms.ljust(3, "0")[:3]) / 1000


def read_cues(path):
    """Return a list of (start, end, [word, ...]). JSON gives real word times; SRT cues are split by length."""
    if path.lower().endswith(".json"):
        data = json.load(open(path))
        words = data["words"] if isinstance(data, dict) else data
        return chunk_words(words)
    cues = []
    for block in re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip()):
        lines = [l for l in block.splitlines() if l.strip()]
        idx = next((i for i, l in enumerate(lines) if "-->" in l), None)
        if idx is None:
            continue
        a, b = [srt_time(x) for x in lines[idx].split("-->")]
        words = " ".join(lines[idx + 1:]).split()
        cues.extend(split_cue(a, b, words))
    return cues


def split_cue(start, end, words):
    """Split one cue into chunks of 2-5 words; time is shared in proportion to letters."""
    if not words:
        return []
    n = len(words)
    k = max(1, -(-n // MAX_WORDS))                       # chunks needed
    size = [n // k + (1 if i < n % k else 0) for i in range(k)]
    if min(size) < MIN_WORDS and n >= MIN_WORDS:
        size = [n]
    out, i = [], 0
    total = sum(len(w) + 1 for w in words)
    t = start
    for sz in size:
        part = words[i:i + sz]; i += sz
        dur = (end - start) * sum(len(w) + 1 for w in part) / total
        out.append((t, t + dur, part)); t += dur
    return out


def chunk_words(words, gap=0.35):
    """Group timed words into chunks of 2-5 words, breaking at sentence ends and pauses."""
    chunks, cur = [], []
    def flush():
        nonlocal cur
        if cur:
            chunks.append(cur); cur = []
    for w in words:
        if cur and (w["start"] - cur[-1]["end"] > gap or len(cur) >= MAX_WORDS):
            flush()
        cur.append(w)
        if w["word"].endswith((".", "?", "!")):
            flush()
        elif len(cur) >= 3 and w["word"].endswith((",", ";", ":")):
            flush()
    flush()
    # a one-word chunk joins its neighbour if there is room
    merged = []
    for c in chunks:
        if merged and len(c) < MIN_WORDS and len(merged[-1]) + len(c) <= MAX_WORDS:
            merged[-1] = merged[-1] + c
        else:
            merged.append(c)
    return [(c[0]["start"], c[-1]["end"], [w["word"] for w in c]) for c in merged]


def pick_gold(words, emphasis):
    """Index of the one word to colour gold, or None."""
    clean = lambda w: re.sub(r"[^\w%]", "", w).lower()
    for i, w in enumerate(words):
        if clean(w) in emphasis:
            return i
    for i, w in enumerate(words):
        if clean(w) in NUMBER_WORDS or re.search(r"\d", w):
            return i
    return None


def wrap(words, font, draw, max_w):
    """Split words into at most two balanced lines that fit max_w. Returns list of lists of indices."""
    space = draw.textlength(" ", font=font)
    widths = [draw.textlength(w, font=font) for w in words]
    def line_w(ix):
        return sum(widths[i] for i in ix) + space * (len(ix) - 1)
    all_ix = list(range(len(words)))
    if line_w(all_ix) <= max_w or len(words) < 2:
        return [all_ix]
    best = min(range(1, len(words)), key=lambda k: max(line_w(all_ix[:k]), line_w(all_ix[k:])))
    return [all_ix[:best], all_ix[best:]]


def ktc_halo(frame):
    import kinetic_captions as ktc
    return ktc.halo(frame)


def render(words, gold_idx, font, size, band_h, gold_rgb, max_w, style="brand"):
    img = Image.new("RGBA", (size[0], band_h), (0, 0, 0, 0))
    probe = ImageDraw.Draw(img)
    lines = wrap(words, font, probe, max_w)
    ascent, descent = font.getmetrics()
    line_h = int((ascent + descent) * 1.05)
    block_h = line_h * len(lines)
    y0 = (band_h - block_h) // 2
    space = probe.textlength(" ", font=font)
    # brand style: no outline (the site's look), a soft shadow instead. classic: thin charcoal edge for white clothing.
    stroke = 0 if style == "brand" else max(2, size[0] // 360)
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(shadow)
    text = Image.new("RGBA", img.size, (0, 0, 0, 0)); td = ImageDraw.Draw(text)
    for li, ix in enumerate(lines):
        w_line = sum(probe.textlength(words[i], font=font) for i in ix) + space * (len(ix) - 1)
        x = (size[0] - w_line) / 2
        y = y0 + li * line_h
        for i in ix:
            white = brand.rgb(brand.OFFWHITE, 255) if style == "brand" else (255, 255, 255, 255)
            colour = gold_rgb + (255,) if i == gold_idx else white
            sd.text((x, y + 4), words[i], font=font, fill=(0, 0, 0, 215), stroke_width=max(stroke, 1 if style == "brand" else 0))
            td.text((x, y), words[i], font=font, fill=colour, stroke_width=stroke, stroke_fill=(20, 24, 34, 255))
            x += probe.textlength(words[i], font=font) + space
    shadow = shadow.filter(ImageFilter.GaussianBlur(max(3, size[0] // 180)))
    img = Image.alpha_composite(img, shadow)
    img = Image.alpha_composite(img, shadow)      # twice: a softer shadow still needs weight on bright video
    out = Image.alpha_composite(img, text)
    if style == "brand":
        out = ktc_halo(out)
    return out


def build(src, out_dir, font_path, size=64, y=0.62, gold="E2B05A", emphasis_file=None,
          width=1080, height=1920, max_seconds=None, style="brand", weight=600):
    """Write the overlay files. Returns (ffconcat_path, meta_dict)."""
    if not os.path.isfile(font_path):
        sys.exit(f"captions_to_overlay.py: font not found: {font_path}")
    if not os.path.isfile(src):
        sys.exit(f"captions_to_overlay.py: captions file not found: {src}")
    os.makedirs(out_dir, exist_ok=True)
    scale = width / 1080
    font = brand.load(font_path, size * scale, weight)
    emphasis = set()
    if emphasis_file:
        emphasis = {re.sub(r"[^\w%]", "", l).lower() for l in open(emphasis_file, encoding="utf-8") if l.strip()}
    gold_rgb = tuple(int(gold.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    cues = read_cues(src)
    if max_seconds is not None:
        cues = [(a, min(b, max_seconds), w) for a, b, w in cues if a < max_seconds]
    if not cues:
        sys.exit("captions_to_overlay.py: no captions found in the input.")

    band_h = int(height * 0.14)
    band_y = int(height * y - band_h / 2)
    max_w = int(width * (1 - 2 * SAFE_SIDE))
    blank = Image.new("RGBA", (width, band_h), (0, 0, 0, 0))
    blank.save(os.path.join(out_dir, "blank.png"))

    lines = ["ffconcat version 1.0"]
    pos, last = 0.0, "blank.png"
    gold_count = 0
    for n, (a, b, words) in enumerate(cues, 1):
        # hold a caption until the next one starts if the gap is small
        nxt = cues[n][0] if n < len(cues) else None
        b = nxt if nxt is not None and 0 <= nxt - b < 0.3 else b + 0.12
        a = max(a, pos)
        if a - pos > 0.01:
            lines += ["file blank.png", f"duration {a - pos:.3f}"]
        g = pick_gold(words, emphasis)
        gold_count += g is not None
        name = f"cap_{n:04d}.png"
        render(words, g, font, (width, height), band_h, gold_rgb, max_w, style).save(os.path.join(out_dir, name))
        lines += [f"file {name}", f"duration {max(b - a, 0.05):.3f}"]
        pos, last = a + max(b - a, 0.05), name
    lines.append(f"file {last}")     # ffconcat needs the last file repeated without a duration
    with open(os.path.join(out_dir, "overlay.ffconcat"), "w") as f:
        f.write("\n".join(lines) + "\n")
    meta = {"x": 0, "y": band_y, "width": width, "band_height": band_h, "end": round(pos, 3),
            "chunks": len(cues), "chunks_with_gold": gold_count, "y_fraction": y}
    json.dump(meta, open(os.path.join(out_dir, "overlay.json"), "w"), indent=1)
    return os.path.join(out_dir, "overlay.ffconcat"), meta


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("captions"); ap.add_argument("out_dir")
    ap.add_argument("--font", required=True)
    ap.add_argument("--size", type=int, default=64)
    ap.add_argument("--y", type=float, default=0.62)
    ap.add_argument("--gold", default="E2B05A")
    ap.add_argument("--style", choices=["brand", "classic"], default="brand")
    ap.add_argument("--weight", type=int, default=600, help="for a variable font such as Inter Tight")
    ap.add_argument("--emphasis")
    ap.add_argument("--width", type=int, default=1080)
    ap.add_argument("--height", type=int, default=1920)
    ap.add_argument("--max-seconds", type=float)
    if len(sys.argv) == 1:
        ap.print_help(); sys.exit(1)
    a = ap.parse_args()
    if not 0.55 <= a.y <= 0.70:
        print(f"warning: --y {a.y} is outside the 0.55 to 0.70 caption zone.", file=sys.stderr)
    path, meta = build(a.captions, a.out_dir, a.font, a.size, a.y, a.gold, a.emphasis, a.width, a.height, a.max_seconds, a.style, a.weight)
    print(f"{meta['chunks']} caption chunks ({meta['chunks_with_gold']} with a gold word) -> {path}")


if __name__ == "__main__":
    main()
