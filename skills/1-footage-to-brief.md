---
name: video-1-footage-to-brief
description: Turn a transcript (chat tier) or footage (agent tier) into a Talent Social video brief with a verbatim hook, a format, a structure, a CTA plan, and a consent and claims list. Use first, before any cut.
---

# 1. footage-to-brief

Read `../IDENTITY.md` first.

## Input
- A transcript with times (chat tier), or the video file (agent tier). A chat cannot watch video. See `../START-HERE.md` for how to get a transcript from CapCut or Instagram captions.
- What it is: date recorded, who is on screen, what the recording was for.
- The format wanted: advice episode, game episode, event teaser, or "suggest".
- People featured and their consent status.
- The account it will post from and the CTA plan.

## Steps
1. **[chat] Triage the input.** Is it a transcript with times, a transcript without times, or an AI-written summary? Ignore any summary as a source. Without times, hook times are `{{NEEDS_VERIFICATION}}`: ask the person to find each line's time in the editor. Auto-captions mis-hear names: list every name and ask the person to confirm each spelling.
2. **[agent] Transcribe.** Run `$STT_PYTHON tools/transcribe.py <video> <out_dir> --model small.en`. Use `transcript.json` for word times and `transcript.txt` for reading. In chat, skip this step and use the uploaded transcript.
3. **[chat] List the 3 strongest candidate hook lines.** Each is verbatim, with its source time. Score each 1 to 3 for surprise, specificity and usefulness. Pick the best line, not the first. For a game episode, the best clash or stake. For a teaser, the claim.
4. **[chat] Name the playbook chapter, persona and career stage** (land the job, succeed in the job, grow, switch, hire well). Advice that does not come from a chapter of our own playbooks is not shot or posted. If no chapter exists yet, say so and ask Lemuel or Tobi for the framework.
5. **[chat] Choose the format.** Use the format pages in `../formats/`. If the footage fits none, say so. Do not force a fit. For panels, interviews and stage moments, use `../formats/talk-clip.md`.
6. **[chat] For a long recording, list up to 5 clips.** One idea per clip, each with source start and end and its own hook line. Brief the strongest first.
7. **[chat] Plan the structure.** Fill the beat table from the format page. Source times beside output times.
8. **[chat] Draft the headline for frame 1.** Caps, 2 lines at most, one gold word. Check it works with the sound off. Every number must be in the speaker's own words.
9. **[chat] Set the CTA.** Default "Follow for part 2" (episodes) or the event link (teaser). A comment keyword only with a named person who will send the replies. A game episode uses the comment question.
10. **[chat] Check what the footage is missing.** If there is no spoken CTA, no action at the end of a point, or the hook line is weak, list short pickup lines for the speaker to record in their own words (one line each). Do not write words for them to say as if they had said them.
11. **[chat] Flag what to clear.** People without consent. Names and roles to confirm. Logos, client names, numbers, "#1", any claim about Vetted. Music. Anything said about who will attend.

## Output
A brief on `../templates/brief.md`, with a short list of the other clips if any. Say which to cut first and why.

## Checks
- Every hook is a verbatim line with a source time (or `{{NEEDS_VERIFICATION}}` for the time).
- No clip features a person without consent, unless they are a public figure.
- One idea per clip.
- The only Vetted claim is "WorkPay cut its hiring cycle from 90 days to 30." Any other is flagged.
- Numbers in the headline match the transcript.
- Names are marked confirmed or unconfirmed.

## Use in another tool
Paste `IDENTITY.md`, then this file, then the format page, then your transcript. Ask for the brief. Nothing else is needed.
