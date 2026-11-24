# Progress

Trigger: "progress", "how am I doing", "where am I". Read-only. Follow `common.md`.

Compute and show briefly (a small table is fine):

- **Course**: current Lektion and part; Lektionen done / 48; study hours left
  (remaining Lektionen × "Hours per A1/A2 Lektion" + "Exam prep hours", minus half a Lektion if
  Part 1 is done).
- **Pace**: planned hours per week (sum of Schedule sessions) vs. actual minutes in the last 7 days
  (Sessions Done + Activity). Projected finish = today + hours left ÷ weekly hours (use the actual
  pace if fewer than "Minimum sessions per week" sessions were done in the last 7 days), plus days
  off. Compare with Settings → Target date and say "on track" or how far behind.
- **Sessions**: done and missed this week; where missed time was moved (Make-up minutes).
- **Streak**: consecutive days back from today (or yesterday) with a Done session or an Activity
  row (Settings → Streak counts); days off don't break it.
- **Words**: Learning / Known counts; Goethe coverage = Words with Goethe A1 (A2) and Box ≥ 1
  ÷ the number of A1 (A2) entries in `curriculum/goethe_words.json`; due today.
- **Weak spots**: top 3 mistake categories of the last 21 days; hard words.
- If Settings → Motivation includes progress facts: one encouraging but factual sentence. If it
  includes sayings: a saying from `curriculum/sayings.json` with its meaning.
