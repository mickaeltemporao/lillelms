"""Génère les schémas de concepts des notebooks J3 matin (modules 3 et 4).

Schémas reproductibles (licence propre, pas de dépendance à une image externe).
Lancer :  uv run python ressources/j3/1_matin/img/make_schemas.py
Sortie :  m3-tokenization.png, m3-bow.png, m3-embeddings.png,
          m4-sentiment.png, m4-classification.png, m4-search.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

OUT = Path(__file__).resolve().parent
BLEU, ORANGE, VERT, GRIS = "#2c6fbf", "#e08a1e", "#2e8b57", "#6b7280"
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})


def boite(ax, x, y, w, h, texte, couleur=BLEU, fc="white", fs=12, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
                                linewidth=1.8, edgecolor=couleur, facecolor=fc))
    ax.text(x + w / 2, y + h / 2, texte, ha="center", va="center", fontsize=fs,
            color="#1f2937", weight="bold" if bold else "normal")


def fleche(ax, x1, y1, x2, y2, couleur=GRIS, lw=2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=16,
                                 linewidth=lw, color=couleur, shrinkA=2, shrinkB=2))


def base(titre, figsize=(8, 4.5)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title(titre, fontsize=13.5, weight="bold", color="#111827", pad=12)
    return fig, ax


def save(fig, nom):
    (OUT / nom[:2]).mkdir(exist_ok=True)
    fig.savefig(OUT / nom[:2] / nom, dpi=130, bbox_inches="tight", facecolor="white")
    plt.close(fig); print("écrit", nom[:2] + "/" + nom)


# Tokenization
fig, ax = base("Tokenization : du texte brut aux tokens")
boite(ax, 0.6, 6.4, 8.8, 1.6, '"A cosy design apartment in Paris"', GRIS, fs=13)
fleche(ax, 5, 6.4, 5, 5.4)
toks = ["cosy", "design", "apartment", "paris"]
xs = np.linspace(1.0, 7.2, len(toks))
for x, t in zip(xs, toks):
    boite(ax, x, 3.4, 1.7, 1.3, t, BLEU, fc="#eef4fc", fs=12, bold=True)
ax.text(5, 1.8, "Minuscules, on garde les suites de lettres, on jette les mots trop courts\n"
                "(« a », « in ») : il reste une liste de tokens.",
        ha="center", fontsize=10.5, color="#374151")
save(fig, "m3-tokenization.png")


# Bag of words : term-document matrix
fig, ax = plt.subplots(figsize=(7.6, 4.6))
cols = ["furnished", "design", "living", "simple", "terrace"]
rows = ["A : Paris design", "B : Paris design", "C : Bruxelles simple"]
M = np.array([[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1]])
ax.imshow(M, cmap="Blues", vmin=0, vmax=2, aspect="auto")
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        ax.text(j, i, M[i, j], ha="center", va="center", fontsize=13,
                color="white" if M[i, j] else "#9ca3af", weight="bold")
ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols, rotation=30, ha="right")
ax.set_yticks(range(len(rows))); ax.set_yticklabels(rows)
ax.set_title("Bag of words : compter les mots (matrice term-document)",
             fontsize=13, weight="bold", pad=12)
ax.tick_params(length=0)
save(fig, "m3-bow.png")


# Embeddings : espace vectoriel
fig, ax = plt.subplots(figsize=(8, 4.8))
groupes = {
    BLEU:   [("luxurious", 1.3, 3.4), ("upscale", 1.9, 3.9), ("elegant", 1.0, 4.2)],
    ORANGE: [("metro", 4.4, 1.2), ("subway", 5.1, 1.6), ("station", 4.7, 0.8)],
    VERT:   [("simple", 3.6, 4.4), ("basic", 4.2, 4.0), ("plain", 3.9, 3.5)],
}
for couleur, pts in groupes.items():
    xs = [p[1] for p in pts]; ys = [p[2] for p in pts]
    ax.scatter(xs, ys, s=70, color=couleur, zorder=3)
    for nom, x, y in pts:
        ax.text(x + 0.12, y + 0.12, nom, fontsize=11, color="#1f2937")
    cx, cy = np.mean(xs), np.mean(ys)
    ax.add_patch(Circle((cx, cy), 0.95, fill=False, ls="--", lw=1.2, color=couleur, alpha=0.6))
ax.set_xlim(0, 6.5); ax.set_ylim(0, 5.2); ax.axis("off")
ax.set_title("Embeddings : proches par le sens, proches dans l'espace",
             fontsize=13, weight="bold", pad=12)
ax.text(3.25, -0.15, "Chaque mot devient un vecteur ; les mots de sens voisin se regroupent.",
        ha="center", fontsize=10.5, color="#374151")
save(fig, "m3-embeddings.png")


# Sentiment
fig, ax = base("Analyse de sentiment : attribuer un score à un texte")
ax.add_patch(plt.Rectangle((1, 4.6), 8, 0.5,
             color="none"))
grad = np.linspace(0, 1, 256).reshape(1, -1)
ax.imshow(grad, extent=(1, 9, 4.6, 5.1), aspect="auto", cmap="RdYlGn")
ax.text(1, 4.1, "négatif", color="#b91c1c", fontsize=11, ha="center")
ax.text(9, 4.1, "positif", color="#15803d", fontsize=11, ha="center")
boite(ax, 0.6, 7.2, 5.0, 1.4, '"Un film inoubliable, magnifique."', GRIS, fs=11)
boite(ax, 0.6, 1.6, 5.0, 1.4, '"Scénario plat, je me suis ennuyé."', GRIS, fs=11)
fleche(ax, 5.6, 7.9, 8.2, 5.15, VERT)
fleche(ax, 5.6, 2.3, 2.0, 4.55, "#b91c1c")
ax.text(5, 0.2, "Le modèle lit le texte et renvoie une note de polarité, lisible à grande échelle.",
        ha="center", fontsize=10.5, color="#374151", style="italic")
save(fig, "m4-sentiment.png")


# Classification supervisée
fig, ax = base("Classification supervisée : automatiser le codage")
boite(ax, 0.3, 5.2, 3.0, 3.2, "Critiques\nétiquetées\n\n+  + −\n−  +  −", VERT, fc="#eaf5ee", fs=12)
boite(ax, 3.9, 5.4, 2.6, 2.8, "modèle\nTF-IDF +\nrégression\nlogistique", BLEU, fc="#eef4fc", bold=True)
boite(ax, 7.0, 5.6, 2.7, 2.4, "nouvelle\ncritique\n→ + ou −", ORANGE, fc="#fdf1e3", fs=12, bold=True)
fleche(ax, 3.3, 6.8, 3.9, 6.8)
fleche(ax, 6.5, 6.8, 7.0, 6.8)
ax.text(2.6, 4.6, "on apprend ici", ha="center", fontsize=10, color=VERT)
ax.text(8.35, 5.2, "on prédit ici", ha="center", fontsize=10, color=ORANGE)
ax.text(5, 2.6, "Avec quelques centaines de textes codés à la main, la machine code le reste,\n"
                "et fournit des métriques de fiabilité.", ha="center", fontsize=10.5, color="#374151")
save(fig, "m4-classification.png")


# Recherche sémantique
fig, ax = plt.subplots(figsize=(8, 4.8))
rng = np.random.default_rng(3)
docs = rng.uniform(0.5, 9.5, size=(22, 2))
q = np.array([6.2, 5.6])
d = np.linalg.norm(docs - q, axis=1)
proches = np.argsort(d)[:3]
ax.scatter(docs[:, 0], docs[:, 1], s=45, color=GRIS, alpha=0.55, zorder=2, label="critiques")
ax.scatter(docs[proches, 0], docs[proches, 1], s=90, color=ORANGE, zorder=3, label="plus proches")
ax.scatter(*q, s=180, marker="*", color=BLEU, zorder=4, label="requête")
for p in proches:
    ax.plot([q[0], docs[p, 0]], [q[1], docs[p, 1]], color=ORANGE, lw=1.4, zorder=1)
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
ax.set_title("Recherche sémantique : retrouver par le sens, pas par les mots",
             fontsize=13, weight="bold", pad=12)
ax.legend(frameon=False, loc="lower center", ncol=3, fontsize=10)
ax.text(5, -0.2, "La requête et les textes sont des vecteurs ; on renvoie les plus proches.",
        ha="center", fontsize=10.5, color="#374151")
save(fig, "m4-search.png")
