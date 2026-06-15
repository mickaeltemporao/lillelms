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


### Reprendre liste biblio critique pour
- fake schism
- transhumanisme + groupes derrière "safety/ethics" 
- enviro ?
- évaluation ?
- exemples recherche.
  - entrainement données historiques pour faire parler les morts
  - silicon réponse questionnaires
  - entretiens par IA
  - demander note sur du texte (exemple média et emission, mais aussi dans littérature scientifique)
  - absence vérification robustesse F1, etc.


### GARDE ÇA : 
AI CON + BOUQUIN JOURNALISTE
dire que les doomers et ceux qui survendent sont les deux face d'une même piece de toute puissance de l'IA, etc.

Bender, E. M. (2023, juillet 5). Talking about a ‘schism’ is ahistorical. Medium. https://medium.com/@emilymenonbender/talking-about-a-schism-is-ahistorical-3c454a77220f

Nature – Editorials. (2023). Stop talking about tomorrow’s AI doomsday when AI poses risks today. Nature, 618(7967), 885‑886. https://doi.org/10.1038/d41586-023-02094-7

Pouré, C. (2026, avril 6). Pilier de l’intelligence artificielle, Hugging Face diffuse des centaines de milliers de documents soumis au droit d’auteur. Mediapart. https://www-mediapart-fr.bnf.idm.oclc.org/journal/economie-et-social/060426/pilier-de-l-intelligence-artificielle-hugging-face-diffuse-des-centaines-de-milliers-de-docume

Reisner, A. (2025a, novembre 4). The Company Quietly Funneling Paywalled Articles to AI Developers. The Atlantic. https://www.theatlantic.com/technology/2025/11/common-crawl-ai-training-data/684567/
Reisner, A. (2025b, novembre 4). The Nonprofit Doing the AI Industry’s Dirty Work. The Atlantic. https://www.theatlantic.com/technology/2025/11/common-crawl-ai-training-data/684567/

Muhammad, I. (2025, juin 25). Why Does Every Commercial for A.I. Think You’re a Moron? The New York Times. https://www.nytimes.com/2025/06/25/magazine/ai-commercials-ads-loneliness.html

Lewis, B. (2025, janvier 29). ‘Headed for technofascism’ : The rightwing roots of Silicon Valley. The Guardian. https://www.theguardian.com/technology/ng-interactive/2025/jan/29/silicon-valley-rightwing-technofascism

Adieu la régulation, bonjour l’innovation : Le pivot de l’Europe sur l’IA. (2025, février 7). POLITICO. https://www.politico.eu/article/adieu-la-regulation-bonjour-linnovation-le-pivot-de-leurope-sur-lia/

« L’intelligence artificielle accélère le désastre écologique, renforce les injustices et aggrave la concentration des pouvoirs ». (2025, février 6). https://www.lemonde.fr/idees/article/2025/02/06/l-intelligence-artificielle-accelere-le-desastre-ecologique-renforce-les-injustices-et-aggrave-la-concentration-des-pouvoirs_6533885_3232.html

algorithmes, D. les. (2024, décembre 10). L’IA générative, nouvelle couche d’exploitation du travail. https://danslesalgorithmes.net/2024/12/10/lia-generative-nouvelle-couche-dexploitation-du-travail/

Loin des critiques originelles, la France devient une terre d’accueil des champions de l’IA générative. (2024, novembre 19). France Culture. https://www.radiofrance.fr/franceculture/podcasts/un-monde-connecte/loin-des-critiques-originelles-la-france-devient-une-terre-d-accueil-des-champions-de-l-ia-generative-1165197

Derrière l’IA, la déferlante des « data centers ». (2024, juin 14). Le Monde.fr. https://www.lemonde.fr/economie/article/2024/06/14/derriere-l-ia-la-deferlante-des-data-centers_6239694_3234.html

Boutet, A., Sénéchal, J., Bernelin, M., & Letrone, W. (2024, avril 10). L’AI Act, ou comment encadrer les systèmes d’IA en Europe. The Conversation. http://theconversation.com/lai-act-ou-comment-encadrer-les-systemes-dia-en-europe-226980

