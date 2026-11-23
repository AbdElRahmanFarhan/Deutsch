---
name: sync
description: Back up the Deutsch dashboard's data into state/, rebuild the calendar file if the learner asked for a rebuild, then commit and push. Use when the learner types /sync or asks to back up or rebuild.
---

# Sync the dashboard into the repo

The dashboard URL is in CLAUDE.md. All paths are relative to the repo root.

1. Export every collection with `ArtifactData` `list`, `out_dir: "build/db"`, `query.limit: 1000`
   (follow `next_cursor` if one comes back): `config`, `meta`, `progress`, `sessions`, `refreshers`,
   `srs`, `mistakes`, `reports`. Skip `lessons` (large, and rebuilt by /prepare). Clear `build/db` first.
2. Run `python3 scripts/after_sync.py`. It writes `state/` and prints a summary, including
   `rebuild_requested`.
3. If `rebuild_requested` is true, or `state/config/schedule.json` / `refreshers.json` /
   `reminders.json` / `plan.json` changed in `git diff`:
   - run `python3 scripts/make_calendar.py`;
   - run the `/prepare` skill's steps for the next 3 days;
   - set `meta/rebuild` `done_at` to the current UTC time with `ArtifactData` `update`
     (pin `if_version` from the export).
4. `git add -A && git commit` with a message like `Sync: 3 sessions, 41 words, 6 mistakes`.
   Push if a remote exists (`git remote -v`).
5. Tell the learner in two or three lines: what changed since the last sync, and whether the
   calendar file changed. If it did, remind them to import `calendar/deutsch.ics` into Google
   Calendar again (Settings → Import & export → choose the "Deutsch" calendar).
