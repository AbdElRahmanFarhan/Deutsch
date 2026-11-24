"""Extract the headwords of the Goethe A1 and A2 word lists into curriculum/goethe_words.json.

The official PDFs (downloaded from goethe.de into Cirriculum/goethe/, not committed) are only
read here. The output keeps just the headword, article, plural and level, for checking which
exam words the learner already knows. This repo is private; don't publish the list.
"""
import json
import re
import subprocess
from collections import Counter

from common import ROOT

SRC = ROOT / "Cirriculum" / "goethe"
LISTS = [  # (level, file, alphabetical section starts on this PDF page, column crops)
    ("A1", "A1_SD1_Wortliste_02.pdf", None, [(0, 596)]),
    ("A2", "Goethe-Zertifikat_A2_Wortliste.pdf", None, [(0, 300), (300, 296)]),
]
ARTICLES = ("der ", "die ", "das ")
# Headings and page furniture on the word-group pages.
GROUP_STOP = {"inhalt", "vorwort", "seite", "wortgruppen", "wortliste", "themen", "themenbereiche",
              "farben", "himmelsrichtungen", "zahlen", "abkürzungen", "anglizismen", "buchstaben",
              "familienmitglieder", "berufe", "länder", "nationalitäten", "sprachen", "uhrzeit",
              "jahreszeiten", "tageszeiten", "wochentage", "monatsnamen", "datum", "maße", "gewichte",
              "geld", "schule", "alphabetische", "alphabetischer", "wortschatz", "goethe", "zertifikat",
              "deutsch", "teil", "und", "oder", "pl", "sg"}


def crop_text(pdf, page, x, w):
    return subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-x", str(x), "-y", "0",
                           "-W", str(w), "-H", "842", "-layout", str(pdf), "-"],
                          capture_output=True, text=True).stdout


def pages(pdf):
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", info).group(1))


def first_alpha_page(pdf):
    for p in range(1, pages(pdf) + 1):
        t = crop_text(pdf, p, 0, 596)
        if re.search(r"\bab\s{2,}Ab morgen", t):  # first entry of both lists
            return p
    raise SystemExit(f"no alphabetical section found in {pdf.name}")


def headword_segments(text):
    """Text from the headword column: the part of each line before the example column."""
    lines = [l for l in text.splitlines() if l.strip()]
    starts = Counter(len(l) - len(l.lstrip()) for l in lines)
    if not starts:
        return []
    used = [s for s, n in starts.items() if n >= 3]  # leftmost column used by several lines
    if not used:
        return []
    col = min(used)
    out = []
    for l in lines:
        indent = len(l) - len(l.lstrip())
        if indent > col + 2:
            out.append(None)  # example-only line: ends the previous headword
            continue
        seg = re.split(r"\s{2,}", l.strip())[0]
        if seg.startswith(("Alphabetische", "Wortliste", "ALPHABETISCHER", "Seite", "VS_", "WORTLISTE")):
            seg = re.sub(r"^(Alphabetische[rs]?|Wortliste|ALPHABETISCHER WORTSCHATZ)\s*", "", seg)
            if not seg:
                continue
        out.append(seg)
    return out


def entries(segments):
    """Join headword-column segments into entries (verb forms run over several lines)."""
    items, cur = [], ""
    for seg in segments:
        if seg is None:
            if cur:
                items.append(cur)
            cur = ""
            continue
        if re.fullmatch(r"[A-ZÄÖÜ]", seg) or re.fullmatch(r"\d+", seg):
            continue  # letter headings, page numbers
        if cur and cur.rstrip().endswith(","):
            cur += " " + seg
        elif cur and re.match(r"(der|die|das) \S+-$", cur) and seg[:1].islower():
            cur = cur[:-1] + seg  # a noun hyphenated across two lines: "das Kranken-" + "haus, ¨-er"
        else:
            if cur:
                items.append(cur)
            cur = seg
    if cur:
        items.append(cur)
    return items


