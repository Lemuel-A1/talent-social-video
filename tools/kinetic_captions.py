#!/usr/bin/env python3
"""kinetic_captions.py - captions that change with what the speaker says (Pillow, transparent PNG frames).

Usage: kinetic_captions.py <transcript.json|words.json> <out_dir> --font <InterTight[wght].ttf>
         [--audio video.mp4] [--emphasis words.txt] [--big words.txt] [--size 62] [--y 0.55]
         [--width 1080] [--height 1920] [--max-seconds S]

Words appear as they are spoken (a short pop). Each word is typeset by its role:
  normal  Inter Tight SemiBold, off-white
  soft    articles and joiners (the, of, to ...): smaller, lighter, a little transparent
  stress  stressed words: Inter Tight ExtraBold, larger, gold. Chosen from --emphasis plus the speaker's delivery
          (louder and slower-than-usual words, measured from --audio), at most two per phrase
  number  digits and number words: Inter Tight Black, larger still, gold
  big     the one word that carries the idea (--big): the gold payoff face (Didot Italic on macOS), very large, on its own line
Writes cap_0001.png ..., blank.png, overlay.ffconcat, overlay.json (the band y). burn_captions.py composites them.
Words come from transcribe.py's transcript.json ({"words": [{"word","start","end"}]}).
"""
import argparse, json, os, re, subprocess, sys

try:
    import numpy as np
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:
    sys.exit("kinetic_captions.py: needs numpy and Pillow. Use $STT_PYTHON.")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand

FPS = 30
SOFT = {"a", "an", "the", "of", "to", "in", "on", "at", "and", "or", "but", "it", "is", "are", "was", "were", "i", "you", "we",
        "that", "this", "so", "for", "with", "as", "by", "be", "my", "me", "your", "our", "its", "it's", "i'm", "you're", "they're",
        "have", "has", "had", "just", "like", "um", "uh", "than", "then", "if", "do", "did", "can", "will", "would", "from"}
NUMBER_WORDS = {"hundred", "thousand", "million", "billion", "percent", "week", "weeks", "days", "minutes", "years"}
SIDE = 140                      # keep clear of the right 140 px (applied both sides so text stays centred)


def clean(w):
    return re.sub(r"[^\w%']", "", w).lower()


def curly(t):
    return t.replace("'", "’").replace('"', "”")


def load_audio(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-vn", "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                       capture_output=True)
    return np.frombuffer(r.stdout, np.float32) if r.returncode == 0 and r.stdout else None


def prosody(words, audio):
    """Per-word stress score from loudness and slowness (z-scored over the clip). 0 when there is no audio."""
    if audio is None:
        return [0.0] * len(words)
    rms, dur = [], []
    for w in words:
        a, b = int(w["start"] * 16000), max(int(w["end"] * 16000), int(w["start"] * 16000) + 160)
        seg = audio[a:b] if a < len(audio) else audio[-160:]
        rms.append(float(np.sqrt(np.mean(seg ** 2) + 1e-12)))
        dur.append((w["end"] - w["start"]) / max(2, len(clean(w["word"]))))
    z = lambda v: (np.array(v) - np.mean(v)) / (np.std(v) + 1e-9)
    return list(z(np.log(rms)) + 0.7 * z(dur))


def phrases(words, max_words=5, gap=0.32):
    out, cur = [], []
    for i, w in enumerate(words):
        if cur and (w["start"] - words[i - 1]["end"] > gap or len(cur) >= max_words):
            out.append(cur); cur = []
        cur.append(i)
        if w["word"].rstrip().endswith((".", "?", "!")) or (len(cur) >= 3 and w["word"].rstrip().endswith((",", ";", ":"))):
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    merged = []
    for p in out:                      # a lone word joins its neighbour
        if merged and len(p) == 1 and len(merged[-1]) < max_words + 1:
            merged[-1] += p
        else:
            merged.append(p)
    return merged


def classify(words, scores, emphasis, big):
    """role per word index."""
    roles = {}
    thresh = np.percentile(scores, 82) if len(scores) > 8 else 9
    for i, w in enumerate(words):
        c = clean(w["word"])
        if c in big:
            roles[i] = "big"
        elif re.search(r"\d", c) or c in NUMBER_WORDS and c not in ("week", "weeks", "days", "minutes", "years"):
            roles[i] = "number"
        elif c in emphasis or (scores[i] >= thresh and c not in SOFT and len(c) >= 4):
            roles[i] = "stress"
        elif c in SOFT:
            roles[i] = "soft"
        else:
            roles[i] = "normal"
    return roles


