# J2 matin — Plan de contenu détaillé

Plan hiérarchique de matière pour la matinée du J2. Sert de squelette commun à 4 paires *slides + notebook*. Le découpage horaire des 3 h sera ajouté ici une fois les durées calées sur les 4 modules.

## Conventions

- chaque **module niveau 1** = 1 deck slides + 1 notebook
- chaque **niveau 2** = 1 chapitre slides / 1 section notebook
- chaque **niveau 3** = 1 sous-chapitre slides / 1 sous-section notebook
- chaque module a **un running example unique**, choisi pour résonner avec les corpus et thématiques des stagiaires (cf. `participants/analyse_des_participants.md`)

Notebook = tutoriel illustré qui tourne quasi clé en main avec quelques cellules TODO. Slide = pitch.

## Modules niveau 1

| # | Titre | Running example | Résonance principale |
|---|---|---|---|
| 1 | Mise en perspective historique | **Tweets / déclarations de personnalités politiques françaises** classés par parti | discours politique, réseaux sociaux, sociologie politique |
| 2 | Concepts clés du machine learning | **Adult Census Income** (déterminants socio-démo du revenu) | démographie, sociologie quantitative, stratification sociale |
| 3 | Qu'est-ce qu'un token ? | **Discours présidentiels français** (De Gaulle → Macron) | analyse de discours, archives politiques |
| 4 | L'idée du génératif : inverser l'encodeur | **Décisions du Conseil d'État** (Légifrance, classées par domaine) | droit, science politique, textes réglementaires |

---

## Module 1 — Mise en perspective historique

**Running example** : un corpus de tweets ou déclarations courtes de personnalités politiques françaises, étiquetées par parti. Tâche transversale : « classer l'auteur par parti à partir du texte ». Même tâche traversée par chacune des époques.

### 1.1 IA symbolique (50s-80s)
- 1.1.1 Règles écrites à la main par un expert
- 1.1.2 Exemple : regex sur mots-clés (« RN » si *immigration*, « LFI » si *retraite*…)
- 1.1.3 Limites : fragile, ne capte pas l'ironie, non-généralisable

### 1.2 Machine Learning statistique (90s-2010s)
- 1.2.1 Bascule : apprendre les règles depuis les données
- 1.2.2 Exemple : TF-IDF + logistic regression sur le corpus → précision bien meilleure
- 1.2.3 Renvoi vers module 2 pour les concepts fondamentaux

### 1.3 Deep Learning (2010-2017)
- 1.3.1 Idée : empilage de couches, représentation apprise (pas de feature engineering manuel)
- 1.3.2 Exemple : un réseau de neurones simple sur le corpus (sans approfondir les embeddings)

### 1.4 Transformers et LLMs (2017→)
- 1.4.1 Rupture 2017 : *Attention is all you need*
- 1.4.2 Pré-entraînement massif → transfert (BERT 2018, GPT 2019)
- 1.4.3 Exemple : BERT fine-tuné sur le corpus politique (très peu de données nécessaires)

### 1.5 IA générative (2020→)
- 1.5.1 Bascule décodeur : générer plutôt que classifier
- 1.5.2 Exemple : demander à un LLM zero-shot de classer une déclaration **et** d'expliquer sa décision
- 1.5.3 Lecture transversale : même tâche traversant 70 ans d'IA

---

## Module 2 — Concepts clés du machine learning

**Running example** : Adult Census Income (1994 US Census, ~48k individus, 14 variables socio-démographiques, cible binaire : revenu > 50 k$). Dataset pédagogique de référence en sociologie quantitative et démographie. Pendant SHS du Titanic.

