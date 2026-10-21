# Video tools

Seven small tools for the agent tier (Claude Code or Codex with the repo cloned). They use ffmpeg, ffprobe, Python 3.12, Pillow, numpy and faster-whisper. Nothing here uses the network, except Whisper downloading its model the first time. Every tool prints its usage when run with no arguments, writes only where you tell it, and never deletes your input.

## Set up

**ffmpeg.** This machine's ffmpeg has no `subtitles`, `ass` or `drawtext` filter. So captions are not burned from a subtitle file. They are drawn as transparent PNGs with Pillow, assembled into one overlay clip, and laid on the video with the `overlay` filter. That is what `captions_to_overlay.py` and `burn_captions.py` do.

**STT_PYTHON.** `transcribe.py` needs faster-whisper and numpy. Make a venv once and point `STT_PYTHON` at its python (the lane's CONFIG records the path):

```
python3 -m venv ~/.local/share/vetted-video/stt
~/.local/share/vetted-video/stt/bin/pip install faster-whisper numpy pillow
export STT_PYTHON=~/.local/share/vetted-video/stt/bin/python
```

Every Python tool below can run under `$STT_PYTHON`. Only `transcribe.py` needs it; the rest work with any python3 that has Pillow (`measure.py` and `cut_silence.py` need no Pillow at all, apart from one optional check).

**Poppins.** The headline font is Poppins ExtraBold (open licence). Download it from Google Fonts (fonts.google.com/specimen/Poppins), unzip, and pass the file as `--font`, for example `~/Fonts/Poppins-ExtraBold.ttf`. Keep it outside the repo. For a quick test any bold TTF works, for example `/System/Library/Fonts/Supplemental/Arial Black.ttf`.

## The tools

**transcribe.py** - speech to text with word times. Writes `transcript.json`, `transcript.txt` and `captions.srt` (short caption chunks).
```
$STT_PYTHON transcribe.py episode.mp4 work/ --model small.en
```

**cut_silence.py** - cuts dead air and writes the kept segments as an EDL (`start,end,reason`). If there is nothing to cut it says so and copies the video.
```
python3 cut_silence.py raw.mp4 cut.mp4 --min-silence 0.4 --pad 0.08 --threshold -35 --edl edl.csv
```

**captions_to_overlay.py** - draws one transparent PNG per caption chunk plus `overlay.ffconcat` and `overlay.json`. White text, thin charcoal edge, soft shadow, 2 to 5 words, centred at `--y` (0.62 of the height), at most one gold word per chunk. The gold word comes from `--emphasis` (one word per line), otherwise a number word such as "hundred" or any digit word.
```
$STT_PYTHON captions_to_overlay.py work/transcript.json work/overlay --font ~/Fonts/Poppins-ExtraBold.ttf --emphasis words.txt
```

**burn_captions.py** - runs the step above and composites the result onto the video. Audio is copied. `--max-seconds` renders only the start, for tests.
```
$STT_PYTHON burn_captions.py cut.mp4 work/transcript.json captioned.mp4 --font ~/Fonts/Poppins-ExtraBold.ttf
```
Captions go into the whole video, so use a clean version. If the footage already has captions burned in, they will double up.

**loudness.sh** - two-pass loudness master to -14 LUFS (second argument changes it), true peak target -2 so the AAC file ends at or under -1.5 dBFS. Prints the before and after numbers. If a clean linear pass cannot get there, it retries with a limiter.
```
./loudness.sh captioned.mp4 master.mp4 -14
```

**measure.py** - QC numbers and a verdict. Checks loudness (-15 to -13 LUFS), true peak (-1 dBFS or lower), first sound within 2 s (advice and game), first frame not black, no black segments, and runtime for the format. Silences, freezes and cuts per minute are reported but not scored; the cut count undercounts punch-ins. `--json` for machine output. Exit code is 0 either way; read the verdict line.
```
python3 measure.py master.mp4 --format advice
```

**contact_sheet.py** - timestamped frames on one JPG. Default spacing is max(2.5, length/36) seconds; 8 columns for vertical video.
```
python3 contact_sheet.py master.mp4 sheet.jpg --every 2.5
```

## Typical order

`transcribe` then `cut_silence` (re-run `transcribe` on the cut file) then `burn_captions` then `loudness.sh` then `measure.py` and `contact_sheet.py`. Animated overlays (ledger, progress tabs, sting, punch-ins) are not automated in v1; build them in CapCut or Canva from the format page.

## Known limits

- `cut_silence.py` removes silence only. It does not cut filler words ("um", "you know"); do that by hand using the transcript.
- `measure.py` cannot see a logo in the first frame; it only checks that the frame is not near black. Check the contact sheet.
- Caption timing comes from Whisper word times. Read the captions once for misheard names before posting.
