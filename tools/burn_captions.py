#!/usr/bin/env python3
"""burn_captions.py - burn captions into a video (Pillow overlay + ffmpeg overlay filter).

Usage: burn_captions.py <in.mp4> <captions.srt|transcript.json> <out.mp4> --font <ttf>
         [--size 64] [--y 0.62] [--gold F5B533] [--emphasis words.txt]
         [--max-seconds S] [--keep-overlay DIR]

Draws caption PNGs with captions_to_overlay.py, then composites them over the video.
Audio is copied unchanged. --max-seconds renders only the first S seconds (for tests).
Temporary PNGs go in <out>_overlay/ next to the output and are removed unless --keep-overlay is given.
"""
import argparse, json, os, shutil, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import captions_to_overlay as cto


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"burn_captions.py: '{cmd[0]}' not found. Install ffmpeg (brew install ffmpeg).")


def probe(path):
    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
             "stream=width,height,r_frame_rate:format=duration", "-of", "json", path])
    if r.returncode:
        sys.exit("burn_captions.py: ffprobe could not read the video.\n" + r.stderr[-400:])
    d = json.loads(r.stdout)
    s = d["streams"][0]
    n, den = s["r_frame_rate"].split("/")
    return s["width"], s["height"], float(n) / float(den), float(d["format"]["duration"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video"); ap.add_argument("captions"); ap.add_argument("output")
    ap.add_argument("--font", required=True)
    ap.add_argument("--size", type=int, default=64)
    ap.add_argument("--y", type=float, default=0.62)
    ap.add_argument("--gold", default="F5B533")
    ap.add_argument("--emphasis")
    ap.add_argument("--max-seconds", type=float)
    ap.add_argument("--keep-overlay")
    if len(sys.argv) == 1:
        ap.print_help(); sys.exit(1)
    a = ap.parse_args()
    if not os.path.isfile(a.video):
        sys.exit(f"burn_captions.py: file not found: {a.video}")
    if os.path.abspath(a.video) == os.path.abspath(a.output):
        sys.exit("burn_captions.py: output must be a different file from the input.")

    w, h, fps, dur = probe(a.video)
    if a.max_seconds:
        dur = min(dur, a.max_seconds)
    work = a.keep_overlay or os.path.splitext(a.output)[0] + "_overlay"
    concat, meta = cto.build(a.captions, work, a.font, a.size, a.y, a.gold, a.emphasis, w, h, a.max_seconds)

    graph = (f"[1:v]fps={fps:.3f},format=rgba[ov];"
             f"[0:v][ov]overlay={meta['x']}:{meta['y']}:eof_action=pass:format=auto,format=yuv420p[v]")
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", a.video,
           "-f", "concat", "-safe", "0", "-i", concat, "-filter_complex", graph,
           "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
           "-c:a", "copy", "-movflags", "+faststart", "-t", f"{dur:.3f}", a.output]
    r = run(cmd)
    try:
        if r.returncode:
            sys.exit("burn_captions.py: ffmpeg failed:\n" + r.stderr[-800:])
    finally:
        if not a.keep_overlay:
            shutil.rmtree(work, ignore_errors=True)

    out_dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", a.output]).stdout.strip() or 0)
    print(f"{meta['chunks']} chunks, {meta['chunks_with_gold']} with a gold word")
    print(f"{os.path.abspath(a.output)}  ({out_dur:.2f} s)")


if __name__ == "__main__":
    main()
