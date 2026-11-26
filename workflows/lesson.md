# Lesson (focus session)

Trigger: "lesson", "start my session", or a planned session is due. Follow `common.md`.

## 1. Work out today's session

1. Read Settings. Read today's Sessions rows (`When` on today's date), in Slot order. Take the
   first with Status `Planned`. If there's none, say so in one line and offer an extra lesson
   (it still moves the course forward; log it as a Sessions row with Status `Done` and Notes "extra").
2. If Settings → "Missed sessions" allows comebacks and the last "Comeback after missed" sessions
   were all Missed, make this a comeback: "Comeback length" minutes, mostly review, then the start
   of the next part. Mention it in one line.
3. Find the current Lektion and part (`common.md` → Progress position) and the lesson page(s):
   - `split`: one part (`L<index>-p1` or `-p2`).
   - `full`: Part 1 then Part 2 of the current Lektion (if Part 1 is already done, Part 2 then the
     next Lektion's Part 1).
   - `practice`: no lesson page. Build it now from the last 2-4 finished Lektionen: mixed
     exercises, one Goethe-A2-style task (A2 phase) or a dialogue task (A1 phase), and speaking.
   - `weekly`: review the week's Lektionen, a 10-item mini-test, then a short check-in (hours this
     week, what felt hard, plan for next week) and update the Weekly reviews row if it exists.
     From Settings → "Goethe Sprechen from Lektion" on, add one Goethe speaking part, rotating
     Teil 1 → 2 → 3 week by week (see the last Sprechen handoff), as a speaking handoff
     (`goethe-sprechen.md`).
   - After Lektion index 47 is done, every session is exam prep: one timed section of a Goethe A2
     model test (Lesen, Hören via the learner's own audio, Schreiben, Sprechen), then feedback.
4. If the session has `Make-up minutes`, add that much extra practice at the end (mixed review of
   the missed material) and say so up front.

Tell the learner in two lines: what this session covers and roughly how long.

## 2. Review (first ~10 minutes, every session)

Due cards and due mistakes, as in `flashcards.md` and `refresher.md`, kept short.

## 3. Work through the lesson page

Fetch the lesson page and go section by section, one step at a time:

- **Goal / Grammar / Recap**: explain in your own words from the page, check understanding with
  one quick question.
- **Words**: show the table, have the learner read the examples aloud (in voice mode), then a quick
  recall round: give the English, ask for the German with article. Repeat missed words at the end
  of the round (max 3 tries each).
- **Workbook**: run the parts one at a time like Exercises (one item at a time, grade, hints,
  Mistakes rows). Never send the learner to the book. If the page still has a `## Book work`
  section instead (older pages), first write a `## Workbook` in our own words as
  `lesson-format.md` describes (the Book work lines tell you only which topics to cover), save it
  into the page in place of the Book work section (`update-page`, `update_content`), then run it.
- **Listening**: tell the learner which track to play and its start time in the Lektion's Audio
  file (Notion, Lektion page → Audio). After they listen, ask the questions one at a time and
  grade them like exercises; if they struggle, suggest listening again before giving hints.
- **Exercises**: one at a time from the page (answers are in the toggle; don't reveal them).
  Grade each answer: accept correct variants; for wrong answers give the correction and a one-line
  reason; offer hints per `common.md`.
- **Writing**: the learner writes; you correct every error with the format from `common.md`, then
  show the corrected text.
- **Speaking**:
  - In the Claude app (voice available): run it now following `speak.md`, using the lesson's
    Speaking section as the brief.
  - In Claude Code: create a speaking handoff (`handoff.md`: Type Speaking, linked to this
    Lesson, Lektion and Session; build the Brief from the lesson's Speaking section, the
    Lektion's words and grammar, and the learner's recent mistakes) and give the learner the
    trigger prompt in a code block: `Deutsch handoff: <handoff URL>`. Say: "Paste this into the
    Deutsch project in the Claude app, do the speaking there, then come back and say done."
    When they say done, fetch the handoff, show its Summary and scores in two lines, add its
    minutes to the session, and set it `Integrated`. If it isn't Done yet, carry on with the
    rest of the lesson and check again at the end.

## 4. Save (at the end, and midway in long sessions)

- Words: add every word from the lesson's Words table (`common.md` → Words table) with Box 1,
  Next review tomorrow, Status Learning, Source Lesson, Lektion = current Lektion. Lesson words
  don't count toward the daily new-word limit (they were taught, not just shown).
- Mistakes: one row per real error (`common.md` → Mistakes).
- Sessions row: Status `Done`, `Minutes` (actual), `Score` ("8/10 exercises"), `Lesson` relation,
  `Lektion` relation, Notes (one line: what was hard).
- Lesson page: Status `Done`, Done on today.
- Lektion: Part 1 finished → Status `Part 1 done`; Part 2 finished → Status `Done`, Done on today.

End with two lines: what was done, and what's next (next session's content).
