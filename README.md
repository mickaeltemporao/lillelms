# Exploration et Applications des IA Génératives en Sciences Sociales

a.k.a LilleLMs | Organisation QuantiLille 2026

22-26 juin 2026

### Intervenant.es
- [Léo Mignot (LM)](leo.mignot[at]cnrs.fr)
- [Mickael Temporão (MT)](m.temporao[at]sciencespobordeaux.fr)
- [Flore Vancompernolle Vromman (FV)](flore.vancompernolle[at]uclouvain.be)
- [Corentin Vande Kerckhove (CV)](corentin.vandekerckhove[at]uclouvain.be)

## Description

Ce module propose d’explorer les fondements et les applications des intelligences artificielles génératives dans le champ des sciences sociales. Conçu pour des participantes débutantes en programmation et curieuses des apports de l’IA en recherche, il offre une double approche. La première partie présente une initiation pratique à Python et la découverte progressive des outils d'analyse et de génération de contenus (textuels, audio, visuels) via des plateformes cloud. La seconde partie est articulée autour d’un focus thématique par jour, permettant d’approfondir chaque grand axe d’application avec des interventions d’expertes lors des demi-journées. L’objectif est d’équiper les chercheuses en sciences sociales de compétences techniques et analytiques permettant d'intégrer les IA génératives dans leurs projets de recherche, que ce soit comme outil d’analyse ou comme objet d’étude.

## Prérequis

- Aucune connaissance préalable en Python n'est requise  
- Une familiarité avec les concepts de base de l’analyse de données est un atout  
- Curiosité et intérêt pour les technologies d’IA et leurs impacts sur les sciences sociales

## Programme

Ce module est structuré en cinq journées thématiques. Vous pouvez lancer chaque notebook interactif directement dans **Google Colab** en cliquant sur les liens ci-dessous :

| Séance | Intervenant·es | ODJ | Supports |
| :--- | :--- | :--- | :--- |
| Lundi AM | AC | **Acceuil PUDL & PROGEDO**<br> | |
| Lundi PM | LM | **Initiation à Python & Google Colab** | - [Introduction à Python](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j1/aprem/01-introduction-python.ipynb)<br>- [Données et structures](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j1/aprem/02-types-et-structures.ipynb)<br>- [Vive les pandas](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j1/aprem/03-pandas-crash-course.ipynb) |
| Mardi AM | CV | **Concepts fondamentaux ML & IA** | - [Introduction to AI](https://github.com/mickaeltemporao/lillelms/blob/main/ressources/j2/1_matin/00-introduction-to-AI.pdf)<br>- [70 ans d'IA en 30 min.](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j2/1_matin/01-perspective-historique.ipynb)<br>- [Machine Learning](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j2/1_matin/02-ml-foundations.ipynb) |
| Mardi PM | MT | **APIs & prompt engineering** | - [L'API Hour](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j2/2_aprem/01-l-api-hour.ipynb)<br>- [Prompt engineering](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j2/2_aprem/02-a-la-recherche-du-prompt-perdu.ipynb) |
| Mercredi AM | CV | **Analyse de données textuelles** | - [Text Mining - PDF](https://github.com/mickaeltemporao/lillelms/blob/main/ressources/j3/1_matin/00-introduction-to-text-mining.pdf)<br>- [Text Mining](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j3/1_matin/01-text-mining-concepts.ipynb)<br>- [Text Mining : Applications](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j3/1_matin/02-text-mining-applications.ipynb) |
| Mercredi PM | MT | **Multimodalité & LLMs** | - [Multimodalité & LLMs](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j3/2_aprem/01-multimodal-analysis.ipynb)<br> TODO...|
| Jeudi AM | LM | **Enjeux éthiques & régulation** | - [Gouvernance de l'IA](https://github.com/mickaeltemporao/lillelms/blob/main/ressources/j4/1_matin/bloc-2-gouvernance-ia.pptx)<br>|
| Jeudi PM | FV | **Équité et explicabilité** | - [Équité](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j4/2_aprem/01-fairness.ipynb)<br>- [Explications & LLM](https://colab.research.google.com/github/mickaeltemporao/lillelms/blob/main/ressources/j4/2_aprem/03-generer-explications.ipynb)<br>[Datagotchi Santé](https://github.com/mickaeltemporao/lillelms/blob/main/ressources/j4/2_aprem/02-explicabilite-projet-datagotchi-sante.pptx) |
| Vendredi AM | ALL | **Consolidation & bilan**<br>- Synthèse générale, perspectives futures des IA génératives en sciences sociales et mini-projets | - [Clôture](https://github.com/mickaeltemporao/lillelms/blob/main/ressources/j5/2_aprem/J5_slides.html)  |
| Vendredi PM | ALL | **Configuration locale & autonomie**<br>- Formation à la configuration d'un environnement de travail personnel (installation pas-à-pas en local) | |


## Analyse des participants

Le dossier `participants/` contient un script qui génère un rapport synthétique sur les stagiaires sélectionnés. Les dépendances Python du repo sont gérées avec [`uv`](https://docs.astral.sh/uv/). Fournir la clé `ANTHROPIC_API_KEY` via un fichier `.env` à la racine (voir `.env.example`).

```
cp .env.example .env   # puis renseigner ANTHROPIC_API_KEY
uv sync
uv run python participants/analyze_participants.py
```

Le rapport est écrit dans `participants/analyse_des_participants.md`. Sans clé API, le rapport est généré en mode descriptif uniquement (sans synthèse LLM des champs texte libre).

> Le CSV brut des candidatures n'est pas fourni dans ce dépôt pour des raisons d'anonymisation des données personnelles (noms, e-mails, motivations détaillées). Seul le rapport synthétique est versionné.

## Datasets

Le dossier `data/` rassemble les scripts qui récupèrent et pré-traitent les datasets utilisés comme « running examples » dans les notebooks. Chaque dataset a son sous-dossier avec un script `fetch_*.py` et un `codebook.md` ; les CSV pré-traités sont versionnés à côté du script.

Pour reconstruire un dataset depuis sa source :

```
uv run python data/<dataset>/fetch_<dataset>.py
```

Convention de colonnes : préfixe `x_` pour les features, `y_` pour les cibles, `z_` pour les attributs sensibles (pivots des analyses fairness). Voir `data/README.md` pour les détails.

