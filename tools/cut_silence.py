#!/usr/bin/env python3
"""cut_silence.py - remove silent stretches from a video and write the kept segments as an EDL.

Usage: cut_silence.py <in.mp4> <out.mp4> [--min-silence 0.4] [--pad 0.08] [--threshold -35] [--edl out.csv]

A silence is any quiet stretch (below --threshold dB) at least --min-silence seconds long.
--pad seconds of that silence are kept on each side so speech is not clipped.
The EDL has columns start,end,reason (one row per kept segment). Needs ffmpeg and ffprobe only.
"""
import argparse, csv, os, re, subprocess, sys, tempfile


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"cut_silence.py: '{cmd[0]}' not found. Install ffmpeg (brew install ffmpeg).")


def duration_of(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path])
    try:
        return float(r.stdout.strip())
    except ValueError:
        sys.exit("cut_silence.py: could not read the video duration.")


def find_silences(path, threshold, min_silence, total):
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af",
             f"silencedetect=n={threshold}dB:d={min_silence}", "-f", "null", "-"])
    starts = [max(float(x), 0.0) for x in re.findall(r"silence_start: (-?[\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: (-?[\d.]+)", r.stderr)]
    out = []
    for i, s in enumerate(starts):
        out.append((s, ends[i] if i < len(ends) else total))   # silence running to the end of the file
    return out


def kept_segments(silences, pad, total):
    """Turn silences into the segments to keep, leaving `pad` seconds of silence on each side."""
    cuts = []
    for s, e in silences:
        cs = s + pad if s > 0.01 else 0.0           # silence at the very start: cut from 0
        ce = e - pad if e < total - 0.01 else total  # silence at the very end: cut to the end
        if ce - cs > 0.05:
            cuts.append((cs, ce))
    kept, pos = [], 0.0
    for cs, ce in cuts:
        if cs - pos > 0.05:
            kept.append((pos, cs))
        pos = max(pos, ce)
    if total - pos > 0.05:
        kept.append((pos, total))
    return kept, cuts


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input"); ap.add_argument("output")
    ap.add_argument("--min-silence", type=float, default=0.4)
    ap.add_argument("--pad", type=float, default=0.08)
    ap.add_argument("--threshold", type=float, default=-35)
    ap.add_argument("--edl")
    if len(sys.argv) == 1:
        ap.print_help(); sys.exit(1)
    a = ap.parse_args()
    if not os.path.isfile(a.input):
        sys.exit(f"cut_silence.py: file not found: {a.input}")
    if os.path.abspath(a.input) == os.path.abspath(a.output):
        sys.exit("cut_silence.py: output must be a different file from the input.")

    total = duration_of(a.input)
    silences = find_silences(a.input, a.threshold, a.min_silence, total)
    kept, cuts = kept_segments(silences, a.pad, total)
    removed = sum(ce - cs for cs, ce in cuts)
    edl = a.edl or os.path.splitext(a.output)[0] + "_edl.csv"

    with open(edl, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["start", "end", "reason"])
        for s, e in kept:
            w.writerow([f"{s:.3f}", f"{e:.3f}", "speech"])

    if not cuts:
        # Nothing to remove: copy the streams untouched so the output still exists.
        r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", a.input, "-c", "copy", a.output])
    else:
        parts = []
        for i, (s, e) in enumerate(kept):
            parts.append(f"[0:v]trim={s:.3f}:{e:.3f},setpts=PTS-STARTPTS[v{i}];"
                         f"[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS[a{i}];")
        joined = "".join(f"[v{i}][a{i}]" for i in range(len(kept)))
        graph = "".join(parts) + f"{joined}concat=n={len(kept)}:v=1:a=1[v][a]"
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as g:
            g.write(graph); gpath = g.name
        try:
            tail = ["-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.output]
            base = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", a.input]
            # ffmpeg 7+ reads a filter file with -/filter_complex; older builds use -filter_complex_script.
            r = run(base + ["-/filter_complex", gpath] + tail)
            if r.returncode and "Unrecognized option" in r.stderr:
                r = run(base + ["-filter_complex_script", gpath] + tail)
        finally:
            os.unlink(gpath)
    if r.returncode:
        sys.exit("cut_silence.py: ffmpeg failed:\n" + r.stderr[-600:])

    print(f"silences found: {len(silences)} | segments kept: {len(kept)}")
    print(f"removed {removed:.2f} s of {total:.2f} s -> {total - removed:.2f} s")
    if removed < 0.5:
        print("note: almost nothing was removed; this footage has little dead air at these settings.")
    print(f"video: {a.output}\nEDL:   {edl}")


if __name__ == "__main__":
    main()
