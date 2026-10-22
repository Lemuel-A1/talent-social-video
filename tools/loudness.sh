#!/bin/bash
# loudness.sh - two-pass loudness master to -14 LUFS with a safe true peak.
#
# Usage: loudness.sh <in.mp4> <out.mp4> [LUFS=-14]
#
# Pass 1 measures, pass 2 applies a linear gain. The true-peak target is -2 dBTP so the AAC
# output stays at or under -1.5 dBFS. Video is copied untouched. Needs ffmpeg only.
set -euo pipefail

if [ $# -lt 2 ]; then
  sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'; exit 1
fi
command -v ffmpeg >/dev/null || { echo "loudness.sh: ffmpeg not found. Install it (brew install ffmpeg)." >&2; exit 1; }

IN="$1"; OUT="$2"; TARGET="${3:--14}"
[ -f "$IN" ] || { echo "loudness.sh: file not found: $IN" >&2; exit 1; }
[ "$(cd "$(dirname "$IN")" && pwd)/$(basename "$IN")" != "$(cd "$(dirname "$OUT")" && pwd)/$(basename "$OUT")" ] \
  || { echo "loudness.sh: output must differ from input." >&2; exit 1; }

# read "I", "TP" from ebur128's summary
measure() {
  ffmpeg -hide_banner -nostats -i "$1" -vn -af ebur128=peak=true -f null - 2>&1 \
    | awk '/Summary:/{s=1} s&&/ I: /{i=$2} s&&/ Peak: /{p=$2} END{print i, p}'
}

read -r BI BTP < <(measure "$IN")
echo "before: ${BI} LUFS, true peak ${BTP} dBFS"

# pass 1: loudnorm analysis (JSON block at the end of stderr)
J=$(ffmpeg -hide_banner -nostats -i "$IN" -vn -af "loudnorm=I=${TARGET}:TP=-2.2:LRA=11:print_format=json" -f null - 2>&1)
val() { printf '%s\n' "$J" | grep "\"$1\"" | tail -1 | sed -E 's/.*: "([^"]*)".*/\1/'; }
MI=$(val input_i); MTP=$(val input_tp); MLRA=$(val input_lra); MTH=$(val input_thresh); MOFF=$(val target_offset)
[ -n "$MI" ] && [ -n "$MOFF" ] || { echo "loudness.sh: could not read loudnorm measurements." >&2; exit 1; }

# pass 2: apply (linear gain; resampled back to 48 kHz because loudnorm upsamples)
ffmpeg -hide_banner -loglevel error -y -i "$IN" -map 0:v? -map 0:a:0 -c:v copy \
  -af "loudnorm=I=${TARGET}:TP=-2.2:LRA=11:measured_I=${MI}:measured_TP=${MTP}:measured_LRA=${MLRA}:measured_thresh=${MTH}:offset=${MOFF}:linear=true:print_format=summary,aresample=48000" \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$OUT"

read -r AI ATP < <(measure "$OUT")

# Fallback: if the clip's peaks are too high for a clean linear gain, loudnorm quietly gives up
# and lands short of the target. Then apply plain gain through a limiter, and trim once more.
needs_retry() { awk -v i="$AI" -v t="$TARGET" -v tp="$ATP" 'BEGIN{ d=i-t; if (d<0) d=-d; exit !(d>0.5 || tp>-1.5) }'; }
if needs_retry; then
  echo "linear pass landed at ${AI} LUFS / ${ATP} dBFS; retrying with a limiter."
  GAIN=$(awk -v t="$TARGET" -v b="$BI" 'BEGIN{printf "%.2f", t-b}')
  for attempt in 1 2 3; do
    ffmpeg -hide_banner -loglevel error -y -i "$IN" -map 0:v? -map 0:a:0 -c:v copy \
      -af "volume=${GAIN}dB,alimiter=limit=0.794:attack=5:release=60:level=false,aresample=48000" \
      -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$OUT"
    read -r AI ATP < <(measure "$OUT")
    [ "$attempt" -lt 3 ] && GAIN=$(awk -v g="$GAIN" -v t="$TARGET" -v i="$AI" 'BEGIN{printf "%.2f", g+(t-i)}')
  done
fi

echo "after:  ${AI} LUFS, true peak ${ATP} dBFS  -> $OUT"
awk -v tp="$ATP" 'BEGIN{ if (tp+0 > -1.5) print "warning: true peak is above -1.5 dBFS; lower the LUFS target (for example -15) and run again." }'