### 2.1 La notion de feature
- 2.1.1 Définition : variable explicative que le modèle utilise (âge, niveau d'éducation, profession, état civil)
- 2.1.2 Features numériques vs catégorielles (encodage one-hot)
- 2.1.3 Feature engineering = créer des features pertinentes à partir des données brutes
- 2.1.4 Exemple : *years_education* recodé en niveau, *hours_per_week* discrétisé

### 2.2 Nettoyage et préparation des données
- 2.2.1 Données manquantes (valeurs `?` dans Adult) : suppression, imputation
- 2.2.2 Outliers et valeurs aberrantes
- 2.2.3 Normalisation / standardisation (impact sur les modèles)
- 2.2.4 « Garbage in, garbage out » : la qualité des données conditionne tout

### 2.3 Train / test split
- 2.3.1 Pourquoi évaluer sur des données non vues : objectif = généraliser
- 2.3.2 Split typique 70/30 ou 80/20, validation croisée
- 2.3.3 Exemple : split + métrique (accuracy ou AUC sur Adult)

### 2.4 Overfitting
- 2.4.1 Définition : le modèle mémorise le train mais échoue sur le test
- 2.4.2 Symptôme : performance train >> performance test
- 2.4.3 Exemple : decision tree de profondeur croissante sur Adult → train accuracy → 100 %, test plafonne
- 2.4.4 Remèdes : régularisation, plus de données, modèles plus simples, validation croisée

### 2.5 Bias-variance tradeoff
- 2.5.1 Biais : erreur due à un modèle trop simple (sous-apprentissage)
- 2.5.2 Variance : erreur due à un modèle trop sensible aux données (sur-apprentissage)
- 2.5.3 Compromis classique illustré graphiquement (courbe en U)
- 2.5.4 Exemple : logistic regression (biais ↑, variance ↓) vs deep tree vs random forest sur Adult
- 2.5.5 Lien avec les LLMs : ils ont une capacité énorme, compensée par le volume colossal de pré-entraînement

---

## Module 3 — Qu'est-ce qu'un token ?

**Running example** : discours présidentiels français (De Gaulle → Macron, ~50 discours majeurs ou plus selon corpus retenu). Disponible via Vie Publique / archives en ligne. Résonne avec analyse de discours politique, élites, archives.

### 3.1 Notion de corpus
- 3.1.1 Définition : collection de documents reliés
- 3.1.2 Métadonnées : auteur, date, contexte (campagne, vœux, allocution de crise)
- 3.1.3 Exemple : charger les discours avec pandas, statistiques de base (nb docs, longueur moyenne, distribution par président)

### 3.2 Tokenisation
- 3.2.1 Tokenisation par espaces (naïve) — limites avec ponctuation et apostrophes (« l'État »)
- 3.2.2 Tokenisation par règles (NLTK, spaCy français)
- 3.2.3 Tokenisation sous-mots (BPE, utilisée par les LLMs)
  - Comparer le découpage NLTK vs tokenizer GPT
  - Implications : coût des APIs, inégalité entre langues (clin d'œil aux participant·es travaillant sur des langues sous-représentées)

### 3.3 Bag of Words et n-grams
- 3.3.1 BoW : matrice termes × discours
- 3.3.2 Limite : ordre perdu
- 3.3.3 n-grams (bigrammes, trigrammes) pour réintroduire l'ordre local
- 3.3.4 Exemple : top bigrammes par président (« croissance » sous Pompidou, « République » sous Macron…)

### 3.4 Cas particuliers (mention rapide)
- 3.4.1 URLs, emails, hashtags, dates → regex de pré-extraction

### 3.5 Pourquoi ça compte pour les LLMs
- 3.5.1 Un LLM ne voit pas des mots mais des tokens
- 3.5.2 Conséquences : fenêtre de contexte, coût, biais linguistique

---

## Module 4 — L'idée centrale du génératif : inverser l'encodeur

**Running example** : décisions du Conseil d'État (Légifrance, sous-corpus disponible HF/Kaggle). Classées par domaine (contentieux administratif, urbanisme, étrangers, sécurité, etc.). Résonne avec les participant·es travaillant sur le droit, le contentieux administratif, les textes réglementaires et institutionnels.

### 4.1 Le transformer (intuition)
- 4.1.1 Notion d'attention : chaque mot regarde les autres pour comprendre son rôle
- 4.1.2 Schéma encodeur / décodeur (sans la math)
- 4.1.3 Rupture vs réseaux séquentiels précédents (RNN/LSTM)

### 4.2 BERT : l'encodeur qui « comprend »
- 4.2.1 Tâche de pré-entraînement : Masked Language Modeling (MLM)
- 4.2.2 Exemple : prédire un mot masqué dans une décision du Conseil d'État
- 4.2.3 Application aval : classer une décision par domaine juridique

### 4.3 GPT : le décodeur qui « génère »
- 4.3.1 Tâche de pré-entraînement : prédire le mot suivant (autoregressif)
- 4.3.2 Exemple : générer un résumé ou une suite d'attendu juridique
- 4.3.3 Conséquences : non-déterminisme (température), hallucinations (un risque évident en droit), sensibilité au prompt

### 4.4 De BERT/GPT aux modèles modernes
- 4.4.1 Famille actuelle : ChatGPT, Claude, Mistral, Gemini, DeepSeek
- 4.4.2 Open vs closed source (clin d'œil local : Ollama, LM Studio)

---

## À faire ensuite

1. Décliner chaque module en 1 deck slides + 1 notebook avec running example codé et cellules TODO
2. Caler les durées des 4 modules dans les 3 h (avec accueil, pause, carrousel et capitalisation) et intégrer le découpage horaire en tête de ce fichier
3. Décider où recaser les notions LLM retirées (pré-entraînement, fine-tuning, RLHF, multimodalité, reasoning) — proposition : transversal dans le carrousel ou dans les sections 1.4-1.5

## Questions ouvertes

- Module 1 : dataset à choisir (tweets de députés français étiquetés par parti, ou Manifesto Project MARPOR)
- Module 4 : sous-corpus Conseil d'État sur HuggingFace ou scraping Légifrance
- Notions LLM retirées (pré-entrain., fine-tuning, RLHF, multimodalité, reasoning) : où les recaser ?
