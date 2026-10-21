---
name: video-2-rough-cut
description: Build the edit decision list for a Talent Social video from the brief, and at the agent tier cut silences and assemble the rough cut. Use after the brief is approved.
---

# 2. rough-cut

Read `../IDENTITY.md` first, then the format page named in the brief.

## Input
- The approved brief (`../templates/brief.md`).
- The transcript with times (chat) or the footage (agent).

## Steps
1. **[chat] Build the EDL.** One row per kept segment, in the order they play: `start,end,reason`, in seconds of the source (`../templates/edl.csv`). Follow the format's beat table. The first spoken line is first: it starts at 0 to 0.3 s of the cut. Reasons are short: `hook`, `context`, `point 1`.
2. **[chat] List silences and fillers to remove.** From the transcript times: gaps over 0.4 s, and filler words ("um", "uh", false starts, repeats). Split the EDL rows around them. Keep a deliberate beat (a laugh, a pause for effect) and mark it in the brief.
3. **[chat] Convert source time to output time.** Add up the kept lengths. Write both times in the brief's beat table and overlay list. Overlays use output time.
4. **[chat] Mark the sting.** A 1 to 1.5 s gap right after the first line. The sting is added later; leave a marker row in the brief, not in the EDL.
5. **[chat] Plan the picture changes.** Episodes: a punch-in, card, wipe or cutaway at least every 5 s, ideally every 3 to 5 s. Teasers: every 1 to 2 s. List the punch-in times in the brief. Punch-ins are 10 to 15%.
6. **[chat] Check the series card.** No title card before the first line. The series name is a small bug (see the format page).
7. **[agent] Cut the silences.** Run `$STT_PYTHON tools/cut_silence.py <in.mp4> <out.mp4> --min-silence 0.4 --pad 0.08 --threshold -35 --edl edl.csv`. It writes the kept segments as `edl.csv`. Compare it with the chat EDL. Keep the chat EDL where they differ on structure.
8. **[agent] Assemble the cut.** Apply the final EDL with ffmpeg directly (trim and join the kept segments; export 1080x1920, 30 fps, H.264, AAC). No v1 tool applies a hand-edited EDL. Do not add overlays: a person builds them (skill 4).
9. **[chat] Check the runtime.** After cuts, add up the length. If outside the format's range, cut a whole beat or loosen the cuts. Never speed up speech.

## Output
- `edl.csv` (chat and agent).
- The brief with output times filled in and the picture-change list.
- A rough cut file (agent).

## Checks
- Runtime inside the format's range.
- The hook line plays within the first 2 s; target 0 to 0.3 s.
- No black or logo first frame.
- No silence over 0.4 s left, except marked beats.
- No cut removes a word that a caption or claim depends on.
- Each episode point still ends with its action.

## Use in another tool
Paste `IDENTITY.md`, this file, the brief and the transcript. Ask for the EDL and the output-time table. Cut in CapCut or Canva from it.