def sprite(text, role, size, gold):
    """Render one word to a padded RGBA sprite plus its baseline offset."""
    text = curly(text)
    if role == "big":
        f = brand.payoff(size * 1.9)
        fill = gold
    elif role == "number":
        f = brand.inter(size * 1.5, 900)
        fill = gold
    elif role == "stress":
        f = brand.inter(size * 1.22, 800)
        fill = gold
    elif role == "soft":
        f = brand.inter(size * 0.82, 500)
        fill = brand.rgb(brand.OFFWHITE, 215)
    else:
        f = brand.inter(size, 600)
        fill = brand.rgb(brand.OFFWHITE, 255)
    probe = ImageDraw.Draw(Image.new("L", (4, 4)))
    l, t, r, b = probe.textbbox((0, 0), text, font=f, anchor="ls")
    pad = 26
    w, h = int(r - l + 2 * pad), int(b - t + 2 * pad)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sh = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ox, oy = pad - l, pad - t          # baseline-left origin inside the sprite
    ImageDraw.Draw(sh).text((ox, oy + 4), text, font=f, fill=(0, 0, 0, 205), anchor="ls")
    sh = sh.filter(ImageFilter.GaussianBlur(5))
    img = Image.alpha_composite(img, sh)
    sw = brand.payoff_stroke(1) if role == "big" else 0       # Didot's hairlines are thin on video; a 1 px stroke in the same colour holds them up
    ImageDraw.Draw(img).text((ox, oy), text, font=f, fill=fill, anchor="ls", stroke_width=sw, stroke_fill=fill)
    return img, oy, int(r - l)          # sprite, baseline y inside sprite, ink width


def halo(frame):
    """A soft warm-black glow behind the words so they read on bright shirts and walls (no box, no outline)."""
    a = frame.getchannel("A")
    if a.getextrema()[1] == 0:
        return frame
    # strong enough for white text on a white shirt: wide, dark, soft
    g = a.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(24)).point(lambda v: min(215, int(v * 1.5)))
    base = Image.new("RGBA", frame.size, brand.rgb(brand.INK, 255))
    base.putalpha(g)
    base.alpha_composite(frame)
    return base


def paste_safe(dst, im, x, y):
    """alpha_composite im onto dst at (x, y), cropping whatever falls outside."""
    l, t = max(0, -x), max(0, -y)
    r, b = min(im.width, dst.width - x), min(im.height, dst.height - y)
    if r > l and b > t:
        dst.alpha_composite(im.crop((l, t, r, b)), (x + l, y + t))


def ease_back(t, s=1.7):
    t = max(0.0, min(1.0, t))
    return 1 + (s + 1) * (t - 1) ** 3 + s * (t - 1) ** 2


def layout(phrase, words, roles, size, gold, max_w, cache):
    """Lines of word sprites. A 'big' word sits on its own line. Returns [(line_items, line_w, line_asc, line_desc)]."""
    items = []
    for i in phrase:
        key = (words[i]["word"], roles[i], size)
        if key not in cache:
            cache[key] = sprite(words[i]["word"], roles[i], size, gold)
        sp, base, ink = cache[key]
        items.append((i, sp, base, ink))
    gap = size * 0.28
    lines, cur, cw = [], [], 0
    for it in items:
        role = roles[it[0]]
        w = it[3] + (gap if cur else 0)
        if cur and (role == "big" or roles[cur[-1][0]] == "big" or cw + w > max_w):
            lines.append(cur); cur, cw = [], 0; w = it[3]
        cur.append(it); cw += w
    if cur:
        lines.append(cur)
    out = []
    for ln in lines:
        lw = sum(i[3] for i in ln) + gap * (len(ln) - 1)
        asc = max(i[2] for i in ln)
        desc = max(i[1].height - i[2] for i in ln)
        out.append((ln, lw, asc, desc))
    return out, gap


