---
name: video-0-shoot-plan
description: Plan a shoot day so the footage is editable at volume and quality, with formats, timed blocks, crew, audio, consent and file names. Use before every event or filming day.
---

# 0. shoot-plan

Read `../IDENTITY.md` first. Formats: the three pages in `../formats/`, plus `../formats/quick-formats.md` and `../formats/founder-story.md`.

## Input
- The event or day, date and venue.
- Rooms available, with a rough sense of noise and light.
- Crew and kit: who, which cameras and phones, mics, lights, stands, storage.
- People available to film, and for how long.
- Formats wanted, if any.
- Output target: how many finished videos, by when.

## Steps
1. **[chat] Choose formats and how many of each.** Match the people and time to the formats. Start from the target number and work back: allow for clips that fail. Say the count per format.
2. **[chat] Book blocks by room and time.**
   - To-camera episodes: the quiet room.
   - Games: a two-shot set.
   - Guest stories: a portrait corner.
   - Behind the scenes: a roaming camera.
   - The event itself: the main room.
   Leave a buffer between blocks and a reset after each.
3. **[chat] Write the prompt list for each block** from the format page or the quick-formats bank (IDs such as RG-J01). Fifteen words or fewer per prompt. Speakers say their own lines.
4. **[chat] Assign crew roles:** camera A, camera B or phone, audio, producer (holds the shot list and times each block), consent desk.
5. **[chat] Set the audio rules.** A lav mic on every speaker. 30 seconds of room tone in every room. Quiet room first: a good mic in a quiet room beats a better camera.
6. **[chat] Set the consent plan.** A visible sign at the entrance and at each set. A quick release by QR code at the consent desk. Film only people who agreed. Public figures are the exception. The consent desk keeps the list of who said yes; no list, no clip.
7. **[chat] Set file naming and hand-off.** `YYYYMMDD_EVENT_CAM_FORMAT_SUBJECT_TAKE`, for example `20261114_EVENT_A_ADVICE_SPEAKER1_T02`. One folder per format. Upload the same night to the shared drive in `../CONFIG.md`. Never keep media in this repo.
8. **[agent] Check the folders.** List each folder, flag any file name that breaks the pattern, and count clips per format against the plan.
9. **[chat] Hand off.** Run skill 1 once per format folder, starting with the format that has the most clips.

## Output
A shoot plan on `../templates/shoot-plan.md`, with the target number of finished videos by format.

## Checks
- Every block has a format, prompts, a mic plan and a consent plan.
- The day adds up to the target number of finished videos, by format.
- Nobody is filmed without consent. Public figures are the exception.
- Every file name follows the pattern; every folder is one format.
- Nothing in the plan promises who will be in the room.

## Use in another tool
Paste `IDENTITY.md`, then this file, then the list of formats, then what you have (venue, crew, kit, people, target). Ask for the shoot plan.
