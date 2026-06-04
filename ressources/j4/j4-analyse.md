# Jeudi | Enjeux éthiques de l'IA

Proposition : structurer la journée en 4 blocs de +/- 1h30.

---

## Bloc 1 | Risques et régulation

**Intervenants :** FV / LM

**Format :** Présentation (slides ou autre support mais à priori pas de code nécessaire) + discussion ouverte avec le groupe (peut-être leur laisser présenter des problématiques qu'ils auraient pu rencontrer de leur côté ?).

### Risques concrets de l'IA
Présenter des exemples de risques dans l'IA. En voilà quelques uns :
- Discriminations dans les données et les modèles (ex. COMPAS, génération d'images, données synthétiques qui amplifient les inégalités)
- Deepfakes
- Désinformation et mésinformation
- Hallucinations des LLM
- Enfermements des utilisateurs dans leurs idéologies

### AI Act européen
- Qu'est-ce qui est mis en place au niveau de l'UE pour limiter ces risque et les légiférer : Ethics guidelines for Trustworthy AI (HLEG EU) + AI act
- Définition de trustworthy et des différents piliers et principes sous-jacents (Human agency & oversight · Fairness · Explicabilité · Sécurité & robustesse · Privacy · Bien-être sociétal)
- AI act : approche fondée sur le risque : inacceptable / haut / limité / minimal
- Réglementation spécifique aux systèmes GenAI 


---

## Bloc 2 | Fairness

**Intervenant :** FV ?

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

## Bloc 3 | Explicabilité

**Intervenants :** FV ou LM

**Format :** Notebook

**Problématique :** Les modèles ML performants sont des boîtes noires. Comment expliquer une prédiction individuelle ou le comportement global du modèle ?

**Dataset :** suite logique sur le dataset Law School (on peut aussi prendre une autre problématique où l'explicabilité est nécessaire comme dans les LLM)

**Contenu notebook :**
- Distinction modèles interprétables (arbres de décision, régression logistique) vs. boîtes noires (forêts aléatoires, gradient boosting)
- SHAP (SHapley Additive exPlanations) : intuition des valeurs de Shapley, graphiques beeswarm et waterfall (librairie `shap`, compatible scikit-learn)
- Application : quelles variables influencent une prédiction individuelle ?


---

## Bloc 4 | Troisième problématique (à choisir)

**Intervenants :** FV ou LM

**Format :** Notebook

Quelques idées pour cette troisième problématique:
- Privacy & RGPD (anonymisation, risques de ré-identification dans des données apparemment anonymisées)
- Fiabilité & Hallucinations des LLM (mécanisme des hallucinations; évaluation des sorties LLM; stratégies de mitigation avec des RAG, prompting structuré, vérification des sources)
- Impact environnemental (ordres de grandeur; outil `codecarbon` pour mesurer les émissions CO₂ d'un script Python en live; stratégies de réduction comme le choix du modèle)
- Autre ?
