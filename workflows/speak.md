# Speaking partner (Claude app)

Two ways in. Follow `common.md` (English for explanations, no emojis, calm).

- **"Deutsch handoff: <Notion URL>"**: a brief prepared by Claude Code. Run it (below).
- **"speak"** with no link: make your own brief first (step 0), then run it the same way.

## 0. Making a brief yourself ("speak")

Read Settings (view `settings_all`), the current Lektion (`lektionen_course_order`: lowest Index
not Done), its latest lesson page's Speaking section (`lessons_by_key`), up to 12 due words
(`words_due`) and the 5 newest mistakes (`mistakes_last_month`). Create a Handoffs row
(`For` Claude app, `Type` Speaking, Status Ready) with a Brief as in `handoff.md`, then run it.

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

## 3. Save to Notion (before the chat ends)

Do this right after the feedback. If you're in voice mode and can't use tools, say
"Type 'save' and I'll store this" and save when the learner types it.

1. Handoff page: replace the empty Results section with the feedback above plus the full list of
   mistakes and notes (turns, words per answer, Hilfe count). Set `Minutes`, `Task`, `Range`,
   `Accuracy`, `Fluency`, `Summary` (one line), `Status` Done.
2. Mistakes: one row per real error (`common.md` → Mistakes), Source `speaking`, Lektion from
   the handoff.
3. Words: any new word you taught when they said "Hilfe" (`common.md` → Words table, Source
   `Speaking`, Box 1, Next review tomorrow). Must-use words they used correctly count as a right
   answer on their card (box + 1) if they were due.
4. Activity: Type `Speaking`, Date today, Minutes, Notes = the Summary and the handoff code.

Then tell the learner in one line that it's saved and, if this came from a lesson in Claude Code,
that they can go back there and say "done".
