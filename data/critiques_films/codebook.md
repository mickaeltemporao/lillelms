# Codebook : Critiques de films (Allociné)

Échantillon de critiques de films notées, utilisé comme running example du
notebook J3 matin « Text mining : applications ».

| Fichier | Lignes | Équilibre |
|---|---|---|
| `critiques_films_train.csv` | 3 000 | 1 500 positifs / 1 500 négatifs |
| `critiques_films_test.csv` | 1 000 | 500 positifs / 500 négatifs |

## Colonnes

| Colonne | Type | Description |
|---|---|---|
| `text` | str | Texte libre de la critique (français), **le corpus à analyser** |
| `polarite` | str | Étiquette de sentiment : `positif` ou `négatif` |

## Construction

Généré par `fetch_critiques.py` :

1. Téléchargement des fichiers parquet `train` / `test` du dataset
   [`tblard/allocine`](https://huggingface.co/datasets/tblard/allocine).
2. Échantillon **équilibré** par classe (`seed=42`).
3. Renommage `review` → `text`, `label` → `polarite` (0 → `négatif`, 1 → `positif`).

La polarité d'origine est dérivée de la note laissée par l'internaute sur
Allociné (notes basses → négatif, notes hautes → positif).

## Usage pédagogique

Cinq applications du text mining, de la plus simple à la plus avancée :

1. **Nuage de mots + mots-clés** distinctifs positif/négatif (descriptif) ;
2. **Analyse de sentiment** avec un modèle pré-entraîné (comparé à `polarite`) ;
3. **Classification supervisée** : TF-IDF + régression logistique → prédire `polarite` ;
4. **Recherche sémantique** : requête → critiques les plus proches (embeddings) ;
5. **Biais éthiques** : limites et biais des modèles et du corpus.

## Source et licence

Dataset Allociné (Théophile Blard), distribué sur Hugging Face à des fins de
recherche. Données collectées à des fins éducatives.
