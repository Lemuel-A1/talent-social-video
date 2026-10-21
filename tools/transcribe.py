#!/usr/bin/env python3
"""transcribe.py - speech to text with word timings, using faster-whisper.

Usage: transcribe.py <video> <out_dir> [--model small.en]

Writes out_dir/transcript.json (words with start, end), transcript.txt (segments with times)
and captions.srt (short caption chunks). Run it with $STT_PYTHON (needs faster-whisper, numpy).
"""
import argparse, json, os, subprocess, sys

try:
    import numpy as np
    from faster_whisper import WhisperModel
except ImportError as e:
    sys.exit(f"transcribe.py: missing Python package ({e.name}). Run it with $STT_PYTHON, "
             "a python that has faster-whisper and numpy. See tools/README.md.")


def load_audio(path):
    """Decode any media file to 16 kHz mono float32 with ffmpeg."""
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-vn", "-ac", "1",
           "-ar", "16000", "-f", "f32le", "-"]
    try:
        r = subprocess.run(cmd, capture_output=True)
    except FileNotFoundError:
        sys.exit("transcribe.py: ffmpeg not found. Install it (brew install ffmpeg).")
    if r.returncode or not r.stdout:
        sys.exit("transcribe.py: ffmpeg could not decode audio from this file.\n" + r.stderr.decode()[-500:])
    return np.frombuffer(r.stdout, dtype=np.float32)


def stamp(t, comma=True):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{',' if comma else '.'}{ms:03d}"


def caption_chunks(words, max_words=5, gap=0.35):
    """Group words into short caption chunks. Break at sentence ends, long pauses or max_words."""
    chunks, cur = [], []
    for w in words:
        if cur and (w["start"] - cur[-1]["end"] > gap or len(cur) >= max_words):
            chunks.append(cur); cur = []
        cur.append(w)
        if w["word"].rstrip().endswith((".", "?", "!")) or (len(cur) >= 3 and w["word"].endswith((",", ";", ":"))):
            chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    return chunks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video"); ap.add_argument("out_dir")
    ap.add_argument("--model", default="small.en")
    if len(sys.argv) == 1:
        ap.print_help(); sys.exit(1)
    a = ap.parse_args()
    if not os.path.isfile(a.video):
        sys.exit(f"transcribe.py: file not found: {a.video}")
    os.makedirs(a.out_dir, exist_ok=True)

    audio = load_audio(a.video)
    model = WhisperModel(a.model, device="cpu", compute_type="int8")
    segs, _ = model.transcribe(audio, word_timestamps=True, vad_filter=True, beam_size=5,
                               condition_on_previous_text=False)
    words, lines = [], []
    for seg in segs:
        lines.append(f"[{stamp(seg.start, False)[:-4]} - {stamp(seg.end, False)[:-4]}] {seg.text.strip()}")
        for w in seg.words or []:
            txt = w.word.strip()
            if not txt:
                continue
            if words and txt[0] in ",.;:!?%":     # Whisper sometimes splits "10,000" into "10" and ",000"
                words[-1]["word"] += txt; words[-1]["end"] = round(w.end, 3)
            else:
                words.append({"word": txt, "start": round(w.start, 3), "end": round(w.end, 3)})

    with open(os.path.join(a.out_dir, "transcript.json"), "w") as f:
        json.dump({"model": a.model, "duration": round(len(audio) / 16000, 2), "words": words}, f, indent=1)
    with open(os.path.join(a.out_dir, "transcript.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(a.out_dir, "captions.srt"), "w") as f:
        for i, ch in enumerate(caption_chunks(words), 1):
            f.write(f"{i}\n{stamp(ch[0]['start'])} --> {stamp(ch[-1]['end'])}\n{' '.join(w['word'] for w in ch)}\n\n")
    print(f"{len(words)} words, {len(lines)} segments -> {a.out_dir}")


if __name__ == "__main__":
    main()
