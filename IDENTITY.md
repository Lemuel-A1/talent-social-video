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

## 3. Colour
| Use | Value | Status |
|---|---|---|
| Accent (gold) | about #F5B533 | to confirm in Canva |
| Base (charcoal) | about #181E2A | to confirm in Canva |
| Off-white | {{NEEDS_VERIFICATION}} | pick one hex in Canva |
| Purple | only inside the Vetted mark | |

- Gold has one job: emphasis. At most one gold word in a caption chunk. Besides that word, only these may be gold: the active tab, the topic line of a label, the CTA button. Never more than three gold items on screen at once.
- Never gold backgrounds. Never every word.
- Yellow emphasis is the short-form convention. Our gold is a shade of it, chosen to sit with warm Nairobi footage and the purple parent mark.

## 4. Type
- **Headline (frame 1):** heavy geometric sans, Poppins ExtraBold (OFL licence), caps, at most 2 lines, 20 to 35% of frame height, one gold word. Every line fits inside the safe zones.
- **Captions:** sentence case (capital letter only at the start of a spoken sentence and for names; a chunk that continues a sentence starts lower case), 2 to 5 words per chunk, white with a soft shadow, 55 to 70% of frame height, at most one gold word per chunk.
- **Labels:** name in white on charcoal; topic or role in gold. Shown on first appearance of a speaker, about 3 s.
- The same values as data: `templates/caption-style.json`.

## 5. Safe zones (1080x1920)
Nothing important in the **top 220 px**, the **bottom 380 px** or the **right 140 px**. That means no headline, tab, logo, label, ledger, price badge, caption or CTA card there.
Usable band: y from 220 to 1540.

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
- One. Said and shown. Held 3 s. Above the bottom safe zone.
- Exception, talk clips: the speaker cannot be asked to say our CTA, so it is shown only (card and caption), unless the speaker said a line that works as one.
- Default: **"Follow for part 2"** (episodes) or **the event link** (teasers).
- A comment keyword ("Comment ROLES and I'll send...") only when a named person will send the replies. No reply plan, no keyword.
- A comment question with no promise ("Who do you think won?") is allowed in the game episode as its one CTA.

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
| CTA | one, said and shown (talk clips: shown), held 3 s, above y 1540 | transcript, contact sheet |
| Consent, claims, licences | all recorded | brief |

DO NOT POST for: a person without consent, a Vetted claim not in the register, music in the file without a recorded licence, or a forward promise about who will attend.
