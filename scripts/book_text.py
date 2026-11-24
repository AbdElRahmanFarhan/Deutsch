"""Print the Menschen Kursbuch and Arbeitsbuch text for one Lektion (local use only).

    python3 scripts/book_text.py 0          # syllabus index 0..47
    python3 scripts/book_text.py 0 --kb     # Kursbuch only

The text is OCR from the PDFs in Cirriculum/ and is rough. It's for preparing lessons
on this laptop; never commit or upload it.
"""
import json
import re
import subprocess
import sys
import unicodedata

from common import ROOT

BOOKS = ROOT / "Cirriculum"
KB = {"A1.1": "A1.1/Kursbuch/Menschen A1-1 KB [einfach.ir].pdf",
      "A1.2": "A1.2/Kursbuch/Menschen A1-2 KB [einfach.ir].pdf",
      "A2.1": "A2.1/Kursbuch/Menschen A2.1 KB [einfach.ir].pdf",
      "A2.2": "A2.2/Kursbuch/Menschen A2.2 KB [einfach.ir].pdf"}
AB = {"A1.1": "A1.1/Arbeitsbuch/Menschen A1-1 AB [einfach.ir].pdf",
      "A1.2": "A1.2/Arbeitsbuch/Menschen A1-2 AB [einfach.ir].pdf",
      "A2.1": "A2.1/Arbeitsbuch/Menschen A2.1 AB [einfach.ir].pdf",
      "A2.2": "A2.2/Arbeitsbuch/Menschen A2.2 AB [einfach.ir].pdf"}
KB_OFFSET = {"A1.1": 0, "A1.2": 0, "A2.1": 0, "A2.2": 2}  # PDF page = printed page + offset


def page_text(pdf, page):
    out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(pdf), "-"],
                         capture_output=True, text=True)
    return out.stdout


def page_count(pdf):
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", info).group(1))


def key(text):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]+", "", t)


def find_title_page(pdf, title, start):
    """First page at or after `start` whose text contains the Lektion title (OCR-tolerant)."""
    words = [w for w in re.findall(r"\w+", title) if len(w) > 2][:3]
    probe = key(" ".join(words))
    for p in range(start, page_count(pdf) + 1):
        text = page_text(pdf, p)
        if "SEITE" in text[:600] or text.count("Basistraining") >= 2:
            continue  # contents pages list every title
        if probe and probe in key(text):
            return p
    return None


def main():
    index = int(sys.argv[1])
    syllabus = json.loads((ROOT / "curriculum" / "syllabus.json").read_text())
    it = syllabus[index]
    vol = it["volume"]
    kb = BOOKS / KB[vol]
    first = it["page"] + KB_OFFSET[vol]
    print(f"# {vol} Lektion {it['lektion']}: {it['title']}\n")
    print(f"## Kursbuch, printed pages {it['page']}-{it['page'] + 3}\n")
    for p in range(first, first + 4):
        print(f"--- Kursbuch page {p - KB_OFFSET[vol]} ---")
        print(page_text(kb, p))
    if "--kb" in sys.argv:
        return
    ab = BOOKS / AB[vol]
    # Page ranges found from each Lektion's Lernwortschatz (last) page; see notion/book_pages.json.
    start, last = json.loads((ROOT / "notion" / "book_pages.json").read_text())[str(index)]["ab"]
    print(f"## Arbeitsbuch, PDF pages {start}-{last}\n")
    for p in range(start, last + 1):
        print(f"--- Arbeitsbuch PDF page {p} ---")
        print(page_text(ab, p))


if __name__ == "__main__":
    main()
