"""Récupère le dataset Law School et écrit quatre CSV pré-traités (train/test).

Source : https://github.com/damtharvey/law-school-dataset

Sorties (à côté de ce script) :
- law_school_for_regression_train.csv     : 75 % - features x_* + sensible z_white + cible y_zgpa
- law_school_for_regression_test.csv      : 25 % - mêmes colonnes
- law_school_for_classification_train.csv : 75 % - features x_* + sensible z_white + cible y_pass_bar
- law_school_for_classification_test.csv  : 25 % - mêmes colonnes

Le même split train/test (indices identiques) est appliqué aux deux tâches :
un·e étudiant·e qui est dans le train pour la régression est aussi dans le
train pour la classification.

Voir codebook.md pour la sémantique de chaque colonne et le détail du split.
"""

from __future__ import annotations

import io
import sys
from pathlib import Path

import pandas as pd
import requests
from sklearn.model_selection import train_test_split

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

TEST_SIZE = 0.25
SEED = 42


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
        f"  y_zgpa moyenne {df[Y_REG].mean():.3f}, "
        f"std {df[Y_REG].std():.3f}, "
        f"min {df[Y_REG].min():.3f}, max {df[Y_REG].max():.3f}"
    )

    train_df, test_df = train_test_split(
        df, test_size=TEST_SIZE, random_state=SEED, shuffle=True
    )
    print(
        f"Split train/test (seed={SEED}, test_size={TEST_SIZE}) : "
        f"{len(train_df):,} train / {len(test_df):,} test"
    )

    reg_cols = X_COLUMNS + [Z_COLUMN, Y_REG]
    cls_cols = X_COLUMNS + [Z_COLUMN, Y_CLS]

    targets = [
        ("law_school_for_regression_train.csv", train_df[reg_cols]),
        ("law_school_for_regression_test.csv", test_df[reg_cols]),
        ("law_school_for_classification_train.csv", train_df[cls_cols]),
        ("law_school_for_classification_test.csv", test_df[cls_cols]),
    ]

    for name, frame in targets:
        path = out_dir / name
        frame.to_csv(path, index=False)
        print(f"Écrit : {path.relative_to(out_dir.parent.parent)} ({len(frame):,} lignes)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
