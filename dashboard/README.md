# Control panel

`index.html` is the course control panel, published as a private claude.ai artifact:
https://claude.ai/artifact/NFccKogXmU69aP5ZNtkPhL

- **Today**: the planned lesson, today's sessions, cards and mistakes due, streak, and buttons for
  every activity. Below: course map (48 Lektionen), words, minutes per day, projected finish, weak
  spots, speaking scores.
- **Lesson player** (`#L<index>-p1` / `-p2`): goal and grammar, words (with audio), a reading text
  Claude writes for the lesson, listening (the Lektion's MP3 with track jumps and questions), book
  work, exercises checked by Claude, writing corrected by Claude, speaking (in the page by
  microphone or typing, or as a handoff to the Claude app), and Finish, which writes words,
  mistakes, the lesson/Lektion status and today's session to Notion.
- **Refresher, weekly revision, quick lesson, flashcards, speaking** follow the matching files in
  `workflows/` (Leitner rules, hints, no repeats, levels) and log to Notion the same way.

All course data stays in Notion. Progress inside an unfinished lesson (step, answers, drafts) is
saved on every change and step, in the browser and in the artifact's private per-viewer store, so it
survives reloads, tab switches and other devices; Finish writes the results to Notion.

## Publishing

The page needs capabilities `mcp` (server `Notion`: `notion-query-data-sources`, `notion-fetch`,
`notion-create-pages`, `notion-update-page`), `sample`, `tts`, `dictation`, and `db` + `user`
(unfinished-lesson progress, saved privately per viewer under `data/users/<id>/lesson-<key>`). Supporting files
published next to it:

- `goethe.json` = `curriculum/goethe_words.json`
- `audio/L<NN>-KB.mp3`, `audio/L<NN>-AB.mp3` = the output of `scripts/lektion_audio.py` (not in
  this repo; the book audio is the learner's own copy). Publish in batches under 64 MB.

To update the page only, publish `dashboard/index.html` again to the same artifact URL; files
already published stay.

## Language

The interface is German by default; the button at the top right switches to English (remembered per
device). The page is written in English and a translation layer (`I18N` phrases and `I18N_RX`
patterns in `index.html`) swaps interface text; German course content and Claude's explanations are
left as they are. New interface text needs an entry in `I18N`, or it stays English.
