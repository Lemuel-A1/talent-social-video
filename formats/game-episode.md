# Format: game episode (The $20 Draft)

Read `../IDENTITY.md` first. Numbers there win.

## Purpose
A light, fun, repeatable game that shows real people and real ambition. Two hosts, a small budget, a draft of public figures. It gives (fun, and a name to follow). It does not sell. Its most reusable asset is the live ledger.

## Length
60 to 90 s. Aim for 70 to 85 s. The times below are for an 80 s cut.

## Shape, beat by beat
| Output time | Beat | On screen | Sound |
|---|---|---|---|
| 0.0 to 3.0 | **Cold open**: the best line in the footage (the stake or the best clash). Not the first line. | Hosts mid-gesture. Headline from frame 1. | Voice from 0 to 0.3 s |
| end of first sentence, about 3 to 6 s (+1.2 s) | **Sting** | Talent Social card | Sting sound |
| 4.2 to 9.0 | **Rules**: one sentence said, one line shown. Say how the winner is decided. | Rules card. Ledger appears for both hosts. Brand mark, series bug. | Voice |
| 9.0 to 66.0 | **The draft**: about 5 picks, about 11 s each. Pick card, price badge, ledger updates. One twist or open loop set early and paid off here. | Pick card 2.5 s, then back to the hosts. Punch-ins on bid peaks. | Voice, room, laughter |
| 66.0 to 76.0 | **Payoff shown**: final rosters on screen and the result or the scoring rule applied. | Both ledgers final | Voice |
| 76.0 to 80.0 | **Comment question** as the CTA | CTA card held 3 s | Host says it |

Rules:
- The rules take one sentence. If they need more, cut them or put them in the caption.
- The payoff is shown on screen. Do not hand the whole verdict to the comments.
- Only one pick card on screen at a time. The old card leaves before the new one enters.

## Hook options
The first-2-seconds rule: a spoken line starts by 0.3 s (QC passes up to 2 s). It is the best line, not the first. Headline from frame 1, readable with sound off, inside the safe zones, no clipped lines. No title card first.
1. **The stake.** Headline pattern: `WE GAVE {WHO} {STAKE} TO {TASK}`. Example shape: `WE GAVE 2 FOUNDERS $20 TO DRAFT {THEME}`. Spoken line: the sharpest clash about it.
2. **The open loop.** A line that promises a payoff later ("this pick cost me the game"). Pay it off in the payoff beat.
3. **The surprising price.** A bid that makes the room react.

## Captions and labels
- Captions: sentence case, 2 to 5 words, white with soft shadow, 55 to 70% height, one gold word at most. A caption never repeats the name already on the pick card.
- Labels: host names sit on the ledger. Guests and pick names get the name (white on charcoal) and role (gold). Roles must be confirmed from a public source: mark MUST CONFIRM until then.

## Overlays (a person builds these in CapCut or Canva)
Times are output times in an 80 s cut.

| Element | Exact text pattern | In | Out | Notes |
|---|---|---|---|---|
| Headline | `WE GAVE {WHO} {STAKE} TO {TASK}` caps, one gold word | 0.0 | 3.0 | Fully inside the safe zones |
| Sting | Talent Social mark card | end of first sentence (about 3 to 6 s) | +1 to 1.5 s | File in `CONFIG.md` |
| Brand mark | `Talent Social · powered by Vetted` | 4.2 | end | Top-left, y 220 or lower |
| Series bug | `THE $20 DRAFT · EP {NN}` | 4.2 | end | Under the brand mark |
| Rules card | `{BUDGET} EACH · {N} PICKS · WINNER: {HOW IT IS DECIDED}` | 4.2 | 9.0 | The line must match what is said |
| Ledger | header `{HOST NAME}` and `$20`; rows `{PICK} · ${PRICE}`; line `LEFT ${N}` | 5.0 | 76.0 | In the band between y 240 and the captions. Left of x 940. Never over a face. Never on the right edge. |
| Pick card | `{NAME}` over `{ROLE}` | at each pick | +2.5 s | One card at a time |
| Price badge | `${PRICE}` pop-in 0.1 to 0.3 s | at the bid | +2 s | Inside x 940 |
| Punch-ins | 10 to 15% scale | on bid peaks, every 3 to 5 s | | List the times in the brief |
| Payoff | final ledgers plus `{RESULT}` | 66.0 | 76.0 | |
| CTA card | `WHO DO YOU THINK WON?` | 77.0 | 80.0 | Held 3 s, bottom edge above 1540 px |

No emoji or cartoon sprites. No ghosted cards.

## CTA
One: the comment question, said by a host and shown. "Who do you think won?" asks for opinion, not for a keyword, so it needs no reply plan. Do not add a follow ask on top.

## Sound
- Voice first. Sting where the first sentence ends (about 3 to 6 s); later beats shift by its length. Short whoosh only on section changes (rules to draft, draft to payoff).
- Keep the laughter. It is part of the format.
- No music in the file by default. Add in the platform at upload, 15 to 20 dB under the voice. Keep a voice-only master.
- Master to -14 LUFS (accept -15 to -13), true peak at or below -1 dBFS. The end card is not silent: the question is spoken over it.

## QC thresholds
Runtime 60 to 90 s. First spoken word within 2 s. First frame not black, not a logo. Loudness and true peak as above. Nothing in the top 220, bottom 380 or right 140 px (check the price badge and the ledger). Picture change at least every 5 s. Ledger values match the speech. One CTA. Full table: `../IDENTITY.md` section 12.

## Worked example: the baseline game episode "Ep. 03" (76 s)
**What the baseline did**
- Good: the hook text (`WE GAVE 2 FOUNDERS $20...`) from the first moments; a live scoreboard and price badges that stayed in sync with speech; consistent caption style; a laughter beat near the end.
- Weak: a 2.4 s title card at about 2.3 s replaced the hook text before the game began; the opening line was banter, not a stake; one locked shot for about 67 s with no punch-ins; a cartoon sprite covered the first name card; the header sat in the top zone and the price badge on the right edge; a caption repeated the card's name; no winner or scoring rule shown; the CTA was small, shown for under 2 s, not said; the end card was silent; true peak over the limit.

**What v1 would do**
- Cold open on the sharpest line about the stake. Headline `WE GAVE 2 FOUNDERS $20 TO DRAFT {THEME}`, inside the safe zones.
- No title card. Series name as the small bug. Sting where the first exchange ends (about 2 to 4 s), never before the first line.
- Rules in one sentence with the scoring rule on the card.
- Keep the ledger and price badges; move them off the right edge and out of the top 220 px.
- Punch-in every 3 to 5 s on bid peaks. Drop the sprite. Drop captions that repeat the card.
- Show the result in the payoff beat, then ask the comment question aloud over a card held 3 s.
- Master to -14 LUFS, true peak at or below -1 dBFS.

## Reference posts (public handles; patterns, not copy)
- **jubileemedia**: a named series with a season, repeatable conversation and game formats. Two-line captions in a dark box with the payoff line in yellow. Do not copy the US political content.
- **thediaryofaceopodcast**: opens on the most surprising line, then a big headline with one coloured word, then small sentence-case captions. Copy the cold open. Do not copy the long runtimes.
- **bigtechprep**: a numbered series with a promise in the title ("Day 1/30" style). Copy the numbering habit, which suits "Ep NN".
