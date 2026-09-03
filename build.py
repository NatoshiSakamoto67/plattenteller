#!/usr/bin/env python3
"""Baut index.html aus der Rumpf-Datei app-body.html (Style + Markup + Script)
und einem vollstaendigen <head> mit Icons, Manifest und Home-Bildschirm-Angaben.

Aufruf: python3 build.py app-body.html
"""

import sys

src = sys.argv[1] if len(sys.argv) > 1 else "app-body.html"
body = open(src, encoding="utf-8").read().replace("<title>Plattenteller</title>\n", "", 1)

FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Ccircle cx='16' cy='16' r='15' fill='%23050706'/%3E"
    "%3Ccircle cx='16' cy='16' r='11' fill='none' stroke='%2329F07C' stroke-width='2'/%3E"
    "%3Ccircle cx='16' cy='16' r='3.5' fill='%2329F07C'/%3E%3C/svg%3E"
)

HEAD = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Plattenteller</title>
<meta name="description" content="Glücksrad für DJ-Treffen: Namen eintragen, drehen, jeder landet zufällig in seinem Stunden-Slot.">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#050706" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#EDF2EF" media="(prefers-color-scheme: light)">

<link rel="icon" href="{FAVICON}">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="manifest.webmanifest">

<!-- Zum Home-Bildschirm: eigenes Symbol, eigener Name, ohne Browser-Leisten -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Plattenteller">
<meta name="apple-mobile-web-app-status-bar-style" content="black">

<style>html,body{{margin:0}}img{{max-width:100%}}</style>
</head>
<body>
"""

open("index.html", "w", encoding="utf-8").write(HEAD + body + "\n</body>\n</html>\n")
print("index.html gebaut aus", src)
