# Settings

Every setting has a home here, one file per area. Each file explains its own values.

**Where to change them:** in the dashboard's Settings tab. The dashboard holds the live
values; these files are the documented defaults it was seeded from. If you'd rather edit a
file, change it here and run `/push-config` in Claude Code. That copies the file's values
into the dashboard, replacing what's there for that area.

| File | What it controls |
|---|---|
| `schedule.toml` | Weekly focus sessions: days, start times, length, kind; days off |
| `refreshers.toml` | Review only: flashcards of due words, then questions on your mistakes and past lessons. How many, time window, difficulty target, no-repeat days |
| `quick.toml` | Quick lessons: 10-15 minutes of new material for the bus. Length, words per lesson, rotating types, situations |
| `reminders.toml` | Calendar and/or email, email address and time, notification lead time, quiet hours |
| `plan.toml` | Goal, exam, target date, phase dates, hours per Lektion, minutes per part of a session |
| `tutor.toml` | English explanations, when help kicks in, correction style, tone |
| `review.toml` | Spaced-repetition limits and intervals |
| `accountability.toml` | Streak rules, what happens to missed sessions, weekend make-up cap, comeback sessions |
| `motivation.toml` | Progress facts and German sayings on the dashboard and in the email |
| `profile.toml` | About you: job, level, why A2 |

Your progress, review queue and mistakes are not settings: they live in the dashboard and
are backed up to `state/` by `/sync`.
