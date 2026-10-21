# Talent Social video kit

Plain-text skills that turn a talk transcript or footage into a finished short vertical video plan for Talent Social, in our format, brand and guardrails. Built by VettedAI for the Talent Social community in Nairobi.

**Using it:** in any chat, paste the link to [`KIT.md`](https://raw.githubusercontent.com/Lemuel-A1/talent-social-video/main/KIT.md) (everything in one file) and upload a transcript. A CapCut or Instagram auto-caption export, or a pasted transcript, is enough. You get back a brief, a hook with its timestamp, an edit decision list, caption text, overlay text with timings, post copy and a QC checklist. A person then builds the animated overlays in CapCut or Canva from the format page.

**With an agent (Claude Code or Codex):** clone this repo and start from `START-HERE.md`. The scripts in `tools/` also transcribe, cut silence, burn in captions, master the loudness and measure the result. They need `ffmpeg`, `ffprobe` and Python with Pillow (and faster-whisper for transcribing). See `tools/README.md`.

**What's here:**
- `ROUTER_PROMPT.md` (start here), `START-HERE.md`, `IDENTITY.md` (brand and measurable thresholds), `CONFIG.md`
- `formats/` (advice episode, game episode, event teaser)
- `skills/` (1 footage to brief, 2 rough cut, 3 captions and type, 4 brand and motion, 5 audio and master, 6 QC check, 7 post and log)
- `templates/` (brief, edit decision list, post copy, performance log, caption style)
- `tools/` (the scripts above, source only)
- `examples/` (references and baseline lessons, text only)
- `LANE-README.md` is the working README of the kit. In `KIT.md` it appears as the section named `README.md`.

There are no videos, images, fonts or music in this repo, and there never will be. Bring your own fonts and logo files.

**Forking it for another channel:** copy the kit, rewrite `IDENTITY.md`, `CONFIG.md` and the references in `examples/`, keep the QC thresholds unless your platform needs different ones, and start your own lessons log.

This repository is published by hand from a private working repo. Changes made here directly will be overwritten; send suggestions to the Talent Social team.
