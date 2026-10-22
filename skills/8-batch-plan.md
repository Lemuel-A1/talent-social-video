---
name: video-8-batch-plan
description: Plan the editing of a whole footage library (many files, several cameras, several events) before cutting anything: source map, posted check, yield table, sequence, consent register, review sheet. Use when someone says "edit everything", points at a folder, or asks what to make from a library.
---

# 8. batch-plan

Read `../IDENTITY.md` first. Skills 1 to 7 make one piece. This one decides which pieces to make, in what order, and for which goal.

## Input
- The folder or folders. A shot log if one exists.
- `CONFIG.md` and the growth hypothesis (which funnels video feeds).
- What is already posted: the accounts' reels pages, read-only, and any list of source files a previous editor used.

## Steps
1. **[agent] Source map.** For every file: camera, resolution, frame rate, whether it carries speech, duration, colour profile (read the metadata), and whether it opens. Unreadable files go on a re-copy list. Group by event.
2. **[agent] Sync check for every new camera.** Find one clear event (the end of a long turn). Compare picture and transcript. If they differ, record a `vshift` for the file and check again on the finished cut (L-2026-10-22-03).
3. **[agent] Transcribe every file with speech.** `tools/transcribe.py`. Keep word times. Names and key words are mishearings until a person confirms them by ear.
4. **[chat] Posted check.** List what is already out. Do not re-cut a posted piece unless the new cut is a different format.
5. **[chat] Compare with what already exists.** Read the previous editor's notes, not just their files: which formats, which footage, what the client rejected. List what is new here and what would repeat.
6. **[chat] Yield table.** One row per source: format, candidate count, publish count, funnel it feeds, playbook chapter, persona, stage. Counts are estimates until the briefs exist.
7. **[chat] Sequence.** By date first (events the pieces should feed), then by goal. Name accounts per `CONFIG.md`.
8. **[chat] Consent and claims register.** Who appears, consent source, names confirmed or not, claims to avoid.
9. **[chat] Brief the first batch with skill 1.** Up to 8 pieces, with at least two structures the previous work does not have.
10. **[agent] Build the batch with skills 2 to 5, QC with skill 6, and write one review sheet** (contact sheet, hook line, verdict buttons, funnel tag).

## Output
A plan document and a review sheet. Nothing is posted by this skill.

## Checks
- No piece duplicates a posted piece.
- Every piece names a playbook chapter, persona and stage, or is marked brand / fun.
- Every source with speech has a sync check on record.
- The first batch names the ideas the library has not been used for before.