def parse(entry, level):
    e = re.sub(r"\s+", " ", entry).strip()
    e = re.sub(r"\((Sg|Pl)\.\)", "", e).strip()
    article = next((a.strip() for a in ARTICLES if e.startswith(a)), "")
    body = e[len(article) + 1:] if article else e
    head, _, rest = body.partition(",")
    head = re.sub(r"^\(sich\)\s*", "", head).strip()
    head = re.sub(r"\s*\(.*?\)\s*", " ", head).strip()
    if not head or len(head) > 40 or not re.match(r"[A-Za-zÄÖÜäöüß]", head):
        return None
    if (head.isupper() and len(head) > 3) or re.match(r"(hat|ist|geht) ", head) or re.search(r"\d|Goethe|\bwith\b|Bsp|e\.V\.|\.", head) or len(head.split()) > 3:
        return None  # verb forms split from their entry, page furniture
    m = re.match(r"\s*([-–¨][¨\wäöüß-]*|–)", rest) if article else None
    plural = m.group(1) if m else ""
    key = head.lower().rstrip("-")
    return {"key": key, "de": f"{article} {head}".strip(), "article": article, "plural": plural, "level": level}


def main():
    words = {}
    for level, name, _, cols in LISTS:
        pdf = SRC / name
        start = first_alpha_page(pdf)
        n = 0
        # Word groups (days, months, times of day, ...) come before the alphabetical part.
        for p in range(2, start):
            text = crop_text(pdf, p, 0, 596)
            # Only list entries (start of a line or a column), not nouns inside running text.
            listed = re.findall(r"(?:^|\s{2,})(?:(?:der|die|das) [A-ZÄÖÜ][\wäöüß]+(?=\s{2,}|\s*$)|[A-ZÄÖÜ][\wäöüß]+,\s*[-¨])", text, re.M)
            for art, head, plural in re.findall(r"(?:^|\s{2,})(der|die|das) ([A-ZÄÖÜ][\wäöüß]+(?:/[A-ZÄÖÜ][\wäöüß]+)?)(?:,\s*([-¨][\wäöüß-]*))?(?=\s{2,}|\s*$)", text, re.M):
                key = head.split("/")[0].lower()
                if key not in words:
                    words[key] = {"key": key, "de": f"{art} {head.split('/')[0]}", "article": art,
                                  "plural": plural or "", "level": level}
                    n += 1
            # Group entries listed without an article: "Onkel, -", "Tante, -n", "blau", "Monat/Monatsnamen".
            # Only on real word-group pages (several "Noun, -plural" entries), not credits or the foreword.
            for head, plural in [] if len(listed) < 3 else re.findall(r"(?:^|\s{2,})([A-Za-zÄÖÜäöüß]+(?:/[A-Za-zÄÖÜäöüß]+)?)(?:,\s*([-¨][\wäöüß-]*|-))?(?:\s*\([^)]*\))?(?=\s{2,}|\s*$)", text, re.M):
                key = head.split("/")[0].lower()
                if len(key) < 3 or key in words or key in GROUP_STOP:
                    continue
                words[key] = {"key": key, "de": head.split("/")[0], "article": "",
                              "plural": plural if plural not in (None, "", "-") else "", "level": level}
                n += 1
        for p in range(start, pages(pdf) + 1):
            for x, w in cols:
                for ent in entries(headword_segments(crop_text(pdf, p, x, w))):
                    item = parse(ent, level)
                    if item and item["key"] not in words:
                        words[item["key"]] = item
                        n += 1
        print(f"{level}: {n} new headwords from page {start} on")
    out = sorted(words.values(), key=lambda x: x["key"])
    (ROOT / "curriculum" / "goethe_words.json").write_text(json.dumps(out, ensure_ascii=False, indent=0))
    print(f"total {len(out)}")


if __name__ == "__main__":
    main()
