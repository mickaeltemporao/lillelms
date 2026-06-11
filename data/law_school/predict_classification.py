"""Génère et sauvegarde les prédictions de classification (`y_pass_bar`) sur Law School.

Point de départ « clé en main » pour la séance fairness : un modèle simple
(régression logistique sur les features `x_*`, **sans** l'attribut sensible
`z_white`) est entraîné sur le train, puis ses prédictions et ses probabilités
sont écrites pour le train et le test, en conservant `z_white` et la vérité
terrain pour les analyses de fairness (parité, equalized odds, etc.).

Lancer :  uv run python data/law_school/predict_classification.py
Sortie :  data/law_school/output/predictions_classification_{train,test}.csv

Déterministe : mêmes CSV d'entrée + modèle déterministe => mêmes prédictions.
"""
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

HERE = Path(__file__).resolve().parent
OUT = HERE / "output"

FEATURES = ["x_lsat", "x_ugpa", "x_fulltime", "x_fam_inc", "x_tier"]
TARGET = "y_pass_bar"
SENSITIVE = "z_white"


def main() -> int:
    OUT.mkdir(exist_ok=True)
    train = pd.read_csv(HERE / "law_school_for_classification_train.csv")
    test = pd.read_csv(HERE / "law_school_for_classification_test.csv")

    # On n'entraîne QUE sur les features x_* : z_white n'est jamais une feature.
    model = LogisticRegression(max_iter=1000)
    model.fit(train[FEATURES], train[TARGET])

    for split, df in [("train", train), ("test", test)]:
        proba = model.predict_proba(df[FEATURES])[:, 1]
        pred = model.predict(df[FEATURES])

        out = df.copy()
        out.insert(0, "id", range(len(out)))
        out["y_pred"] = pred
        out["y_proba_pass"] = proba.round(6)

        path = OUT / f"predictions_classification_{split}.csv"
        out.to_csv(path, index=False)
        acc = accuracy_score(df[TARGET], pred)
        print(f"{split:>5} : {len(out):>6} lignes, accuracy {acc:.3f} "
              f"-> {path.relative_to(HERE.parent.parent)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
