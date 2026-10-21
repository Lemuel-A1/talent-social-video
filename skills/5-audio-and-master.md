---
name: video-5-audio-and-master
description: Plan the sound for a Talent Social video (sting, whooshes, music) and master it to -14 LUFS with true peak at or below -1 dBFS. Use after the overlays are built.
---

# 5. audio-and-master

Read `../IDENTITY.md` first (section 8) and the format page's Sound section.

## Input
- The branded cut (overlays built by the person).
- The sting file name from `CONFIG.md`.
- Music plan: added in the platform, a licensed file, or none.

## Steps
1. **[chat] Write the sound plan.** List: the sting at its output time; whooshes on section changes only; any hits (teaser); where music comes in. Music sits 15 to 20 dB under the voice. No lyrics under speech.
2. **[chat] Decide the music route.** Default: add music inside the platform at upload, so the platform keeps the licence. Also export a clean voice-only master. For LinkedIn and WhatsApp, a music version only if the track is licensed and the licence is recorded in the brief.
3. **[chat] Hand the sound edit to the person.** In CapCut or Canva they level the voice, reduce room noise, place the sting sound and whooshes, and export H.264 at 1080x1920, 30 fps, with AAC audio (`../CONFIG.md`). In chat, loudness cannot be measured: mark it UNMEASURED in the brief.
4. **[agent] Master the loudness.** Run `sh tools/loudness.sh <in.mp4> <out.mp4> -14`. It runs two passes, targets -14 LUFS and true peak -2 so the AAC output stays at or under -1.5 dBFS, and prints the measured I and TP of the output. Use the output as the voice-only master.
5. **[chat] Name the files.** `{format}-{episode}-{platform}-{voice-or-music}.mp4`, for example `advice-ep03-ig-voice.mp4`. Platform codes: `ig`, `tt`, `li`, `wa`.
6. **[chat] Record licences.** Music title, source and licence for every track in a file. Sting sound source and licence. Font licence (Poppins, OFL). Blank means not cleared.

## Output
- Final files named as above, including a voice-only master.
- The measured loudness and true peak printed by the tool (agent), or UNMEASURED (chat).
- A licence note in the brief.

## Checks
- Integrated loudness -14 LUFS; accept -15 to -13.
- True peak at or below -1 dBFS.
- Voice-only master exists.
- No music in a file without a recorded licence.
- No silent tail: the last spoken word or sound ends within about 0.5 s of the end.

## Use in another tool
Paste `IDENTITY.md`, this file and the brief. Ask for the sound plan and the file names. Measure with the agent tier or ask the person to run the agent tier before posting.
