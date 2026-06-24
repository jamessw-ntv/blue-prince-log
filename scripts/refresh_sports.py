#!/usr/bin/env python3
"""Refresh sports/data.json from public sources.

Runs in GitHub Actions (open internet), NOT in the dev sandbox. Design rules:
  - keep-last-good: a source that errors leaves its existing data untouched.
  - validate before accept: numbers must reconcile (e.g. AFL pts == 4*W + 2*D).
  - editorial fields (focus.note, paths narratives) are preserved, never overwritten.
  - only write when the meaningful data changed, so we don't spam timestamp-only commits.

Add a source by writing a refresh_<x>(data) -> str function and listing it in SOURCES.
"""
import json
import sys
import urllib.request
import datetime
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPORTS = ROOT / "sports" / "data.json"
YEAR = 2026
UA = "jamessw-ntv-dashboard/1.0 (+https://github.com/jamessw-ntv/jamessw-ntv.github.io)"


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


# --- AFL via Squiggle (https://api.squiggle.com.au) -------------------------
# Squiggle team name -> dashboard display name (keeps the rest of the board consistent).
AFL_NAME = {
    "Adelaide": "Adelaide Crows", "Brisbane Lions": "Brisbane Lions", "Carlton": "Carlton",
    "Collingwood": "Collingwood", "Essendon": "Essendon", "Fremantle": "Fremantle",
    "Geelong": "Geelong Cats", "Gold Coast": "Gold Coast SUNS",
    "Greater Western Sydney": "GWS GIANTS", "Hawthorn": "Hawthorn", "Melbourne": "Melbourne",
    "North Melbourne": "North Melbourne", "Port Adelaide": "Port Adelaide", "Richmond": "Richmond",
    "St Kilda": "St Kilda", "Sydney": "Sydney Swans", "West Coast": "West Coast Eagles",
    "Western Bulldogs": "Western Bulldogs",
}


def refresh_afl(data):
    st = get_json(f"https://api.squiggle.com.au/?q=standings;year={YEAR}").get("standings") or []
    if len(st) < 18:
        raise ValueError(f"AFL standings looked wrong ({len(st)} rows, expected 18)")
    ladder = []
    for r in st:
        name = AFL_NAME.get(r["team"], r["team"])
        forp, against = int(r["for"]), int(r["against"])
        pct = round(forp / against * 100, 1) if against else 0.0
        ladder.append([int(r["rank"]), name, int(r["played"]), int(r["wins"]), int(r["losses"]),
                       int(r["draws"]), forp, against, pct, int(r["pts"])])
    # reconcile: premiership points must equal 4*W + 2*D
    for pos, nm, P, W, L, D, FOR, AG, PCT, PTS in ladder:
        if PTS != 4 * W + 2 * D:
            raise ValueError(f"AFL points mismatch for {nm}: {PTS} != 4*{W}+2*{D}")
    data["afl"]["ladder"] = ladder
    # sync Carlton's focus numbers; leave note/form/next/fixtures (editorial) alone for now
    car = next((row for row in ladder if row[1] == "Carlton"), None)
    if car:
        f = data["afl"]["focus"]
        f["pos"], f["pts"], f["pct"] = car[0], car[9], car[8]
        f["record"] = f"{car[3]}–{car[4]}" + (f"–{car[5]}" if car[5] else "")
    return f"AFL ladder ({len(ladder)} teams)"


# Register sources here. World Cup and NRL fetchers land next.
SOURCES = [
    ("afl", refresh_afl),
]


def _canon(d):
    """Structural fingerprint ignoring the freshness stamps, so we only commit real changes."""
    c = json.loads(json.dumps(d))
    c.get("meta", {}).pop("fetched", None)
    c.get("meta", {}).pop("updated", None)
    return json.dumps(c, ensure_ascii=False, sort_keys=True)


def main():
    data = json.loads(SPORTS.read_text(encoding="utf-8"))
    before = _canon(data)
    results, errors = [], []
    for name, fn in SOURCES:
        try:
            results.append(fn(data))
        except Exception as e:  # noqa: BLE001 - one bad source must not sink the rest
            errors.append(f"{name}: {e}")
            print(f"::warning::{name} refresh failed, keeping last-good: {e}", file=sys.stderr)

    changed = _canon(data) != before
    if changed:
        now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
        data["meta"]["fetched"] = now
        data["meta"]["updated"] = now[:10]
        SPORTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"updated: {', '.join(results) or 'none'}")
    if errors:
        print(f"errors:  {'; '.join(errors)}")
    print(f"changed: {changed}")
    # Fail the job only if every source errored (so transient single-source blips stay green).
    if errors and not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
