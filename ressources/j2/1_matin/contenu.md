# J2 matin — Plan de contenu détaillé

Plan hiérarchique de matière pour la matinée du J2. Sert de squelette commun à 2 paires *slides + notebook*. Le découpage horaire des 3 h sera ajouté ici une fois les durées calées sur les 2 modules + accueil + pause + carrousel + capitalisation.

## Conventions

- chaque **module niveau 1** = 1 deck slides + 1 notebook
- chaque **niveau 2** = 1 chapitre slides / 1 section notebook
- chaque **niveau 3** = 1 sous-chapitre slides / 1 sous-section notebook
- chaque module a **un running example unique**, choisi pour résonner avec les corpus et thématiques des stagiaires (cf. `participants/analyse_des_participants.md`)

Notebook = tutoriel illustré qui tourne quasi clé en main avec quelques cellules à compléter (Hack Time). Slide = pitch.

**Périmètre** : 2 modules seulement. Les notions plus pointues (tokens, BERT/GPT, encodeur/décodeur, RAG, agentic…) sont renvoyées aux séances suivantes (J2 PM avec MT pour APIs/prompt/RAG/agentic ; J3 matin pour text mining).

## Modules niveau 1

| # | Titre | Running example | Résonance principale |
|---|---|---|---|
| 1 | Mise en perspective historique : 70 ans d'IA en 30 minutes | Déclarations politiques françaises étiquetées par parti (mini-corpus inline, 16 phrases) | discours politique, sociologie politique |
| 2 | Concepts clés du machine learning | Adult Census Income (déterminants socio-démo du revenu) | démographie, sociologie quantitative, stratification sociale |

---

## Module 1 — Mise en perspective historique

**Running example** : un mini-corpus inline de 16 déclarations politiques (4 par parti : RN, LFI, LR, EELV). Tâche transversale : « classer l'auteur par parti à partir du texte ». La même tâche traverse chaque époque pour rendre visible ce que chaque génération de modèles ajoute.

### 1.1 IA symbolique (50s-80s)
- 1.1.1 Règles écrites à la main par un expert (listes de mots-clés par parti)
- 1.1.2 Démo : un classifier de 10 lignes qui regarde si des mots-clés apparaissent
- 1.1.3 Hack Time : étendre les règles, écrire une phrase qui « casse » le classifier
- 1.1.4 Limites : fragile, ne capte pas les paraphrases, non-généralisable

### 1.2 Machine Learning statistique (90s-2010s) — voir le modèle apprendre
- 1.2.1 **Préparer des features** : présence/absence binaire d'une liste de mots-clés (matrice 0/1)
- 1.2.2 **Train / test split** : 12 phrases pour entraîner, 4 pour tester
- 1.2.3 **Voir le modèle apprendre** : régression logistique sur la matrice 0/1, lecture directe des coefficients appris (par mot × par parti) → le modèle redécouvre nos règles, en chiffres
- 1.2.4 Hack Time « entraînement » : modifier le train, retrain, observer les coefficients qui bougent
- 1.2.5 **Tester** : prédire sur des phrases jamais vues, lire les probabilités
- 1.2.6 Hack Time « test » : composer une phrase et la faire prédire, essayer de tromper le modèle

