# J3 matin (CV) — Text mining : classique + LLM-based

**Mercredi 24 juin 2026, 9h-12h** | Intervenant : Corentin Vande Kerckhove

## Logique

Mercredi matin = *détails text mining*. Approfondit les idées vues mardi (tokens, embeddings, RAG) avec du concret sur la pratique du text mining. Deux pipelines présentés en miroir :

- **Pipeline classique** : TDM, nettoyage, TF-IDF, embeddings sémantiques, similarité cosinus
- **Pipeline LLM-based** : classification zero-shot, RAG, agentic

## Pré-requis (acquis mardi)

- Notion de token, d'embedding, de RAG, d'agentic
- Premier contact avec les APIs (J2 PM avec MT)

## Déroulé

| Créneau | Durée | Bloc |
|---|---|---|
| 9h00-9h10 | 10' | Récap J2 + fil du jour |
| 9h10-9h25 | 15' | Pipeline classique : TDM, nettoyage, stopwords, lemmatisation vs stemming |
| 9h25-9h55 | 30' | TF-IDF (concept + notebook pratique) |
| 9h55-10h15 | 20' | Embeddings sémantiques (Word2Vec → BERT) |
| 10h15-10h30 | 15' | Pause |
| 10h30-10h50 | 20' | Similarité cosinus + applications classiques (nuages de mots, sentiment, clustering) |
| 10h50-11h20 | 30' | Text mining LLM-based : zero-shot, structured output, codage thématique assisté |
| 11h20-11h40 | 20' | RAG pour explorer un corpus |
| 11h40-11h55 | 15' | Agentic pour text mining (démo conceptuelle) |
| 11h55-12h00 | 5' | Synthèse + transition PM (audio/vidéo) |

## À créer

- Notebook TF-IDF prêt-à-l'emploi (corpus SHS court)
- Notebook embeddings (via `sentence-transformers`)
- Slides + notebook « classification zero-shot avec LLM »
- Notebook RAG minimal (vector store + LLM)
- Slides conceptuelles agentic

## À caler

- Réutilisation possible des notebooks CUSO2026 mentionnés dans `j3-analyse.md`
- Cohérence avec J3 PM (MT, audio/visuel : Whisper, captionning)
