# Lesson format (Notion "Lessons" database)

Every Lektion has two lesson pages, one per hour of study:

| Key | Part | Content |
|---|---|---|
| `L<index>-p1` | Part 1 | goal, grammar explanation, new words, Kursbuch work, exercises |
| `L<index>-p2` | Part 2 | recap, Arbeitsbuch work, more exercises, writing, speaking |

`<index>` is the course position 0-47 from `curriculum/syllabus.json` (A1.1 L1 = 0, A2.2 L24 = 47).
A `full` session (2-3 hours) does Part 1 then Part 2 in one sitting. Practice and weekly sessions
are made on the day by the session workflow, not prepared here.

## Page properties

- **Lesson** (title): `A1.1 L1 · Part 1 · Greetings and introductions` (volume, Lektion number, part, short topic in English)
- **Key**: `L0-p1`
- **Lektion**: relation to the Lektion page (ids in `notion/ids.json` → `lektion_pages`)
- **Part**: `Part 1` or `Part 2`
- **Minutes**: 60 (A1) or 105 (A2: 3.5 h per Lektion over two parts, done across sessions)
- **Status**: `Ready`

## Page body (Notion markdown)

Part 1:

```
## Goal
One sentence: what you can do after this lesson (CEFR "can do", English).

## Grammar
Short explanation in English with 4-6 example sentences from everyday adult life in Germany
(work, flat, doctor, Behörden, shopping, public transport). Tables are fine.

## Words
| German | Plural | English | Example |
|---|---|---|---|
| der Name | die Namen | name | Mein Name ist Abdelrahman. |
(15 words for A1, 20 for A2; nouns with article; verbs in the infinitive)

## Book work
- Kursbuch p. 9, ex. 1-2: what to do, which audio file (e.g. "Lektion 1, 3")
- ...

## Exercises
1. Instruction in English + the German to work on
2. ...
(8-10 items: fill-in, transformation, translation, word order)

<toggle> Answers
1. answer (also accepted: ...)
2. ...
</toggle>
```

Part 2:

```
## Recap
Three-line reminder of Part 1's grammar, plus one new related point if the Lektion has one.

## Book work
- Arbeitsbuch Lektion N: exercises 1-6 and the Test page; check with the answer key (Books database)
- Kursbuch p. 12: Sprechtraining / phrase box

## Exercises
(10-12 items, harder than Part 1, mixing this and earlier Lektionen)

<toggle> Answers ... </toggle>

## Writing
A 5-6 sentence task in English that uses the Lektion's grammar and words (exam-style for A2:
an email, a message, a short form).

## Speaking
A role-play topic for the voice session, with 3-4 questions the partner should ask.
```

Use the toggle syntax `<toggle>` exactly as in the Notion markdown spec: the summary line right
after the tag, children after a blank line, then `</toggle>`.

## Rules

- Everything the learner reads is English, except the German being taught.
- Write in your own words. Never copy the book's texts, dialogues, exercises or word lists; refer
  to them by page and exercise number instead. Articles and plurals come from the book's word
  pages (Lernwortschatz), not memory.
- Words must be on the Goethe A1/A2 list (`curriculum/goethe_words.json`) unless the Lektion makes
  one essential.
- Exercise questions never contain their own answers.
- The learner is an adult engineer living in Germany; examples should fit adult life, not school.