### 1.3 Deep Learning (2010-2017)
- 1.3.1 Bascule conceptuelle : on arrête de fabriquer les features à la main, on laisse le réseau les apprendre
- 1.3.2 Renvoi à [playground.tensorflow.org](https://playground.tensorflow.org/) pour voir un réseau apprendre en direct
- 1.3.3 Mention des embeddings, renvoyée à J3 text mining

### 1.4 Transformers (2017→) — comparaison 4 méthodes sur paraphrases
- 1.4.1 Rupture 2017 : *Attention is all you need*. Pré-entraînement massif → comprendre le sens dans son contexte
- 1.4.2 **Test piégeux** : 4 phrases qui paraphrasent les thèmes des partis sans utiliser nos mots-clés
- 1.4.3 Comparaison de 4 méthodes sur ces phrases :

| | Méthode | Entrée | Origine |
|---|---|---|---|
| ① | Règles à la main | mots-clés | section 1.1 |
| ② | Régression logistique | mots-clés | section 1.2 |
| ③ | Réseau de neurones (MLP, sans attention) | mots-clés | nouveau |
| ④ | Transformer pré-entraîné (zero-shot) | texte brut | nouveau |

  - ① ② ③ tombent toutes : entrée vide → sortie aléatoire. Augmenter la complexité du modèle ne sauve pas si les features sont limitées.
  - ④ réussit : le transformer lit le texte brut et reconnaît le sens (« rémunération » ≈ « salaire », « écosystème » ≈ « écologie »).
- 1.4.4 Hack Time : inventer sa propre phrase piégeuse, ajouter des synonymes aux mots-clés et voir à partir de quand les méthodes ① ② ③ rattrapent ④

### 1.5 IA générative (2020→)
- 1.5.1 Dernière bascule : le transformer en **variante décodeur** (chaque mot ne voit que la gauche, on apprend à prédire le suivant)
- 1.5.2 ChatGPT, Claude, Mistral, Gemini : le modèle génère sa réponse **et explique son choix**
- 1.5.3 Démo : appel à un LLM via une API (clé dans `.env`), classer + justifier une déclaration
- 1.5.4 Hack Time : relancer 3 fois la même requête, observer le non-déterminisme ; essayer de tromper le modèle
- 1.5.5 Sous le capot : toujours du transformer, mais **échelle massive + affinage par retours humains**

---

## Module 2 — Concepts clés du machine learning

**Running example** : Adult Census Income (1994 US Census, ~48k individus, 14 variables socio-démographiques, cible binaire : revenu > 50 k$). Pendant SHS du Titanic.

### 2.1 La notion de feature
- 2.1.1 Définition : variable explicative que le modèle utilise (âge, niveau d'éducation, profession, état civil)
- 2.1.2 Features numériques vs catégorielles (encodage one-hot)
- 2.1.3 Feature engineering = créer des features pertinentes à partir des données brutes

### 2.2 Nettoyage et préparation des données
- 2.2.1 Données manquantes (valeurs `?` dans Adult) : suppression, imputation
- 2.2.2 Outliers et valeurs aberrantes
- 2.2.3 Normalisation / standardisation (impact sur les modèles)
- 2.2.4 « Garbage in, garbage out » : la qualité des données conditionne tout

### 2.3 Train / test split
- 2.3.1 Pourquoi évaluer sur des données non vues : objectif = généraliser
- 2.3.2 Split typique 70/30 ou 80/20, stratification sur la cible

### 2.4 Overfitting
- 2.4.1 Définition : le modèle mémorise le train mais échoue sur le test
- 2.4.2 Symptôme : performance train >> performance test
- 2.4.3 Exemple : arbre de décision de profondeur croissante sur Adult → train accuracy → 100 %, test plafonne
- 2.4.4 Remèdes : régularisation, plus de données, modèles plus simples

### 2.5 Biais-variance
- 2.5.1 Biais : erreur due à un modèle trop simple (sous-apprentissage)
- 2.5.2 Variance : erreur due à un modèle trop sensible aux données (sur-apprentissage)
- 2.5.3 Compromis classique : courbe en U
- 2.5.4 Comparaison sur Adult : logistic regression (biais ↑) vs arbre profond (variance ↑) vs random forest (compromis)
- 2.5.5 Lien avec les LLMs : variance énorme, compensée par un pré-entraînement colossal

---

## À faire ensuite

1. ✅ Notebook module 1 — `01-perspective-historique.ipynb`
2. ✅ Notebook module 2 — `02-ml-foundations.ipynb`
3. Slides correspondants (1 deck par module)
4. Caler les durées des 2 modules dans les 3 h (avec accueil, pause, carrousel et capitalisation) et intégrer le découpage horaire en tête de ce fichier

## Questions ouvertes

- Module 1 : remplacer le mini-corpus inline (16 phrases) par un vrai dataset de tweets de députés français étiquetés par parti, ou un dataset équivalent
