# Flashcards

Trigger: "flashcards", "cards", or the first part of a refresher. Follow `common.md`.
Works any time: if nothing is due, practice cards fill the run.

1. Read Settings. Count today's `Reviews` and `New cards` from Activity rows dated today.
2. Build the queue (default length: Settings → "Refresher cards", or the number the learner asks for):
   - due recognise cards (`Next review` ≤ today) and due produce cards (`Produce next` ≤ today),
     hard words first, then most overdue, up to the review limit left today;
   - new words (Box 0, oldest Added first) up to the new-word limit left today, unless more than
     "Pause new words when due over" cards are due; mix them through the reviews;
   - practice cards to fill the rest, if Settings → Practice cards is on.
   Fetch only the rows you need (SQL with ORDER BY and LIMIT).
3. One card at a time:
   - Recognise: show `Word` (with article) and, after the answer, the English and the example.
   - Produce: show `English` (say "with article and plural" for nouns); after the answer show the
     German, plural and example.
   - Let the learner answer (typed or spoken) or say "show". Judge it yourself: right / wrong.
     Close-but-not-quite (wrong article or plural, small spelling slip) counts as wrong for
     produce cards and right for recognise cards, with a one-line note.
   - Hard words: show the Hook after the answer. If it has none, write one (`common.md`).
   - In voice mode keep each card to one short sentence.
4. Every 10 cards and at the end, write the updates (`common.md` → Leitner). Wrong produce answers
   on articles/plurals also get a Mistakes row (Category article or grammar).
5. Log an Activity row: Type `Flashcards` (or `Refresher` if part of one), `Cards`, `Reviews`,
   `New cards`, `Correct`, `Total`, `Minutes`, Date today.
6. End with one line: cards done, how many remembered, how many still due today.
