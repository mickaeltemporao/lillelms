# J3 matin (CV) — Text mining : de la collecte aux embeddings

**Mercredi 24 juin 2026, 9h-12h** | Intervenant : Corentin Vande Kerckhove

## Logique

Mercredi matin = *text mining*. On déroule une chaîne complète, du texte brut récupéré en ligne jusqu'aux représentations vectorielles modernes :

1. **Collecter** un corpus en ligne par scraping (`requests` + `BeautifulSoup`)
2. **Découper** le texte en tokens et le nettoyer
3. **Vectoriser** : bag of words → term-document matrix → réduction de dimension → TF-IDF
4. **Représenter le sens** : le principe d'embedding, de Word2Vec à BERT
5. **Faire quelque chose** : applications concrètes (similarité, clustering, recherche sémantique, sentiment)

Fil rouge : *« comment passe-t-on d'un texte à des nombres exploitables, et qu'est-ce que chaque génération de méthode gagne ? »*

## Pré-requis (acquis mardi)

- Notion de feature, de vectorisation, de token, d'embedding (J2 matin)
- Premier contact avec les APIs (J2 PM avec MT)

## Déroulé

| Créneau | Durée | Bloc |
|---|---|---|
| 9h00-9h10 | 10' | Récap J2 + fil du jour : « du texte aux nombres » |
| 9h10-9h35 | 25' | **Collecter** : scraping avec `requests` + `BeautifulSoup` (récupérer un corpus en ligne) |
| 9h35-9h55 | 20' | **Tokenization** + nettoyage : tokens, stopwords, lemmatisation vs stemming |
| 9h55-10h30 | 35' | **Vectorisation classique** : bag of words → term-document matrix → réduction de dimension → TF-IDF |
| 10h30-10h45 | 15' | Pause |
| 10h45-11h00 | 15' | **Le principe d'embedding** : de la vectorisation creuse (one-hot/TDM) aux vecteurs denses |
| 11h00-11h30 | 30' | **Embeddings sémantiques** : Word2Vec → BERT (intuition, démo) |
| 11h30-11h55 | 25' | **Applications concrètes** : similarité cosinus, clustering, recherche sémantique, nuages de mots, sentiment |
| 11h55-12h00 | 5' | Synthèse + transition PM (audio/vidéo, MT) |

## Contenu détaillé

### 1. Collecter — scraping
- `requests` : récupérer une page HTML
- `BeautifulSoup` : parser le DOM, extraire le texte utile (titres, paragraphes, liens)
- Bonnes pratiques : `robots.txt`, délais entre requêtes, structure d'une page
- Résultat : un mini-corpus SHS construit en direct

### 2. Tokenization + nettoyage
- Du texte brut aux tokens (mots, sous-mots)
- Stopwords, ponctuation, casse
- Lemmatisation vs stemming : normaliser les formes
- Pourquoi ces choix changent la suite du pipeline

### 3. Vectorisation classique
- **Bag of words** : représenter un document par les mots qu'il contient (sans ordre)
- **Term-document matrix** : documents × vocabulaire, matrice de comptages
- **Réduction de dimension** : vocabulaire énorme et matrice creuse → filtrage, fréquences
- **TF-IDF** : pondérer les mots par leur rareté → faire ressortir ce qui est discriminant

### 4. Le principe d'embedding et de vectorisation
- Limite des représentations creuses : pas de notion de *sens* ni de proximité entre mots
- Idée de l'embedding : projeter mots/documents dans un espace dense où la distance ≈ similarité sémantique
- Vectorisation = transformer du texte en vecteurs ; embedding = vectorisation *qui capte le sens*

### 5. Word2Vec → BERT
- **Word2Vec** : un vecteur par mot, appris par contexte (« king - man + woman ≈ queen »). Limite : un seul vecteur par mot, hors contexte
- **BERT** : embeddings *contextuels*, le même mot a un vecteur différent selon la phrase
- Démo via `sentence-transformers` (embeddings de phrases prêts à l'emploi)

### 6. Applications concrètes
- **Similarité cosinus** : retrouver des documents proches
- **Recherche sémantique** : requête → documents les plus proches dans l'espace d'embedding
- **Clustering** : regrouper des textes par thème
- **Nuages de mots**, **analyse de sentiment** : exemples rapides

## Notebooks

- ✅ `01-text-mining-concepts.ipynb` — chaîne complète sur les descriptions Airbnb (Inside Airbnb) : scraping `requests`/`BeautifulSoup` → tokenization → bag of words/TDM → réduction de dimension → TF-IDF → Word2Vec → BERT + similarité cosinus pour tester H1/H2/H3. Dataset : [`data/airbnb/`](../../../data/airbnb/).
- ✅ `02-text-mining-applications.ipynb` — 5 applications (du plus simple au plus difficile) sur des critiques de films notées (Allociné) : nuage de mots/mots-clés → analyse de sentiment → classification supervisée → recherche sémantique → biais éthiques. Dataset : [`data/critiques_films/`](../../../data/critiques_films/).
- Slides (1 deck pour le fil du matin) — à faire.

## À caler

- Réutilisation possible des notebooks CUSO2026 (`j3-analyse.md`) : « Le texte comme un sac de mots », `pandas_et_texte`, `topic_modeling`
- Cohérence avec J3 PM (MT, audio/visuel : Whisper, captionning)
- Choisir le site cible du scraping (corpus qui résonne avec les stagiaires)
