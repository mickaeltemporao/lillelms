# Codebook : ina_zfe

Ce dossier contient un corpus simulé (mock data) inspiré des requêtes sur le catalogue de l'INA (Institut National de l'Audiovisuel). Il rassemble des métadonnées sur les reportages et débats télévisés concernant les Zones à Faibles Émissions (ZFE), principalement sur TF1 et CNews.

## Colonnes

| Nom de la colonne | Type | Description |
|---|---|---|
| `indice` | Entier | Identifiant unique de la ligne |
| `chaine` | Texte | Nom de la chaîne de télévision (ex: TF1, CNews). |
| `date` | Date | Date de diffusion au format JJ/MM/AAAA. |
| `heure` | Heure | Heure de diffusion au format HH:MM:SS. |
| `duree` | Durée | Durée de la séquence consacrée au sujet (HH:MM:SS). |
| `titre` | Texte | Titre ou bandeau décrivant la séquence. |
| `lien` | URL | Lien vers la notice INA correspondante (fictif dans ce dataset). |
| `emission` | Texte | Nom de l'émission dans laquelle s'inscrit la séquence. |
| `type` | Texte | Format de la séquence (Plateau, Débat, Reportage, etc.). |

## Notes

Ce dataset est utilisé dans la session J2 pour illustrer l'analyse de sentiment et le codage thématique à l'aide de Modèles de Langage (LLMs). 
