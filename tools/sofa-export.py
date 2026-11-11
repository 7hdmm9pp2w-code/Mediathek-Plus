#!/usr/bin/env python3
"""Sofa-Web-App (Stufe G): erstellt sofa.json mit den Reihen der Startseite.

Fragt einen laufenden Mediathek-Plus-Server (NAS-Fassung, z. B. das Docker-Image) über seine
Web-Schnittstelle ab – dort steckt die ganze Logik (Film-Themen der Sender, filmdienst, TMDB).
Das TMDB-Token bleibt beim Server, in der Datei stehen nur Plakat-Adressen.

    python3 scripts/sofa-export.py http://127.0.0.1:8080 build-sofa/sofa.json
"""
import json
import sys
import time
import urllib.request

SERVER = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://127.0.0.1:8080"
OUT = sys.argv[2] if len(sys.argv) > 2 else "sofa.json"

# Höchstzahl Einträge je Reihe in der Datei (Serien: Folgen, werden in der Web-App zu Karten)
LIMITS = {"films": 160, "series": 400, "docs": 200, "kids": 200, "expiring": 80, "live": 80}
# Diese Felder braucht die Web-App; der Rest bleibt draußen (Dateigröße)
KEEP = (
    "url title kind channel topic description duration timestamp website subtitle urlStd availableUntil "
    "downloadable ovUrl ovSubtitle ovLang multiAudio series season episode variant ovOnly pick added"
).split()


def call(cmd, args=None, timeout=300):
    req = urllib.request.Request(
        f"{SERVER}/api/{cmd}",
        data=json.dumps(args or {}).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as res:
        return json.loads(res.read())


def slim(v):
    out = {k: v[k] for k in KEEP if k in v and v[k] not in ("", None)}
    # Pflichtfelder der Oberfläche
    for k, d in (("suggestedName", ""), ("preview", ""), ("downloadedAt", 0), ("onDisk", False)):
        out.setdefault(k, d)
    for k in ("ovUrl", "ovSubtitle", "subtitle", "urlStd", "website", "series", "description", "topic"):
        out.setdefault(k, "")
    for k in ("season", "episode", "duration", "timestamp", "availableUntil"):
        out.setdefault(k, 0)
    for k in ("variant", "ovOnly", "multiAudio"):
        out.setdefault(k, False)
    out.setdefault("downloadable", True)
    return out


def main():
    started = time.time()
    shelves = {}
    for kind, limit in LIMITS.items():
        shelves[kind] = [slim(v) for v in call("sofa_shelf", {"kind": kind, "channel": None})[:limit]]
        print(f"{kind}: {len(shelves[kind])}", file=sys.stderr)
    picks = [v for v in call("filmdienst_list") if not (v.get("media") or {}).get("played")]
    shelves["picks"] = [slim(v) for v in picks]
    stage = call("film_of_the_day")
    if stage:
        stage = [slim(stage[0]), stage[1]]

    # Filminfos (Plakat, Jahr, Genre, Bewertung) für Filme, Bilder für Serien/Dokus/Kinder/Live
    films = [v for k in ("films", "picks", "expiring") for v in shelves[k] if not v.get("episode")]
    infos = call("film_info", {"videos": films, "request": None}, timeout=900) if films else {}
    if stage:
        infos[stage[0]["url"]] = stage[1]
    rest = [v for k in ("series", "docs", "kids", "picks") for v in shelves[k] if not (infos.get(v["url"]) or {}).get("poster")]
    art = call("artwork", {"videos": rest}, timeout=900) if rest else {}

    # Trailer: nur für das, was vorne steht (eine Anfrage je Film)
    ids = []
    for v in ([stage[0]] if stage else []) + shelves["picks"] + shelves["expiring"] + shelves["films"][:60]:
        tmdb = (infos.get(v["url"]) or {}).get("tmdb")
        if tmdb and tmdb not in ids:
            ids.append(tmdb)
    trailers = {}
    for tmdb in ids:
        try:
            trailers[str(tmdb)] = call("film_trailer", {"id": tmdb}, timeout=60)
        except Exception:
            pass

    data = {"generated": int(time.time()), "stage": stage, "shelves": shelves, "infos": infos, "art": art, "trailers": trailers}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{OUT}: {sum(len(s) for s in shelves.values())} Einträge, {len(infos)} Filminfos, {len(art)} Bilder, "
          f"{sum(1 for t in trailers.values() if t)} Trailer – {time.time() - started:.0f} s", file=sys.stderr)


if __name__ == "__main__":
    main()
