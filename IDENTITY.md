# Talent Social video: identity (every skill reads this first)

One file, shared by every skill. If a format page and this file disagree, this file wins.

## 1. Who and why
Talent Social is for professionals in and around Nairobi. The videos give: a useful tip, a fun game, a reason to come to the room. They never beg and never sell hard. Feel: useful, warm, a bit fun.

Brand line on video: **"Talent Social · powered by Vetted"**.

Two kinds of video, two jobs:
- **Episodes** (advice, game) give. Their ask is soft: follow, or a comment question.
- **Teasers** invite. Their ask is the event link.

## 2. Voice
- Speakers say their own lines. Tobi or Lemuel to camera for advice. Nobody is quoted saying something they did not say.
- First person covers only what that speaker did or said.
- No unsourced "#1", no award, no number without a source.
- No forward promise about who will be in the room. Allowed: past-tense evidence, or what we control.
- Words: "assessment", never "audition". Never "proof of work". Never "can't cheat".
- Plain, warm, short sentences. No hype words, no false urgency.

## 3. Colour (brand v2, measured from talentsocial.network on 22 Oct 2026)
| Use | Value |
|---|---|
| Page and base (warm black) | #131210; raised #191715 and #1E1C1A |
| Text | off-white #F6F5F4; muted #A9A39E |
| Gold on cards and the payoff phrase | #D8B579 |
| Gold on video (small text, emphasis words, any button) | #E2B05A (the site's button fill; it reads better over moving footage) |
| Dark text on gold | #181410 |
| Purple | only inside the Vetted mark |

