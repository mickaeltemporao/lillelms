"""Construit un échantillon de descriptions d'annonces Airbnb (Inside Airbnb).

Running example du notebook J3 matin « Text mining : concepts ».

Pipeline :
1. Scraper la page Inside Airbnb « get-the-data » (requests + BeautifulSoup) pour
   découvrir dynamiquement les liens `listings.csv.gz` les plus récents.
2. Télécharger ces fichiers pour Bruxelles, Paris et Amsterdam.
3. Nettoyer les descriptions (retrait du HTML), ne garder que celles **en anglais**,
   échantillonner ~SAMPLE_PER_CITY annonces par ville.
4. Écrire un seul CSV léger `airbnb_listings.csv` à côté de ce script.

Source : https://insideairbnb.com/get-the-data/ (données sous licence CC0 1.0).
Voir codebook.md pour la sémantique des colonnes.

La détection de langue est volontairement simple (comptage de mots fonctionnels
EN vs FR) pour éviter une dépendance supplémentaire : suffisant pour filtrer un
corpus pédagogique, pas pour de la production.
"""

from __future__ import annotations

import html
import io
import re
import sys
import time
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

DATA_PAGE = "https://insideairbnb.com/get-the-data/"
HEADERS = {"User-Agent": "Mozilla/5.0 (lillelms research notebook)"}

# Sous-chaîne identifiant chaque ville dans l'URL du fichier listings.csv.gz.
CITIES = {
    "Brussels": "/brussels/",
    "Paris": "/paris/",
    "Amsterdam": "/amsterdam/",
}

# Certains dumps récents ont une colonne `price` entièrement vide (cas du dernier
# dump Paris listé sur la page). On épingle alors une date connue-bonne. Le
# scraping reste réel : il sert à découvrir/valider les autres villes.
PINNED_URLS = {
    "Paris": (
        "https://data.insideairbnb.com/france/ile-de-france/"
        "paris/2025-06-06/data/listings.csv.gz"
    ),
}

KEEP_COLUMNS = [
    "id",
    "description",
    "neighbourhood_cleansed",
    "room_type",
    "price",
    "latitude",
    "longitude",
]

SAMPLE_PER_CITY = 400
MIN_DESC_WORDS = 15
SEED = 42

# Détection de langue minimaliste (mots fonctionnels très fréquents).
EN_WORDS = {
    "the", "and", "with", "you", "your", "for", "this", "is", "are", "of",
    "to", "in", "near", "from", "we", "our", "have", "has", "will", "all",
}
FR_WORDS = {
    "le", "la", "les", "et", "avec", "vous", "votre", "pour", "une", "un",
    "des", "du", "est", "dans", "près", "nous", "notre", "sur", "ou", "au",
}

_TAG_RE = re.compile(r"<[^>]+>")
_WORD_RE = re.compile(r"[a-zàâäéèêëïîôöùûüç]+", re.IGNORECASE)
_PRICE_RE = re.compile(r"[^0-9.]")


def find_listing_urls() -> dict[str, str]:
    """Scrape la page Inside Airbnb et renvoie {ville: url listings.csv.gz}."""
    response = requests.get(DATA_PAGE, headers=HEADERS, timeout=60)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    links = [
        a["href"]
        for a in soup.find_all("a", href=True)
        if a["href"].endswith("listings.csv.gz")
    ]

    found: dict[str, str] = {}
    for city, token in CITIES.items():
        matches = [link for link in links if token in link]
        if not matches:
            raise RuntimeError(f"Aucun lien listings.csv.gz trouvé pour {city}")
        # Le premier match correspond au dump le plus récent listé sur la page,
        # sauf si on a épinglé une date connue-bonne (prix disponibles).
        found[city] = PINNED_URLS.get(city, matches[0])
    return found


def strip_html(text: str) -> str:
    text = _TAG_RE.sub(" ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def is_english(text: str) -> bool:
    tokens = [w.lower() for w in _WORD_RE.findall(text)]
    if not tokens:
        return False
    en = sum(tok in EN_WORDS for tok in tokens)
    fr = sum(tok in FR_WORDS for tok in tokens)
    return en >= 3 and en > fr * 1.5


def parse_price(value) -> float | None:
    if pd.isna(value):
        return None
    cleaned = _PRICE_RE.sub("", str(value))
    try:
        return float(cleaned) if cleaned else None
    except ValueError:
        return None


def load_city(city: str, url: str) -> pd.DataFrame:
    print(f"  [{city}] téléchargement {url}")
    response = requests.get(url, headers=HEADERS, timeout=180)
    response.raise_for_status()
    raw = pd.read_csv(io.BytesIO(response.content), compression="gzip")

    df = raw[KEEP_COLUMNS].copy()
    df = df.dropna(subset=["description"])
    df["description"] = df["description"].map(strip_html)
    df = df[df["description"].str.split().str.len() >= MIN_DESC_WORDS]

    english = df[df["description"].map(is_english)].copy()
    english["price"] = english["price"].map(parse_price)
    # On exige un prix (nécessaire pour tester H1 confort/luxe vs prix).
    english = english.dropna(subset=["price"])
    english["city"] = city
    print(f"  [{city}] {len(raw):,} brutes -> {len(df):,} avec desc -> "
          f"{len(english):,} en anglais avec prix")

    n = min(SAMPLE_PER_CITY, len(english))
    return english.sample(n=n, random_state=SEED)


def main() -> int:
    out_dir = Path(__file__).resolve().parent

    print(f"Scraping des liens sur {DATA_PAGE}")
    urls = find_listing_urls()
    for city, url in urls.items():
        print(f"  {city}: {url}")

    frames = []
    for city, url in urls.items():
        frames.append(load_city(city, url))
        time.sleep(1)  # courtoisie : on espace les requêtes

    corpus = pd.concat(frames, ignore_index=True)
    corpus = corpus.rename(columns={"neighbourhood_cleansed": "neighbourhood"})
    corpus = corpus[
        ["id", "city", "neighbourhood", "room_type", "price",
         "latitude", "longitude", "description"]
    ]

    path = out_dir / "airbnb_listings.csv"
    corpus.to_csv(path, index=False)
    print(f"\nÉcrit : {path.relative_to(out_dir.parent.parent)} "
          f"({len(corpus):,} lignes)")
    print(corpus["city"].value_counts().to_dict())
    return 0


if __name__ == "__main__":
    sys.exit(main())
