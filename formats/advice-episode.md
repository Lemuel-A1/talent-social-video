# Format: advice episode (Job Search Tips 101)

Read `../IDENTITY.md` first. Numbers there win.

## Purpose
Give a job seeker one useful thing in about a minute. This is a give, not an ask. One person to camera: Tobi or Lemuel. Three numbered points, one action, one soft CTA. It is also the best template for any talk clip that grows into a tip.

## Length
45 to 75 s. Aim for 55 to 65 s. The times below are for a 58 s cut. Stretch or trim the three points to fit.

## Shape, beat by beat
| Output time | Beat | On screen | Sound |
|---|---|---|---|
| 0.0 to 3.0 | **Hook** | Speaker mid-sentence. Headline from the first frame. | First spoken word at 0 to 0.3 s |
| end of first sentence, about 3 to 6 s (+1.2 s) | **Sting** | Full-screen Talent Social card | Sting sound |
| 4.2 to 10.0 | **Context**: who this is for, what is at stake. One beat. | Speaker. Name and topic label (3 s). Brand mark, series bug and the three tabs appear. | Voice |
| 10.0 to 22.0 | **Point 1** | Band wipe in. Tab 1 goes gold. Point card. Optional checklist card. | Whoosh on the wipe |
| 22.0 to 34.0 | **Point 2** | Same | Same |
| 34.0 to 46.0 | **Point 3** | Same. Ends on a concrete thing to do. | Same |
| 46.0 to 54.0 | **One action** for this week | Action card | Voice |
| 54.0 to 58.0 | **CTA** | CTA card held 3 s | Speaker says it |

Rules for the points:
- Each point is one claim and one thing to do. A point that ends without an action is not finished.
- The speaker says the number: "First...", "Second...", "Third...".
- No title card at the start. The series name is a small bug (see overlays), not a card.

## Hook options
The first-2-seconds rule: a spoken line starts by 0.3 s (QC passes up to 2 s) and states the stake. No "Hi, I'm...". No logo, black frame, fade-in or title card first. The headline is on screen from frame 1. It must make sense with the sound off.

Pick the best line in the footage, not the first.
1. **Stake with a number.** "{N} applications and nobody replied?" Headline: `{N}+ APPLICATIONS. ZERO REPLIES.` The number must be in the speaker's own words.
2. **Outcome claim in a boxed line.** The headline sits in a charcoal box. Borrowed from jerryjhlee.
3. **The reader's situation as a question.** "Is your CV the reason nobody replies?"
4. **Contrarian line.** "Stop {common advice}." Only if the speaker means it.

## Captions and labels
- Captions: sentence case, 2 to 5 words, white with soft shadow, 55 to 70% height, one gold word at most. Style data: `../templates/caption-style.json`.
- Gold word: the number, the verb of the action, or the stake. Not a filler word.
- Label once, at 4.2 s, for 3 s: `{NAME}` white on charcoal, `{TOPIC}` gold. Names spelled as their owners spell them.
- Check five caption chunks against the audio.

## Overlays (a person builds these in CapCut or Canva)
Times are output times in a 58 s cut. Shift with the cut.

| Element | Exact text pattern | In | Out | Notes |
|---|---|---|---|---|
| Headline | `{LINE 1}` / `{LINE 2}` in caps, one gold word | 0.0 | the sting | Out at the sting. 20 to 35% height. |
| Sting | Talent Social mark card | end of first sentence (about 3 to 6 s) | +1 to 1.5 s | File in `CONFIG.md` |
| Brand mark | `Talent Social · powered by Vetted` | 4.2 | end | Top-left, y 220 or lower |
| Series bug | `JOB SEARCH TIPS 101 · EP {NN}` | 4.2 | end | Directly under the brand mark |
| Label | `{NAME}` over `{TOPIC}` | right after the sting | +3 s | Lower band, 72 to 79% height |
| Progress tabs | `1 {WORD}` `2 {WORD}` `3 {WORD}` | 5.0 | 46.0 | One or two caps words each. Under the bug, y 240 or lower. Active tab gold, others outline. |
| Band wipe | gold band, diagonal | 10.0, 22.0, 34.0 | +0.3 s | The only transition |
| Point card | `#{N} {TITLE}` (1 to 3 words) | start of each point | +2.5 s | One card at a time |
| Checklist card | up to 3 lines, up to 4 words a line | as said | +3 s | Ticks appear as the speaker names them. Above 1540 px. |
| Action card | `THIS WEEK: {ACTION}` (up to 8 words) | 46.0 | 54.0 | |
| CTA card | `FOLLOW FOR PART 2` | 55.0 | 58.0 | Held 3 s, bottom edge above 1540 px |
| Punch-ins | 10 to 15% scale | every 3 to 5 s | | List the times in the brief. Alternate in and out. |

