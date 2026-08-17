# -*- coding: utf-8 -*-
"""
update-thumbs.py
----------------
Liest alle Bilder aus dem Ordner "imgs" und schreibt die Liste automatisch
in "thumbs.json". Die Website zeigt dann alle Bilder in "Recent thumbnails"
und in der Slideshow oben.

So benutzt du es:
1. Lege deine Bilder in den Ordner "imgs" (PNG, JPG, JPEG, WEBP oder GIF).
2. Fuehre dieses Skript aus:  python update-thumbs.py
   (Du kannst es auch einfach doppelt anklicken, falls Python installiert ist.)
3. Oeffne index.html neu - fertig!
"""
import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))
IMGS = os.path.join(BASE, "imgs")
OUT = os.path.join(BASE, "thumbs.json")

EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".gif")

if not os.path.isdir(IMGS):
    print("Ordner 'imgs' nicht gefunden. Lege ihn neben dieses Skript und versuche es erneut.")
    raise SystemExit(1)

files = sorted(
    f for f in os.listdir(IMGS)
    if f.lower().endswith(EXTENSIONS) and os.path.isfile(os.path.join(IMGS, f))
)

content = (
    "// Auto-generiert von update-thumbs.py - nicht von Hand bearbeiten!\n"
    "// Fuehre das Skript erneut aus, nachdem du Bilder in den Ordner 'imgs' gelegt hast.\n"
    "window.THUMBNAILS = " + json.dumps(files, ensure_ascii=False, indent=2) + ";\n"
)

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(content)

print("Fertig! {} Bild(er) gefunden -> thumbs.json aktualisiert.".format(len(files)))
for f in files:
    print("  -", f)
