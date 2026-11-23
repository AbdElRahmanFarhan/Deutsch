"""Shared helpers: load settings, and pick the day's refresher times.

The refresher-time picker must stay identical to `slotsFor` in dashboard/index.html,
so the calendar, the email and the dashboard all show the same times.
"""
import json
import tomllib
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AREAS = ["schedule", "refreshers", "reminders", "plan", "tutor", "review",
         "accountability", "motivation", "profile"]
DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def load_config():
    """Live settings from the last /sync snapshot, falling back to the TOML defaults."""
    cfg = {}
    for area in AREAS:
        snap = ROOT / "state" / "config" / f"{area}.json"
        if snap.exists():
            cfg[area] = json.loads(snap.read_text())
        else:
            cfg[area] = tomllib.loads((ROOT / "config" / f"{area}.toml").read_text())
    return cfg


def to_min(hhmm):
    if not hhmm:
        return None
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def fnv1a(text):
    h = 0x811C9DC5
    for ch in text:
        h ^= ord(ch)
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h


def mulberry32(seed):
    state = [seed & 0xFFFFFFFF]

    def imul(x, y):
        return (x * y) & 0xFFFFFFFF

    def rnd():
        a = (state[0] + 0x6D2B79F5) & 0xFFFFFFFF
        state[0] = a
        t = imul(a ^ (a >> 15), 1 | a)
        t = ((t + imul(t ^ (t >> 7), 61 | t)) & 0xFFFFFFFF) ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296

    return rnd


def in_days_off(day, days_off):
    iso = day.isoformat()
    for entry in days_off or []:
        if ".." in entry:
            a, b = entry.split("..")
            if a <= iso <= b:
                return True
        elif entry == iso:
            return True
    return False


def sessions_for(day, cfg):
    """Focus sessions scheduled on `day` (a date), in schedule order, with their slot number."""
    sched = cfg["schedule"]
    if day.isoformat() < sched["start_date"] or in_days_off(day, sched.get("days_off")):
        return []
    key = DAYS[day.weekday()]
    out = []
    for s in sched["session"]:
        if s["day"] == key:
            out.append({**s, "slot": len(out) + 1, "id": f"{day.isoformat()}-{len(out) + 1}"})
    return out


def refresher_slots(day, cfg):
    """Start times (minutes after midnight) of the day's scheduled refreshers."""
    r = cfg["refreshers"]
    rem = cfg["reminders"]
    if not r.get("enabled") or DAYS[day.weekday()] not in r.get("days", []):
        return []
    lo = max(to_min(r["window_start"]), to_min(rem.get("quiet_end") or "00:00"))
    hi = min(to_min(r["window_end"]), to_min(rem.get("quiet_start") or "23:59"))
    length = int(r["minutes"])
    if hi - lo < length:
        return []
    blocked = []
    for s in sessions_for(day, cfg):
        start = to_min(s.get("start"))
        if start is not None:
            blocked.append((start - 15, start + int(s["minutes"]) + 15))
    rnd = mulberry32(fnv1a(day.isoformat() + "|refresher"))
    steps = (hi - length - lo) // 5 + 1
    picks = []
    for _ in range(300):
        if len(picks) >= int(r["per_day"]):
            break
        m = lo + int(rnd() * steps) * 5
        if any(m < b and m + length > a for a, b in blocked):
            continue
        if any(abs(m - p) < int(r["min_gap_minutes"]) for p in picks):
            continue
        picks.append(m)
    return sorted(picks)


def hhmm(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


if __name__ == "__main__":
    c = load_config()
    print([hhmm(m) for m in refresher_slots(date.today(), c)])
