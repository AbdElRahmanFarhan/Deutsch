# Deutsch A2: personal German course (A1 → Goethe A2)

This repo holds **how** the course runs (workflows, syllabus, helper scripts). **All data lives in
Notion** under the page "Deutsch A2": settings, Lektionen, lessons, words, mistakes, sessions,
activity, weekly reviews, book PDFs. Nothing personal or stateful is stored here.

- **The learner:** Abdelrahman, adult engineer living and working in Germany, Egyptian, studies in
  English. Everything the tutor writes is in English; German only as the thing being learned.
- **Where he practises:** the Claude app Project "Deutsch" (phone/laptop, text or voice), set up
  from `project/INSTRUCTIONS.md`. Claude Code sessions on this repo (cloud or laptop) can run the
  same workflows.
- **Automation:** cloud routines run `workflows/morning-plan.md` daily and
  `workflows/weekly-review.md` on Sundays.

## Map

| Path | What |
|---|---|
| `workflows/` | The instructions for every activity. Start with `workflows/README.md` and `common.md`. |
| `.claude/skills/` | Thin wrappers so `/lesson`, `/refresher`, ... run the matching workflow |
| `project/INSTRUCTIONS.md` | Setup and custom instructions for the Claude app Project |
| `notion/ids.json` | Notion page and data source ids; Lektion page id per course index |
| `notion/book_pages.json` | Kursbuch/Arbeitsbuch PDF page ranges per Lektion |
| `curriculum/syllabus.md`, `syllabus.json` | The 48 Menschen Lektionen (index 0-47) |
| `curriculum/goethe_words.json` | Goethe A1/A2 headwords, for vocabulary choice and coverage |
| `curriculum/sayings.json` | German sayings for motivation |
| `scripts/book_text.py` | Laptop only: OCR text of a Lektion's book pages from `Cirriculum/` |
| `scripts/goethe_list.py` | Laptop only: rebuilds `goethe_words.json` from the official PDFs |
| `scripts/lektion_audio.py` | Laptop only: joins each Lektion's audio tracks into `L<index>-KB.mp3` / `-AB.mp3` (needs ffmpeg) |

## Sources

- **Primary:** Menschen (Hueber) A1.1-A2.2, Kursbuch + Arbeitsbuch: the learner's own copies, in
  `Cirriculum/` on the laptop (ignored by this public repo, never commit them here). Complete
  copies with audio are in the private repo github.com/AbdElRahmanFarhan/deutsch-books; to work
  on lessons elsewhere, clone it into `Cirriculum/`. Per-Lektion page extracts and
  the answer keys are in the learner's private Notion (Lektionen → Book pages, Books database).
  Lessons are written in our own words with page references; never paste book texts, dialogues or
  exercises into lesson pages.
- Vocabulary fits the Goethe A1/A2 word lists. Articles and plurals come from the book.

## Rules

- Follow `workflows/common.md` in every workflow: read Settings first, Leitner boxes, mistakes,
  hints, no repeats, Europe/Berlin time.
- Don't create data files in the repo; write data to Notion.
- Commit after each change with a clear message and push (`origin` = github.com/AbdElRahmanFarhan/Deutsch, public).
