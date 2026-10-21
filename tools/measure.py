#!/usr/bin/env python3
"""measure.py - QC numbers for a finished video. Needs ffmpeg and ffprobe; Pillow for the first-frame check.

Usage: measure.py <video> [--format advice|game|teaser] [--json]
"""
import argparse, json, re, subprocess, sys, tempfile, os

LUFS_TARGET, LUFS_TOL = -14.0, 1.0      # accept -15 to -13
TP_MAX = -1.0                            # dBFS
FIRST_SOUND_MAX = 2.0                    # seconds, voice formats only
RUNTIME = {"advice": (45, 75), "game": (60, 90), "teaser": (12, 25)}
SILENCE_MIN, SILENCE_DB = 0.4, -35


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"measure.py: '{cmd[0]}' not found. Install ffmpeg (brew install ffmpeg).")


def probe(path):
    r = run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", path])
    if r.returncode:
        sys.exit(f"measure.py: ffprobe could not read {path}\n{r.stderr.strip()}")
    info = json.loads(r.stdout)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    if not v:
        sys.exit("measure.py: no video stream found.")
    num, den = (v.get("avg_frame_rate") or "0/1").split("/")
    fps = float(num) / float(den) if float(den) else 0.0
    return {"duration": float(info["format"]["duration"]), "fps": round(fps, 2),
            "width": v["width"], "height": v["height"], "has_audio": a is not None}


