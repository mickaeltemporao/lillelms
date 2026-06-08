"""Construit un échantillon léger de critiques de films notées (Allociné).

Running example du notebook J3 matin « Text mining : applications ».

Source : dataset `tblard/allocine` sur Hugging Face (critiques Allociné en
français, étiquetées positif/négatif d'après la note laissée par l'internaute).

Pipeline :
1. Télécharger les fichiers parquet `train` et `test`.
2. Échantillonner de façon **équilibrée** (autant de positifs que de négatifs).
3. Renommer les colonnes (`review` -> `text`, `label` -> `polarite`).
4. Écrire `critiques_films_train.csv` et `critiques_films_test.csv`.

Voir codebook.md pour le détail des colonnes.
"""

from __future__ import annotations

import io
import sys
from pathlib import Path

import pandas as pd
import requests

BASE = "https://huggingface.co/datasets/tblard/allocine/resolve/main/allocine"
SPLITS = {
    "train": f"{BASE}/train-00000-of-00001.parquet",
    "test": f"{BASE}/test-00000-of-00001.parquet",
}
HEADERS = {"User-Agent": "Mozilla/5.0 (lillelms research notebook)"}

# Échantillon léger et équilibré (par classe).
PER_CLASS = {"train": 1500, "test": 500}
LABELS = {0: "négatif", 1: "positif"}
SEED = 42


def download(url: str) -> pd.DataFrame:
    response = requests.get(url, headers=HEADERS, timeout=180)
    response.raise_for_status()
    return pd.read_parquet(io.BytesIO(response.content))


def sample_balanced(df: pd.DataFrame, per_class: int) -> pd.DataFrame:
    parts = [
        grp.sample(n=min(per_class, len(grp)), random_state=SEED)
        for _, grp in df.groupby("label")
    ]
    out = pd.concat(parts, ignore_index=True)
    return out.sample(frac=1.0, random_state=SEED).reset_index(drop=True)


def main() -> int:
    out_dir = Path(__file__).resolve().parent

    for split, url in SPLITS.items():
        print(f"Téléchargement {split} : {url}")
        raw = download(url)
        print(f"  lignes brutes : {len(raw):,}")

        sample = sample_balanced(raw, PER_CLASS[split])
        sample = sample.rename(columns={"review": "text", "label": "polarite"})
        sample["polarite"] = sample["polarite"].map(LABELS)
        sample = sample[["text", "polarite"]]

        path = out_dir / f"critiques_films_{split}.csv"
        sample.to_csv(path, index=False)
        print(
            f"  écrit : {path.relative_to(out_dir.parent.parent)} "
            f"({len(sample):,} lignes, {sample['polarite'].value_counts().to_dict()})"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
