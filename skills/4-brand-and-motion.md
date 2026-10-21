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
