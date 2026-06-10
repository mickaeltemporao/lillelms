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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

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
boite(ax, 0.2, 4, 2.7, 2, "Texte\n« réduire\nl'immigration »", GRIS, fs=11)
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
mots = ["L'", "avocat", "plaide", "devant", "le", "tribunal"]
xs = np.linspace(0.9, 9.1, len(mots))
for x, m in zip(xs, mots):
    focus = (m == "avocat")
    boite(ax, x - 0.7, 4.5, 1.4, 1.1, m, ORANGE if focus else GRIS, fs=10,
          fc="#fdf1e3" if focus else "white", bold=focus)
src = xs[1]
poids = {5: .9, 2: .5, 3: .15}  # "avocat" attend surtout "tribunal" et "plaide"
for j, w in poids.items():
    ax.add_patch(FancyArrowPatch((src, 5.6), (xs[j], 5.6), connectionstyle="arc3,rad=-0.4",
                 arrowstyle="-|>", mutation_scale=12, linewidth=1 + 4 * w, color=BLEU, alpha=0.7))
ax.text(5, 2.3, "Le sens de « avocat » est fixé par les mots auxquels il prête le plus d'attention\n"
                "(ici « tribunal » et « plaide » : l'homme de loi, pas le fruit).",
        ha="center", fontsize=10, color="#374151")
save(fig, "m1-transformers.png")


# 1.6 IA générative : prédire le mot suivant (bande horizontale, une seule ligne)
fig, ax = plt.subplots(figsize=(9, 2.8))
ax.set_xlim(0, 12); ax.set_ylim(0, 4); ax.axis("off")
ax.set_title("IA générative : prédire le mot suivant, encore et encore",
             fontsize=13.5, weight="bold", color="#111827", pad=10)
boite(ax, 0.2, 1.1, 3.6, 1.8, "« Le chat est\nsur le ___ »", GRIS, fs=12)
boite(ax, 4.3, 1.2, 2.0, 1.6, "modèle", BLEU, fc="#eef4fc", bold=True)
fleche(ax, 3.8, 2.0, 4.3, 2.0)
fleche(ax, 6.3, 2.0, 7.0, 2.0)
probas = [("canapé", .42), ("tapis", .27), ("toit", .18)]
for i, (mot, p) in enumerate(probas):
    y = 2.9 - i * 0.95
    ax.add_patch(plt.Rectangle((8.6, y), 3.0 * p, 0.6, color=ORANGE, alpha=0.85))
    ax.text(8.5, y + 0.3, mot, ha="right", va="center", fontsize=10)
    ax.text(8.7 + 3.0 * p, y + 0.3, f"{p:.0%}", ha="left", va="center", fontsize=9, color=GRIS)
ax.text(6, 0.15, "On tire un mot selon ces probabilités, on l'ajoute, puis on recommence.",
        ha="center", fontsize=9.5, color=GRIS, style="italic")
fig.savefig(OUT / "m1-generative.png", dpi=130, bbox_inches="tight", facecolor="white")
plt.close(fig); print("écrit m1-generative.png")


# 1.2 Machine Learning statistique : apprendre les règles depuis les données
fig, ax = base("Machine Learning : apprendre les règles au lieu de les écrire")
boite(ax, 0.2, 3.9, 2.7, 2.6, "Exemples\nétiquetés\n\n«…immigration…» → RN\n«…salaire…» → LFI",
      VERT, fc="#eaf5ee", fs=9.5)
boite(ax, 3.5, 4.2, 2.3, 2.0, "Features 0/1\n« mot présent ? »", GRIS, fs=10.5)
boite(ax, 6.4, 4.0, 3.4, 2.4, "Le modèle\napprend les poids\n(régression\nlogistique)",
      BLEU, fc="#eef4fc", bold=True, fs=10.5)
fleche(ax, 2.9, 5.2, 3.5, 5.2)
fleche(ax, 5.8, 5.2, 6.4, 5.2)
ax.text(5, 2.1, "Le modèle découvre tout seul combien chaque mot compte pour chaque parti :\n"
                "il réinvente les règles de l'IA symbolique, mais en chiffres.",
        ha="center", fontsize=10, color="#374151")
save(fig, "m1-ml.png")


# 1.3 Deep Learning : le réseau apprend lui-même la représentation
fig, ax = base("Deep Learning : le réseau apprend lui-même les features")
layers = [3, 5, 4, 4]
xpos = np.linspace(1.4, 8.6, len(layers))
coords = [[(x, y) for y in np.linspace(7.2, 2.8, n)] for x, n in zip(xpos, layers)]
for a, b in zip(coords[:-1], coords[1:]):
    for x1, y1 in a:
        for x2, y2 in b:
            ax.plot([x1, x2], [y1, y2], color="#d1d5db", lw=0.5, zorder=1)
couleurs = [GRIS, BLEU, BLEU, ORANGE]
for li, layer in enumerate(coords):
    for x, y in layer:
        ax.add_patch(Circle((x, y), 0.22, color=couleurs[li], zorder=3))
ax.text(xpos[0], 8.1, "entrée\n(texte)", ha="center", fontsize=9.5, color="#374151")
ax.text((xpos[1] + xpos[2]) / 2, 8.1, "couches cachées\n(représentation apprise)",
        ha="center", fontsize=9.5, color=BLEU)
ax.text(xpos[3], 8.1, "sortie\n(parti)", ha="center", fontsize=9.5, color=ORANGE)
ax.text(5, 1.4, "On ne fabrique plus les features à la main : les couches cachées les apprennent.",
        ha="center", fontsize=10, color="#374151")
save(fig, "m1-dl.png")


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