def build(src, out_dir, font_path=None, size=62, y=0.55, gold="E2B05A", emphasis_file=None, big_file=None,
          width=1080, height=1920, max_seconds=None, audio_from=None):
    data = json.load(open(src))
    words = data["words"] if isinstance(data, dict) else data
    if max_seconds is not None:
        words = [w for w in words if w["start"] < max_seconds]
    if not words:
        sys.exit("kinetic_captions.py: no words")
    read = lambda p: {clean(l) for l in open(p, encoding="utf-8") if l.strip()} if p and os.path.isfile(p) else set()
    emphasis, big = read(emphasis_file), read(big_file)
    scores = prosody(words, load_audio(audio_from) if audio_from else None)
    roles = classify(words, scores, emphasis, big)
    gold_rgb = brand.rgb(gold, 255)
    os.makedirs(out_dir, exist_ok=True)
    band_h = 560
    max_w = width - 2 * SIDE
    cache = {}
    blank = Image.new("RGBA", (width, band_h), (0, 0, 0, 0))
    blank.save(os.path.join(out_dir, "blank.png"))
    ph = phrases(words)
    # cap at two stressed words per phrase (keep the highest scores)
    for p in ph:
        st = sorted([i for i in p if roles[i] == "stress"], key=lambda i: -scores[i])
        for i in st[2:]:
            roles[i] = "normal"
    events = []                         # (t0, t1, png)
    n = 0
    for pi, p in enumerate(ph):
        t_start = words[p[0]]["start"] - 0.04
        t_end = words[p[-1]]["end"] + 0.10
        if pi + 1 < len(ph):
            t_end = min(t_end, words[ph[pi + 1][0]]["start"] - 0.04)
        t_end = max(t_end, t_start + 0.25)
        lines, gap = layout(p, words, roles, size, gold_rgb, max_w, cache)
        line_h = [asc + desc for _, _, asc, desc in lines]
        block = sum(line_h) + (len(lines) - 1) * int(size * 0.12)
        top = (band_h - block) // 2
        # time grid: animate for 0.3 s after each word appears and during the last 0.12 s
        pop_end = max(words[i]["start"] for i in p) + 0.32
        t = t_start
        while t < t_end - 1e-6:
            animating = t < pop_end or t > t_end - 0.12
            step = 1 / FPS if animating else (t_end - 0.12) - t
            step = max(step, 1 / FPS) if not animating else step
            frame = Image.new("RGBA", (width, band_h), (0, 0, 0, 0))
            yy = top
            for (ln, lw, asc, desc), lh in zip(lines, line_h):
                x = (width - lw) / 2
                for (i, sp, base, ink) in ln:
                    age = t - (words[i]["start"] - 0.04)
                    if age >= 0:
                        role = roles[i]
                        d = 0.30 if role == "big" else 0.18
                        k = ease_back(age / d, 2.2 if role == "big" else 1.7)
                        scale = (0.55 + 0.45 * k) if role == "big" else (0.7 + 0.3 * k)
                        alpha = min(1.0, age / 0.09)
                        rise = (1 - min(1.0, age / d)) * (22 if role == "big" else 12)
                        if t > t_end - 0.12:
                            alpha *= max(0.0, (t_end - t) / 0.12)
                        im = sp
                        if abs(scale - 1) > 0.004:
                            im = sp.resize((max(1, int(sp.width * scale)), max(1, int(sp.height * scale))), Image.LANCZOS)
                        if alpha < 0.999:
                            a = im.getchannel("A").point(lambda v: int(v * alpha)); im = im.copy(); im.putalpha(a)
                        # scale about the word's centre; keep the baseline on the line's baseline
                        bx = int(round(x + ink / 2 - im.width / 2))
                        by = int(round(yy + asc - base * scale + rise))
                        paste_safe(frame, im, bx, by)
                    x += ink + gap
                yy += lh + int(size * 0.12)
            frame = halo(frame)
            n += 1
            name = f"cap_{n:05d}.png"
            frame.save(os.path.join(out_dir, name))
            events.append((t, min(t + step, t_end), name))
            t += step
    # ffconcat
    lines_c = ["ffconcat version 1.0"]
    pos, last = 0.0, "blank.png"
    for t0, t1, name in events:
        t0 = max(t0, pos)
        if t0 - pos > 0.008:
            lines_c += ["file blank.png", f"duration {t0 - pos:.4f}"]
        dur = max(t1 - t0, 1 / 60)
        lines_c += [f"file {name}", f"duration {dur:.4f}"]
        pos, last = t0 + dur, name
    lines_c.append(f"file {last}")
    open(os.path.join(out_dir, "overlay.ffconcat"), "w").write("\n".join(lines_c) + "\n")
    band_y = int(height * y - band_h / 2)
    meta = {"x": 0, "y": band_y, "width": width, "band_height": band_h, "end": round(pos, 3), "chunks": len(ph),
            "chunks_with_gold": sum(1 for p in ph if any(roles[i] in ("stress", "number", "big") for i in p)),
            "roles": {r: sum(1 for v in roles.values() if v == r) for r in ("normal", "soft", "stress", "number", "big")}}
    json.dump(meta, open(os.path.join(out_dir, "overlay.json"), "w"), indent=1)
    return os.path.join(out_dir, "overlay.ffconcat"), meta


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("captions"); ap.add_argument("out_dir")
    ap.add_argument("--font"); ap.add_argument("--audio"); ap.add_argument("--emphasis"); ap.add_argument("--big")
    ap.add_argument("--size", type=int, default=62); ap.add_argument("--y", type=float, default=0.55)
    ap.add_argument("--gold", default="E2B05A"); ap.add_argument("--width", type=int, default=1080)
    ap.add_argument("--height", type=int, default=1920); ap.add_argument("--max-seconds", type=float)
    if len(sys.argv) == 1:
        ap.print_help(); sys.exit(1)
    a = ap.parse_args()
    p, meta = build(a.captions, a.out_dir, a.font, a.size, a.y, a.gold, a.emphasis, a.big, a.width, a.height, a.max_seconds, a.audio)
    print(f"{meta['chunks']} phrases, roles {meta['roles']} -> {p}")


if __name__ == "__main__":
    main()
