# Rules for every workflow

## Who and how

- The learner: Abdelrahman, an adult engineer living and working in Germany, Egyptian, studying in
  English. A1 mostly forgotten when the course started; goal Goethe-Zertifikat A2.
- Everything you write is in English, except the German being practised. No emojis.
- Calm, brief tone (Settings → Tone). Never lecture about missed days; one line at most.
- One question at a time. Wait for the answer before the next one.
- Corrections: the mistake, the correct form, a one-line reason (Settings → Correction style).
- Never put the answer inside a question.
- Examples come from adult everyday life in Germany: work, flat, doctor, Behörden, shopping,
  public transport (Settings → Situations).

## Time

Use Europe/Berlin time. "Today" is the Berlin date.

## Notion

All data is in Notion under the page "Deutsch A2". Ids are in `notion/ids.json` (the Claude app
Project instructions repeat them). Write with `create-pages` / `update-page`. Batch writes: collect
results during the activity and write them at the end (and also after every ~10 answers in long
sessions, so nothing is lost if the chat stops).

**Read through the saved views**, with `query-data-sources` in **view mode**
(`{"mode": "view", "view_url": <url>, "page_size": 100}`). The free Notion plan allows only a small
number of SQL/rows-mode queries per hour across the whole workspace, but view mode isn't limited.
Use SQL only for something no view covers, and expect it to fail sometimes ("usage limit"); then
fall back to a view and filter the rows yourself. The views (`notion/ids.json` → `views`):

| View | Rows |
|---|---|
| `settings_all` | every setting |
| `words_due` | words due today (recognise or produce), hard words first |
| `words_new` | words with Box 0 |
| `words_practice` | all started words, weakest first (most lapses, lowest box) |
| `mistakes_due` | mistakes due today |
| `mistakes_last_month` | mistakes of the last month, newest first (weak spots) |
| `sessions_around_today` | sessions from a week ago to a week ahead |
| `sessions_missed` | missed sessions of the last month |
| `activity_last_week` | activity of the last 7 days (limits, no-repeat, streak) |
| `lessons_by_key` | all lesson pages with Key, Part, Status (fetch a page by its url) |
| `lektionen_course_order` | the 48 Lektionen in order, with Status and Book pages |

To check whether a word already exists, use `notion-search` with the Words data source url and the
word as the query.

**Read Settings first**, every time (`settings_all`). Use the values; never assume defaults when a
setting exists.

## Flashcards: Leitner boxes

Words have two stages:

- **Recognise**: show the German (with article), recall the English. Columns `Box`, `Next review`.
- **Produce**: show the English, say the German with article and plural. Columns `Produce box`,
  `Produce next`. Opens when `Box` reaches Settings → "Open produce stage at box" (set
  `Produce box` 1, `Produce next` tomorrow).

Intervals from Settings → "Leitner intervals" (default 1, 2, 4, 8, 16 days for boxes 1-5).

- **Right**: box + 1 (max 5); next review = today + interval of the new box.
- **Wrong**: box = 1; next review = tomorrow; `Lapses` + 1.
- **Hard word**: when `Lapses` reaches Settings → "Hard word after lapses": tick `Hard`, keep its
  box at 2 or below, and write a `Hook` (a short, vivid memory aid in English, plus a fresh example
  sentence in `Example`/`Example EN`) if it has none. Show the hook after revealing a hard word.
- **Status**: `Learning` once Box ≥ 1; `Known` when Box ≥ 4 and Produce box ≥ 3.
- **New word**: a word with Box 0 or a word just taught. Starting it = Box 1, Next review tomorrow.
- **Due**: `Next review` ≤ today (or `Produce next` ≤ today). Most overdue first, hard words first.
- **Daily limits** (Settings → Flashcards): count today's `Reviews` and `New cards` in Activity.
  Stop due reviews at "Reviews per day"; stop new words at "New words per day"; if more than
  "Pause new words when due over" cards are due, no new words today.
- **Practice cards** (Settings → Practice cards = on): when fewer cards are due than requested,
  fill up with words the learner knows that aren't due, weakest first (most lapses, lowest box).
  A remembered practice card changes nothing; a forgotten one is treated as Wrong.

Mistakes use the same boxes (`Box`, `Next review`, `Lapses`).

## Mistakes

Every wrong answer that shows a real error gets a Mistakes row: `Correct` (title), `Wrong`,
`Reason` (one line), `Category` (article, case, word order, verb form, grammar, vocabulary,
spelling, pronunciation), `Question` (what was asked), `Source`, `Date` today, `Box` 1,
`Next review` tomorrow, `Lektion` (current Lektion page). If the same point already has a row,
update that row instead (Wrong, Date, Box 1, Lapses + 1).

**Weak spot** = the most common Category among Mistakes dated in the last 21 days.

## Hints (Settings → Hints)

When the learner asks for help or types "?":
1. The shape: number of words, first letter of each word with dots (`W··· w····· d·?`), and the
   noun's gender if relevant.
2. A one-line rule reminder that does not contain the answer or any word of it.
3. The answer. This counts as a miss.
Right after a hint counts as right, but the card moves up only one box less (stays in its box).

## Difficulty level (refresher and quick-lesson questions)

Level 1 = single words, articles, short gaps; 2 = phrases and short sentences; 3 = full sentences,
transformations, word order, cases. Start at 2. After each refresher, compare its accuracy with
Settings → Target accuracy: 5+ points above → level + 1 (max 3); 15+ points below → level − 1
(min 1). Store the level used in the Activity row.

## No repeats

Before writing questions, read Activity rows from the last Settings → "No-repeat days" days and
their `Questions asked`. Never repeat or closely copy those; vary the situation, verb and people.
Store the questions you asked (short, `;`-separated) in the new Activity row.

## Words table

When adding a word: `Word` (German, nouns with article), `English`, `Plural`, `Gender`
(der/die/das/-), `Example`, `Example EN`, `Key` (lowercase headword without article, e.g.
`tisch`), `Goethe` (A1/A2 if the key is in `curriculum/goethe_words.json`, else "Not on list"),
`Source`, `Added` today, `Lektion`. Check first that the word isn't already there (by Key).

## Progress position

The current Lektion = lowest `Index` in Lektionen whose Status isn't Done. Its next part is Part 2
if Status is "Part 1 done", else Part 1. Lessons are found by Key `L<index>-p1` / `L<index>-p2`.
