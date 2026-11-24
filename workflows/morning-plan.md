# Morning plan (daily cloud routine, ~06:30 Berlin)

Runs unattended in a Claude Code cloud session on this repo. Follow `common.md`. Don't ask
questions; do what you can and list anything that failed at the end.

1. **Settings.** Read all of them. Today = Berlin date.
2. **Past sessions.** Every Sessions row with `When` before now (date-only rows: before today)
   and Status `Planned` → Status `Missed`.
3. **Make-up** (Settings → Missed sessions):
   - `weekend`: for each session missed in the last 14 days that hasn't been made up (no
     "made up" note), add its minutes to the next Saturday/Sunday sessions' `Make-up minutes`, at
     most "Weekend make-up cap" per day; note "made up on <date>" in the missed row's Notes. Time
     that doesn't fit moves the projected finish (step 7).
   - `shrink`: no make-up; the projected finish moves.
   - `skip`: nothing.
4. **Upcoming sessions.** Make sure Sessions rows exist for today and the next 6 days, from the
   Schedule settings ("Mon session", "Sat session 1", ... format `HH:MM · minutes · kind`; "time
   not set" → date-only). Skip "Days off". Title: `Tue 24 Nov · Lektion part` (kind names:
   split = Lektion part, full = Full Lektion, practice = Practice block, weekly = Weekly review).
   Fill Slot, Kind, Planned minutes, Status Planned. Don't duplicate existing rows (match date + slot).
   If a Schedule setting changed since rows were created, update future Planned rows to match.
5. **Calendar** (Settings → Calendar events = on). Use the Notion Calendar tools. If they say no
   calendar is connected, skip this step and mention it in the summary.
   - For today's sessions with a time: create an event (title from the session, description
     "Say 'lesson' in the Claude app Deutsch project.", reminder = Notification lead) unless the
     row's `Calendar event` already has an id; store the event id there.
   - Refresher slots: pick "Refreshers per day" random times today inside "Refresher window",
     outside "Quiet hours", at least "Refresher gap" minutes apart, not within 15 minutes of a
     session. Create 10-minute events "Deutsch refresher" (description: "Say 'refresher' in the
     Claude app"). Use the date as the random seed so a rerun gives the same times; don't create
     duplicates if events for today already exist.
6. **Due counts.** Words due today (recognise + produce), mistakes due today.
7. **Home page** ("Deutsch A2", id `home_page` in `notion/ids.json`): replace the contents of the
   two callouts under "Today" and "Progress" (keep everything else on the page):
   - Today: today's sessions (time, length, what they cover: current Lektion and part), refresher
     times, cards due, make-up minutes if any, one line if sessions were missed yesterday.
   - Progress: Lektionen done / 48, current Lektion, words Learning/Known, Goethe A1/A2 coverage,
     streak, hours this week vs plan, projected finish vs target date (`progress.md` maths), a
     progress fact and a saying (Settings → Motivation), updated time.
8. **Email** (Settings → Daily email = on): send one plain-text email with the Gmail connector to
   the address in that setting. Subject `Deutsch today: <weekday> <date>`. Body: the Today and
   Progress content, a link to the Notion page, and one line if anything in this run failed.
9. **Summary**: two lines in the session output: what changed, anything that failed.