Proof card: optional. If the speaker says it and it fits the point, show only the text `WorkPay cut its hiring cycle from 90 days to 30.` No logos. No candidate counts without a source.

## CTA
Default: **"Follow for part 2."** Said by the speaker at about 54 s and shown on the card at 55 s. One CTA, nothing else.
A comment keyword only with a named person who will send the replies.

## Sound
- Voice first. Sting where the first sentence ends (about 3 to 6 s); later beats shift by its length. Whoosh on the three band wipes only.
- No music in the file by default. Add music in the platform at upload, 15 to 20 dB under the voice. Keep a clean voice-only master.
- Master to -14 LUFS (accept -15 to -13), true peak at or below -1 dBFS.
- No silent tail: the CTA is spoken while the card shows.

## QC thresholds
Runtime 45 to 75 s. First spoken word within 2 s. First frame not black, not a logo. Loudness and true peak as above. No silence over 0.4 s. Nothing in the top 220, bottom 380 or right 140 px. Picture change (punch-in, card or wipe) at least every 5 s. One CTA, said and shown, held 3 s. Full table: `../IDENTITY.md` section 12.

## Worked example: the baseline episode "Ep. 02" (65 s, "no feedback")
**What the baseline did**
- Good: a face mid-sentence at 0.2 s; a counter hook ("100+ jobs, 0 feedback") with a red pill; three numbered tabs; ticking checklist cards; Nairobi b-roll.
- Weak: a title card at about 6 s with a loud sweep stalled the hook; a proof card paired a screened-candidates count with a wall of seven client logos (outside the claims register; the transcript also hears a different year from the one on the card, so check both before reuse); tabs and captions sat inside the top and bottom unsafe zones; tip 3 ended with no action; the b-roll lines named employers; the CTA was shown but not said; the end card was silent; true peak was over the limit; no music or sting.

**What v1 would do**
- Keep the counter hook and the red-pill idea, but as the gold headline `100+ APPLICATIONS. ZERO REPLIES.` from frame 1. Use the same words only if the speaker still says them.
- Move the title into a small series bug (`JOB SEARCH TIPS 101 · EP 02`). Add the sting where the first sentence ends (in this episode, about 6 s).
- Drop the logo wall and the employer-name lines. If a proof card is wanted, use only the approved proof line as text.
- Check that the number on the card matches the spoken number before export.
- Move the tabs under the bug (y 240 or lower) and the captions to 55 to 70% height.
- End tip 3 with a concrete action, then `THIS WEEK: {ACTION}`.
- Speak the CTA ("Follow for part 2") over the CTA card. Hold it 3 s. No silent end card.
- Master to -14 LUFS with true peak at or below -1 dBFS.

## Reference posts (public handles; patterns, not copy)
- **jerryjhlee**: opens on a concrete outcome in a boxed line at the top and shows app screenshots as the proof. Uses a comment-keyword CTA; we only copy that with a reply plan. Do not copy the US-specific offers.
- **the.career.whisperer**: career advice for Africans in a series, including a multi-day prep challenge. The closest African model. Reels not yet reviewed in full: {{NEEDS_VERIFICATION}}.
- **hormozi**: one idea per clip, plain background, quiet captions, no filler. Copy the discipline, not the yellow word-highlight template or the money-guru tone.
