# Prepare or refine lessons (laptop)

The book PDFs are on the laptop in `Cirriculum/` (not in git). All 48 Lektionen were prepared
once; use this to rewrite or improve one.

1. Read `lesson-format.md`.
2. Read the book pages: `python3 scripts/book_text.py <index>` (OCR text). Alternatively open the
   Lektion's "Book pages" PDF in Notion. Page ranges per Lektion: `notion/book_pages.json`.
3. Read the learner's data that should shape the lesson: weak-spot categories (Mistakes, last 21
   days), hard words, and any notes the learner left on the lesson page.
4. Rewrite the lesson page(s) in Notion (`update-page` with `replace_content`), keeping the
   properties. Own words only; page and exercise references instead of copied book content.

From a cloud session (no book files): you can still refine a lesson from its existing content,
the syllabus and the learner's data; for book details, download the Lektion's "Book pages" PDF
from Notion (`get_file_download_urls`) and read it with `pdftotext` if available.
