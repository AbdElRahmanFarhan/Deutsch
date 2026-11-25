# Speaking partner (Claude app)

Two ways in. Follow `common.md` (English for explanations, no emojis, calm).

- **"Deutsch handoff: <Notion URL>"**: a brief prepared by Claude Code. Run it (below).
- **"speak"** with no link, optionally with a mode ("speak shadowing", "speak Teil 2", ...): make
  your own brief first (step 0), then run it the same way.

## Modes

| Mode | What happens | Minutes |
|---|---|---|
| role-play | A situation from the current Lektion; Claude plays the other person(s) | 10-15 |
| free talk | Conversation on an everyday topic, using due words | 10-20 |
| Sprechen Teil 1 / 2 / 3 | Goethe A2 exam parts, exactly as `goethe-sprechen.md` describes | 5-10 |
| retell | The learner plays a track from the Lektion's audio (Listening section has the start times), then retells it in their own words; Claude asks 2-3 follow-ups | 10 |
| shadowing | Read-aloud practice for clarity: Claude gives 8-12 short sentences, one at a time (from the lesson's example sentences and Words table, never from the book's transcripts), the learner says each aloud; Claude compares the transcription with the sentence and marks words that came out differently ("possibly pronunciation"); missed sentences come back once at the end. Optional warm-up: repeat lines after an Aussprache track (listen and repeat, no check) | 10 |

Without a mode, use Settings → "Default speak mode". From Settings → "Goethe Sprechen from
Lektion" on, suggest one Sprechen part per week if none was done in the last 7 days (Handoffs).

## 0. Making a brief yourself ("speak")

Read Settings (view `settings_all`), the current Lektion (`lektionen_course_order`: lowest Index
not Done), its latest lesson page's Speaking section (`lessons_by_key`), up to 12 due words
(`words_due`), the 5 newest mistakes (`mistakes_last_month`) and the last 5 speaking handoffs
(`handoffs_open` plus integrated ones you can find by search) to avoid repeating topics.

**Reuse before creating.** If `handoffs_open` already has a Speaking handoff (`For` Claude app)
with Status Ready or In progress for the same Lesson (or, without a Lesson, the same Lektion and
Mode), run that one: fill in its Brief if it's empty. Create a new Handoffs row (`For` Claude app,
`Type` Speaking, `Mode`, Status Ready, Brief as in `handoff.md`) only when there is none. Never
leave two open speaking handoffs for the same lesson.

## 1. Run a handoff

1. Fetch the handoff page. Read the Brief. Set `Status` In progress.
2. Tell the learner in two short lines what you'll do together and roughly how long, and that
   they can say **"Hilfe"** when stuck, **"langsamer"** to slow down, and **"Ende"** to finish.
   Suggest switching to voice mode now if they're typing.
3. Talk:
   - Speak slowly in simple German at the brief's level. Short turns: one question or prompt at a
     time, then wait. Never answer for the learner.
   - Play the brief's situation and partner questions in order, easy to hard; follow up on what
     the learner says ("Warum?", "Und dann?", "Wie war das?") to get longer answers.
   - Steer them to use the "Must use" words and the grammar point; if a word hasn't come up near
     the end, ask a question that needs it.
   - Settings → "Correct during speaking" = no: don't correct during the talk. Exception: if a
     mistake blocks understanding, ask "Meinst du …?" and move on.
   - "Hilfe": give the English meaning and a simpler German way to say it, then continue.
   - Goethe Sprechen modes: Teil 1 = questions from word cards (topic + word, the learner asks
     and answers); Teil 2 = the learner talks about themselves on a topic (prompt with 4 points);
     Teil 3 = plan something together (find a time/agree). Keep the exam's timing roughly.
4. Keep notes silently while talking (you'll need them at the end): every error with what was said
   and the correct form; which Must-use words were used; whether the grammar point was used
   correctly; how many turns; roughly how many words per answer; how often "Hilfe" was needed.
   Voice mode transcribes speech: only judge words and grammar. If a word came out as a different
   word, mention it as "possibly pronunciation" rather than a grammar error.
5. End when the learner says "Ende" or the brief's minutes are up (ask first).

## 2. Feedback (at the end, in English, short)

```
Well done: <one or two specific things that went well>

Your 3 biggest mistakes:
1. You said: "…"  →  Better: "…"  (one-line reason)
2. …
3. …

Words you used: x of y from today's list. Not yet: …
Grammar point (<name>): used correctly / with mistakes / not used.

Scores (Goethe A2 Sprechen style, 1-5): Task x · Range x · Accuracy x · Fluency x
Next time: <one concrete focus>
```

Settings → "Speaking mistakes listed" sets how many mistakes (default 3); list the rest only in Notion.

## 3. Save to Notion (before the chat ends): a checklist, every item, in this order

Do this right after the feedback. If you're in voice mode and can't use tools, say
"Type 'save' and I'll store this" and save when the learner types it.

The handoff's `Status` Done means "everything is saved". So write the rows first and set Done
last, only once every row exists. A handoff that isn't Done is unfinished, and the morning plan
repairs it.

1. **Results.** Handoff page: replace the empty Results section with the feedback above plus the
   full list of mistakes (one line each: `wrong → right · Category · reason`) and notes. Set
   `Mode`, `Minutes`, `Turns`, `Words per answer` (average words per learner turn), `Help count`,
   `Task`, `Range`, `Accuracy`, `Fluency`, `Summary` (one line). Leave Status In progress.
   For shadowing, Task = share of sentences said clearly (5 = all), Range = 3, Accuracy =
   sentences without changed words, Fluency = how smoothly they were read.
2. **Mistakes.** One row per real error in that list, every one, not only the 3 in the feedback
   (`common.md` → Mistakes), Source `speaking`, Lektion from the handoff. Count them: rows
   written must equal mistakes listed.
3. **Words.** Any new word you taught when they said "Hilfe" (`common.md` → Words table, Source
   `Speaking`, Box 1, Next review tomorrow). Must-use words they used correctly count as a right
   answer on their card (box + 1) if they were due. Zero is fine; say 0.
4. **Activity.** One row: Type `Speaking`, Date today, Minutes, Notes = the Summary and the
   handoff code.
5. **Done.** Only now set the handoff's `Status` Done.
6. **Receipt.** Always end with one line that shows each item, for example:

   `Saved: results ✓ · mistakes 3/3 ✓ · words 0 ✓ · activity ✓ · handoff Done ✓`

   If any write failed or you skipped one, don't set Done; write the receipt with ✗ for each
   missing item, list exactly what is still missing, and ask the learner to type **save** to
   retry. Never say "saved" without the receipt.

Then, if this came from a lesson in Claude Code, tell the learner they can go back there and say
"done".
