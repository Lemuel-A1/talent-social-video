---
name: video-3-captions-and-type
description: Write the captions, headline and labels for a Talent Social cut to the house style, and at the agent tier burn the captions in. Use after the rough cut.
---

# 3. captions-and-type

Read `../IDENTITY.md` first. Style data: `../templates/caption-style.json`.

## Input
- The rough cut (agent) and the word-timed transcript, in output time.
- The brief: headline, labels, confirmed name spellings.

## Steps
1. **[chat] Chunk the captions.** 2 to 5 words each, sentence case, in the order spoken. Break on meaning, not just on length. Write them as an SRT: number, `00:00:00,000 --> 00:00:00,000`, text. Times in output time. For a teaser, the captions are the claim and reason (see the format page), not the speech.
2. **[chat] Choose the gold word.** At most one per chunk, and not in every chunk: the number, the verb of an action, the stake. List the words, one per line, in `words.txt`.
3. **[chat] Write the headline and labels.** Headline in caps, 2 lines at most, one gold word. Labels: name (white on charcoal) and topic or role (gold). Use the spellings the owners use. Mark any unconfirmed name MUST CONFIRM.
4. **[chat] Check the words against the speech.** Spot-check 5 chunks at different points. Fix mis-heard words, especially names and numbers.
5. **[agent] Make the caption overlay.** Run `$STT_PYTHON tools/captions_to_overlay.py captions.srt <out_dir> --font <ttf> --size 64 --y 0.62 --gold F5B533 --emphasis words.txt`. It writes a transparent PNG per chunk and `overlay.ffconcat`. Use the font path in `CONFIG.md`.
6. **[agent] Burn the captions in.** Run `$STT_PYTHON tools/burn_captions.py <in.mp4> captions.srt <out.mp4> --font <ttf>` with the same options. It prints the output path and the duration.
7. **[chat] Hand the headline and labels to the person.** The headline, labels and any card text are built in CapCut or Canva from the format page. The agent does not draw them in v1.

## Output
- `captions.srt` and `words.txt`.
- Headline and label text, with times.
- A captioned render (agent). In chat, the person imports the SRT into CapCut or Canva and applies the values in `caption-style.json`.

## Checks
- Captions match the speech (5 spot-checks).
- Every chunk is 2 to 5 words, sentence case, at most one gold word.
- Captions sit at 55 to 70% of frame height.
- Nothing in the top 220 px, the bottom 380 px or the right 140 px.
- No caption repeats a name already on a card.
- Names spelled as their owners spell them.

## Use in another tool
Paste `IDENTITY.md`, this file and the word-timed transcript. Ask for the SRT, `words.txt`, headline and labels.
