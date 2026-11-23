# Deutsch A2: personal German course (A1 → Goethe A2)

This repo is the back office of a personal German course. The learner uses a dashboard on
claude.ai (phone and laptop); Claude Code on the laptop prepares lessons, backs up data,
builds the calendar and sends the daily email.

- **Dashboard:** https://claude.ai/artifact/5ZAdS7RsTg3dDGn6p15gQ4 (source: `dashboard/index.html`)
- **Live data** (settings, progress, review queue, mistakes, sessions, prepared lessons) lives in
  the dashboard's database. Read and write it with the `ArtifactData` tool and the URL above.
- **The learner:** Abdelrahman, lives and works in Germany (engineering/tech), Egyptian, studies in
  English. Everything the tutor writes is in English; German only as the thing being learned.

## Sources

- **Primary:** Menschen (Hueber) A1.1, A1.2, A2.1, A2.2, Kursbuch + Arbeitsbuch, in `Cirriculum/`
  (the learner's own copies). Never commit, upload or paste those files or long passages from
  them anywhere: not into the repo, the dashboard database, or a prompt. Use them on this laptop to
  see what each Lektion covers, then write lessons in your own words, pointing to page numbers.
- `curriculum/syllabus.md` (human) and `curriculum/syllabus.json` (machine) list the 48 Lektionen.
  `scripts/book_text.py <index>` prints the OCR text of a Lektion's pages for reference.
- Vocabulary must fit the Goethe A1/A2 word lists. Take articles and plurals from the book, not memory.

## Database layout (dashboard)

| Path | What |
|---|---|
| `config/<area>` | Settings: schedule, refreshers, reminders, plan, tutor, review, accountability, motivation, profile. Defaults documented in `config/*.toml`. |
| `meta/syllabus`, `meta/sayings` | The 48 Lektionen; German sayings |
| `meta/rebuild` | `{requested_at, done_at}`: the learner pressed Rebuild |
| `progress/main` | `{current_index, current_part, done: [indexes], started}` |
| `sessions/<YYYY-MM-DD-slot>` | A focus session: `status` done/missed/extra, `minutes`, `kind`, `lektion_index`, `phase` |
| `refreshers/<id>` | A finished refresher: `date`, `minutes`, `total`, `correct` |
| `srs/<id>` | Review item (`w-…` word, `m-…` mistake): `de`, `en`, `ef`, `reps`, `interval`, `due`, `lektion` |
| `mistakes/<id>` | `date`, `wrong`, `right`, `reason`, `category`, `source` |
| `lessons/<key>` | Prepared lesson. Key: `L<index>-p1`/`L<index>-p2` (split sessions), `L<index>-full`, or a session id for practice/weekly sessions |
| `reports/<id>` | Reports pasted from Claude app voice sessions |

A lesson document is `{title, lektion_index, part, kind, minutes, steps: [...]}` where each step is one of:
`{type:"explain", title, body}` (body: short markdown), `{type:"vocab", title, words:[{de, plural, en, example, example_en}]}`,
`{type:"book", title, body}` (which Kursbuch/Arbeitsbuch exercises and audio to do, by page number),
`{type:"exercise", title, items:[{q, answer, accept:[...]}]}`, `{type:"writing", title, prompt}`,
`{type:"speaking", title, prompt}`.

## Commands

- `/sync`: back up the dashboard into `state/`, rebuild the calendar if asked, commit and push.
- `/prepare`: prepare the next lessons from the book into the dashboard.
- `/push-config <area>`: copy a `config/<area>.toml` file into the dashboard.
- The daily email runs as a Claude app scheduled task ("Deutsch daily plan").

## Rules for tutoring content

- Explanations in English, short, with examples from everyday life in Germany (work, flat, doctor,
  Behörden, shopping, public transport). Respect `config/tutor` (tone, correction style).
- Corrections show the mistake, the correct form and a one-line reason.
- Missed days: mention briefly, never lecture. Follow `config/accountability`.
- Exercise questions never contain their own answers.

## Git

Commit after each change with a clear message. `Cirriculum/`, `build/` and caches are ignored.
Remote: a private GitHub repo (see `git remote -v`); push after commits when a remote exists.
