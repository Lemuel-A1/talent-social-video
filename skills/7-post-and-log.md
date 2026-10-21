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
