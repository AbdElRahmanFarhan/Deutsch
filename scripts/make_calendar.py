"""Write calendar/deutsch.ics: focus sessions and refresher slots until the target date.

Import it into Google Calendar (Settings -> Import & export) into a calendar called
"Deutsch". Events keep stable ids, so importing a rebuilt file updates them.
"""
from datetime import date, datetime, timedelta, timezone

from common import ROOT, hhmm, load_config, refresher_slots, sessions_for, to_min

KIND = {"split": "Lektion part", "full": "Full Lektion", "practice": "Practice block", "weekly": "Weekly review"}


def stamp(day, minutes):
    return f"{day.strftime('%Y%m%d')}T{hhmm(minutes).replace(':', '')}00"


def event(uid, day, start, length, title, desc, lead):
    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid}@deutsch-a2",
        f"DTSTAMP:{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
        f"DTSTART;TZID=Europe/Berlin:{stamp(day, start)}",
        f"DTEND;TZID=Europe/Berlin:{stamp(day, start + length)}",
        f"SUMMARY:{title}",
        f"DESCRIPTION:{desc}",
    ]
    if lead is not None:
        lines += ["BEGIN:VALARM", "ACTION:DISPLAY", f"DESCRIPTION:{title}",
                  f"TRIGGER:-PT{lead}M", "END:VALARM"]
    return lines + ["END:VEVENT"]


def main():
    cfg = load_config()
    rem = cfg["reminders"]
    lead = int(rem.get("session_lead_minutes", 10))
    start = max(date.fromisoformat(cfg["schedule"]["start_date"]), date.today())
    end = date.fromisoformat(cfg["plan"]["goal"]["target_date"])
    out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//deutsch-a2//EN", "CALSCALE:GREGORIAN",
           "X-WR-CALNAME:Deutsch", "X-WR-TIMEZONE:Europe/Berlin"]
    n_sessions = n_refreshers = skipped = 0
    day = start
    while day <= end:
        for s in sessions_for(day, cfg):
            m = to_min(s.get("start"))
            if m is None:
                skipped += 1
                continue
            out += event(s["id"], day, m, int(s["minutes"]), f"Deutsch: {KIND.get(s['kind'], s['kind'])}",
                         "Open the Deutsch A2 dashboard and press Start.", lead)
            n_sessions += 1
        if rem.get("refresher_events", True):
            length = int(cfg["refreshers"]["minutes"])
            for k, m in enumerate(refresher_slots(day, cfg)):
                out += event(f"{day.isoformat()}-r{k + 1}", day, m, length, "Deutsch: 10-min refresher",
                             "Dashboard -> Practice -> Start refresher.", 0)
                n_refreshers += 1
        day += timedelta(days=1)
    out.append("END:VCALENDAR")
    path = ROOT / "calendar" / "deutsch.ics"
    path.parent.mkdir(exist_ok=True)
    path.write_text("\r\n".join(out) + "\r\n")
    print(f"{path}: {n_sessions} sessions, {n_refreshers} refreshers"
          + (f"; {skipped} sessions skipped because they have no start time" if skipped else ""))


if __name__ == "__main__":
    main()
