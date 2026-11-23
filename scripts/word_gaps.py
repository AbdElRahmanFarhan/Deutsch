"""List Goethe-list words not yet in the review queue, for filling a lesson's word list.

    python3 scripts/word_gaps.py <lektion index> [--all]

Reads the review queue from the last /sync (state/srs.json). Prints the Lektion's level first
(A1 Lektionen draw on the A1 list, A2 Lektionen on both), then candidates in list order.
Choosing the words that fit the Lektion's topic is left to whoever prepares the lesson.
"""
import json
import re
import sys

from common import ROOT


def lemma_key(de):
    """Same rule as lemmaKey() in dashboard/index.html."""
    s = re.sub(r"^(der|die|das)\s+", "", de or "", flags=re.I).split(",")[0]
    return re.sub(r"\(.*?\)", "", s).strip().lower().rstrip("-")


def main():
    index = int(sys.argv[1])
    item = json.loads((ROOT / "curriculum" / "syllabus.json").read_text())[index]
    words = json.loads((ROOT / "curriculum" / "goethe_words.json").read_text())
    srs_file = ROOT / "state" / "srs.json"
    srs = json.loads(srs_file.read_text()) if srs_file.exists() else {}
    have = {lemma_key(it.get("de", "")) for it in srs.values() if it.get("type") == "word"}
    levels = {"A1"} if item["level"] == "A1" else {"A1", "A2"}
    gaps = [w for w in words if w["level"] in levels and w["key"] not in have]
    print(f"{item['volume']} L{item['lektion']} {item['title']} | topic: {item['topic']}")
    print(f"{len(have)} words in the review queue; {len(gaps)} Goethe {'/'.join(sorted(levels))} words not yet learned\n")
    limit = None if "--all" in sys.argv else 400
    for w in gaps[:limit]:
        print(f"{w['de']}{', ' + w['plural'] if w['plural'] else ''}  [{w['level']}]")


if __name__ == "__main__":
    main()
