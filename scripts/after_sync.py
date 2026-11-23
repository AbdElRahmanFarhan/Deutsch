"""Turn the raw dashboard export in build/db/ into readable backups in state/.

/sync exports every collection with ArtifactData (out_dir=build/db), then runs this.
Writes state/config/<area>.json, state/progress.json, state/srs.json,
state/sessions.json and state/mistakes.md.
"""
import json
from collections import defaultdict

from common import ROOT

RAW = ROOT / "build" / "db"
STATE = ROOT / "state"


def docs(collection):
    out = {}
    for f in sorted((RAW / collection).glob("*.json")) if (RAW / collection).exists() else []:
        d = json.loads(f.read_text())
        body = d.get("data", d) if isinstance(d, dict) and "data" in d and "id" in d else d
        out[f.stem] = body
    return out


def dump(name, data):
    (STATE / name).write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def main():
    (STATE / "config").mkdir(parents=True, exist_ok=True)
    for area, body in docs("config").items():
        dump(f"config/{area}.json", body)
    dump("progress.json", docs("progress").get("main", {}))
    dump("srs.json", docs("srs"))
    dump("sessions.json", docs("sessions"))
    dump("refreshers.json", docs("refreshers"))
    mistakes = list(docs("mistakes").values())
    groups = defaultdict(list)
    for m in sorted(mistakes, key=lambda m: m.get("date", ""), reverse=True):
        groups[m.get("category") or "other"].append(m)
    lines = ["# Mistakes", "", "Grouped by type, newest first. Written by /sync from the dashboard.", ""]
    for cat, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        lines += [f"## {cat} ({len(items)})", ""]
        for m in items:
            reason = f" — {m['reason']}" if m.get("reason") else ""
            lines.append(f"- {m.get('date', '')}: ~~{m.get('wrong', '')}~~ → **{m.get('right', '')}**{reason}")
        lines.append("")
    (STATE / "mistakes.md").write_text("\n".join(lines))
    rebuild = docs("meta").get("rebuild", {})
    print(json.dumps({
        "config_areas": len(list((STATE / "config").glob("*.json"))),
        "srs_items": len(docs("srs")), "sessions": len(docs("sessions")), "mistakes": len(mistakes),
        "rebuild_requested": bool(rebuild.get("requested_at")) and not rebuild.get("done_at"),
    }))


if __name__ == "__main__":
    main()
