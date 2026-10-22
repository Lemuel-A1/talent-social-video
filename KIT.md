# Talent Social video kit (all files in one)

Version: 2026-10-22 (source 95c489c+uncommitted). Start with the ROUTER_PROMPT section below. File references such as `IDENTITY.md`, `formats/advice-episode.md` or `skills/6-qc-check.md` point to the sections of this file with that name. The agent-tier scripts (tools/*.py, tools/*.sh) are in the repo, not in this file: a chat does not need them.

## Contents

- README.md
- START-HERE.md
- EDIT-TEST.md
- ROUTER_PROMPT.md
- IDENTITY.md
- CONFIG.md
- formats/advice-episode.md
- formats/game-episode.md
- formats/event-teaser.md
- formats/quick-formats.md
- formats/founder-story.md
- formats/talk-clip.md
- skills/0-shoot-plan.md
- skills/1-footage-to-brief.md
- skills/2-rough-cut.md
- skills/3-captions-and-type.md
- skills/4-brand-and-motion.md
- skills/5-audio-and-master.md
- skills/6-qc-check.md
- skills/7-post-and-log.md
- skills/8-batch-plan.md
- templates/shoot-plan.md
- templates/brief.md
- templates/edl.csv
- templates/post-copy.md
- templates/performance-log.csv
- templates/caption-style.json
- templates/edit-test-report.md
- examples/REFERENCES.md
- examples/BASELINE-LESSONS.md
- tools/README.md


---

<!-- FILE: README.md -->
# FILE: README.md

# Talent Social Video: skills

Seven plain markdown skills, three format pages, and a few small tools. They turn a transcript or a recording into a finished Talent Social short video in the house look and voice, check it, and log how it did. Fork it.

## Files

| File | Job |
|---|---|
| `IDENTITY.md` | Shared by every skill: voice, colour, type, safe zones, motion, sting, audio, CTA, claims, QC thresholds |
| `formats/advice-episode.md` | Job Search Tips 101: 45 to 75 s |
| `formats/game-episode.md` | The $20 Draft: 60 to 90 s |
| `formats/event-teaser.md` | Event teaser: 12 to 25 s |
| `formats/quick-formats.md` | Bank of 15 quick series, the five-beat hook system, two prompts each |
| `formats/founder-story.md` | Founder story: Lemuel's and Tobi's personal and behind-the-scenes videos, six beats |
| `skills/0-shoot-plan.md` | Plan a shoot day: formats, timed blocks, crew, audio, consent, file names |
| `skills/1-footage-to-brief.md` | Transcript to brief: hook, format, structure, CTA, consent, claims |
| `skills/2-rough-cut.md` | Edit list and rough cut |
| `skills/3-captions-and-type.md` | Captions, headline, labels |
| `skills/4-brand-and-motion.md` | Overlay list with exact text and times |
| `skills/5-audio-and-master.md` | Sound plan and loudness master |
| `skills/6-qc-check.md` | Measured and visual QC; READY, FIX or DO NOT POST |
| `skills/7-post-and-log.md` | Post copy, cover frame, performance log, one lesson |
| `templates/` | Shoot plan, brief, edit list, post copy, performance log, caption style data |
| `tools/` | Small scripts for the agent tier (see `tools/README.md`) |
| `examples/` | What the baseline videos taught us; the reference creators |
| `CONFIG.md` | Accounts, asset folder, sting file names, export settings |
| `ROUTER_PROMPT.md` | The single entry point for any chat |
| `START-HERE.md` | One page for the team |

## The order

Before a shoot: skill 0 → the shoot plan. Then: transcript → skill 1 → skill 2 → skill 3 → skill 4 → a person builds the overlays → skill 5 → skill 6 → a person posts → skill 7. Many files at once, or a whole folder: skill 8 first (the batch plan).

## Two tiers

| Tier | Needs | Does |
|---|---|---|
| **Chat** | Claude or ChatGPT, the kit link, a transcript | Brief, hook with time, edit list, caption text, overlay text and times, post copy, QC checklist |
| **Agent** | Claude Code or Codex, this repo cloned, ffmpeg | The chat steps, plus transcribe, silence cut, burned-in captions, loudness master, measured QC |

Each skill marks every step [chat] or [agent]. In v1 a person builds the animated overlays in CapCut or Canva from the format page. No tier builds them.

## Public kit (no login)

An allowlist of these files is published by hand to a public repo as one `KIT.md`. Anyone can point a chat at `https://raw.githubusercontent.com/Lemuel-A1/talent-social-video/main/KIT.md`. The publish is blocked if a private term or a metric appears. Private facts live in a private notes file that is never published. Team guide: `START-HERE.md`.

## Use it in your tool

**Claude Code or Codex.** Clone the repo, set `STT_PYTHON` (see `CONFIG.md`), say what you have (a file path and the format).

**claude.ai.** Create a Project. Paste `ROUTER_PROMPT.md` as the instructions. Upload `IDENTITY.md`, `CONFIG.md`, `formats/`, `skills/`, `templates/` and `examples/` as project knowledge. Drop in your transcript.

**ChatGPT.** Create a custom GPT. Paste `ROUTER_PROMPT.md` into Instructions and upload the same files as Knowledge.

**CapCut and Canva.** Not the thinking tools here. Plan with one of the above, then build from the format page and `templates/caption-style.json`.

**No setup.** Paste `IDENTITY.md`, then one format page, then one skill, then your transcript.

## Fork it for another series

1. Copy this folder to a new lane.
2. Rewrite section 1 of `IDENTITY.md` (audience, brand line, colours) and the format pages.
3. Keep the hard rules unless the audience needs different ones.
4. Start a fresh `log/`.
5. Send lessons back by pull request.

## Rules that never change
Every fact has a source. No invented numbers, quotes or claims. No consent, no clip. No media files in this repo: footage, music, fonts and logos live in a shared drive named in `CONFIG.md`. No personal data. Nothing here posts anything.


---

<!-- FILE: START-HERE.md -->
# FILE: START-HERE.md

# Start here: make a Talent Social video in any chat

For anyone on the team who edits or posts. No GitHub login, no Claude Code.

## 1. Open a chat and paste this

> Read https://raw.githubusercontent.com/Lemuel-A1/talent-social-video/main/KIT.md and follow its router prompt. I want to make a Talent Social video from the transcript I'm uploading.

Works in Claude and ChatGPT. Web access must be on: in Claude, web search; in ChatGPT, search or browsing. If the chat says it can't open the link, download `KIT.md` from the same link and upload it instead.

The kit updates itself: the link always gives the latest version.

## 2. Get a transcript (the chat cannot watch video)
- **CapCut:** open your project, add auto captions (Captions, then Auto captions). Export the captions as an SRT file if your version offers it: SRT keeps a time on every caption, which the kit needs for exact cuts. Plain text works, but times will be estimates. Menu names change: {{NEEDS_VERIFICATION}}. If you cannot find an export, copy the caption text from the captions panel into a text file.
- **Instagram:** if you used the captions sticker, copy the text if your version lets you. Otherwise use CapCut.
- **SRT is best** because it has times. Plain text works, but the chat then cannot give hook times. Find them in your editor and tell the chat.
- Check names and numbers in the transcript. Auto-captions mis-hear them.

## 3. What to tell the chat
- Which format: advice episode, game episode or event teaser (or "suggest").
- Who is in it, how they spell their name, their role, and whether they said yes in writing. No yes, no clip.
- Which account you will post from.
- Your CTA plan. If unsure, say "default".
- For an event teaser: name, date, area and link.

## 4. What you get
A brief (check it, then say go), an edit list with times, captions as an SRT, headline and label text, a list of overlays with exact text and times, post copy, and a QC check with a verdict. The chat cannot measure loudness: the verdict will say so.

## 5. What you do yourself
Build the animated parts in CapCut or Canva from the overlay list: the sting, tabs or ledger, punch-ins, the CTA card. The format pages show where each one goes. Then ask the chat to check your plan for sound and QC.

## 6. Never upload
Contact lists or subscriber lists, DMs, logins or passwords, anyone's phone number or email, files a partner marked confidential, screenshots that show viewers' names. Do not upload video files: the chat cannot use them.

## 7. Feedback
At the end the chat asks "Any feedback to log?" Say what you would change. Copy the lesson entry it writes and send it to Lemuel. Lemuel updates the kit and everyone gets the change through the same link.


---

<!-- FILE: EDIT-TEST.md -->
# FILE: EDIT-TEST.md

# Edit test: turn last event's footage into 3 short clips

## Message Lemuel can send
> Hi! We're testing our new video-editing kit before next week's event. Could you take 3 clips from the last event's folder (panel, interviews) and edit them with the guide below? Nothing gets posted: it's a private test, and your notes on what was confusing matter as much as the videos. About 45 minutes for the first clip, less after. Guide: https://github.com/Lemuel-A1/talent-social-video/blob/main/EDIT-TEST.md

## What this is
A private test of the Talent Social video kit. You use a normal chat (ChatGPT or Claude) plus CapCut. Nothing is posted. Send everything back to Lemuel.

## Have ready
- The folder with the last event's footage (panel, interviews, clips).
- ChatGPT or Claude in a browser, with web access switched on.
- CapCut (desktop is easier than mobile for this).
- The report form: https://github.com/Lemuel-A1/talent-social-video/blob/main/templates/edit-test-report.md

## Before you start: consent
- Panel speakers: use their clips only if their speaker form is on file. Interviews: only if they signed a release. Not sure? Ask Lemuel first.
- Do not use close-ups of audience members.

## Step 1: choose 3 clips
One from the panel, one interview, and one other moment. In each, find a stretch of 1 to 3 minutes where one person makes one clear point.

## Step 2: get a transcript with times
In CapCut: import the clip, add auto captions, and export them as an SRT file if your version offers it (SRT keeps a time on every line). If you can only copy plain text, write the start time of the key line next to it.

## Step 3: open the kit in your chat
Paste this, then upload the transcript:
> Read https://raw.githubusercontent.com/Lemuel-A1/talent-social-video/main/KIT.md and follow its router prompt. I want to make a talk clip from the transcript I'm uploading.

If the chat says it cannot open the link, open the link yourself, save the page as `KIT.md`, and upload it with the transcript.

## Step 4: answer its questions
It will ask who is speaking, their role, consent, which account it is for, and the CTA. Use "follow" as the CTA for this test.

## Step 5: cut it in CapCut
The chat gives you a brief, an edit list (which seconds to keep, in order), the caption text and the on-screen text with timings. Build the cut from those. If Lemuel has shared the overlay pack (a folder called `capcut-pack`), use its headline, label, brand mark and CTA card; otherwise use plain CapCut text in the same places. Keep text out of the top and bottom of the screen.

## Step 6: export and check
Export 1080x1920. Go through the QC checklist the chat gives you. If you cannot measure loudness, say so in the report; Lemuel's side will measure it.

## Step 7: send back
For each clip: the exported video, the chat's brief and edit list (copy and paste is fine), and the filled report form.

## What good looks like
- The key line is heard in the first 2 seconds, and the same words are on screen.
- One idea, one speaker, 20 to 45 seconds.
- Captions readable on a phone; no text at the very top or bottom.
- The speaker's name and role are right.
- The voice is clear and not too quiet.


---

<!-- FILE: ROUTER_PROMPT.md -->
# FILE: ROUTER_PROMPT.md

# Router prompt: start here (any chat: Claude, ChatGPT, or a Project)

You help make Talent Social short videos for Instagram and other platforms. Talent Social is for professionals in and around Nairobi. Every file you need is in this kit. Read IDENTITY first, then CONFIG, then the format page and the skill you need.

## Before you start
- If you were given a link to `KIT.md`, you have the latest version. Check that you can see the line `END OF KIT` at the very end. If you cannot, the page was cut off: ask the person to download `KIT.md` from the link and upload it.
- If an upload starts with an AI-written summary, never quote it or take facts from it. Use only the transcript.
- Auto-caption transcripts mis-hear names and numbers. Treat every name and number as unconfirmed until the person confirms it.
- Ask the person for anything below that they have not given you. Do not guess.

## What to ask for
1. **The transcript.** Exported text from CapCut or Instagram auto-captions, or a pasted transcript. With times if possible (SRT is best). You cannot watch a video: do not ask for one.
2. **The format:** advice episode, game episode, event teaser, talk clip (panels, interviews, stage: `formats/talk-clip.md`), or "suggest one". If the footage fits none, say so. Also available: quick formats (`formats/quick-formats.md`) and the founder story (`formats/founder-story.md`). Not yet available: numbered series, news desk, making-of, build-in-public.
3. **People featured and consent.** For each person: how they spell their name, their role, and whether they are a public figure, have given written OK, or have given none. No consent and not a public figure: they are not in the clip. For event teasers, only faces that agreed.
4. **The account** it will post from (see `CONFIG.md`) and who the collaborators are.
5. **The CTA plan.** Default: "Follow for part 2" (episodes) or the event link (teaser). A game episode asks "Who do you think won?". A comment keyword only if a named person will send the replies.
6. **Anything to clear:** logos, client names, numbers, music, partner footage, anything said about who will attend.
7. For a teaser: the event name, date, area and link. If the person has not given them, leave `{{...}}` placeholders.

## The order
Pointed at a whole folder of footage, or asked to edit everything? Use skill 8 (`skills/8-batch-plan.md`) before anything else. Planning a shoot day first? Use skill 0 (`skills/0-shoot-plan.md`): it gives a shoot plan on `templates/shoot-plan.md`. Then, for each format folder of footage: transcript → skill 1 (brief) → skill 2 (edit list) → skill 3 (captions and type) → skill 4 (overlay list) → the person builds in CapCut or Canva → skill 5 (sound and master) → skill 6 (QC verdict) → the person posts → skill 7 (post copy and log).

Follow each skill's Input, Steps, Output and Checks. Show the brief and wait for an OK before the edit list.

## What you can and cannot do in chat
- You cannot watch video. Work from the transcript and the frames or screenshots the person uploads.
- You cannot measure. Loudness, true peak, silences, size and frame rate are UNMEASURED in chat. Say so in the QC verdict. Never invent a measurement.
- You cannot build animated overlays. You write their exact text and times from the format page. The person builds them in CapCut or Canva.
- You cannot write files. Where a skill says to add a log row or a lesson, give the text for the person to send to Lemuel.
- You cannot open the private claims register. Only the approved line below passes. Anything else about Vetted fails until Lemuel checks it.
- You cannot test links. Put them under MUST CONFIRM.
- If the person has Claude Code or Codex with this repo cloned, the agent steps in each skill add transcribing, silence cuts, burned-in captions, loudness mastering and measured QC.

## Rules that always apply
- Speakers say their own lines. Never put words in anyone's mouth. Hook lines are verbatim from the transcript with a source time.
- Never invent a fact, quote, name, role or number. Mark unknowns `{{NEEDS_VERIFICATION}}`.
- Naming people on screen:

  | What supports it | What to write |
  |---|---|
  | A labelled transcript, or someone who was there confirms it | the name and role |
  | Only the flow of the transcript or the event's own copy | the name and role, flagged MUST CONFIRM; the video does not post until confirmed |
  | Neither | no label |

- The only approved public claim about Vetted is "WorkPay cut its hiring cycle from 90 days to 30." No other client names. No client logos as proof. No unsourced "#1". No forward promise about who will be at an event.
- One CTA, said and shown, held 3 s (talk clips: shown only, unless the speaker said a line that works as one).
- Words: "assessment", never "audition". Never "proof of work". Never "can't cheat".
- Plain English. Short sentences. Cut rather than add.
- Never accept or copy contact lists, DMs, logins, or anyone's contact details. Nothing is posted by you.
- Keep the brand line "Talent Social · powered by Vetted" and the colours and type in `IDENTITY.md`.

## End of every run
Ask: "Any feedback to log?" If yes, write it as a lesson entry in this format, for the person to send to Lemuel:

```
### L-YYYY-MM-DD-NN · area · Short title
- What you said: "..."
- Lesson: ...
- Rule changed: none yet (Lemuel updates the kit)
- Evidence: the video and the moment
- Status: proposed
```


---

<!-- FILE: IDENTITY.md -->
# FILE: IDENTITY.md

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


---

<!-- FILE: CONFIG.md -->
# FILE: CONFIG.md

# Config (fill once; skills read this instead of guessing)

No logins, passwords or emails belong in this file.

| Item | Value | Status |
|---|---|---|
| Advice and game episodes | Post from @lemuel_abishua. Add @africaproductpeers and @talentsocial.network as collaborators. | decision recorded for v1 |
| Events, panels and teasers | Post from @africaproductpeers | decision recorded for v1 |
| Other platforms | TikTok, LinkedIn, WhatsApp: only from accounts the team owns and has confirmed | {{NEEDS_VERIFICATION}} |
| Brand line on video | "Talent Social · powered by Vetted" on the series bug of advice and game episodes. Talk clips, interviews and stories carry only a small quiet talentsocial.network at the bottom-left and the glass outro (no brand mark near faces) | decided 22 Oct |
| Asset folder (shared drive) | `{{DRIVE_ASSET_FOLDER}}` | name to fill. Holds footage, music, fonts, logos, the sting. Never in the repo. |
| Sting file | `sting-talentsocial.mp4` | placeholder name; the asset is made outside the repo |
| Sting sound alone | `sting-talentsocial-sound.wav` | placeholder name {{NEEDS_VERIFICATION}} |
| Brand mark file | `mark-talentsocial-powered-by-vetted.png` | placeholder name {{NEEDS_VERIFICATION}} |
| Sting sound licence | `{{NEEDS_VERIFICATION}}` | licensed or composed; record the source |
| Export preset | 1080x1920, 9:16, H.264 video, AAC audio, 30 fps | |
| Loudness target | -14 LUFS (accept -15 to -13), true peak at or below -1 dBFS | |
| Shoot-day file names | `YYYYMMDD_EVENT_CAM_FORMAT_SUBJECT_TAKE`, one folder per format, uploaded the same night | see `skills/0-shoot-plan.md` |
| Export files | one voice-only master per post; a music version only for licensed tracks | |
| File names | `{format}-{episode}-{platform}-{voice-or-music}.mp4`, for example `advice-ep03-ig-voice.mp4` | platform codes: `ig`, `tt`, `li`, `wa` |
| Music | add inside the platform at upload where possible | licence stays with the platform |
| Safe zones (1080x1920) | top 220 px, bottom 380 px, right 140 px | usable band y 220 to 1540 |
| Fonts | Inter Tight (variable, open licence, Google Fonts): `InterTight[wght].ttf` and `InterTight-Italic[wght].ttf` | keep them outside the repo, in `~/.local/share/vetted-video/fonts` or `$TS_FONT_DIR`; the tools find them there. The gold serif payoff uses Didot Italic on macOS |
| `STT_PYTHON` | a Python 3 from a virtual environment that has faster-whisper, numpy and Pillow, for example `~/.local/share/vetted-video/stt/bin/python` | set once per machine. `export STT_PYTHON=<path>`. Tools that need only Pillow run with any python3. |
| System tools | `ffmpeg` and `ffprobe` on the path | some builds lack the `subtitles`, `ass` and `drawtext` filters; the tools draw captions with Pillow and use `overlay` |
| Claims register | private; ask Lemuel | if you cannot open it (for example, using the public kit), only the approved line in `IDENTITY.md` section 10 passes |
| Event link, date, area | supplied per teaser | `{{EVENT_LINK}}`, `{{DATE}}`, `{{AREA}}` |

## Colour and type

Values and status: `templates/caption-style.json`. Brand v2 values were measured from talentsocial.network on 22 Oct 2026 (see `IDENTITY.md` section 3).

## Defaults

- Shoot days: plan with `skills/0-shoot-plan.md` and `templates/shoot-plan.md`. Format pages added: `formats/quick-formats.md`, `formats/founder-story.md`.
- Episodes: follow-for-part-2 CTA. Game episode: the comment question.
- Teasers: the event link, said and shown.
- No music in the exported file unless its licence is recorded.


---

<!-- FILE: formats/advice-episode.md -->
# FILE: formats/advice-episode.md

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


---

<!-- FILE: formats/game-episode.md -->
# FILE: formats/game-episode.md

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


---

<!-- FILE: formats/event-teaser.md -->
# FILE: formats/event-teaser.md

# Format: event teaser

Read `../IDENTITY.md` first. Numbers there win.

## Purpose
Invite people to the next Talent Social event. One claim, real faces, one reason to come, then the date and link. This is the one v1 format that asks. Keep it short and clear.

## Length
12 to 25 s. Aim for 15 to 20 s. The times below are for an 18 s cut.

## Gate: faces and consent
Use only people who agreed to appear. Attendees at past events may not have agreed to marketing use. Until the team confirms that registration terms cover it, use only faces with a recorded OK. No consent, no clip. Ask Lemuel.

## Shape, beat by beat
| Output time | Beat | On screen | Sound |
|---|---|---|---|
| 0.0 to 2.0 | **Claim** | A face mid-gesture, already moving. One-line claim as a headline from the first frame. | A hit on the claim. Music in. If a host speaks the claim, the voice starts by 0.3 s. |
| 2.0 to 3.2 | **Sting** | Talent Social card | Sting sound |
| 3.2 to 14.2 | **Faces and one reason to come**: about 8 shots of 1.2 to 1.5 s | Hard cuts on the beat. Captions read as one sentence across the shots. Up to 2 name labels. | Music; a short hit at the midpoint |
| 14.2 to 18.0 | **Date and link card**, held at least 3 s | Event name, date and area, link | Host voice-over says it. Music dips under it. |

Rules:
- Picture change every 1 to 2 s after the sting.
- The first frame is a face, not black and not a logo.
- No split screen that delays the claim.

## Hook options
The first-2-seconds rule: the claim is on screen from frame 1 and, if a person speaks, the first word lands by 0.3 s (QC passes up to 2 s). It must make sense with the sound off.
1. **A sourced fact from the last event**, in the past tense: `{N} {THINGS} AT {LAST EVENT}`. The number needs a source: {{NEEDS_VERIFICATION}} until Lemuel gives one.
2. **What the room is for**: `A ROOM FOR {WHO} TO {DO WHAT}`. Describe what we control. Never who will be there.
3. **A real line from a past guest**, said on camera by that guest with consent, as the cold open.
Never: "#1" without a source, "recruiters will be there", a logo wall, "participants from" lists. The brand tagline is {{NEEDS_VERIFICATION}}: ask Lemuel which one to use.

## Captions and labels
- Captions: sentence case, 2 to 5 words, white with soft shadow, 55 to 70% height, one gold word at most. They are the claim and the reason, not the speech, unless a person speaks.
- Up to 2 labels (`{NAME}` white on charcoal, `{ROLE}` gold), 2 s each, only for people who agreed and whose role is confirmed. Otherwise no label.

## Overlays (a person builds these in CapCut or Canva)
Times are output times in an 18 s cut.

| Element | Exact text pattern | In | Out | Notes |
|---|---|---|---|---|
| Claim headline | `{ONE LINE CLAIM}` caps, one gold word | 0.0 | 2.0 | 20 to 35% height; one line if it fits |
| Sting | Talent Social mark card | 2.0 | 3.2 | File in `CONFIG.md` |
| Brand mark | `Talent Social · powered by Vetted` | 3.2 | end | Top-left, y 220 or lower |
| Caption arc | up to 3 short lines, up to 5 words each, one sentence in total | 3.2 | 13.5 | Switch on the cuts |
| Label | `{NAME}` over `{ROLE}` | any shot | +2 s | Up to 2 |
| Date and link card | `{EVENT NAME}` / `{DATE} · {AREA}` / `{LINK or LINK IN BIO}` | 14.2 | 18.0 | Held 3 s or more. Bottom edge above 1540 px. Clear of the right 140 px. |

No colour wash, no emoji, no logos on the card except the Talent Social mark.

## CTA
One: the event link. The host says it (for example, "{EVENT NAME} is on {DATE}. Link in bio.") and the card shows it. Record a short host line for this if no one speaks in the footage. A shown-only CTA is a FIX.

## Sound
- Music is the bed. Add it in the platform at upload where possible; otherwise use a licensed file and record the licence.
- Short hits on the claim (0.0 s), the midpoint, and the card. These are the audio hook. No riser longer than 1 s.
- Cut on the beat. The baseline cut about every 1.2 s.
- Voice-over only on the final card. Dip the music under it.
- Master the exported file to -14 LUFS (accept -15 to -13), true peak at or below -1 dBFS.

## QC thresholds
Runtime 12 to 25 s. First frame not black, not a logo. Claim on screen by 0.3 s. Picture change every 1 to 2 s. Link card held 3 s or more, above y 1540. CTA said and shown. No silence over 0.4 s. Loudness and true peak as above. Consent recorded for every face. Full table: `../IDENTITY.md` section 12.

## Worked example: the baseline teaser "short v5" (15 s)
**What the baseline did**
- Good: cuts on a steady beat of about 1.2 s; a one-sentence caption arc across shots; yellow emphasis on white; smiling faces; a branded end card with a link button; level near the target loudness.
- Weak: the first frame was black; the first label was an unsourced "#1" claim; a wall of local-employer logos, with a "participants from" line, was small and partly unreadable and sat in the bottom zone; an off-palette colour wash; the link button was shown for about 1.5 s in the bottom zone and never said; no designed audio hook; no names or reason a viewer could use.

**What v1 would do**
- Open on the waving face with the claim as a headline from frame 1. No black frame.
- Replace "#1" with a sourced past-tense fact, or a line about the room we control.
- Drop the logo wall and the "participants from" line. No colour wash.
- Add the sting after the claim, a short hit on the claim and at the midpoint.
- Keep the beat-grid cuts and the one-sentence caption arc.
- End on the date and link card, held 3 s, above y 1540, with a host line over it.
- Check consent for every face before export.

## Reference posts (public handles; patterns, not copy)
- **sendthecv**: a local career series that puts a branded sting on a black card shortly after the guest's first line, with a sound, and reuses one caption template in every post. Copy the sting placement and the template habit. Their accent is lemon yellow; our gold stays warmer.
- **techcabal**: African tech media. Use as the cautionary example: long event and talking clips draw little. Copy only the series bug on the clip.
- **thediaryofaceopodcast**: cold open on the single most surprising line, then a big headline with one coloured word. Copy the line-first habit; keep our runtime short.


---

<!-- FILE: formats/quick-formats.md -->
# FILE: formats/quick-formats.md

# Format bank: quick formats

Read `../IDENTITY.md` first. If this page and that file disagree, that file wins (safe zones, captions, CTA, claims, loudness).

## Purpose
Fifteen short series the team can shoot in one sitting (see `../skills/0-shoot-plan.md`). Each is a repeatable shell with a prompt bank. The full banks are in the team's content playbook; use the prompt IDs below to find them.

## The fifteen series
| Series | Format | Usual length | Face on camera |
|---|---|---|---|
| Flag Check | Red flag or green flag | 20 to 40 s | Yes |
| Pick One | This or that | 20 to 35 s | Yes |
| Tier Talk | Tier list | 35 to 60 s | Yes |
| Three Ways | Bad, good, great | 30 to 50 s | Yes |
| Level Up | Levels | 30 to 50 s | Yes |
| Fast List | Rapid-fire list | 25 to 45 s | Optional |
| Swap It | Don't say, say instead | 20 to 40 s | Yes |
| Overrated or Underrated | Overrated or underrated | 20 to 40 s | Yes |
| Daily, Weekly, Monthly | Habits | 30 to 50 s | Yes |
| Two of Me | Dual role | 30 to 60 s | Yes |
| Show Me | Explainers | 40 to 60 s | Yes |
| Inside Vetted | Product video | 45 to 60 s | Voice-over works |
| Inside Copilot | Product video | 45 to 60 s | Voice-over works |
| One Honest Answer | Walk, car, podcast | 20 to 90 s | Yes |
| Debate Night | Walk, car, podcast | 20 to 90 s | Yes |

Write "[Brand]'s Copilot" on screen at least once, so it is not mistaken for another company's tool.

## Five beats (every video)
| Beat | Time | Job | Rule |
|---|---|---|---|
| Visual hook | 0 to 1 s | Something to see in frame one: a face, a prop, a card, a board | No logo intro, no "hi guys", no fade in |
| Spoken hook | 0 to 3 s | One line, 12 words or fewer, the same words on screen | One promise only |
| Setup | 3 to 8 s | Say who it is for and what they get | "If you are applying for {role}" or "Employers:" |
| Payoff | 8 to 35 s | The content, in beats of 3 to 5 s, a picture change every 2 to 3 s | Answer first, reasons second |
| Close | last 3 to 5 s | One action | End on the payoff, not a goodbye. Best: loop back to the hook line |


## Seven hook types
| Type | Pattern | Example |
|---|---|---|
| Callout | Name the person, tell them to stop | "Graduate applying for a first job? Stop writing 'career objective.'" |
| Contradiction | Say what everyone says, then why it stalls | "Everyone says apply to more jobs. Here is why that stalls." |
| Verdict | Quote a phrase, ask for the call | "'We're like a family.' Red flag or green flag?" |
| Challenge | Give the viewer a short task | "You have 15 seconds to fix this message." |
| Proof | Show the real thing | "This is what a skills assessment looks like." |
| Stakes | Name what one choice could cost | "This one phrase can get your CV skipped." |
| Split | Offer two options | "Candidate A or Candidate B?" |

A Proof hook about Vetted's results passes only with the approved line in `../IDENTITY.md` section 10.

## Edit rules
- Captions on every video, two lines at most, one key word in gold (see `../templates/caption-style.json`).
- A cut, zoom or on-screen change every 2 to 3 s. In a one-shot talk, punch in on the key phrase.
- Cover frame: 5 words or fewer, large, readable on a phone.
- Clean audio first: a quiet room and a lav mic beat a good camera.
- Export a clean copy for each platform. Do not re-post a clip with another platform's watermark.

## Prompts: two per series
Find the full bank in the team's content playbook by ID.

| Series | Prompt ID | Prompt |
|---|---|---|
| Flag Check | RG-J01 | Ad says "competitive salary": red. Ask for the range first. |
| Flag Check | RG-J03 | Ad says "we're like a family": red. Ask about hours and overtime. |
| Pick One | TO-01 | Referral or cold apply: referral. |
| Pick One | TO-17 | CV screen or skills test (hiring side): skills test first. |
| Tier Talk | TL-01 | Rank job-search tactics, S to F. |
| Tier Talk | TL-03 | Rank ways to screen a candidate. |
| Three Ways | BG-C02 | A customer-service CV bullet, three ways. |
| Three Ways | BG-M01 | A first message to a hiring manager, three ways. |
| Level Up | LV-03 | A LinkedIn profile at three levels. |
| Level Up | LV-05 | Employer hiring at three levels, up to a scored skills assessment. |
| Fast List | RF-01 | Twenty reasons a CV gets skipped, read fast. |
| Fast List | RF-05 | Fifteen things job scams have in common. |
| Swap It | DS-I01 | Don't say "I'm a perfectionist." Say what you changed. |
| Swap It | DS-S01 | Don't say "I need more because rent is high." Tie the number to scope. |
| Overrated or Underrated | OU-01 | Job-search advice: a perfect template is overrated, results are underrated. |
| Overrated or Underrated | OU-02 | Interview advice: a memorised script is overrated, three real stories are underrated. |
| Daily, Weekly, Monthly | HB-01 | Job-search habits, daily, weekly and monthly. |
| Daily, Weekly, Monthly | HB-02 | Hiring habits for founders, daily, weekly and monthly. |
| Two of Me | DR-01c | "What's your weakness?" as Candidate A and B, then a verdict. |
| Two of Me | DR-02 | What you say versus what the recruiter hears. |
| Show Me | EX-02 | The 10-second CV test: three CVs, ten seconds each, out loud. |
| Show Me | EX-03 | What a skills assessment looks like, on a screen recording. |
| Inside Vetted | PR-01 | Vetted in 60 seconds, employer side. |
| Inside Vetted | PR-03 | Vetted for talent: a skills task instead of a CV. |
| Inside Copilot | PR-04 | Answer badly on purpose, then fix it with feedback. |
| Inside Copilot | PR-05 | A full mock interview in under a minute. |
| One Honest Answer | WT-01 | "What's one thing about getting hired people don't want to hear?" |
| One Honest Answer | WT-01 | "What's one thing hiring managers do that candidates never see?" |
| Debate Night | DB-01 | "Brilliant coder, can't explain anything. Hire or pass?" |
| Debate Night | DB-01 | "Should companies state salary in every job ad?" |

The speaker answers in their own words. A prompt is never a script.

Close: one CTA. A comment keyword (such as the playbook's "Comment CV") only when a named person will send the replies.

## Local facts (named sources, check the live page before use)
- Kenya News Agency reported education stakeholders estimating about 1.2 million learners graduating a year against about 100,000 jobs created. Say "estimated".
- Fuzu's guidance: refuse fees for applications, interviews, shortlisting, training, uniforms, medicals, placement or visas; verify the company on eCitizen's Business Registration Service.
- The National Employment Authority says real vacancies appear only on its official website and its NEAIMS system.
- Corporate Staffing: Kenyan recruiters mark down a careless file name, informal email, dense paragraphs, mixed dates and needless personal details.


---

<!-- FILE: formats/founder-story.md -->
# FILE: formats/founder-story.md

# Format: founder story

Read `../IDENTITY.md` first. Numbers there win.

## Purpose
A personal or behind-the-scenes video by Lemuel or Tobi: a day in the life, an office visit, travel, a launch moment. It gives the viewer a person to follow. One speaker, to camera or voice-over, six beats. A story, not a pitch. Plan the footage with `../skills/0-shoot-plan.md`.

## The six beats
| # | Beat | What it does | Rule |
|---|---|---|---|
| 1 | **Time and physical action** | Ground the viewer in one moment: when, what you did, where | Never open with a stat, a question or "I'm excited to share" |
| 2 | **Counter-narrative** | Name what you left or had, and make it good | Not "I left because it was bad" |
| 3 | **Stacked questions** | Three questions in a row, voiced. The viewer is asking them too | Do not answer at once. Slow the pace |
| 4 | **The honest truth** | The real reason. The peak of the video | Say "the honest truth is" once, here only |
| 5 | **The promise** | What you will do: document, test, build, ship | Action verbs. Nothing you cannot do |
| 6 | **Anti-perfection and hook** | Say it will not be clean, then promise one specific payoff to follow | Gives the viewer a reason to follow |

Beat 1 is the first spoken line, at 0 to 0.3 s. A headline is on screen from frame 1, as in `../IDENTITY.md`.

## Voice rules
- Declarative, not interrogative. Say it. Do not ask the viewer to imagine.
- Specific, not abstract: a real place, a real time. A number only if it is in the claims register.
- Short, simple sentences. If you need a breath in the middle, cut it.
- No copywriter tricks: "Imagine if", "Picture this", "What if I told you", "I'm thrilled to announce", "It's been an incredible journey".
- "I" for the personal arc, "we" for team work.
- Name a person only if they agreed and the brief records it. No names in the public kit.
- Direct address once or twice a video, when it puts the viewer in their real day.
- One bold claim, no hype words such as "revolutionary", "cutting-edge", "world-class", "game-changing", "incredible".
- Speakers say their own lines.

## Numbers and claims
The team's video-series spreadsheet holds example figures (candidates evaluated, hires, countries). They are **not approved. Do not copy them.** A figure about Vetted's results comes only from the claims register, or is the approved line in `../IDENTITY.md` section 10. No approved figure: leave `{{FROM_CLAIMS_REGISTER}}` and say the beat without a number.

## Effort tiers
| Tier | Time | Use | Look |
|---|---|---|---|
| HIGH | 4 to 6 h | Anchor moments, about one a month | Multi-shot, scripted, several takes, riser and impact, heavy edit. 80 to 90 s |
| MEDIUM | 2 to 3 h | Real moments with weight | Scripted but lighter, talking head and b-roll, light music, hard cuts, one shoot session. 50 to 75 s |
| LOW | 30 to 90 min | Weekly, life as it happens | Selfie mode, auto-captions, one take or hard cuts, minimal edit. 30 to 45 s |

Do not make a celebration video for a sale. Tell it as a customer story, only with their written permission and only the approved line.

## Sound design
- **Riser** at the open: slow swell, no harsh end.
- **Music** 15 to 18 dB under the voice. Instrumental, 80 to 100 BPM, no vocals.
- **One impact note** at the turn: the line in beat 4 where everything changes. One only.
- Music swells through the promise (beat 5), then resolves before beat 6.
- **Music ends rather than fades.** The last 2 s resolve to silence or a held note.
- **Room tone always** under talking head. Record 30 s in each room.
- Loudness and licences: `../IDENTITY.md` section 8. Record the licence of every track and effect before posting.

## Shot library
Capture once, reuse. 9:16, plus a wide where useful.
1. Walking shots, filmed by someone else, low angle.
2. Main talking head: plain wall, window light, eye level, 3 to 4 ft from camera.
3. Selfie talking head, for raw moments.
4. Work b-roll: whiteboard, laptop, hands sketching. No client logos.
5. Past community footage: only people who agreed.
6. Travel and transition shots.
7. Screens: product and work in progress. No client names.
8. Team shots: only people who agreed.
9. End-frame templates, made once in Canva with the brand line.

## Worked outline: a MEDIUM office-visit story (about 60 s)
Braces are filled from the real footage. Nothing here is a fact.

| Time | Beat | Line (the speaker's own words) | Picture | Sound |
|---|---|---|---|---|
| 0 to 6 | 1 | "{Time} ago, I {physical action} in {place}." | One walking shot. Caption: the time | Ambient, riser starts |
| 6 to 18 | 2 | "{Where we were} was good. {One true, good thing}." | Past footage, consented | Music in, low |
| 18 to 28 | 3 | "So why {leave or change}? Why {second}? Why {third}?" | Talking head, music dips | Pace slows |
| 28 to 42 | 4 | "The honest truth is {the real reason}." | Talking head, one cut to b-roll | Impact on the turn line |
| 42 to 52 | 5 | "I'm going to {document, test, build}. {Figure from register, or none}." | Quick cuts of work | Music swells, resolves |
| 52 to 60 | 6 | "It won't be clean. {One specific thing the viewer will get}. Follow for it." | Talking head, CTA card held 3 s | Room tone, music ends |

Before export: watch it on mute (captions and picture tell the story); no unapproved figure; consent on every face; one CTA, said and shown.


---

<!-- FILE: formats/talk-clip.md -->
# FILE: formats/talk-clip.md

# Format: talk clip (panels, interviews, stage moments)

Read `../IDENTITY.md` first. Numbers there win.

## Purpose
Turn one idea from a panel, an interview or a stage moment into a short clip someone who was not in the room still wants to watch. One speaker, one idea, their own words.

## Length
20 to 45 s. Aim for 30 to 40 s.

## Choosing the line (do this before cutting)
- Pick the most surprising or most useful line in the recording, not the first one. It can come from anywhere in the recording.
- It must make sense with no context, and it must be one idea.
- The speaker has consented (the speaker form for panelists, a release for interviews). No consent, no clip.
- No names of third parties unless they are public figures. No claim about Vetted except the approved line in IDENTITY.
- No audience faces unless those people agreed.
- From a 40-minute panel, take up to 5 clips per speaker, ranked. Brief the best first.

## Shape, beat by beat
| Output time | Beat | On screen | Sound |
|---|---|---|---|
| 0.0 to 3.0 | **Hook**: the chosen line, in the speaker's words | Speaker, tight frame. Headline from frame 1 with the same words (or a faithful short version), one gold word | Voice from 0 to 0.3 s |
| 3.0 to 5.0 | The speaker finishes the thought, if needed | Speaker | Voice |
| 5.0 to 8.0 | **Label** (at the first full sentence after the hook) | `{NAME}` over `{ROLE}` exactly as the speaker form or event copy gives them | Voice |
| 8.0 to 32.0 | **The idea**: the reason, the example, the how | Punch-in or cutaway every 3 to 5 s (other camera angle, the speaker's hands, the room wide) | Voice; one whoosh at most |
| 32.0 to 36.0 | **Landing line**: the sentence that closes the idea | Speaker, still frame | Voice |
| 36.0 to 39.0 | **CTA** | CTA card held 3 s | The CTA is said only if the speaker said something that works as one; otherwise shown only, with the caption |

The sting is optional in talk clips: use it only if the hook ends cleanly at a sentence break.

## Hook patterns (fill with the speaker's own line)
1. **Stake:** a line that names a cost or a risk the viewer has.
2. **Contradiction:** a line that disagrees with common advice.
3. **Number:** a number the speaker said themselves, with its unit.
4. **Answered question:** cut the question from the moderator into the first second, then the speaker's answer.
Never write a hook line the speaker did not say. If no line works, the recording does not have a clip: say so.

## Captions, labels and overlays
- Captions per IDENTITY: sentence case, 2 to 5 words, 55 to 70% height, at most one gold word.
- Overlays from the overlay pack: `headline` (0 s to the label), `brand-mark` (from 5 s), `label` (3 s), `cta-card` (last 3 s). Plain CapCut text in the same positions works if the pack is not to hand.
- Nothing in the top 220 px, the bottom 380 px or the right 140 px.

## Audio for room recordings
- Use the best mic channel (the lav or the desk mic), not the camera's built-in mic.
- Reduce room noise lightly; do not make the voice sound underwater.
- Master to -14 LUFS (accept -15 to -13), true peak at or below -1 dBFS.

## QC thresholds
Runtime 20 to 45 s. First spoken word within 2 s. First frame not black and not an empty room. Label matches the speaker form. Consent recorded. One idea, one CTA. Full table: `../IDENTITY.md` section 12.

## Worked example: a partner roundtable recap (baseline)
- **What it did:** opened on an empty room and the venue banner; the first person appeared at about 5 s; a strong spoken line about AI making good work easier sat at 1 s, uncaptioned, under b-roll; no names, no captions, no CTA.
- **What v1 would do:** cut straight to the speaker saying that line at 0 s, with it as the headline; label the speaker at 5 s; keep the best 30 s of the answer with two cutaways; end on the landing line and a follow CTA card.

## Reference posts (patterns, not copy)
- **thediaryofaceopodcast:** cold open on the most surprising line; a big headline with one coloured word; then small sentence-case captions.
- **hormozi:** one idea per clip, plain frame, quiet captions, no filler.


---

<!-- FILE: skills/0-shoot-plan.md -->
# FILE: skills/0-shoot-plan.md

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


---

<!-- FILE: skills/1-footage-to-brief.md -->
# FILE: skills/1-footage-to-brief.md

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


---

<!-- FILE: skills/2-rough-cut.md -->
# FILE: skills/2-rough-cut.md

---
name: video-2-rough-cut
description: Build the edit decision list for a Talent Social video from the brief, and at the agent tier cut silences and assemble the rough cut. Use after the brief is approved.
---

# 2. rough-cut

Read `../IDENTITY.md` first, then the format page named in the brief.

## Input
- The approved brief (`../templates/brief.md`).
- The transcript with times (chat) or the footage (agent).

## Steps
1. **[chat] Build the EDL.** One row per kept segment, in the order they play: `start,end,reason`, in seconds of the source (`../templates/edl.csv`). Follow the format's beat table. The first spoken line is first: it starts at 0 to 0.3 s of the cut. Reasons are short: `hook`, `context`, `point 1`.
2. **[chat] List silences and fillers to remove.** From the transcript times: gaps over 0.4 s, and filler words ("um", "uh", false starts, repeats). Split the EDL rows around them. Keep a deliberate beat (a laugh, a pause for effect) and mark it in the brief.
3. **[chat] Convert source time to output time.** Add up the kept lengths. Write both times in the brief's beat table and overlay list. Overlays use output time.
4. **[chat] Mark the sting.** A 1 to 1.5 s gap right after the first line. The sting is added later; leave a marker row in the brief, not in the EDL.
5. **[chat] Plan the picture changes.** Episodes: a punch-in, card, wipe or cutaway at least every 5 s, ideally every 3 to 5 s. Teasers: every 1 to 2 s. List the punch-in times in the brief. Punch-ins are 10 to 15%.
6. **[chat] Check the series card.** No title card before the first line. The series name is a small bug (see the format page).
7. **[agent] Cut the silences.** Run `$STT_PYTHON tools/cut_silence.py <in.mp4> <out.mp4> --min-silence 0.4 --pad 0.08 --threshold -35 --edl edl.csv`. It writes the kept segments as `edl.csv`. Compare it with the chat EDL. Keep the chat EDL where they differ on structure.
8. **[agent] Assemble the cut.** Apply the final EDL with ffmpeg directly (trim and join the kept segments; export 1080x1920, 30 fps, H.264, AAC). No v1 tool applies a hand-edited EDL. Do not add overlays: a person builds them (skill 4).
9. **[chat] Check the runtime.** After cuts, add up the length. If outside the format's range, cut a whole beat or loosen the cuts. Never speed up speech.

## Output
- `edl.csv` (chat and agent).
- The brief with output times filled in and the picture-change list.
- A rough cut file (agent).

## Checks
- Runtime inside the format's range.
- The hook line plays within the first 2 s; target 0 to 0.3 s.
- No black or logo first frame.
- No silence over 0.4 s left, except marked beats.
- No cut removes a word that a caption or claim depends on.
- Each episode point still ends with its action.

## Use in another tool
Paste `IDENTITY.md`, this file, the brief and the transcript. Ask for the EDL and the output-time table. Cut in CapCut or Canva from it.


---

<!-- FILE: skills/3-captions-and-type.md -->
# FILE: skills/3-captions-and-type.md

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


---

<!-- FILE: skills/4-brand-and-motion.md -->
# FILE: skills/4-brand-and-motion.md

---
name: video-4-brand-and-motion
description: Produce the overlay list for a Talent Social video (brand mark, series bug, sting, tabs or ledger, cards, punch-ins, CTA card) with exact text and timings, for a person to build in CapCut or Canva. Use after captions.
---

# 4. brand-and-motion

Read `../IDENTITY.md` first, then the format page. In v1 the agent does not build animated overlays. It writes their text and timings. A person builds them.

## Input
- The captioned cut and the brief (with output times).
- The format page's overlay table.

## Steps
1. **[chat] Fill the overlay list.** One row per element from the format page: output time in and out, element, exact text, notes. Use the text patterns exactly. Keep it in the brief's section 5.
2. **[chat] Place the brand mark and series bug.** Top-left, y 220 px or lower, from the sting to the end. Bug text from the format page.
3. **[chat] Place the sting.** Right after the first line, 1 to 1.5 s, never frame 1. Name the file from `CONFIG.md`.
4. **[chat] Place the series overlays.** Advice: three tabs, active tab gold, checklist cards. Game: the ledger and price badges. Check each sits inside x 0 to 940, y 220 to 1540, clear of faces and captions.
5. **[chat] Place punch-ins and wipes.** Punch-ins 10 to 15% every 3 to 5 s on talking heads. One transition style: the gold band wipe, only between sections.
6. **[chat] Place the CTA card.** One CTA, text from the format page, held 3 s, bottom edge above y 1540, with the spoken line under it.
7. **[chat] Hand the list to the person to build in CapCut or Canva.** Say plainly that the agent has not built it. The person builds the overlays, then sends the file back for skill 5.
8. **[agent] Check what can be checked.** After the build, make a contact sheet (`$STT_PYTHON tools/contact_sheet.py <video> <sheet.jpg>`) and look at it for overlay position and overlap. Do not try to build overlays with ffmpeg in v1.

## Output
The overlay list with times and exact text. The built video comes from the person.

## Checks
- One transition style only.
- No element covers a face or a caption.
- One overlay card on screen at a time; no ghosting.
- No emoji, cartoon sprite, light leak, glitch burst or colour wash.
- The CTA card is held 3 s and sits above y 1540.
- No client logo, logo wall or unsourced claim anywhere.

## Use in another tool
Paste `IDENTITY.md`, this file, the format page and the brief. Ask for the overlay list. Build it in CapCut or Canva.


---

<!-- FILE: skills/5-audio-and-master.md -->
# FILE: skills/5-audio-and-master.md

---
name: video-5-audio-and-master
description: Plan the sound for a Talent Social video (sting, whooshes, music) and master it to -14 LUFS with true peak at or below -1 dBFS. Use after the overlays are built.
---

# 5. audio-and-master

Read `../IDENTITY.md` first (section 8) and the format page's Sound section.

## Input
- The branded cut (overlays built by the person).
- The sting file name from `CONFIG.md`.
- Music plan: added in the platform, a licensed file, or none.

## Steps
1. **[chat] Write the sound plan.** List: the sting at its output time; whooshes on section changes only; any hits (teaser); where music comes in. Music sits 15 to 20 dB under the voice. No lyrics under speech.
2. **[chat] Decide the music route.** Default: add music inside the platform at upload, so the platform keeps the licence. Also export a clean voice-only master. For LinkedIn and WhatsApp, a music version only if the track is licensed and the licence is recorded in the brief.
3. **[chat] Hand the sound edit to the person.** In CapCut or Canva they level the voice, reduce room noise, place the sting sound and whooshes, and export H.264 at 1080x1920, 30 fps, with AAC audio (`../CONFIG.md`). In chat, loudness cannot be measured: mark it UNMEASURED in the brief.
4. **[agent] Master the loudness.** Run `sh tools/loudness.sh <in.mp4> <out.mp4> -14`. It runs two passes, targets -14 LUFS and true peak -2 so the AAC output stays at or under -1.5 dBFS, and prints the measured I and TP of the output. Use the output as the voice-only master.
5. **[chat] Name the files.** `{format}-{episode}-{platform}-{voice-or-music}.mp4`, for example `advice-ep03-ig-voice.mp4`. Platform codes: `ig`, `tt`, `li`, `wa`.
6. **[chat] Record licences.** Music title, source and licence for every track in a file. Sting sound source and licence. Font licence (Poppins, OFL). Blank means not cleared.

## Output
- Final files named as above, including a voice-only master.
- The measured loudness and true peak printed by the tool (agent), or UNMEASURED (chat).
- A licence note in the brief.

## Checks
- Integrated loudness -14 LUFS; accept -15 to -13.
- True peak at or below -1 dBFS.
- Voice-only master exists.
- No music in a file without a recorded licence.
- No silent tail: the last spoken word or sound ends within about 0.5 s of the end.

## Use in another tool
Paste `IDENTITY.md`, this file and the brief. Ask for the sound plan and the file names. Measure with the agent tier or ask the person to run the agent tier before posting.


---

<!-- FILE: skills/6-qc-check.md -->
# FILE: skills/6-qc-check.md

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


---

<!-- FILE: skills/7-post-and-log.md -->
# FILE: skills/7-post-and-log.md

---
name: video-7-post-and-log
description: Write the post copy for a Talent Social video, pick the cover frame, and log its performance at 48 hours and 7 days with one lesson. Use after QC says READY.
---

# 7. post-and-log

Read `../IDENTITY.md` first (sections 9 and 11).

## Input
- The final video and its brief, with a READY verdict.
- Later: the numbers from the Instagram app insights, typed by the person.

## Steps
1. **[chat] Write the caption.** On `../templates/post-copy.md`. Line 1 is the hook and is true to the video. One or two plain lines on what the viewer gets. The one CTA, the same as in the video. 3 to 5 hashtags.
2. **[chat] Pick the cover frame.** A clear face, headline visible, nothing in the unsafe zones. Give the time.
3. **[chat] Choose the account and collaborators.** From `../CONFIG.md`: advice and game episodes from the personal account with the two partner accounts as collaborators; events and panels from the partner account. Add the collaborators in the app before posting.
4. **[chat] Run the caption checks.** No claim the video does not support. No "#1", no forward promise, no unsourced number. Any Vetted claim is the approved line.
5. **[chat] Log at 48 hours.** The person types: views, average watch time, shares, saves, follows (from the app insights, not the web view). Add one row to the performance log (`../templates/performance-log.csv` columns). Chat cannot write files: give the row as text for the person to send to Lemuel.
6. **[chat] Log at 7 days.** The same fields in the same row.
7. **[chat] State what changed.** One thing that differs from the last post of this format (hook type, length, CTA, cover, posting time). If two things changed, say the cause is unknown.
8. **[chat] Write one lesson.** In the lesson format in `../ROUTER_PROMPT.md`.
9. **[agent] Append the row and the lesson** to `log/performance-log.csv` and `log/LESSONS.md`. Never edit earlier entries.

## Output
- Post copy, cover time, account and collaborators.
- A performance-log row (48 hours, then 7 days).
- A lesson entry (chat: text to send to Lemuel).

## Checks
- One change measured per post.
- Judged by views, average watch time, shares, saves and follows. Not likes alone.
- No claim in the caption that the video does not support.
- Numbers come from the app insights, never from memory.
- No viewer names or comments with personal details in the log.

## Use in another tool
Paste `IDENTITY.md`, this file, the post copy template and the numbers. Ask for the log row and the lesson.


---

<!-- FILE: skills/8-batch-plan.md -->
# FILE: skills/8-batch-plan.md

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


---

<!-- FILE: templates/shoot-plan.md -->
# FILE: templates/shoot-plan.md

# Shoot plan

Fill every line. Unknowns are `{{NEEDS_VERIFICATION}}`. Made with `../skills/0-shoot-plan.md`.

## 1. Header
- Event or day:
- Date and venue:
- Output target (finished videos, by format, and by when):
- Producer:

## 2. Crew
| Role | Person | Kit they carry |
|---|---|---|
| Camera A | | |
| Camera B or phone | | |
| Audio | | |
| Producer (shot list and timing) | | |
| Consent desk | | |

## 3. Kit list
| Item | Count | Owner | Checked |
|---|---|---|---|
| Cameras and phones | | | |
| Lav mics (one per speaker, plus spares) | | | |
| Stands, lights | | | |
| Batteries, cards, storage | | | |
| Consent sign and QR code | | | |

## 4. Room map
| Room | Use | Noise and light | Room tone done (30 s) |
|---|---|---|---|
| Quiet room | To-camera episodes | | |
| Two-shot set | Games | | |
| Portrait corner | Guest stories | | |
| Roaming | Behind the scenes | | |
| Main room | The event | | |

## 5. Timed blocks
| Time | Room | Format | Who | Prompts | Camera and audio | Target clips |
|---|---|---|---|---|---|---|
| | | | | | | |

Every row needs a format, prompts, a mic plan and a consent plan.

## 6. Consent plan
- Sign placed at:
- Release (QR) link: `{{RELEASE_LINK}}`
- Who keeps the yes list:
- Public figures (named here):
- Rule: no yes, no clip.

## 7. File naming
`YYYYMMDD_EVENT_CAM_FORMAT_SUBJECT_TAKE`, one folder per format. Upload the same night to `{{DRIVE_ASSET_FOLDER}}`.

## 8. Hand-off
- Folders to run through skill 1, in order:
- Who runs them, and by when:
- Clips per format against target (fill after upload):


---

<!-- FILE: templates/brief.md -->
# FILE: templates/brief.md

# Video brief

Fill every line. Unknowns are `{{NEEDS_VERIFICATION}}`. Times are in the finished video unless marked "source".

## 1. Basics
- Working title:
- Format: advice episode | game episode | event teaser
- Series and episode number (if a series):
- Account to post from, and collaborators (see `CONFIG.md`):
- Source: transcript file or footage name, date recorded:
- Target runtime (format range in `IDENTITY.md` section 12):

## 2. People and consent
| Person (as they spell it) | Role on screen | Consent | Spelling confirmed |
|---|---|---|---|
| | | public figure / written OK / none | yes / no |

No consent and not a public figure: the person is not in the clip.

## 3. The hook
- Hook line (verbatim): "..."
- Source time (start to end): 
- Why this line (surprise, specificity, usefulness):
- Two other candidates, verbatim with source times:
  1. 
  2. 
- Headline for frame 1 (caps, 2 lines at most, one gold word):
- Muted test: does the headline alone make sense? yes / no

## 4. Structure
| Beat | Output time | Source time | What is said or shown |
|---|---|---|---|
| Hook | 0.0 to | | |
| Sting | | none | brand card, 1 to 1.5 s |
| | | | |

The edit list for this brief is `edl.csv` (columns `start,end,reason`, source times).

## 5. Overlay list (a person builds these in CapCut or Canva)
| Output time in to out | Element | Exact text | Notes |
|---|---|---|---|
| | | | |

Include: headline, brand mark, series bug, labels, tabs or ledger, point or pick cards, band wipes, punch-ins, CTA card.

## 6. CTA
- Line said (verbatim):
- Card text shown:
- Output time held (3 s at least):
- Reply plan (only if a comment keyword): who sends, how.

## 7. Claims, names, logos, music to clear
| Item | Where in the video | Status |
|---|---|---|
| | | approved line / needs Lemuel / cut |

Only approved Vetted line: "WorkPay cut its hiring cycle from 90 days to 30."

## 8. Sound
- Sting file (from `CONFIG.md`):
- Music: added in the platform at upload | licensed file (licence recorded: yes / no) | none
- Whoosh points (section changes only):

## 9. Open questions
- 


---

<!-- FILE: templates/edl.csv -->
# FILE: templates/edl.csv

start,end,reason
0.00,3.40,hook
3.40,9.80,context


---

<!-- FILE: templates/post-copy.md -->
# FILE: templates/post-copy.md

# Post copy

## Caption
Line 1 is the hook. It must be true to the video and readable on its own.

```
{hook line, one sentence}

{one or two short lines: what the viewer gets, in plain words}

{the one CTA, same as in the video}

{3 to 5 hashtags}
```

## Checks before posting
- [ ] Line 1 matches the video's hook. No claim the video does not support.
- [ ] One CTA only. It matches the CTA said and shown in the video.
- [ ] 3 to 5 hashtags.
- [ ] No "#1", no award, no number without a source, no forward promise about who will be there.
- [ ] Any Vetted claim is the approved line or is cleared by Lemuel.
- [ ] Names spelled as their owners spell them.
- [ ] Link works (event teasers).

## Post details
- Account and collaborators (see `CONFIG.md`):
- Cover frame time (s) and why:
- Music: added in the platform | none | licensed file
- Posted at (date, time EAT):
- Voice-only master and music version file names:


---

<!-- FILE: templates/performance-log.csv -->
# FILE: templates/performance-log.csv

date_posted,format,episode,account,collaborators,hook_line,caption_mode,pair_id,runtime_s,cover_time_s,cta,music_source,qc_verdict,views_48h,avg_watch_time_s_48h,shares_48h,saves_48h,follows_48h,views_7d,avg_watch_time_s_7d,shares_7d,saves_7d,follows_7d,what_changed,lesson


---

<!-- FILE: templates/caption-style.json -->
# FILE: templates/caption-style.json

{
  "_note": "The house caption and type style as data (brand v2, 22 Oct 2026). Values come from IDENTITY.md sections 3 and 4. Tools read the font files from $TS_FONT_DIR or ~/.local/share/vetted-video/fonts; chat-tier users copy the values into CapCut or Canva.",
  "canvas": {
    "width_px": 1080,
    "height_px": 1920,
    "fps": 30
  },
  "fonts": {
    "face": {
      "family": "Inter Tight",
      "weights": {
        "normal": 600,
        "soft": 500,
        "name": 700,
        "stress": 800,
        "number": 900
      },
      "licence": "OFL",
      "source": "Google Fonts"
    },
    "payoff": {
      "family": "Didot Italic (macOS) or Inter Tight Italic",
      "note": "portable choice, open: a Google serif such as Instrument Serif"
    },
    "files": [
      "InterTight[wght].ttf",
      "InterTight-Italic[wght].ttf"
    ]
  },
  "colours": {
    "page": "131210",
    "raised": [
      "191715",
      "1E1C1A"
    ],
    "text": "F6F5F4",
    "muted": "A9A39E",
    "gold_cards": "D8B579",
    "gold_video": "E2B05A",
    "on_gold": "181410",
    "purple": "only inside the Vetted mark",
    "source": "talentsocial.network, measured 22 Oct 2026"
  },
  "captions": {
    "style": "kinetic",
    "size_px": 62,
    "y_position_ratio": 0.55,
    "y_range_ratio": [
      0.5,
      0.62
    ],
    "align": "centre",
    "roles": {
      "normal": {
        "scale": 1.0
      },
      "soft": {
        "scale": 0.82,
        "opacity": 0.85
      },
      "stress": {
        "scale": 1.22,
        "colour": "gold_video",
        "max_per_phrase": 2
      },
      "number": {
        "scale": 1.5,
        "colour": "gold_video"
      },
      "big": {
        "scale": 1.9,
        "face": "payoff",
        "colour": "gold_video",
        "own_line": true,
        "max_per_phrase": 1
      }
    },
    "words_per_phrase": [
      3,
      6
    ],
    "reveal": "word by word as spoken, short pop",
    "halo": "soft warm-black glow, no outline",
    "case": "sentence",
    "modes": [
      "none",
      "plain",
      "kinetic"
    ],
    "default_mode": "plain",
    "kinetic_status": "experiment from 22 Oct 2026; adopt for rule-5 clips only if it beats plain on watch time in 6 of 8 matched pairs",
    "clean_master": "always exported"
  },
  "headline": {
    "use": "only when the first spoken line is not on screen as captions, or when the framing is editorial",
    "y_range_ratio": [
      0.26,
      0.4
    ],
    "max_lines": 2,
    "plus": "one gold payoff line",
    "align": "left at 92 px",
    "case": "sentence"
  },
  "cards": {
    "style": "liquid glass",
    "name_card": {
      "name": "Inter Tight 700, fits 64 px",
      "role": "Inter Tight 600, 26 px, tracked caps, gold_video"
    },
    "outro": {
      "title": "Talent Social",
      "line": "talentsocial.network",
      "held_s": 3,
      "no_date": true
    },
    "glass": {
      "backdrop": "real picture, gaussian blur sigma 22, saturation 1.5, magnified 12%",
      "tint": "white 52% to 18% top to bottom",
      "rim": "white top-left to faint bottom-right",
      "warm_edge": "gold_video bottom-right",
      "shadow": "soft, offset 12 px"
    },
    "left_px": 92,
    "bottom_max_px": 1440
  },
  "safe_zones_px": {
    "top": 220,
    "right": 140,
    "bottom_hard": 380,
    "text_bottom_max_y": 1440
  },
  "usable_area_px": {
    "x_min": 0,
    "x_max": 940,
    "y_min": 220,
    "y_max": 1540
  },
  "motion": {
    "punch_in_percent": [
      10,
      15
    ],
    "punch_in_every_s": [
      3,
      5
    ],
    "note": "punch-ins are continuity cuts at sentence boundaries; the audio is not cut"
  },
  "watermark": {
    "text": "talentsocial.network",
    "size_px": 22,
    "opacity": 0.6,
    "position": "bottom-left, x 92, y 1402",
    "hide_while": "a glass card is on screen",
    "note": "No eyebrow or logo near faces (Lemuel, 22 Oct)"
  }
}

---

<!-- FILE: templates/edit-test-report.md -->
# FILE: templates/edit-test-report.md

# Edit test report (one per clip)

- Your name:
- Date:

## Clip
- Source file name:
- Source length / finished length:
- Format used (talk clip, advice episode, other):
- Speaker and consent: speaker form on file / release signed / not sure (ask Lemuel)

## Time spent (minutes)
| Step | Minutes |
|---|---|
| Choosing the clip | |
| Getting the transcript | |
| Chat: brief and edit list | |
| Cutting in CapCut | |
| Captions and on-screen text | |
| Audio and export | |
| QC checklist | |

## Where the kit or the chat was unclear or wrong
Quote the instruction, then say what happened.
-

## What you had to guess
-

## Scores (1 = poor, 5 = great)
| Could I follow it? | Hook strength | Captions | Brand look | Audio |
|---|---|---|---|---|
| | | | | |

## QC verdict from the chat
READY / FIX / DO NOT POST, and the failures it listed:

## Three questions
1. What slowed you down most?
2. What would you change in the kit?
3. Would you use this every week? Why or why not?

## Facts to confirm with Lemuel
Names, roles and consent you were not sure about:


---

<!-- FILE: examples/REFERENCES.md -->
# FILE: examples/REFERENCES.md

# Reference creators: what to borrow

Public Instagram handles only. Patterns, not copy: nothing here reproduces a caption or a post. Each was checked by opening a few recent reels, read only. A handful of reels per creator is a pattern, not a study.

Why references first: we copy patterns that already work and make them ours. Every format page cites its references.

| Handle | Why them | Borrow | Do not copy |
|---|---|---|---|
| **jerryjhlee** | Career advice for job seekers: the same job as the advice episode | A concrete outcome claim in a boxed line at the top; app screenshots as proof; a comment-keyword CTA (only with a reply plan) | US-specific offers; a selfie look for a brand account |
| **thediaryofaceopodcast** | Turns long conversations into clips: our panels and Recruiters Ring | Cold open on the most surprising line; a big headline with one coloured word; small sentence-case captions | Long runtimes for our audience |
| **hormozi** | The discipline benchmark | One idea per clip; plain background; minimal captions; no filler | The yellow word-highlight template; the money-guru tone |
| **jubileemedia** | The closest model for a repeatable game or debate series | A named series with a season; two-line captions in a dark box with the payoff line in colour | US political content |
| **fisayofosudo** | African creator with clean craft and local utility | Clean setting; one object or screen as the visual; small sentence-case captions; useful local topics | Gadget-review topics |
| **techcabal** | Our ecosystem: shows what event and talking-head coverage gets | A series bug on the clip. Also the cautionary example: long talking clips and event coverage draw little | Long runtimes |
| **sendthecv** | The closest local career series | A branded sting on a black card shortly after the guest's first line, with a sound; one caption template reused every post ("Applicant 00X" style numbering) | Lemon yellow on black: ours is a warmer gold |
| **the.career.whisperer** | The one African career-advice account at scale found | Career advice for Africans in a series; a multi-day prep challenge framing. Reels not yet reviewed in full: {{NEEDS_VERIFICATION}} | |
| **bigtechprep** | A numbered interview-prep series | A promise in the title ("Day 1/30" style); the numbered habit suits "Ep NN" | Runtimes much longer than ours |
| **calculusphile** | A numbered interview-question series | A clear question as the hook; one problem per post | Runtimes much longer than ours |

## Which format uses which
- Advice episode: jerryjhlee, the.career.whisperer, hormozi (and bigtechprep for numbering).
- Game episode: jubileemedia, thediaryofaceopodcast, bigtechprep.
- Event teaser: sendthecv, techcabal, thediaryofaceopodcast.
- Talk clip (coming): thediaryofaceopodcast, techcabal (what not to do).

## Yellow is the convention
Several large accounts put their emphasis word in yellow. Our warm gold is a shade of that convention, chosen to fit warm Nairobi footage and the purple parent mark. It is not an escape from it. Colour alone will not make us recognisable: faces, named formats, the sting and the voices will.

## Add a reference
A reference needs: the public handle, what it does in the first 2 seconds, the one thing to borrow, the one thing not to copy. No metrics. No quotes beyond a few words.


---

<!-- FILE: examples/BASELINE-LESSONS.md -->
# FILE: examples/BASELINE-LESSONS.md

# Baseline lessons: what nine early videos taught us

Nine short videos were audited before this kit was written: three episodes with a presenter or two hosts, four event reels with music and no voice, and two partner-event recaps. Each lesson below is a rule the kit now follows. No client, brand, person or number appears here on purpose.

## Hook
1. **Open on the line.** In two of the three episodes a title card of about 2.4 s cut in during the hook. The series name is now a small bug. The sting comes right after the first line.
2. **Never open on black or a logo.** One reel opened on a black frame. The first frame is a face or the claim.
3. **The hook must make sense muted.** The best baseline hooks were short text claims with a number or a stake, from the first frame. Keep that. Say the same line aloud.
4. **An opening of banter is not a hook.** One game episode opened on small talk. Pick the sharpest line, not the first.
5. **A label is not a claim.** One reel's first text was a slogan, not a reason to stay. Lead with one claim.

## Structure
6. **Long static shots need changes.** Several episodes held one shot for about a minute, carried only by overlays. Add a punch-in, card or cutaway every 3 to 5 s.
7. **Every point ends with something to do.** One advice episode ended its last point with a vague line. Each point is a claim and an action.
8. **Show the payoff.** One game episode never showed who won or how it was scored. The payoff is on screen.
9. **Keep the live ledger and the progress tabs.** They were the strongest reusable parts.
10. **Event reels must say something.** They showed faces and said nothing. Add a claim, a reason to come, and where useful a name label for someone who agreed.
11. **A recap with a usable spoken line should surface it.** One partner recap had a good spoken line buried under b-roll and uncaptioned. Caption it and lead with it.

## Captions and type
12. **One caption position.** Caption height ranged widely. Keep it at 55 to 70% of height.
13. **Smaller, sentence case.** All-caps word-pop now looks like a template. Keep caps for the headline only.
14. **Do not fill the top or bottom.** Every video that carried text put text or logos in a platform-UI zone. Respect the safe zones.
15. **Do not clip a headline.** A line that runs edge to edge gets cut. Keep every line inside the safe zones.
16. **Tiny labels do not work.** Name labels and ledger names were too small to read. Make them readable at arm's length.
17. **No ghosting.** Two cards overlapped on screen in one episode. One card at a time.

## Brand
18. **A mark on every video.** The recaps for events had no mark at all. A small mark sits top-left from the sting to the end.
19. **No off-palette effects.** A colour wash, emoji sprites and a cartoon rocket appeared in several. Drop them.
20. **One transition.** A single band wipe, between sections only.

## Proof and claims
21. **No logo walls.** Walls of local employers sat small and unreadable, and some sat in the bottom zone. They also name organisations as proof. Drop them.
22. **No unsourced superlatives or counts.** A "#1" slogan and an unsourced "40+" style count appeared in several. Use a sourced, past-tense fact or nothing.
23. **Numbers on screen match speech.** One episode's card and speech disagreed on the year. Check before export.
24. **No forward promise.** Do not say who will be at the next event.
25. **Partner footage belongs to the partner.** Ask whose it is before reuse, and check consent and branding.

## Audio
26. **Most baseline files were over the true-peak limit.** Master to -14 LUFS with true peak at or below -1 dBFS and measure it.
27. **No designed audio hook.** None had a hit or riser on the claim. Add a short hit on the claim and the sting after the first line.
28. **Loudness varied a lot.** Some files were far too loud and one far too quiet. Measure every export.
29. **Silent end cards waste the CTA.** Speak the CTA over the card.

## CTA
30. **Most had no CTA, or only a shown one.** One CTA, said and shown, held 3 s, above the bottom zone.

## Rights
31. **Record music and font licences.** Music licences were unknown for most reels. Add music in the platform at upload where possible, and record the rest.
32. **Attendee consent.** Faces in event footage need a recorded OK. See the event teaser format.

## What to keep
Real faces and Nairobi context. A text hook with a number from frame 1. Cuts on a steady beat in teasers. A one-sentence caption arc across shots. Colour emphasis on one word. Hard cuts. One grade per video. A branded end card with a link.


---

<!-- FILE: tools/README.md -->
# FILE: tools/README.md

# Video tools

Small tools for the agent tier (Claude Code or Codex with the repo cloned). They use ffmpeg, ffprobe, Python 3.12, Pillow, numpy and faster-whisper. Nothing here uses the network, except Whisper downloading its model the first time. Every tool prints its usage when run with no arguments, writes only where you tell it, and never deletes your input.

## Set up

**ffmpeg.** This machine's ffmpeg has no `subtitles`, `ass` or `drawtext` filter. So captions are not burned from a subtitle file. They are drawn as transparent PNGs with Pillow, assembled into one overlay clip, and laid on the video with the `overlay` filter. That is what `captions_to_overlay.py` and `burn_captions.py` do.

**STT_PYTHON.** `transcribe.py` needs faster-whisper and numpy. Make a venv once and point `STT_PYTHON` at its python (the lane's CONFIG records the path):

```
python3 -m venv ~/.local/share/vetted-video/stt
~/.local/share/vetted-video/stt/bin/pip install faster-whisper numpy pillow
export STT_PYTHON=~/.local/share/vetted-video/stt/bin/python
```

Every Python tool below can run under `$STT_PYTHON`. Only `transcribe.py` needs it; the rest work with any python3 that has Pillow (`measure.py` and `cut_silence.py` need no Pillow at all, apart from one optional check).

**Fonts.** The house type is Inter Tight (setup lines, captions, cards) with Instrument Serif Italic for the gold payoff word. Both are open licence (Google Fonts). Download `InterTight[wght].ttf`, `InterTight-Italic[wght].ttf` and `InstrumentSerif-Italic.ttf` from fonts.google.com and put them in `~/.local/share/vetted-video/fonts` (or point `TS_FONT_DIR` at the folder). `brand.py` finds them there. No fonts are kept in this repo. Without Instrument Serif the payoff falls back to Didot Italic on a Mac, then Inter Tight Italic.

## The tools

**transcribe.py** - speech to text with word times. Writes `transcript.json`, `transcript.txt` and `captions.srt` (short caption chunks).
```
$STT_PYTHON transcribe.py episode.mp4 work/ --model small.en
```

**cut_silence.py** - cuts dead air and writes the kept segments as an EDL (`start,end,reason`). If there is nothing to cut it says so and copies the video.
```
python3 cut_silence.py raw.mp4 cut.mp4 --min-silence 0.4 --pad 0.08 --threshold -35 --edl edl.csv
```

**captions_to_overlay.py** - draws one transparent PNG per caption chunk plus `overlay.ffconcat` and `overlay.json`. White text, thin charcoal edge, soft shadow, 2 to 5 words, centred at `--y` (0.62 of the height), at most one gold word per chunk. The gold word comes from `--emphasis` (one word per line), otherwise a number word such as "hundred" or any digit word.
```
$STT_PYTHON captions_to_overlay.py work/transcript.json work/overlay --font ~/.local/share/vetted-video/fonts/InterTight[wght].ttf --emphasis words.txt
```

**burn_captions.py** - runs the step above and composites the result onto the video. `--style brand` is plain steady captions (the default mode); `--style kinetic` is the experiment: words pop in as spoken and are typeset by role (stressed words larger and gold, numbers larger, one `--big` word in the gold serif); `--style classic` is the old outlined look. Choose the mode by the rules in `skills/3-captions-and-type.md`. Audio is copied. `--max-seconds` renders only the start, for tests.
```
$STT_PYTHON burn_captions.py cut.mp4 work/transcript.json captioned.mp4 --font ~/.local/share/vetted-video/fonts/InterTight[wght].ttf --style kinetic --emphasis words.txt --big big.txt
```
Captions go into the whole video, so use a clean version. If the footage already has captions burned in, they will double up.

**loudness.sh** - two-pass loudness master to -14 LUFS (second argument changes it), true peak target -2 so the AAC file ends at or under -1.5 dBFS. Prints the before and after numbers. If a clean linear pass cannot get there, it retries with a limiter.
```
./loudness.sh captioned.mp4 master.mp4 -14
```

**measure.py** - QC numbers and a verdict. Checks loudness (-15 to -13 LUFS), true peak (-1 dBFS or lower), first sound within 2 s (advice and game), first frame not black, no black segments, and runtime for the format. Silences, freezes and cuts per minute are reported but not scored; the cut count undercounts punch-ins. `--json` for machine output. Exit code is 0 either way; read the verdict line.
```
python3 measure.py master.mp4 --format advice
```

**contact_sheet.py** - timestamped frames on one JPG. Default spacing is max(2.5, length/36) seconds; 8 columns for vertical video.
```
python3 contact_sheet.py master.mp4 sheet.jpg --every 2.5
```


**brand.py** - the brand values (colours, font loading) the drawing tools share. Values come from the live site (see `IDENTITY.md`).

**brand_cards.py** - draws the on-screen cards as transparent PNGs from a small JSON spec: a static headline with a gold payoff line, a small quiet site address, number cards, and liquid-glass name cards and outro (the picture behind the glass is blurred when the cards are composited). It checks the safe zones and stops if text lands in one.
```
$STT_PYTHON brand_cards.py cards.json out_dir
```

**kinetic_captions.py** - the kinetic caption renderer used by `burn_captions.py --style kinetic`. Words appear as spoken; each is typeset by its role; stress is read from the speaker's delivery (louder and slower than their usual).

## Typical order

`transcribe` then `cut_silence` (re-run `transcribe` on the cut file) then `burn_captions` then `loudness.sh` then `measure.py` and `contact_sheet.py`. Animated overlays (ledger, progress tabs, sting, punch-ins) are not automated in v1; build them in CapCut or Canva from the format page.

## Known limits

- `cut_silence.py` removes silence only. It does not cut filler words ("um", "you know"); do that by hand using the transcript.
- `measure.py` cannot see a logo in the first frame; it only checks that the frame is not near black. Check the contact sheet.
- Caption timing comes from Whisper word times. Read the captions once for misheard names before posting.

## Overlay pack (make_overlay_pack.py)

**make_overlay_pack.py** - builds the on-screen graphics for the editor (CapCut) from one command: transparent 1080x1920 PNGs, three short transparent clips with a green-screen backup, three placeholder sounds, a `CAPCUT-HOW-TO.md` and a `manifest.json`. Every graphic is already in its right place, so the editor drops each file on the overlay track at full frame. With only `--out` and `--font` every text has a default and the whole pack is written.
```
$STT_PYTHON make_overlay_pack.py --out ~/video-pack --font "/System/Library/Fonts/Supplemental/Arial Black.ttf" \
  --series "JOB SEARCH TIPS 101" --episode 02 --name "Speaker Name" --topic "CAREER ADVICE" \
  --headline "100+ APPLICATIONS.|ZERO REPLIES." --gold-word ZERO --tabs "STRATEGY,CV,STAND OUT" \
  --points "FIX YOUR STRATEGY,FIX YOUR CV,STAND OUT" --cta "FOLLOW FOR PART 2"
```
Other options: `--checklist` (3 lines, default = `--points`), `--action` (up to 8 words), `--keyword` (for the comment card), `--skip-clips`, `--skip-sounds`, `--tmp DIR`. The defaults are sample text from the format pages, not claims; change them for each episode. `--name` is not forced to capitals (names are spelled as their owners spell them); for a talk clip put the speaker's role in `--topic`.

What it writes under `--out` (the script refuses an `--out` inside a git repo, because media never goes in the repo):
- `stills/` PNG, sRGB, transparent: `brand-mark`, `series-bug`, `label`, `tabs-0` (all outlined) and `tabs-1..3` (that tab gold), `point-card-1..3`, `checklist-card` (all ticked) with `-step1` and `-step2`, `action-card`, `cta-card`, `comment-keyword-card`, `headline`.
- `clips/` `band-wipe.mov` (9 frames, 0.3 s; the whole frame is gold on frame 5, so cut there), `sting.mov` (1.2 s, solid charcoal card, text only), `cta-in.mov` (slides up in 8 frames, then follow with `cta-card.png`). The `.mov` files are ProRes 4444 with alpha at 30 fps. Backups on #00FF00: `band-wipe-green.mp4`, `cta-in-green.mp4`; `sting.mp4` is opaque and needs no key.
- `sounds/` `sting.wav`, `whoosh.wav`, `tick.wav`: mono, 48 kHz, synthesised with ffmpeg (no licensing issue), peak -6 dBFS. **Placeholders** until a designed sting exists. `tick.wav` is not used by default, because IDENTITY section 8 allows only the sting and the whoosh.

Rules it enforces: nothing in the top 220 px, the bottom 380 px (y 1540 and below) or the right 140 px (x 940 and over); the label sits at 72 to 79% of the height, the headline at 20 to 35%, the CTA's bottom edge at y 1500. After writing it re-reads every PNG, checks that the four corners are transparent and that no pixel with alpha above zero lies outside the band, and exits 1 on any failure. Invisible soft-shadow tails (alpha 12 or less) that fall outside the band are cleared; anything stronger fails the run. The clips are motion and may pass through the unsafe zones on purpose (the wipe and the sting cover the frame).

(The overlay pack below is the earlier brand v1 look, for the advice and game episodes, and has not been migrated. Colours there: gold F5B533, charcoal 181E2A.) Purple is not used. Gold appears only on the one headline word, the active tab, the label's topic line, the CTA button and the sting underline.

Placeholders and limits:
- The brand mark is **text only** until the real logo file exists.
- `--font` takes any heavy TTF for the older overlay pack. The default is Arial Black, then Arial Bold. Arial Black is wide, so headline lines are fitted down in size to stay inside the band (long lines get small).
- Graphics are centred on x 490, the middle of the usable band (60 to 920), not the middle of the frame.
- Clip sizes: `sting.mov` is about 2.3 MB; the other clips are under 1 MB. The files were checked with ffprobe and by decoding frames. They have **not** been imported into CapCut: every CapCut step in `CAPCUT-HOW-TO.md` is marked `{{NEEDS_VERIFICATION in CapCut}}`.
- Not in the pack: the game episode's ledger, pick cards and price badges.


---

END OF KIT
