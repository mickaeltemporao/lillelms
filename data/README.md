# `data/` — Datasets pour les running examples

Ce dossier centralise les datasets utilisés comme « running examples » dans les notebooks pédagogiques. Chaque dataset a son propre sous-dossier qui contient :

- `fetch_<dataset>.py` — script qui télécharge la source brute, la pré-traite et écrit les CSV finaux à côté de lui
- `codebook.md` — codebook qui décrit la sémantique des colonnes
- les CSV pré-traités (versionnés)

Les scripts sont idempotents : ré-exécuter un `fetch_*.py` ne change pas le contenu des CSV (mêmes données → mêmes hash).

## Convention de nommage des colonnes

| Préfixe | Rôle |
|---|---|
| `x_` | feature prédictive ordinaire (entre dans `X`) |
| `y_` | cible à prédire |
| `z_` | attribut sensible (jamais utilisé directement comme feature ; sert aux analyses fairness) |

Un même dataset peut produire plusieurs CSV qui partagent `X` et `z` mais diffèrent par `y` (ex. law school : une cible régression, une cible classification).

Quand un split train/test est livré, les fichiers se terminent par `_train.csv` et `_test.csv` (suffixes uniformes dans tout le dossier).

## Régénérer un dataset

```bash
uv run python data/<dataset>/fetch_<dataset>.py
```

## Datasets disponibles

| Dossier | Description | Cibles | Split |
|---|---|---|---|
| `law_school/` | LSAC National Longitudinal Bar Passage Study (Wightman 1998) | `y_zgpa` (régression), `y_pass_bar` (classification) | 75/25 aléatoire |
