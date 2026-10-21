# Config (fill once; skills read this instead of guessing)

No logins, passwords or emails belong in this file.

| Item | Value | Status |
|---|---|---|
| Advice and game episodes | Post from @lemuel_abishua. Add @africaproductpeers and @talentsocial.network as collaborators. | decision recorded for v1 |
| Events, panels and teasers | Post from @africaproductpeers | decision recorded for v1 |
| Other platforms | TikTok, LinkedIn, WhatsApp: only from accounts the team owns and has confirmed | {{NEEDS_VERIFICATION}} |
| Brand line on video | "Talent Social · powered by Vetted" | decided |
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
| Headline font | Poppins ExtraBold, OFL licence | not installed on every machine; tools take `--font <ttf>`. Path: `{{FONT_PATH}}` |
| `STT_PYTHON` | a Python 3 from a virtual environment that has faster-whisper, numpy and Pillow, for example `~/.local/share/vetted-video/stt/bin/python` | set once per machine. `export STT_PYTHON=<path>`. Tools that need only Pillow run with any python3. |
| System tools | `ffmpeg` and `ffprobe` on the path | some builds lack the `subtitles`, `ass` and `drawtext` filters; the tools draw captions with Pillow and use `overlay` |
| Claims register | private; ask Lemuel | if you cannot open it (for example, using the public kit), only the approved line in `IDENTITY.md` section 10 passes |
| Event link, date, area | supplied per teaser | `{{EVENT_LINK}}`, `{{DATE}}`, `{{AREA}}` |

## Colour and type

Values and status: `templates/caption-style.json`. Gold about #F5B533 and charcoal about #181E2A are to confirm in Canva.

## Defaults

- Shoot days: plan with `skills/0-shoot-plan.md` and `templates/shoot-plan.md`. Format pages added: `formats/quick-formats.md`, `formats/founder-story.md`.
- Episodes: follow-for-part-2 CTA. Game episode: the comment question.
- Teasers: the event link, said and shown.
- No music in the exported file unless its licence is recorded.
