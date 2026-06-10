"""Génère les schémas de concepts des notebooks J2 matin (modules 1 et 2).

Schémas reproductibles (licence propre, pas de dépendance à une image externe).
Lancer :  uv run python ressources/j2/1_matin/img/make_schemas.py
Sortie :  m1-symbolic.png, m1-transformers.png, m1-generative.png,
          m2-split.png, m2-overfitting.png, m2-confusion.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
BLEU, ORANGE, VERT, GRIS = "#2c6fbf", "#e08a1e", "#2e8b57", "#6b7280"
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})


def boite(ax, x, y, w, h, texte, couleur=BLEU, fc="white", fs=12, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
                                linewidth=1.8, edgecolor=couleur, facecolor=fc))
    ax.text(x + w / 2, y + h / 2, texte, ha="center", va="center", fontsize=fs,
            color="#1f2937", weight="bold" if bold else "normal", wrap=True)


def fleche(ax, x1, y1, x2, y2, couleur=GRIS, lw=2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=16,
                                 linewidth=lw, color=couleur, shrinkA=2, shrinkB=2))


def base(titre, figsize=(8, 4.5)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title(titre, fontsize=14, weight="bold", color="#111827", pad=12)
    return fig, ax


def save(fig, nom):
    fig.savefig(OUT / nom, dpi=130, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("écrit", nom)


# 1.1 IA symbolique : des règles écrites à la main
fig, ax = base("IA symbolique : des règles écrites à la main")
boite(ax, 0.2, 4, 2.7, 2, "Texte\n« défendre\nnos frontières »", GRIS, fs=11)
boite(ax, 3.6, 2.2, 2.8, 5.6, "Règles (mots-clés)\n\nimmigration → RN\nsalaire → LFI\nmarché → LR\nclimat → EELV",
      BLEU, fc="#eef4fc", fs=11)
boite(ax, 7.3, 4, 2.5, 2, "Parti prédit\nRN", ORANGE, fc="#fdf1e3", fs=12, bold=True)
fleche(ax, 2.9, 5, 3.6, 5)
fleche(ax, 6.4, 5, 7.3, 5)
ax.text(5, 1.2, "L'humain écrit la liste de mots-clés ; la machine se contente de compter.",
        ha="center", fontsize=10, color=GRIS, style="italic")
save(fig, "m1-symbolic.png")


# 1.4 Transformers : mécanisme d'attention
fig, ax = base("Mécanisme d'attention : chaque mot regarde les autres")
mots = ["Je", "dépose", "à", "la", "banque", "près", "de", "la", "rivière"]
xs = np.linspace(0.7, 9.3, len(mots))
for x, m in zip(xs, mots):
    couleur = ORANGE if m == "banque" else GRIS
    boite(ax, x - 0.45, 4.5, 0.9, 1.1, m, couleur, fs=10,
          fc="#fdf1e3" if m == "banque" else "white")
src = xs[4]
poids = {2: .12, 4: 0, 8: .9, 1: .25}  # "banque" attend surtout "rivière"
for j, w in poids.items():
    if w == 0:
        continue
    ax.add_patch(FancyArrowPatch((src, 4.5), (xs[j], 4.5), connectionstyle="arc3,rad=-0.45",
                 arrowstyle="-|>", mutation_scale=12, linewidth=1 + 4 * w, color=BLEU, alpha=0.7))
ax.text(5, 2.3, "Le sens de « banque » est fixé par les mots auxquels il prête le plus d'attention\n"
                "(ici « rivière » : il s'agit d'une berge, pas d'un établissement financier).",
        ha="center", fontsize=10, color="#374151")
save(fig, "m1-transformers.png")


# 1.6 IA générative : prédire le mot suivant
fig, ax = base("IA générative : prédire le mot suivant, encore et encore")
boite(ax, 0.3, 6.2, 4.2, 1.6, "« Le chat est assis sur le ___ »", GRIS, fs=12)
boite(ax, 5.4, 6.0, 2.2, 2.0, "modèle\n(transformer)", BLEU, fc="#eef4fc", bold=True)
fleche(ax, 4.5, 7, 5.4, 7)
probas = [("canapé", .42), ("tapis", .27), ("toit", .18), ("clavier", .07)]
y0 = 3.7
for i, (mot, p) in enumerate(probas):
    y = y0 - i * 0.85
    ax.add_patch(plt.Rectangle((3.2, y), 5.0 * p, 0.6, color=ORANGE, alpha=0.85))
    ax.text(3.1, y + 0.3, mot, ha="right", va="center", fontsize=11)
    ax.text(3.3 + 5.0 * p, y + 0.3, f"{p:.0%}", ha="left", va="center", fontsize=10, color=GRIS)
fleche(ax, 6.5, 6.0, 5.7, 4.3)
ax.text(5, 0.2, "On tire un mot selon ces probabilités, on l'ajoute, puis on recommence.",
        ha="center", fontsize=10, color=GRIS, style="italic")
save(fig, "m1-generative.png")


# 2.3 Train / test split
fig, ax = base("Train / test : apprendre, puis évaluer sur des données jamais vues")
ax.add_patch(plt.Rectangle((0.6, 5), 6.6, 1.6, color=BLEU, alpha=0.85))
ax.add_patch(plt.Rectangle((7.2, 5), 2.2, 1.6, color=ORANGE, alpha=0.85))
ax.text(3.9, 5.8, "entraînement (75 %)", ha="center", va="center", color="white", fontsize=12, weight="bold")
ax.text(8.3, 5.8, "test (25 %)", ha="center", va="center", color="white", fontsize=11, weight="bold")
ax.text(3.9, 4.3, "le modèle apprend ici", ha="center", fontsize=10, color=BLEU)
ax.text(8.3, 4.3, "on le juge ici", ha="center", fontsize=10, color=ORANGE)
ax.text(5, 2.6, "Tout le dataset, mélangé puis coupé en deux.\n"
                "On ne regarde JAMAIS le test pendant l'apprentissage.",
        ha="center", fontsize=11, color="#374151")
save(fig, "m2-split.png")


# 2.4 Overfitting
fig, ax = plt.subplots(figsize=(8, 4.5))
x = np.linspace(1, 10, 200)
train = 1.0 / x + 0.04
test = 0.18 + 0.55 * (x / 10 - 0.42) ** 2
ax.plot(x, train, color=BLEU, lw=2.4, label="erreur sur le train")
ax.plot(x, test, color=ORANGE, lw=2.4, label="erreur sur le test")
xb = x[np.argmin(test)]
ax.axvline(xb, color=GRIS, ls="--", lw=1.3)
ax.text(xb, 0.62, "  bon compromis", color=GRIS, fontsize=10, va="top")
ax.annotate("le modèle mémorise\n(overfitting)", xy=(9.2, test[-1]), xytext=(6.4, 0.5),
            fontsize=10, color="#374151", arrowprops=dict(arrowstyle="->", color=GRIS))
ax.set_xlabel("complexité du modèle"); ax.set_ylabel("erreur")
ax.set_title("Overfitting : l'erreur de test remonte quand le modèle mémorise",
             fontsize=13, weight="bold", pad=12)
ax.set_xticks([]); ax.set_yticks([]); ax.legend(frameon=False, loc="upper center")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.savefig(OUT / "m2-overfitting.png", dpi=130, bbox_inches="tight", facecolor="white")
plt.close(fig); print("écrit m2-overfitting.png")


# 2.5 Matrice de confusion
fig, ax = plt.subplots(figsize=(7.2, 4.8))
cm = np.array([[62, 8], [10, 20]])
labels = np.array([["VP\n(vrai positif)", "FN\n(faux négatif)"],
                   ["FP\n(faux positif)", "VN\n(vrai négatif)"]])
ax.imshow([[1, 0], [0, 1]], cmap="Blues", alpha=0.18, extent=(0, 2, 0, 2))
for i in range(2):
    for j in range(2):
        ax.text(j + 0.5, 1.5 - i, f"{labels[i, j]}\n{cm[i, j]}", ha="center", va="center",
                fontsize=12, weight="bold", color="#1f2937")
ax.set_xticks([0.5, 1.5]); ax.set_xticklabels(["prédit : passe", "prédit : rate"])
ax.set_yticks([1.5, 0.5]); ax.set_yticklabels(["réel : passe", "réel : rate"])
ax.set_xlim(0, 2); ax.set_ylim(0, 2)
for k in (0, 1, 2):
    ax.axhline(k, color="white", lw=2); ax.axvline(k, color="white", lw=2)
ax.set_title("Matrice de confusion : la source d'accuracy, precision, recall",
             fontsize=13, weight="bold", pad=12)
ax.tick_params(length=0)
fig.savefig(OUT / "m2-confusion.png", dpi=130, bbox_inches="tight", facecolor="white")
plt.close(fig); print("écrit m2-confusion.png")
