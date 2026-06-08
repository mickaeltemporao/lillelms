# Codebook : Airbnb (Inside Airbnb)

Échantillon de descriptions d'annonces Airbnb, utilisé comme running example du
notebook J3 matin « Text mining : concepts ».

| Fichier | Lignes | Contenu |
|---|---|---|
| `airbnb_listings.csv` | 1 200 | 400 annonces par ville (Bruxelles, Paris, Amsterdam) |

## Construction

Généré par `fetch_airbnb.py` :

1. **Scraping** de la page [Inside Airbnb get-the-data](https://insideairbnb.com/get-the-data/)
   (requests + BeautifulSoup) pour découvrir les liens `listings.csv.gz`.
2. Téléchargement des fichiers détaillés par ville.
3. Nettoyage des descriptions (retrait du HTML), filtre **anglais uniquement**
   (heuristique mots fonctionnels EN vs FR), longueur minimale 15 mots, prix présent.
4. Échantillon aléatoire de 400 annonces par ville (`seed=42`).

> **Note** : le dernier dump Paris listé a une colonne `price` vide ; on épingle
> donc le dump Paris du 2025-06-06 (prix disponibles). Bruxelles et Amsterdam
> utilisent le dernier dump listé.

## Colonnes

| Colonne | Type | Description |
|---|---|---|
| `id` | int | Identifiant de l'annonce sur Airbnb |
| `city` | str | Ville (`Brussels`, `Paris`, `Amsterdam`) |
| `neighbourhood` | str | Quartier (champ `neighbourhood_cleansed` d'Inside Airbnb) |
| `room_type` | str | Type de logement (`Entire home/apt`, `Private room`, `Hotel room`, `Shared room`) |
| `price` | float | Prix par nuit (devise locale, symbole et séparateurs retirés) |
| `latitude` | float | Latitude (sert à dériver la centralité du logement) |
| `longitude` | float | Longitude |
| `description` | str | Texte libre de présentation du logement (anglais), **le corpus à analyser** |

## Usage pédagogique

Problématique : *quels imaginaires du voyage les hôtes mobilisent-ils ?* On
transforme les descriptions en embeddings, on construit des requêtes thématiques
(« logement confortable », « expérience locale authentique », « hébergement de
luxe ») et on calcule leur similarité cosinus avec chaque annonce pour tester :

- **H1** : prix élevé ↔ discours de confort/luxe (colonne `price`) ;
- **H2** : quartier central ↔ discours d'expérience touristique (`latitude`/`longitude`) ;
- **H3** : chambre privée ↔ discours d'hospitalité (`room_type`).

## Source et licence

Inside Airbnb (<https://insideairbnb.com>), données publiées sous licence
**CC0 1.0** (domaine public). Données collectées à des fins éducatives.