Régulation de l’IA : « Le problème n’est pas éthique, ni technologique, il est politique ». (2024, mai 21). La Croix. https://www.la-croix.com/a-vif/regulation-de-l-ia-le-probleme-nest-pas-ethique-ni-technologique-il-est-politique-20240521

Emmanuel Macron veut faire de la France « un des pays champions de l’IA ». (2024, mai 22). Le Monde.fr. https://www.lemonde.fr/economie-francaise/article/2024/05/22/emmanuel-macron-veut-faire-de-la-france-un-des-pays-champions-de-l-ia_6234677_1656968.html

Electricity grids creak as AI demands soar. (s. d.). Consulté 21 mai 2024, à l’adresse https://www.bbc.com/news/articles/cj5ll89dy2mo

Generative AI Takes Stereotypes and Bias From Bad to Worse. (s. d.). Consulté 21 mai 2024, à l’adresse https://www.bloomberg.com/graphics/2023-generative-ai-bias/?utm_source=wedodata.beehiiv.com&utm_medium=referral&utm_campaign=des-insectes-c3po-sauce-ia-des-graphiques-live-des-villes-corails-et-des-paradis-fiscaux

Hern, A. (2024, avril 16). TechScape : How cheap, outsourced labour in Africa is shaping AI English. The Guardian. https://www.theguardian.com/technology/2024/apr/16/techscape-ai-gadgest-humane-ai-pin-chatgpt

CNIL : Les propositions-chocs de la Commission de l’IA pour faciliter l’accès aux données personnelles. (2024, mars 13). Le Monde.fr. https://www.lemonde.fr/economie/article/2024/03/13/cnil-les-propositions-chocs-de-la-commission-de-l-ia-pour-faciliter-l-acces-aux-donnees-personnelles_6221779_3234.html

Intelligence artificielle : « Il faut faire des données de santé un bien commun pour la recherche ». (2023, mars 31). Le Monde.fr. https://www.lemonde.fr/idees/article/2023/03/31/intelligence-artificielle-il-faut-faire-des-donnees-de-sante-un-bien-commun-pour-la-recherche_6167803_3232.html

La Commission de l’intelligence artificielle veut faciliter l’installation de centres de données en France. (2024, mars 13). Le Monde.fr. https://www.lemonde.fr/economie/article/2024/03/13/la-commission-de-l-intelligence-artificielle-veut-faciliter-l-installation-de-centres-de-donnees-en-france_6221778_3234.html


Buolamwini, J. (2023, octobre 30). We need to focus on the AI harms that already exist. MIT Technology Review. https://www.technologyreview.com/2023/10/30/1082656/focus-on-existing-ai-harms/
Expert Comment : No need to wait for the future, the danger of AI is already here | University of Oxford. (2023, mai 15). https://www.ox.ac.uk/news/2023-05-15-expert-comment-no-need-wait-future-danger-ai-already-here

How elite schools like Stanford became fixated on the AI apocalypse. (2023, juillet 5). Washington Post. https://www.washingtonpost.com/technology/2023/07/05/ai-apocalypse-college-students/

Bender, E. M. (2023, juillet 5). Talking about a ‘schism’ is ahistorical. Medium. https://medium.com/@emilymenonbender/talking-about-a-schism-is-ahistorical-3c454a77220f

« Sur l’intelligence artificielle, l’opposition entre les pessimistes et les optimistes est simpliste, voire dangereuse ». (2023, mai 4). Le Monde.fr. https://www.lemonde.fr/idees/article/2023/05/04/sur-l-intelligence-artificielle-l-opposition-entre-les-pessimistes-et-les-optimistes-est-simpliste-voire-dangereuse_6171999_3232.html

https://www.nytimes.com/2026/06/10/business/economy/back-office-workers-ai.html

