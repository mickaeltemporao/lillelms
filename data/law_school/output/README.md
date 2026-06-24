# Prédictions pré-générées — Law School (classification)

Prédictions prêtes à l'emploi pour la **séance fairness**. La personne qui anime fairness dispose ainsi directement des sorties d'un modèle, sans avoir à le ré-entraîner.

Le train et le test sont **rééquilibrés à 50/50** (autant de réussites que d'échecs) par sous-échantillonnage, comme dans le notebook `02-ml-foundations.ipynb` (J2 matin). Les prédictions ne portent donc que sur ce jeu équilibré.

## Fichiers

| Fichier | Contenu |
|---|---|
| `predictions_classification_train.csv` | prédictions sur le jeu d'entraînement rééquilibré 50/50 (2 738 lignes) |
| `predictions_classification_test.csv` | prédictions sur le jeu de test rééquilibré 50/50 (934 lignes) |

## Colonnes

| Colonne | Description |
|---|---|
| `id` | index de ligne dans le split (0..n-1) |
| `x_lsat`, `x_ugpa`, `x_fulltime`, `x_fam_inc`, `x_tier` | features utilisées par le modèle |
| `z_white` | attribut sensible (jamais utilisé comme feature) |
| `y_pass_bar` | vérité terrain (1 = bar exam réussi) |
| `y_pred` | classe prédite (0/1) |
| `y_proba_pass` | probabilité prédite de réussite (classe 1) |

## Modèle

Régression logistique (`sklearn`, `max_iter=1000`) entraînée sur le **train rééquilibré**, en n'utilisant **que les features `x_*`** (l'attribut sensible `z_white` n'entre jamais dans le modèle). Sur un jeu 50/50, l'accuracy ≈ 0,67 (train comme test) : les métriques ne sont plus gonflées par le déséquilibre des classes.

Le modèle reproduit volontairement les disparités du dataset : même à classes équilibrées, l'accuracy et les taux d'erreur diffèrent nettement selon `z_white`, ce qui donne matière à l'analyse fairness (parité démographique, equalized odds, etc.).

## Génération

Produites par le modèle décrit ci-dessus. Le script de génération est conservé localement (non versionné). Sorties déterministes et stables : mêmes CSV d'entrée + modèle déterministe => mêmes prédictions.
