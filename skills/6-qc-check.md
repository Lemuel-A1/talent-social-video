---
name: video-6-qc-check
description: Check a finished Talent Social video against the identity thresholds, consent, claims and licences, and return READY, FIX or DO NOT POST. Use before every post.
---

# 6. qc-check

Read `../IDENTITY.md` first (section 12 is the checklist).

## Input
- The final file and its brief.
- Agent tier: the file itself. Chat tier: the contact sheet or screenshots the person uploads (frames at 0 s, 1 s, 2 s, the sting, the middle, the CTA card), plus the transcript.

## Steps
1. **[agent] Measure.** Run `$STT_PYTHON tools/measure.py <video> --format advice|game|teaser --json`. It reports duration, fps, size, loudness, true peak, silences over 0.4 s, cuts per minute (it undercounts punch-ins), first-frame black check, black or freeze segments, and runtime against the format range. It prints PASS or FIX per threshold and an overall READY or FIX.
2. **[agent] Make a contact sheet.** Run `$STT_PYTHON tools/contact_sheet.py <video> <sheet.jpg>` and look at it. Chat tier: the person makes the sheet with the agent tier or uploads screenshots.
3. **[chat] Check what the tool cannot.** From the frames and the transcript: first spoken line within 2 s; headline visible and readable; sting position; captions 2 to 5 words at 55 to 70% height; nothing in the top 220, bottom 380 or right 140 px; picture change spacing; CTA one, said and shown, held 3 s, above y 1540; overlay text matches speech.
4. **[chat] Check consent.** Every featured person who is not a public figure has a recorded OK. Event faces: only people who agreed.
5. **[chat] Check claims.** Every statement about Vetted is the approved line or cleared by Lemuel. No client logos or names as proof. No unsourced "#1". No forward promise about who will attend. Every number on screen has a source and matches what is said.
6. **[chat] Check licences.** Music, sting sound and font each recorded.
7. **[chat] Say what is unmeasured.** In chat, loudness, true peak, silences, size and fps cannot be measured. List them as UNMEASURED. In chat the best verdict is READY PENDING MEASURE: the person runs the agent tier (or the editor's own loudness meter) before posting.

## Output
```
VERDICT: READY | READY PENDING MEASURE (chat only) | FIX | DO NOT POST

FAILURES
1. [Check] what is wrong, where (time)
   -> Fix: ...

WARNINGS
- ...

UNMEASURED (chat tier)
- ...

MUST CONFIRM
- ...
```

## Checks
DO NOT POST for any of:
- a featured person without consent;
- a Vetted claim not in the register or not the approved line;
- music in the file without a recorded licence;
- a forward promise about who will attend.

FIX for any failed threshold. READY only when every threshold passes and nothing is unmeasured. In chat, use READY PENDING MEASURE.

## Use in another tool
Paste `IDENTITY.md`, this file, the brief and the transcript, and upload the contact sheet. Ask for the verdict.
