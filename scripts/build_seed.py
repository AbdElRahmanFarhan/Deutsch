"""Build the documents that seed the dashboard's database.

Writes one JSON file per document to build/seed/<collection>__<doc>.json, plus
curriculum/syllabus.json. Run from anywhere:  python3 scripts/build_seed.py [area ...]
With area names, only those config documents are written (used by /push-config).
"""
import json
import re
import sys
import tomllib

from common import AREAS, ROOT

OUT = ROOT / "build" / "seed"
VOLUMES = ["A1.1", "A1.2", "A2.1", "A2.2"]


def parse_syllabus():
    text = (ROOT / "curriculum" / "syllabus.md").read_text()
    items = []
    for vol in VOLUMES:
        section = text.split(f"## {vol} (")[1].split("\n## ")[0]
        for line in section.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 6 or not cells[1].isdigit():
                continue
            modul, lek, page, title, topic, grammar = cells
            items.append({
                "index": len(items),
                "volume": vol,
                "level": vol[:2],
                "modul": int(modul),
                "lektion": int(lek),
                "page": int(page),
                "title": title,
                "topic": topic,
                "grammar": re.sub(r"\*", "", grammar),
            })
    assert len(items) == 48, f"expected 48 Lektionen, found {len(items)}"
    return items


def write(collection, doc, data):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{collection}__{doc}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))


def main(areas):
    for area in areas:
        write("config", area, tomllib.loads((ROOT / "config" / f"{area}.toml").read_text()))
    if areas != AREAS:
        return
    syllabus = parse_syllabus()
    (ROOT / "curriculum" / "syllabus.json").write_text(
        json.dumps(syllabus, ensure_ascii=False, indent=1))
    write("meta", "syllabus", {"items": syllabus})
    write("meta", "sayings", {"items": json.loads((ROOT / "curriculum" / "sayings.json").read_text())})
    goethe = json.loads((ROOT / "curriculum" / "goethe_words.json").read_text())
    write("meta", "goethe", {"words": [[w["key"], w["level"]] for w in goethe]})
    write("progress", "main", {"current_index": 0, "current_part": 1, "done": [], "started": None})
    print(f"wrote {len(list(OUT.glob('*.json')))} documents to {OUT}")


if __name__ == "__main__":
    main(sys.argv[1:] or AREAS)
