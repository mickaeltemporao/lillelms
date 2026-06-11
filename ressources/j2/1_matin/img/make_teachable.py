"""Construit l'illustration de la démo Teachable Machine (section 1.2 du module 1).

Montre les deux classes d'exemples (portefeuille / clef), une étape « Entraîner »,
puis une prédiction à la webcam. Utilise les photos fournies dans le sous-dossier
`m1-ml-google-teachable-machine/`.

Lancer :  uv run python ressources/j2/1_matin/img/make_teachable.py
Sortie :  m1-ml-teachable.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from PIL import Image

D = Path(__file__).resolve().parent
SRC = D / "m1-ml-google-teachable-machine"
VERT, BLEU, GRIS = "#2e8b57", "#2c6fbf", "#6b7280"

PORTE = ["portefeuille_1.jpg", "portefeuille_2.png", "portefeuille_3.jpg"]
CLEF = ["clefs_1.jpeg", "clefs_2.jpg", "clefs_3.jpg"]


def load_sq(name, size=300):
    im = Image.open(SRC / name).convert("RGB")
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2)).resize((size, size))
    return np.asarray(im)


def thumb(fig, img, l, b, w, h, color, lw=2.5):
    a = fig.add_axes([l, b, w, h])
    a.imshow(img)
    a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values():
        s.set_edgecolor(color); s.set_linewidth(lw)


fig = plt.figure(figsize=(10, 4.3))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

ax.text(0.5, 0.95, "Machine Learning en direct : montrer des exemples, pas écrire des règles",
        ha="center", fontsize=14, weight="bold", color="#111827")
ax.text(0.05, 0.82, "Portefeuille", fontsize=12, weight="bold", color=VERT)
ax.text(0.05, 0.40, "Clef", fontsize=12, weight="bold", color=BLEU)

xs = [0.05, 0.17, 0.29]
for x, nm in zip(xs, PORTE):
    thumb(fig, load_sq(nm), x, 0.50, 0.11, 0.30, VERT)
for x, nm in zip(xs, CLEF):
    thumb(fig, load_sq(nm), x, 0.08, 0.11, 0.30, BLEU)

ax.add_patch(FancyArrowPatch((0.43, 0.5), (0.57, 0.5), arrowstyle="-|>",
                             mutation_scale=22, lw=2.5, color=GRIS))
ax.text(0.50, 0.56, "Entraîner", ha="center", fontsize=11, color=GRIS)

ax.add_patch(FancyBboxPatch((0.60, 0.17), 0.36, 0.63, boxstyle="round,pad=0.004,rounding_size=0.02",
                            linewidth=2, edgecolor=GRIS, facecolor="#f3f4f6"))
ax.text(0.78, 0.84, "Webcam", ha="center", fontsize=11, color=GRIS)
thumb(fig, load_sq("portefeuille_1.jpg"), 0.635, 0.345, 0.29, 0.39, GRIS, lw=1)
ax.add_patch(plt.Rectangle((0.635, 0.225), 0.29, 0.075, color=VERT, alpha=0.9))
ax.text(0.78, 0.262, "Portefeuille  97 %", ha="center", va="center", color="white",
        fontsize=11, weight="bold")

ax.text(0.5, 0.02, "Teachable Machine (Google) : on montre des exemples déjà classés, "
                   "la machine apprend à reconnaître. Aucune règle écrite.",
        ha="center", fontsize=9.5, color="#374151")

import io

buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=120, facecolor="white")
plt.close(fig)
buf.seek(0)
out = Image.open(buf).convert("RGB")
w, h = out.size
if w > 1000:
    out = out.resize((1000, round(h * 1000 / w)))
out.save(D / "m1-ml-teachable.jpg", "JPEG", quality=84, optimize=True)
print("écrit m1-ml-teachable.jpg")
