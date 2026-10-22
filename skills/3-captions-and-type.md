---
name: video-3-captions-and-type
description: Write the captions, headline and labels for a Talent Social cut to the house style, and at the agent tier burn the captions in. Use after the rough cut.
---

# 3. captions-and-type

Read `../IDENTITY.md` first. Style data: `../templates/caption-style.json`.

## Input
- The rough cut (agent) and the word-timed transcript, in output time.
- The brief: caption mode and its one-line reason, headline (if any), labels, confirmed name spellings.

## Step 0: choose the caption mode (write it in the brief with a one-line reason)
Three modes. Kinetic is an experiment (status below), not the house default.
- **none**: no captions burned in. The clean master is the deliverable. Another tool (CapCut auto-captions, the platform's captions) adds them, or none are wanted.
- **plain**: steady phrases of 2 to 5 words, brand type, at most one gold word per phrase, no animation (`--style brand`). The default.
- **kinetic**: words appear as spoken and are typeset by role: stressed words heavier, larger and gold, numbers largest, one big idea word in the gold serif (`--style kinetic`).

Rules, first match wins:
1. No speech, speech only in the background, or the piece is music-led: **none**. A teaser's claim goes on as a headline card, not as captions.
2. Someone will caption it elsewhere, or the editor asks for a clean file: **none**.
3. Sensitive subject (health, money harm, legal, a personal story), two or more people talking in turns, or a measured speaker with little emphasis: **plain**.
4. Over 45 s, or captions would be on screen for most of a long story: **plain** (reading fatigue).
5. It has to land with the sound off, runs 45 s or less, and has at least one of: a number, a one-idea line, humour, a strong opinion said with stress: **kinetic**.
6. Anything else: **plain**.
Limits for kinetic: never over a static headline that repeats the same words; one big word per phrase; if the contact sheet shows any frame where the words are hard to read, use plain for that clip.
Always, whatever the mode: export a **clean master** (cards and outro, no captions), like the team's textless masters. It is the file other tools start from.

Experiment (from 22 Oct 2026): kinetic captions are tested against plain on matched pairs, the same cut in both modes, posted on different days. Log `caption_mode` (none, plain, kinetic) in `templates/performance-log.csv`. Judge on average watch time and a readability review, not likes (reels get 5 to 100 likes, too few to separate them). Kinetic becomes a standard mode for rule-5 clips only if it beats plain on average watch time in at least 6 of 8 pairs. Otherwise it stays an option and is not extended.

## Steps
1. **[chat] Chunk the captions (plain mode).** 2 to 5 words each, sentence case, in the order spoken. Break on meaning, not just on length. Write them as an SRT, or use the word-timed `transcript.json` directly. Times in output time. For a teaser, the claim is a headline card (see the format page), not the speech.
2. **[chat] Choose the gold word (plain) or the stressed and big words (kinetic).** Plain: at most one gold word per chunk, not in every chunk: the number, the verb of an action, the stake. Kinetic: list stressed words in `words.txt` (they also come from the speaker's delivery) and the one big word per idea in `big.txt`.
3. **[chat] Write the headline and labels.** A static headline only when the first spoken line is not already on screen or the framing is editorial. Labels are name cards (see `IDENTITY.md` section 4). Use the spellings the owners use. Mark any unconfirmed name MUST CONFIRM.
4. **[chat] Check the words against the speech.** Spot-check 5 chunks at different points. Fix mis-heard words, especially names, numbers and tool names (Claude was heard as "cloud" and "clothes"). Put fixes in the brief.
5. **[agent] Burn the captions in.** `$STT_PYTHON tools/burn_captions.py <in.mp4> transcript.json <out.mp4> --font <InterTight[wght].ttf> --style kinetic|brand --emphasis words.txt --big big.txt --y 0.55`. For an SRT use `--style brand`. It prints the output path and duration. Skip this step in mode none.
6. **[agent] Export the clean master** with `tools/loudness.sh` from the cut that has cards and the outro but no captions.
7. **[agent] Look at the contact sheet** at a stride of 2 to 3 s. Check legibility on bright backgrounds, overlap with cards, and that kinetic words are readable on every frame shown.

## Output
- The caption mode and reason, `words.txt` (and `big.txt` for kinetic), the SRT for plain mode in chat.
- Headline and label text, with times.
- A captioned render (agent) and the clean master. In chat, the person imports the SRT into CapCut or Canva and applies the values in `caption-style.json`.

## Checks
- Captions match the speech (5 spot-checks).
- The mode follows the rules, and the brief says why.
- Plain: every chunk is 2 to 5 words, sentence case, at most one gold word. Kinetic: at most two stressed words and one big word per phrase.
- Captions are centred at about 55% of frame height (range 50 to 62%).
- A clean master exists for every piece.
- Nothing in the top 220 px, the bottom 380 px or the right 140 px.
- No caption repeats a name already on a card.
- Names spelled as their owners spell them.

## Use in another tool
Paste `IDENTITY.md`, this file and the word-timed transcript. Ask for the caption mode with its reason, the SRT (plain mode), `words.txt`, headline and labels.
