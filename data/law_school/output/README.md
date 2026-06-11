# Prédictions pré-générées — Law School (classification)

Prédictions prêtes à l'emploi pour la **séance fairness**. La personne qui anime fairness dispose ainsi directement des sorties d'un modèle, sans avoir à le ré-entraîner.

## Fichiers

| Fichier | Contenu |
|---|---|
| `predictions_classification_train.csv` | prédictions sur le jeu d'entraînement (14 019 lignes) |
| `predictions_classification_test.csv` | prédictions sur le jeu de test (4 673 lignes) |

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

Régression logistique (`sklearn`, `max_iter=1000`) entraînée sur le **train**, en n'utilisant **que les features `x_*`** (l'attribut sensible `z_white` n'entre jamais dans le modèle). Accuracy ≈ 0,90 sur train comme sur test.

Le modèle reproduit volontairement les disparités du dataset : sur le test, l'accuracy et les taux d'erreur diffèrent nettement selon `z_white`, ce qui donne matière à l'analyse fairness (parité démographique, equalized odds, etc.).

## Régénérer

```bash
uv run python data/law_school/predict_classification.py
```

Déterministe : mêmes CSV d'entrée + modèle déterministe => mêmes prédictions (fichiers stables, versionnés).
