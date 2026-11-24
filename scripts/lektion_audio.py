"""Join each Lektion's Menschen audio tracks into two compact MP3s (Kursbuch, Arbeitsbuch).

    python3 scripts/lektion_audio.py <unpacked audio dir> <out dir> <ffmpeg path>

<unpacked audio dir> holds the unzipped audio folders as "<volume>-<Kursbuch|Arbeitsbuch>/...".
Writes <out>/L00-KB.mp3, L00-AB.mp3, ... (mono, 40 kbit/s, 1.5 s of silence between tracks) and
<out>/tracks.json: for each file, the track names and their start times, for the lesson pages.
Laptop only; the audio comes from the learner's own copies.
"""
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RATE = 22050
GAP = b"\x00\x00" * int(RATE * 1.5)
FIRST_INDEX = {"A1.1": (1, 0), "A1.2": (13, 12), "A2.1": (1, 24), "A2.2": (13, 36)}  # book Lektion -> index


def lektion_tracks(audio_dir):
    """{(index, "KB"|"AB"): [(order, label, path)]}"""
    out = {}
    for f in sorted(Path(audio_dir).rglob("*.mp3")):
        vol, book = f.relative_to(audio_dir).parts[0].split("-")
        name = unicodedata.normalize("NFC", f.name)  # some zips store umlauts decomposed
        m = re.search(r"Lektion[ _](\d+)[ _,]+(.+)\.mp3$", name)
        if not m:
            continue  # intros, module tracks
        first, base = FIRST_INDEX[vol]
        index = int(m.group(1)) - first + base
        label = re.sub(r"[_ ]+", " ", m.group(2)).replace(" ,", ",").strip()
        lead = re.match(r"(\d+)", name)
        order = int(lead.group(1)) if lead else 0
        kind = "KB" if book == "Kursbuch" else "AB"
        out.setdefault((index, kind), []).append((order, natural(label), f"Lektion {m.group(1)}, {label}", f))
    return out


def natural(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def pcm(ffmpeg, path):
    return subprocess.run([ffmpeg, "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(RATE),
                           "-f", "s16le", "-"], capture_output=True, check=True).stdout


def main():
    audio_dir, out_dir, ffmpeg = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    out_dir.mkdir(parents=True, exist_ok=True)
    index = {}
    for (idx, kind), tracks in sorted(lektion_tracks(audio_dir).items()):
        tracks.sort(key=lambda t: (t[0], t[1]))
        raw, listing = b"", []
        for _, _, label, path in tracks:
            listing.append({"track": label, "start": f"{len(raw) // 2 // RATE // 60}:{len(raw) // 2 // RATE % 60:02d}"})
            raw += pcm(ffmpeg, path) + GAP
        name = f"L{idx:02d}-{kind}.mp3"
        subprocess.run([ffmpeg, "-v", "error", "-y", "-f", "s16le", "-ar", str(RATE), "-ac", "1", "-i", "-",
                        "-b:a", "40k", str(out_dir / name)], input=raw, check=True)
        index[name] = {"index": idx, "book": kind, "minutes": round(len(raw) / 2 / RATE / 60, 1),
                       "bytes": (out_dir / name).stat().st_size, "tracks": listing}
        print(name, index[name]["minutes"], "min", index[name]["bytes"] // 1024, "KB", len(listing), "tracks")
    (out_dir / "tracks.json").write_text(json.dumps(index, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