def analyse(path, has_audio):
    """One ffmpeg pass: loudness, silences, black, freezes, scene cuts."""
    vf = "scale=320:-2,blackdetect=d=0.1:pic_th=0.98:pix_th=0.10,freezedetect=n=-60dB:d=1,scdet=t=10"
    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-map", "0:v:0", "-vf", vf]
    if has_audio:
        cmd += ["-map", "0:a:0", "-af", f"ebur128=peak=true,silencedetect=n={SILENCE_DB}dB:d={SILENCE_MIN}"]
    cmd += ["-f", "null", "-"]
    r = run(cmd)
    if r.returncode:
        sys.exit("measure.py: ffmpeg analysis failed:\n" + r.stderr[-800:])
    log = r.stderr
    out = {}
    # Final summary block of ebur128 (the last occurrence of each value)
    summary = log[log.rfind("Summary:"):] if "Summary:" in log else ""
    def grab(pat):
        m = re.search(pat, summary)
        return float(m.group(1)) if m else None
    out["lufs"] = grab(r"I:\s+(-?[\d.]+) LUFS")
    out["lra"] = grab(r"LRA:\s+(-?[\d.]+) LU")
    out["true_peak"] = grab(r"Peak:\s+(-?[\d.]+) dBFS")
    # silences
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", log)]
    ends = [(float(a), float(b)) for a, b in re.findall(r"silence_end: (-?[\d.]+) \| silence_duration: ([\d.]+)", log)]
    sil = []
    for i, s in enumerate(starts):
        e = ends[i][0] if i < len(ends) else None
        sil.append({"start": max(s, 0.0), "end": e})
    out["silences"] = sil
    out["black"] = [{"start": float(a), "end": float(b)} for a, b in
                    re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", log)]
    fs = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", log)]
    fd = [float(x) for x in re.findall(r"freeze_duration: ([\d.]+)", log)]
    out["freezes"] = [{"start": s, "duration": (fd[i] if i < len(fd) else None)} for i, s in enumerate(fs)]
    out["cuts"] = len(re.findall(r"lavfi\.scd\.time", log))
    return out


def first_frame_luma(path):
    """Average brightness (0-255) of the first frame, or None if Pillow is missing."""
    try:
        from PIL import Image, ImageStat
    except ImportError:
        return None
    with tempfile.TemporaryDirectory() as d:
        png = os.path.join(d, "f.png")
        r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-frames:v", "1", "-vf", "scale=160:-2", png])
        if r.returncode or not os.path.exists(png):
            return None
        return ImageStat.Stat(Image.open(png).convert("L")).mean[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--format", choices=list(RUNTIME))
    ap.add_argument("--json", action="store_true")
    if len(sys.argv) == 1:
        ap.print_help(); sys.exit(1)
    args = ap.parse_args()
    if not os.path.isfile(args.video):
        sys.exit(f"measure.py: file not found: {args.video}")

    p = probe(args.video)
    a = analyse(args.video, p["has_audio"])
    luma = first_frame_luma(args.video)
    minutes = p["duration"] / 60.0

    # first sound: if the audio starts in silence, speech/sound begins when that silence ends
    first_sound = 0.0
    if a["silences"] and a["silences"][0]["start"] <= 0.05:
        first_sound = a["silences"][0]["end"] if a["silences"][0]["end"] is not None else p["duration"]

    checks = []   # (name, status, detail)
    def add(name, ok, detail):
        checks.append({"check": name, "status": "PASS" if ok else "FIX", "detail": detail})

    if not p["has_audio"]:
        add("loudness", False, "no audio stream")
    else:
        add("loudness", a["lufs"] is not None and abs(a["lufs"] - LUFS_TARGET) <= LUFS_TOL,
            f"{a['lufs']} LUFS (accept -15 to -13)")
        add("true peak", a["true_peak"] is not None and a["true_peak"] <= TP_MAX,
            f"{a['true_peak']} dBFS (max {TP_MAX})")
        if args.format in ("advice", "game"):
            add("first sound within 2 s", first_sound <= FIRST_SOUND_MAX, f"first sound at {first_sound:.2f} s")
    w, h = p.get("width"), p.get("height")
    if w and h:
        add("size 1080x1920 (9:16)", (w, h) == (1080, 1920), f"{w}x{h}" + (" (vertical, scale to 1080x1920 at export)" if w * 16 == h * 9 and (w, h) != (1080, 1920) else ""))
    if p.get("fps"):
        add("frame rate 30 fps", abs(p["fps"] - 30) < 0.5, f"{p['fps']:.2f} fps")
    if luma is None:
        add("first frame not black", True, "skipped (Pillow missing)")
    else:
        add("first frame not black", luma > 12, f"average brightness {luma:.0f}/255")
    long_black = [b for b in a["black"] if b["end"] - b["start"] >= 0.3]
    add("no black segments", not long_black,
        "none" if not long_black else ", ".join(f"{b['start']:.1f}-{b['end']:.1f}s" for b in long_black))
    if args.format:
        lo, hi = RUNTIME[args.format]
        add(f"runtime {lo}-{hi} s ({args.format})", lo <= p["duration"] <= hi, f"{p['duration']:.1f} s")

    verdict = "READY" if all(c["status"] == "PASS" for c in checks) else "FIX"
    result = {
        "file": args.video, "duration_s": round(p["duration"], 2), "fps": p["fps"],
        "size": f"{p['width']}x{p['height']}",
        "lufs": a["lufs"], "lra": a["lra"], "true_peak_dbfs": a["true_peak"],
        "silences_over_0_4s": len(a["silences"]),
        "cuts_detected": a["cuts"], "cuts_per_min": round(a["cuts"] / minutes, 1) if minutes else None,
        "first_sound_s": round(first_sound, 2), "first_frame_brightness": None if luma is None else round(luma),
        "black_segments": a["black"], "freeze_segments": a["freezes"],
        "checks": checks, "verdict": verdict,
        "notes": ["cut count undercounts punch-ins and zooms", "silences and freezes are reported, not scored"],
    }
    if args.json:
        print(json.dumps(result, indent=2)); return
    print(f"{args.video}")
    print(f"  duration {result['duration_s']} s | {result['fps']} fps | {result['size']}")
    print(f"  loudness {a['lufs']} LUFS | LRA {a['lra']} | true peak {a['true_peak']} dBFS")
    print(f"  silences over 0.4 s: {len(a['silences'])} | cuts: {a['cuts']} ({result['cuts_per_min']}/min, undercounts punch-ins)")
    _long=[b for b in a['black'] if b['end']-b['start']>=0.3]
    print(f"  black segments: {len(_long)} of 0.3 s or more ({len(a['black'])-len(_long)} shorter flashes ignored) | freeze segments: {len(a['freezes'])}")
    for c in checks:
        print(f"  [{c['status']}] {c['check']}: {c['detail']}")
    print(f"VERDICT: {verdict}")


if __name__ == "__main__":
    main()
