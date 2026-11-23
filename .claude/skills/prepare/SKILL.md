---
name: prepare
description: Prepare upcoming Deutsch lessons from the Menschen book and store them in the dashboard. Use when the learner types /prepare, after a rebuild, or from the daily task.
---

# Prepare upcoming lessons

Read CLAUDE.md first (dashboard URL, lesson format, the rule about the book).

1. Read the live state with `ArtifactData`: `progress/main`, `config/schedule`, `config/plan`,
   `config/tutor`, `config/profile`, the ids in `lessons`, plus `mistakes` and `srs` (use
   `out_dir: "build/db"` for the big ones to keep them out of the conversation). Then work out:
   - **weak spots:** the most common `category` among mistakes of the last 21 days, with examples;
   - **hard words:** `srs` words with `leech: true`;
   - **word gaps:** run `python3 scripts/word_gaps.py <index>` for Goethe-list words that fit this
     Lektion's topic and aren't in the review queue yet.
2. Work out which lesson keys the next 3 days of sessions need, starting from
   `current_index` / `current_part`:
   - a `split` session uses `L<index>-p<part>`, then moves to part 2, or to the next Lektion after part 2;
   - a `full` session uses `L<index>-full`, then moves to the next Lektion;
   - `practice` and `weekly` sessions use their session id (`YYYY-MM-DD-slot`) and don't move the pointer.
   Skip keys that already exist in `lessons`, unless a rebuild asked for fresh lessons.
3. For each missing Lektion, read the book locally: `python3 scripts/book_text.py <index>`. The OCR is
   rough; use it to learn what the Kursbuch and Arbeitsbuch pages cover, which exercises and audio
   tracks there are, and the Lektion's words (with articles and plurals as printed).
4. Write each lesson in your own words as JSON in `lessons/<key>.json` (committed; your own words only), following the lesson
   format in CLAUDE.md. For a 1-hour `split` part, aim for:
   - part 1: `explain` (the grammar point, short, with 4-6 examples from everyday life in Germany),
     `vocab` (15 words from this Lektion), `book` (Kursbuch exercises by page and number, with the audio
     track numbers), `exercise` (8-10 items).
   - part 2: `explain` (a short recap or a second point), `book` (Arbeitsbuch exercises by page and
     number, checked with the AB answer key), `exercise` (10-12 items: transformation, translation,
     fill-in), `writing` (5-6 sentences), `speaking` (topic for the voice session).
   - `full` (2-3 h): both parts together, with ~25 words.
   - `practice` / `weekly`: mixed exercises on the last 2-4 Lektionen, one Goethe-A2-style task,
     `speaking`; `weekly` adds a 10-item mini-test.
   Words: take them from the Lektion, and every one must be on the Goethe A1/A2 list
   (`curriculum/goethe_words.json`) unless the book makes it essential. Nouns always with article
   and plural. If the Lektion has fewer than needed, fill up from the word gaps.
   Personalise: 2-3 exercise items on the top weak spot, and reuse 2-3 hard words in examples.
   Exercise items: `q` in English plus the German to work on, never containing the answer;
   `answer` the correct German; `accept` other correct forms. Explanations English only.
   Don't copy book texts, dialogues or exercises; refer to them by page and number instead.
   Include `lektion_index`, `part`, `kind` and `minutes` in the document.
5. Store them with one `ArtifactData` `batch` (`set`, collection `lessons`, `file_path` per entry).
6. Report which lessons are ready, in one or two lines.
