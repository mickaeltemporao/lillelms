"""Récupère le dataset Law School et écrit deux CSV pré-traités.

Source : https://github.com/damtharvey/law-school-dataset

Sorties (à côté de ce script) :
- law_school_for_regression.csv      : features x_* + sensible z_white + cible y_zgpa
- law_school_for_classification.csv  : features x_* + sensible z_white + cible y_pass_bar

Voir codebook.md pour la sémantique de chaque colonne.
"""

from __future__ import annotations

import io
import sys
from pathlib import Path

import pandas as pd
import requests

SOURCE_URL = (
    "https://raw.githubusercontent.com/damtharvey/"
    "law-school-dataset/main/law_dataset.csv"
)

KEEP_COLUMNS = [
    "lsat",
    "ugpa",
    "fulltime",
    "fam_inc",
    "racetxt",
    "tier",
    "zgpa",
    "pass_bar",
]

X_COLUMNS = ["x_lsat", "x_ugpa", "x_fulltime", "x_fam_inc", "x_tier"]
Z_COLUMN = "z_white"
Y_REG = "y_zgpa"
Y_CLS = "y_pass_bar"


def download() -> pd.DataFrame:
    response = requests.get(SOURCE_URL, timeout=30)
    response.raise_for_status()
    return pd.read_csv(io.StringIO(response.text))


def preprocess(raw: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in KEEP_COLUMNS if c not in raw.columns]
    if missing:
        raise RuntimeError(
            f"Colonnes attendues manquantes dans le CSV source : {missing}"
        )

    df = raw[KEEP_COLUMNS].copy()
    df = df.dropna()

    df[Z_COLUMN] = df["racetxt"].astype(int)
    df = df.drop(columns=["racetxt"])

    df = df.rename(
        columns={
            "lsat": "x_lsat",
            "ugpa": "x_ugpa",
            "fulltime": "x_fulltime",
            "fam_inc": "x_fam_inc",
            "tier": "x_tier",
            "zgpa": Y_REG,
            "pass_bar": Y_CLS,
        }
    )

    df["x_fulltime"] = df["x_fulltime"].astype(int)
    df[Y_CLS] = df[Y_CLS].astype(int)
    return df


def main() -> int:
    out_dir = Path(__file__).resolve().parent

    print(f"Téléchargement depuis {SOURCE_URL}")
    raw = download()
    print(f"  lignes brutes : {len(raw):,}")

    df = preprocess(raw)
    print(f"  lignes après nettoyage : {len(df):,}")
    print(f"  proportion z_white == 1 : {df[Z_COLUMN].mean():.3f}")
    print(f"  distribution y_pass_bar : {df[Y_CLS].value_counts().to_dict()}")
    print(
        f"  y_zgpa — moyenne {df[Y_REG].mean():.3f}, "
        f"std {df[Y_REG].std():.3f}, "
        f"min {df[Y_REG].min():.3f}, max {df[Y_REG].max():.3f}"
    )

    reg_cols = X_COLUMNS + [Z_COLUMN, Y_REG]
    cls_cols = X_COLUMNS + [Z_COLUMN, Y_CLS]

    reg_path = out_dir / "law_school_for_regression.csv"
    cls_path = out_dir / "law_school_for_classification.csv"

    df[reg_cols].to_csv(reg_path, index=False)
    df[cls_cols].to_csv(cls_path, index=False)

    print(f"Écrit : {reg_path.relative_to(out_dir.parent.parent)}")
    print(f"Écrit : {cls_path.relative_to(out_dir.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
