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

Before a shoot: skill 0 → the shoot plan. Then: transcript → skill 1 → skill 2 → skill 3 → skill 4 → a person builds the overlays → skill 5 → skill 6 → a person posts → skill 7.

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