- Gold has one job: emphasis. In plain captions, one word per phrase. In kinetic captions, stressed words, numbers and the one big word (see section 4). Besides captions, only the role line of a name card and the payoff phrase may be gold. Never more than four gold items on screen at once.
- Never gold backgrounds. Never every word.
- Old values (#F5B533 gold, #181E2A navy) were guesses from reels. Do not use them in new work.
- Colour grade: the team's `NTS_Signature` LUT for the Sony camera (S-Log3), a light trim on the Rec.709 interview camera. The warm look matches the site's warm blacks.

## 4. Type (brand v2)
- **Face:** Inter Tight (open licence, Google Fonts) for setup lines, captions, cards and the outro. Files: `InterTight[wght].ttf` and `InterTight-Italic[wght].ttf`, kept outside the repo (see `CONFIG.md`). Weights: 600 normal, 700 names, 800 stress, 900 numbers.
- **Payoff face:** a gold serif italic for the one word or phrase that carries the idea: Didot Italic where macOS has it (the team's confirmed taste), Inter Tight Italic elsewhere. A Google serif such as Instrument Serif is the portable choice (open decision).
- **Headline (static):** sentence case, Inter Tight SemiBold, tight tracking, left aligned at a 92 px margin, at most 2 lines plus a gold payoff line, 26 to 40% of frame height, over a soft warm-black gradient (no boxes). Use it only when the first spoken line is not already on screen as captions, or when the framing is editorial (a question the speakers did not say).
- **Captions have three modes: none, plain, kinetic** (rules in `skills/3-captions-and-type.md`, step 0). Plain is the default: steady phrases, Inter Tight SemiBold, off-white, at most one gold word per phrase, sentence case, centred at 55% of frame height (range 50 to 62%), a soft dark halo and no outline. **Kinetic is an experiment** (from 22 Oct 2026, tested on matched pairs): words appear as they are spoken, a short pop each, typeset by role:
  - normal: Inter Tight SemiBold, off-white
  - soft (articles and joiners): smaller, lighter, a little transparent
  - stress: ExtraBold, 1.2 times larger, gold. Chosen from the lines marked in the brief and from the speaker's delivery (louder and slower than their usual), at most two per phrase
  - number: Black, 1.5 times larger, gold
  - big: the one word that carries the idea, in the payoff face, 1.9 times larger, gold, on its own line
  Every piece also gets a clean master with no captions, so other tools can add their own.
- **Branding on screen is minimal.** No eyebrow or logo near the faces. One small, quiet `talentsocial.network` at the bottom-left (22 px, about 60% opacity, above y 1440), hidden while a glass card is up. The glass outro carries the brand at the end.
- **Cards are liquid glass.** Name cards (name in Inter Tight Bold, role in tracked gold caps) and the outro (Talent Social, talentsocial.network) show the real picture behind them, blurred and brightened, with a white tint, a bright rim top-left, a warm edge bottom-right and a soft shadow. Left aligned at the 92 px margin, ending by y 1440. No other boxes.
- The same values as data: `templates/caption-style.json`.
- Status: the advice and game series overlays (tabs, ledger, checklist cards, sting) in the overlay pack are still brand v1. Migrating them is open. Talk clips, interviews, stories and quick clips use brand v2.

## 5. Safe zones (1080x1920)
Nothing important in the **top 220 px**, the **bottom 380 px** or the **right 140 px**. That means no headline, tab, logo, label, ledger, price badge, caption or CTA card there.
Usable band: y from 220 to 1540. Text and cards end by y 1440 (the team's confirmed rule: nothing in the bottom 25%, where captions and buttons of the platform sit); the 1540 line is the hard limit for everything else.

## 6. Motion
- Hard cuts by default.
- Punch-ins of 10 to 15% every 3 to 5 s on talking heads.
- One section transition: the gold band wipe, about 0.3 s, only between sections.
- Picture change every 3 to 5 s in episodes; every 1 to 2 s in teasers.
- No emoji sprites, cartoon stickers, light leaks, glitch bursts or colour washes.
- Series overlays are house assets: progress tabs (advice) and the draft ledger (game). One overlay card on screen at a time; no ghosting.
- In v1 a person builds the animated overlays (tabs, ledger, sting, punch-ins) in CapCut or Canva from the format page. The kit supplies their text and timings.

## 7. The sting
- A 1 to 1.5 s full-screen card: the Talent Social mark and a short sound. The same every time.
- Placed right after the first spoken sentence (usually 3 to 6 s). Never frame 1. Optional in talk clips (only if the hook ends cleanly at a sentence break). The headline stays up until the sting; the speaker label comes right after the sting.
- The asset is made outside this kit. Its file name is in `CONFIG.md`.

## 8. Audio
- Voice first. Integrated loudness -14 LUFS (accept -15 to -13). True peak at or below -1 dBFS.
- Music 15 to 20 dB under the voice.
- Add music inside the platform at upload where possible, so the platform keeps the licence. Also export a clean voice-only master. Make a music version for LinkedIn and WhatsApp only if the music is licensed.
- Whoosh only on section changes. The sting on the hook (optional in talk clips). Nothing else.
- For founder stories: riser at the open, one impact note at the turn, music ends rather than fades.
- No silent end card: the CTA is spoken while its card shows; the video ends at most 0.5 s after the card's 3 s. Talk clips: the speaker's landing line plays under the CTA card instead.

## 9. CTA
- **Evergreen by default.** Talk clips, interviews, founder stories and quick formats end on the glass outro (Talent Social and talentsocial.network), held 3 s, with no date and no edition. Any of these can be reposted next month.
- Event teasers are the only format that names an edition. They carry the event details, are made per edition, and the host says them. They are not reposted after the event.
- Episodes: **"Follow for part 2"**, said and shown, held 3 s, above the bottom zone.
- A comment keyword ("Comment ROLES and I'll send...") only when a named person will send the replies. No reply plan, no keyword.
- A comment question with no promise ("Who do you think won?") is allowed in the game episode as its one CTA.
- No RSVP buttons, no ticket prices and no countdowns in evergreen pieces.

## 10. People and claims
- Written consent for anyone featured who is not a public figure. No consent, no clip.
- Faces at events: use only people who agreed, until the team confirms that registration terms cover marketing use.
- A **Vetted claim** is any statement about Vetted's results, customers, scale or numbers, including a speaker's first-person line about work done through Vetted ("I've helped companies screen 10,000 candidates"). Vetted claims: only wording approved in the claims register (private). The only approved public proof line: **"WorkPay cut its hiring cycle from 90 days to 30."**
- No client logos as proof. No logo walls. No "participants from" lists.
- Every number on screen matches what is said, and has a source.
- Music and font licences are recorded before posting.

## 11. Measures
Judge by views, average watch time, shares, saves and follows in the Instagram app insights. Not likes alone. Change one thing per post. Past numbers are kept privately; ask Lemuel.

## 12. QC thresholds (skill 6 checks these)
| Check | Pass | Tool |
|---|---|---|
| Size and rate | 1080x1920, 30 fps | `measure.py` |
| Integrated loudness | -14 LUFS; accept -15 to -13 | `measure.py` |
| True peak | at or below -1 dBFS | `measure.py` |
| Runtime | advice 45 to 75 s; game 60 to 90 s; teaser 12 to 25 s; talk clip 20 to 45 s | `measure.py --format` |
| First spoken line (voice formats) | starts within 2 s; target 0 to 0.3 s | transcript |
| First frame | not black, not a logo | `measure.py`, contact sheet |
| Silences | none over 0.4 s, unless the brief marks a deliberate beat | `measure.py` |
| Safe zones | nothing important in top 220, bottom 380, right 140 px | contact sheet |
| Captions | 2 to 5 words, 55 to 70% height, sentence case, at most one gold word | contact sheet |
| Sting | 1 to 1.5 s, after the first line, not frame 1 (optional in talk clips) | contact sheet, brief |
| Picture change | episodes every 3 to 5 s; teasers every 1 to 2 s | contact sheet (`measure.py` undercounts punch-ins) |
| CTA | one; evergreen glass outro on talk clips, interviews and stories (no date); said and shown on episodes; held 3 s, above y 1440 | transcript, contact sheet |
| Consent, claims, licences | all recorded | brief |

DO NOT POST for: a person without consent, a Vetted claim not in the register, music in the file without a recorded licence, or a forward promise about who will attend.
