# Jeudi | Enjeux éthiques de l'IA

Proposition : structurer la journée en 4 blocs de +/- 1h30.

---

## Bloc 1 | Tout ce que j'ai détesté en IA Gé(nérative)

**Intervenants :** LM

**Format :** Présentation (slides/supports)

### Enjeux sociopolitiques

Repartir des diapos léo sur enjeux pouvoir, travail, etc. et compléter avec les points sur enjeux vol massif données, AI con, évoquer ludite labs, etc.

Cf. illustration inspirations des supports existants :

- AI beyond technology: power and politics
- Algorithms and society: acceptability, bias, data -> sera plutôt côté Flore
- AI and the transformation of organizations and work

Autres enjeux sociopolitiques :
- Enfermements des utilisateurs dans leurs idéologies (bulles de filtre). Exemple repris dans ce papier récent : https://www.nature.com/articles/s41586-026-10447-1
- Désinformation et mésinformation

### (Mé-)usages en recherche

- des exemples du pire pour en dire du mal
- et évoquer les points suivants en creux et opposition IE illustrer le fait que ça peut être mal fait et donc poser soucis
  - [intégrer les idées suivantes de Flore par point entrée en recherche]
  - Privacy & RGPD (anonymisation, risques de ré-identification dans des données apparemment anonymisées) -> RGPD plutôt à discuter dans la partie régulation ?
  - Fiabilité & Hallucinations des LLM (mécanisme des hallucinations; évaluation des sorties LLM; stratégies de mitigation avec des RAG, prompting structuré, vérification des sources)
  - [aviser car sans doute au dessus] Impact environnemental (ordres de grandeur; outil `codecarbon` pour mesurer les émissions CO₂ d'un script Python en live; stratégies de réduction comme le choix du modèle)

### Risques concrets de l'IA (autres que sociopolitique et recherche)
Présenter des exemples de risques dans l'IA. En voilà quelques uns :
- Discriminations dans les données et les modèles (ex. COMPAS, génération d'images, données synthétiques qui amplifient les inégalités)

---

## Bloc 2 | Régulation

**Intervenants :** FV / LM

**Format :** Présentation (slides ou autre support mais à priori pas de code nécessaire) + discussion ouverte avec le groupe (peut-être leur laisser présenter des problématiques qu'ils auraient pu rencontrer de leur côté ?).


### RGPD

### AI Act européen
- Qu'est-ce qui est mis en place au niveau de l'UE pour limiter ces risque et les légiférer : Ethics guidelines for Trustworthy AI (HLEG EU) + AI act
- Définition de trustworthy et des différents piliers et principes sous-jacents (Human agency & oversight · Fairness · Explicabilité · Sécurité & robustesse · Privacy · Bien-être sociétal)
- AI act : approche fondée sur le risque : inacceptable / haut / limité / minimal
- Réglementation spécifique aux systèmes GenAI 

---

## Bloc 3 | Fairness

**Intervenant :** FV

**Format :** Notebook

**Problématique :** Comment des inégalités présentes dans les données d'entraînement se reproduisent et s'amplifient dans les prédictions d'un modèle ?

**Dataset :** Law School (Bar Passage Study) — prédire le passage du barreau.

**Contenu notebook :**
- Rappel du modèle de classification entraîné en j2/j3 sur les mêmes données
- Mesure des métriques de précision (accuracy, precision, recall) et fairness (taux de faux positifs/négatifs par groupe, demographic parity, equal opportunity)
- Stratégies de mitigation : présentation théorique des différentes étapes sur lesquelles on peut agir (in-/pre-/post-processing) et implémentation d'une méthode de post-processing pour pouvoir l'appliquer directement sur les prédictions du modèle obtenues dans les jours précédents
- Mesure des mêmes métriques à nouveau pour voir l'impact de la mitigation
- Réflexion collective : peut-on optimiser accuracy ET fairness simultanément ? Quel critère choisir selon le contexte ?


---

## Bloc 4 | Explicabilité

**Intervenants :** FV

**Format :** Présentation (slides) + Notebook

**Problématique :** Les sorties techniques d'un modèle ML (coefficients, valeurs SHAP) sont difficiles à interpréter pour un utilisateur final. Comment les transformer en explications personnalisées et compréhensibles ?

**Dataset :** Datagotchi Santé — modèle de régression ridge prédisant un score de bien-être (0-100) à partir de 20 questions sur le mode de vie.

**Contenu présentation :**
- Présentation du projet Datagotchi Santé et de ses résultats
- Retour sur les méthodes d'explicabilité appliquées au projet et test par les participants des différentes méthodes
- Discussion collective (Wooclap) sur les méthodes d'explication présentées

**Contenu notebook :**
- Pourquoi utiliser un LLM pour générer des explications ? Pipeline : modèle ML → coefficients × réponses utilisateur → LLM → explication en langage naturel
- Construction d'un prompt structuré (rôle, contexte, tâche, format, calcul des contributions par variable)
- Appel à l'API OpenAI (`gpt-4o-mini`) et affichage de l'explication générée
- Hack time (exercices optionnels) : modifier le ton/format, ajouter des recommandations concrètes
- Limites et enjeux éthiques : qualité du prompt, risque de confabulation, transparence et responsabilité (lien AI Act)


