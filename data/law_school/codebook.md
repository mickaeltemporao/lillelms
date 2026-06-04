# Codebook : Law School

Codebook commun aux deux CSV pré-traités :

- `law_school_for_regression.csv` : cible continue `y_zgpa`
- `law_school_for_classification.csv` : cible binaire `y_pass_bar`

Les deux fichiers partagent **la même matrice de features** `x_*` et **le même attribut sensible** `z_white`. Ils diffèrent uniquement par la cible `y_*`.

## Contexte : parcours d'un·e étudiant·e en droit aux États-Unis

```
Admission
   ↓
LSAT + UGPA        ← prédicteurs disponibles à l'entrée (x_lsat, x_ugpa)
   ↓
1ère année de droit
   ↓
FYGPA (First-Year GPA)   ← variable zfygpa, exclue (post-admission)
   ↓
Fin des études de droit
   ↓
Law School GPA     ← cible régression y_zgpa
   ↓
Bar Exam
   ↓
Pass / Fail        ← cible classification y_pass_bar
```

Acronymes :

- **GPA** (*Grade Point Average*) : moyenne des notes, sur une échelle de 0 à 4 dans le système américain.
- **UGPA** (*Undergraduate GPA*) : GPA obtenu pendant les études *undergraduate*, c'est-à-dire avant l'entrée en faculté de droit (équivalent du cycle bachelor).
- **LSAT** (*Law School Admission Test*) : examen d'aptitude standardisé exigé pour candidater dans les facultés de droit américaines (raisonnement logique, compréhension écrite, argumentation). Score brut sur ~120-180 dans les barèmes modernes ; échelle ~11-48 dans ce dataset historique.
- **FYGPA** (*First-Year GPA*) : GPA obtenu à la fin de la première année de droit. Standardisé dans le dataset sous le nom `zfygpa`.
- **Law School GPA** : GPA cumulé sur l'ensemble des années de droit. Standardisé dans le dataset sous le nom `zgpa`.
- **Bar Exam** : examen national de licence professionnelle pour exercer comme avocat·e aux États-Unis. Organisé par chaque État après l'obtention du diplôme de droit.

Cette chronologie explique pourquoi seules les variables disponibles **avant** l'admission (LSAT, UGPA, revenu familial, tier de la faculté) sont conservées comme features `x_*`. Tout ce qui se produit après l'entrée en droit (FYGPA, déciles intermédiaires) serait du target leakage pour prédire la suite du parcours.

## Que prédit-on ?

- **`y_zgpa`** : version standardisée (z-score) du **Law School GPA**, c'est-à-dire la moyenne cumulée des notes obtenues sur l'ensemble des années de droit. Le préfixe `z` du nom vient du z-score, pas du préfixe sensible de notre convention. Mesure la performance académique pendant les études.
- **`y_pass_bar`** : résultat du **Bar Exam**, sous forme binaire (0/1), valant 1 si l'étudiant·e l'a réussi. Mesure le franchissement du seuil d'aptitude professionnelle après les études.

## Source

- Repo : [damtharvey/law-school-dataset](https://github.com/damtharvey/law-school-dataset)
- Fichier brut : `law_dataset.csv` (18 692 lignes)
- Origine première : *LSAC National Longitudinal Bar Passage Study* (Wightman, 1998), dataset de référence en sociologie quantitative du droit et en fairness ML.

## Population

Étudiantes et étudiants en droit aux États-Unis, ~18 700 individus après pré-traitement.

## Convention de préfixes

| Préfixe | Rôle | Usage |
|---|---|---|
| `x_` | features prédictives | entrent dans `X` du modèle |
| `y_` | cible | variable à prédire |
| `z_` | attribut sensible | jamais utilisé tel quel comme feature ; pivot des analyses fairness (parité démographique, equalized odds, etc.) |

## Features (`x_*`)

| Colonne | Type | Description |
|---|---|---|
| `x_lsat` | numérique | Score au LSAT (Law School Admission Test), ~11–48 |
| `x_ugpa` | numérique | GPA undergraduate (avant l'entrée en faculté de droit), échelle 0–4 |
| `x_fulltime` | binaire 0/1 | 1 = étudiant·e à temps plein |
| `x_fam_inc` | catégorielle ordinale 1–5 | Niveau de revenu familial déclaré (1 = bas, 5 = haut) |
| `x_tier` | catégorielle ordinale 1–6 | Tier / classement de la faculté de droit |

## Attribut sensible (`z_*`)

| Colonne | Type | Description |
|---|---|---|
| `z_white` | binaire 0/1 | 1 si « white », 0 sinon |

Proportion observée : ~93,6 % `z_white == 1`. Fort déséquilibre, à garder en tête pour les métriques fairness conditionnelles.

## Cibles (`y_*`)

| Colonne | Type | Description | Tâche |
|---|---|---|---|
| `y_zgpa` | numérique standardisé | Law School GPA standardisé (~moyenne 0, écart-type 1) | régression |
| `y_pass_bar` | binaire 0/1 | Résultat du Bar Exam : 1 = réussi | classification |

Distribution observée : `y_pass_bar` est très déséquilibré (~90 % de réussite). L'accuracy seule est trompeuse, préférer F1 ou rappel sur la classe minoritaire.

### Lien entre `y_zgpa` et `y_pass_bar`

Les deux cibles sont corrélées sans que l'une se déduise de l'autre (corrélation Pearson ≈ 0,36). Le barreau est un seuil pass/fail atteint par environ 90 % des diplômés, y compris une grande partie de ceux dont la moyenne en droit était basse (72 % du quartile inférieur de `y_zgpa` réussit quand même). Les deux variables mesurent des choses distinctes : une performance étalée sur plusieurs années pour `y_zgpa`, le franchissement d'un seuil unique sur un examen ciblé pour `y_pass_bar`. Ce sont donc deux tâches d'apprentissage authentiquement différentes sur la même population.

## Régénérer les CSV

```bash
uv run python data/law_school/fetch_law_school.py
```

Script idempotent : ré-exécuter ne change pas le contenu des CSV.

---

## Filtrage des données

Section de référence, pas indispensable pour utiliser les CSV. Utile pour comprendre comment on est passé du fichier source aux CSV livrés.

### Étapes appliquées par `fetch_law_school.py`

1. **Sélection des colonnes utiles** : on passe des 12 colonnes du CSV brut aux 8 colonnes retenues (`lsat`, `ugpa`, `fulltime`, `fam_inc`, `racetxt`, `tier`, `zgpa`, `pass_bar`).
2. **`dropna()`** sur les colonnes retenues (aucun effet sur cette version du fichier source).
3. **Binarisation de `racetxt`** vers `z_white` (déjà 0/1 dans la source `damtharvey`, on se contente d'un cast en `int`).
4. **Renommage** avec préfixes `x_` / `y_` / `z_`.
5. **Coercition `int`** pour les colonnes binaires (`x_fulltime`, `z_white`, `y_pass_bar`) afin d'éviter les `.0` flottants à la sortie.

### Variables volontairement exclues

- `decile1b`, `decile3` : rang dans la promotion en cours/fin de droit. Outcomes intermédiaires qui causent un target leakage massif pour `y_pass_bar`.
- `zfygpa` : GPA standardisé de première année. Même problème, résultat post-admission, pas un prédicteur disponible à l'entrée.
- `male` : variable de genre retirée du périmètre par décision pédagogique (focus fairness sur `z_white` uniquement dans ce module).

Pour respecter le cadre classique de la littérature counterfactual fairness, on n'utilise que des variables disponibles **avant** l'entrée en faculté + métadonnées de la faculté (`x_tier`).
