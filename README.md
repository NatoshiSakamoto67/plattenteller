# Plattenteller

Glücksrad für DJ-Treffen: Namen eintragen, Rad drehen, jeder landet zufällig in
seinem Stunden-Slot. Eine einzelne HTML-Datei, kein Build, keine Abhängigkeiten,
kein Server — alles läuft im Browser, gespeichert wird nur lokal im Gerät.

**Live:** https://natoshisakamoto67.github.io/plattenteller/

## Bedienung

- Namen eintragen (mehrere auf einmal: mit Komma trennen oder Liste einfügen)
- **Drehen** → der Getroffene wird in den nächsten freien Slot geschrieben
- Einstellungen (oranger Balken): Startzeit, Länge pro Slot, Anzahl Slots, Modus
- *Jeder 1×* = niemand doppelt · *Mehrfach* = alle bleiben im Rad
- Läuft der Abend über Mitternacht, markiert ein **+1** den Tageswechsel

## Auf dem Handy

Seite im Browser öffnen → Teilen → **Zum Home-Bildschirm**. Sie bekommt dann ein
eigenes Icon (Glücksrad in Schwarz/Grün) und startet ohne Browser-Leisten.

## Entwicklung

- `app-body.html` — die eigentliche App (Style, Markup, Script in einer Datei)
- `build.py` — setzt den `<head>` mit Icons und Manifest davor → `index.html`
- `make-icon.py` — zeichnet die App-Icons aus Code (PIL), keine Bilddateien nötig

```bash
python3 build.py app-body.html   # nach Änderungen an app-body.html
git add -A && git commit -m "..." && git push
```

GitHub Pages baut selbst, nach ~1 Minute ist es live.
