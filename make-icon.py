#!/usr/bin/env python3
"""Erzeugt die App-Icons (Glücksrad in Schwarz/Grün) aus reinem Code.

Aufruf: python3 make-icon.py
Ergebnis: icon-512.png, icon-192.png, apple-touch-icon.png
"""

from PIL import Image, ImageDraw

SIZE = 512
SS = 4                      # vierfach zeichnen, dann verkleinern = weiche Kanten
BG = "#050706"
RIM = "#16211A"
NEON = "#29F07C"
SEAM = "#050706"
RAMP = ["#0F2A1B", "#1F7A41", "#22B85B", "#29F07C"]
SEGMENTS = 8


def draw_icon(px):
    img = Image.new("RGB", (px, px), BG)
    d = ImageDraw.Draw(img)
    c = px / 2
    r_wheel = px * 0.352
    r_rim = px * 0.382
    r_hub = px * 0.094

    # Aussenring als ruhige Fassung um das Rad
    d.ellipse([c - r_rim, c - r_rim, c + r_rim, c + r_rim],
              outline=RIM, width=int(px * 0.016))

    # Segmente: Rampe von Schwarzgruen bis Neongruen
    box = [c - r_wheel, c - r_wheel, c + r_wheel, c + r_wheel]
    step = 360 / SEGMENTS
    for i in range(SEGMENTS):
        d.pieslice(box, start=i * step - 90, end=(i + 1) * step - 90,
                   fill=RAMP[i % len(RAMP)], outline=SEAM, width=int(px * 0.006))

    # Nabe wie ein Plattenlabel
    d.ellipse([c - r_hub, c - r_hub, c + r_hub, c + r_hub],
              fill=BG, outline=NEON, width=int(px * 0.014))
    r_dot = px * 0.019
    d.ellipse([c - r_dot, c - r_dot, c + r_dot, c + r_dot], fill=NEON)

    # Zeiger oben, mit dunklem Rand damit er auf hellen Segmenten steht
    tip = px * 0.215
    half = px * 0.068
    top = px * 0.078
    d.polygon([(c - half, top), (c + half, top), (c, tip)],
              fill=NEON, outline=BG, width=int(px * 0.016))
    return img


big = draw_icon(SIZE * SS)
for name, size in [("icon-512.png", 512), ("icon-192.png", 192), ("apple-touch-icon.png", 180)]:
    big.resize((size, size), Image.LANCZOS).save(name, optimize=True)
    print("geschrieben:", name)
