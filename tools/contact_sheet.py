#!/usr/bin/env python3
"""contact_sheet.py - timestamped frames on one image, for a quick visual check.

Usage: contact_sheet.py <video> <out.jpg> [--every S]

Default spacing is max(2.5, length/36) seconds. Vertical video gets 8 columns, other shapes 5.
Needs ffmpeg and ffprobe, plus Pillow.
"""
import argparse, glob, json, os, subprocess, sys, tempfile

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("contact_sheet.py: Pillow is missing. Use $STT_PYTHON or `pip install pillow`.")


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"contact_sheet.py: '{cmd[0]}' not found. Install ffmpeg (brew install ffmpeg).")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video"); ap.add_argument("out")
    ap.add_argument("--every", type=float)
    if len(sys.argv) == 1:
        ap.print_help(); sys.exit(1)
    a = ap.parse_args()
    if not os.path.isfile(a.video):
        sys.exit(f"contact_sheet.py: file not found: {a.video}")

    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
             "stream=width,height:format=duration", "-of", "json", a.video])
    if r.returncode:
        sys.exit("contact_sheet.py: ffprobe could not read the video.")
    d = json.loads(r.stdout)
    w, h, dur = d["streams"][0]["width"], d["streams"][0]["height"], float(d["format"]["duration"])
    every = a.every or max(2.5, dur / 36)
    vertical = h > w
    cols = 8 if vertical else 5
    tw = 200 if vertical else 300
    th = int(tw * h / w)

    with tempfile.TemporaryDirectory() as tmp:
        times = []
        t = 0.0
        while t < dur - 0.05:
            times.append(t); t += every
        for i, t in enumerate(times):
            out = os.path.join(tmp, f"f{i:04d}.jpg")
            # -ss before -i seeks fast; one frame per timestamp
            run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", a.video,
                 "-frames:v", "1", "-vf", f"scale={tw}:{th}", "-q:v", "3", out])
        frames = sorted(glob.glob(os.path.join(tmp, "f*.jpg")))
        if not frames:
            sys.exit("contact_sheet.py: no frames could be extracted.")
        try:
            font = ImageFont.load_default(size=16)
        except TypeError:
            font = ImageFont.load_default()
        gap, label_h = 6, 22
        rows = -(-len(frames) // cols)
        sheet = Image.new("RGB", (cols * (tw + gap) + gap, rows * (th + label_h + gap) + gap), (24, 30, 42))
        draw = ImageDraw.Draw(sheet)
        for i, f in enumerate(frames):
            x = gap + (i % cols) * (tw + gap)
            y = gap + (i // cols) * (th + label_h + gap)
            sheet.paste(Image.open(f), (x, y + label_h))
            draw.text((x + 2, y + 2), f"{times[i]:.1f}s", font=font, fill=(245, 181, 51))
        sheet.save(a.out, quality=88)
    print(f"{len(frames)} frames every {every:.1f} s, {cols} columns -> {a.out}")


if __name__ == "__main__":
    main()