AI benchmarks hampered by bad science. (s. d.). Consulté 27 novembre 2025, à l’adresse https://www.theregister.com/2025/11/07/measuring_ai_models_hampered_by/
AI’s capabilities may be exaggerated by flawed tests, according to new study. (2025, novembre 6). NBC News. https://www.nbcnews.com/tech/tech-news/ai-chatgpt-test-smart-capabilities-may-exaggerated-flawed-study-rcna241969

Boelaert, J., Coavoux, S., Ollion, É., Petev, I., & Präg, P. (2025). Machine Bias. How Do Generative Language Models Answer Opinion Polls?1. Sociological Methods & Research, 00491241251330582. https://doi.org/10.1177/00491241251330582

Barrie, C., Palmer, A., & Spirling, A. (s. d.). Replication for Language Models.

Park, J. S., Zou, C. Q., Shaw, A., Hill, B. M., Cai, C., Morris, M. R., Willer, R., Liang, P., & Bernstein, M. S. (2024). Generative Agent Simulations of 1,000 People (arXiv:2411.10109). arXiv. https://doi.org/10.48550/arXiv.2411.10109


- https://openai.com/index/scaling-social-science-research/
  - Gabriel =  "God is my strength". God help us
- https://github.com/google-deepmind/concordia

Résumé par IA des textes scientifiques en page éditeurs alors qu'il y a un abstract

Review par IA (avec intérêts possibles et risques)
papier sur génération enquête quanti automatique

https://www.linkedin.com/feed/update/urn:li:activity:7413610180048818177/
- "i have not verified the results" (vérif citation)

https://ai.nejm.org/doi/full/10.1056/AIe2501175
Léo Mignot
 — 
12/12/2025 09:34
What a bright future for peer review. What could possibly go wrong?
TL;DR: editorial from the NEJM-AI describing their new "Fast Track" using LLM to speed up evaluation process https://ai.nejm.org/doi/full/10.1056/AIe2501175
Léo Mignot
 — 
12/12/2025 11:56
To be honest : there is still a (kinda strong) human evaluation in their loop. But 1) for how long? ; 2) it was in their best interest to play it safe with the creation and publication of their track ;  3) if the NEJM legitimizes this, I don't see how it could turn out well with shady publishers.

Etienne
 — 
22/09/2025 13:04
Yet another paper on "LLMs can replace survey" (unearthed by Leo): https://arxiv.org/pdf/2503.16498




https://www.technologyreview.com/2024/12/18/1108796/this-is-where-the-data-to-build-ai-comes-from/


Léo Mignot
 — 
21/11/2024 14:54
TL;DR : je doute pas que la performance technique soit follement prometteuse pour certaines applications, mais si les gens ne veulent plus interroger d'humains, autant le dire on gagnera du temps. 


De AeXiv, vu sur Twitter (grace à @Léo Mignot ) : "Generative Agent Simulations of 1,000 People" https://arxiv.org/abs/2411.10109 "The generative agents replicate participants' responses on the General Social Survey 85% as accurately as participants replicate their own answers two weeks later, and perform comparably in predicting personality traits and outcomes in experimental replications"
arXiv.org
Generative Agent Simulations of 1,000 People
The promise of human behavioral simulation--general-purpose computational agents that replicate human behavior across domains--could enable broad applications in policymaking and social science. We present a novel agent architecture that simulates the attitudes and behaviors of 1,052 real individuals--applying large language models to qualitativ...
Image
Léo Mignot
 — 
21/11/2024 13:50
Avec également un fil sur bluesky d'un des auteurs : https://bsky.app/profile/joon-s-pk.bsky.social/post/3lbagnqdnic2i
Joon Sung Park (@joon-s-pk.bsky.social)
Simulating human behavior with AI agents promises a testbed for policy and the social sciences. We interviewed 1,000 people for two hours each to create generative agents of them. These agents replicate their source individuals’ attitudes and behaviors. 🧵

arxiv.org/abs/2411.10109
Joon Sung Park (@joon-s-pk.bsky.social)
Bluesky•18/11/2024 18:21
