# Handoffs: Claude Code ⇄ Claude app

The Claude app (phone, voice) and Claude Code (cloud or laptop) don't talk to each other directly.
They pass work through the Notion database **Handoffs** (ids in `notion/ids.json`). A handoff page
is a small, self-contained job: a **Brief** written by the sender and **Results** written by the
receiver. The learner only carries a one-line trigger prompt from one to the other.

## Lifecycle

`Ready` (sender created it) → `In progress` (receiver started) → `Done` (receiver wrote results)
→ `Integrated` (Claude Code folded the results into the course: sessions, lessons, progress).

## Sending a handoff to the Claude app (from Claude Code)

Used for speaking practice, and for anything that's better done by voice on the phone.

1. Create a Handoffs row: `Handoff` (title, e.g. "Speaking · A1.1 L1 · introducing yourself"),
   `Type` Speaking, `Status` Ready, `For` Claude app, `Created` today, `Lektion` (and `Lesson`,
   `Session` if this belongs to a lesson or planned session).
2. Page body, exactly these sections:

   ```
   ## Brief
   Mode: role-play | free talk | Sprechen Teil 1 | Sprechen Teil 2 | Sprechen Teil 3 | retell | shadowing
   (modes are described in speak.md; exam parts in goethe-sprechen.md; also set the Mode property)
   Minutes: 10-20
   Level: A1 or A2, current Lektion and its grammar
   Situation: who the partner plays, where, what the learner has to achieve
   Partner's questions: 4-8 questions or turns, in German, easy to hard
   Must use: up to 12 words/phrases (due words + this Lektion's words)
   Grammar to use: the Lektion's point, with one example
   Watch for: the learner's recent mistakes (from Mistakes), 3-5 lines "wrong → right"
   Success: what a good performance sounds like, in one or two lines

   ## Results
   (empty: the Claude app fills this in)
   ```
3. Give the learner the **trigger prompt** in a code block, so it's easy to copy:

   ```
   Deutsch handoff: <the handoff page's Notion URL>
   ```

## Running a handoff (in the Claude app)

See `speak.md` → "Run a handoff". In short: fetch the page, set Status `In progress`, run the brief,
give feedback, write the Results section, Mistakes rows, Words rows, one Activity row, set the
scores and `Summary`, Status `Done`. Then tell the learner they can go back.

## Sending work to Claude Code (from the Claude app)

When the learner asks for something the app can't do well (rewrite a lesson, change the plan,
anything that needs the repo or many writes), create a row with `Type` Request, `For` Claude Code,
`Status` Ready and a Brief describing the request in a few lines. Tell the learner it's queued;
the next morning plan (or any Claude Code session) picks it up.

## Integrating (Claude Code)

The morning plan, and any Claude Code session that starts or resumes a lesson, reads the view
`handoffs_open`:

- `For` Claude app, `Status` Done: check the Mistakes/Words/Activity rows exist (create any that
  the Results list but are missing), link the handoff to its Session and mark the session's
  speaking part done (Notes: "speaking via handoff <Code>"), add the scores to the lesson's progress
  notes, then set `Integrated`.
- `For` Claude Code, `Status` Ready: do the request, write Results, set `Done` then `Integrated`.
- Older than 7 days and still Ready/In progress: set `Integrated` with Summary "expired".
