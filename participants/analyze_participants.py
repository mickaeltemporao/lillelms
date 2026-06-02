"""Analyse des participants à l'école d'été QuantiLille 2026.

Lit le CSV de sélection, calcule des stats descriptives et utilise Claude
(Haiku 4.5) pour synthétiser les champs texte libre. Écrit le rapport
markdown `analyse_des_participants.md` dans le même dossier.
"""

from __future__ import annotations

import os
import sys
from collections import Counter
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
PARTICIPANTS_DIR = Path(__file__).resolve().parent
CSV_PATH = PARTICIPANTS_DIR / "MaJ_QL26_Selection_IA_2026_05_11.csv"
OUTPUT_PATH = PARTICIPANTS_DIR / "analyse_des_participants.md"

MODEL = "claude-haiku-4-5-20251001"
CURRENT_YEAR = 2026

COL = {
    "tarif": 3,
    "selection": 4,
    "nom": 5,
    "prenom": 6,
    "themes": 8,
    "enquetes_yn": 9,
    "enquetes": 10,
    "soft_python": 11,
    "soft_r": 12,
    "soft_sas": 13,
    "soft_spss": 14,
    "soft_stata": 15,
    "soft_jamovi": 16,
    "soft_autres": 17,
    "soft_aucun": 18,
    "autres_logiciels": 20,
    "annee_naissance": 21,
    "universite": 25,
    "unite_recherche": 26,
    "discipline": 29,
    "discipline_autre": 30,
    "commentaires": 45,
}

SOFTWARE_LABELS = {
    "soft_python": "Python",
    "soft_r": "R",
    "soft_sas": "SAS",
    "soft_spss": "SPSS / PSPP",
    "soft_stata": "Stata",
    "soft_jamovi": "JAMOVI / JASP",
    "soft_autres": "Autres",
    "soft_aucun": "Aucun",
}


def get(row, key, default=""):
    val = row.iloc[COL[key]]
    if pd.isna(val):
        return default
    return str(val).strip()


def is_yes(row, key):
    return get(row, key).lower() == "oui"


def load_data() -> pd.DataFrame:
    return pd.read_csv(CSV_PATH)


def descriptive_stats(df: pd.DataFrame) -> dict:
    stats = {"total": len(df)}

    stats["selection"] = Counter(df.iloc[:, COL["selection"]].fillna("(vide)"))
    stats["disciplines"] = Counter(df.iloc[:, COL["discipline"]].fillna("(non renseigné)"))

    years = pd.to_numeric(df.iloc[:, COL["annee_naissance"]], errors="coerce")
    ages = (CURRENT_YEAR - years).dropna()
    age_groups = Counter()
    for a in ages:
        decade = int(a // 10) * 10
        age_groups[f"{decade}-{decade + 9} ans"] += 1
    stats["age_groups"] = age_groups
    stats["age_min"] = int(ages.min()) if len(ages) else None
    stats["age_max"] = int(ages.max()) if len(ages) else None
    stats["age_median"] = int(ages.median()) if len(ages) else None
    stats["age_missing"] = int(years.isna().sum())

    softs = {}
    for key, label in SOFTWARE_LABELS.items():
        col = df.iloc[:, COL[key]].fillna("").astype(str).str.strip().str.lower()
        softs[label] = int((col == "oui").sum())
    stats["softwares"] = softs

    stats["universities"] = Counter(df.iloc[:, COL["universite"]].fillna("(non renseigné)"))

    return stats


def build_records(df: pd.DataFrame) -> list[dict]:
    records = []
    for _, row in df.iterrows():
        records.append(
            {
                "prenom": get(row, "prenom"),
                "nom": get(row, "nom"),
                "universite": get(row, "universite"),
                "unite": get(row, "unite_recherche"),
                "discipline": get(row, "discipline") or get(row, "discipline_autre"),
                "themes": get(row, "themes"),
                "enquetes": get(row, "enquetes"),
                "autres_logiciels": get(row, "autres_logiciels"),
                "commentaires": get(row, "commentaires"),
                "selection": get(row, "selection"),
                "python_oui": is_yes(row, "soft_python"),
                "r_oui": is_yes(row, "soft_r"),
                "aucun_oui": is_yes(row, "soft_aucun"),
            }
        )
    return records


def _strip_leading_headers(text: str) -> str:
    """Retire les titres markdown H1/H2 en début de réponse (parfois ajoutés
    par le LLM malgré l'instruction). Le rendu du rapport gère ses propres titres."""
    lines = text.splitlines()
    while lines and (lines[0].lstrip().startswith(("# ", "## ")) or not lines[0].strip()):
        lines.pop(0)
    return "\n".join(lines).strip()


def call_llm(client, prompt: str, max_tokens: int = 4096) -> str:
    system = (
        "Tu es un assistant pédagogique qui aide une équipe d'enseignants à préparer "
        "une école d'été en sciences sociales sur les IA génératives. Tu produis des "
        "synthèses concises, factuelles, en français, en markdown."
    )
    msg = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def analyze_text_globally(client, records: list[dict]) -> dict:
    themes_block = "\n\n".join(
        f"[{i + 1}] ({r['discipline'] or '?'}) {r['themes']}"
        for i, r in enumerate(records)
        if r["themes"]
    )
    enquetes_block = "\n\n".join(
        f"[{i + 1}] {r['enquetes']}"
        for i, r in enumerate(records)
        if r["enquetes"]
    )
    commentaires_block = "\n\n".join(
        f"[{i + 1}] {r['commentaires']}"
        for i, r in enumerate(records)
        if r["commentaires"] and r["commentaires"].lower() != "nan"
    )

    motivations = call_llm(
        client,
        f"""Voici les thèmes de recherche et motivations exprimés par les {len(records)} stagiaires :

{themes_block}

Produis 4 paragraphes courts en français, **sans titre principal**, **sans listes à puces**, **sans citer de participants spécifiques**. Chaque paragraphe commence par son intitulé en gras suivi d'un point :

**Grands axes de motivation.** 2-4 phrases résumant les principaux motifs d'inscription observés dans le groupe.

**Clusters thématiques de recherche.** 2-4 phrases regroupant les thématiques en quelques grandes familles.

**Types de données mentionnées.** 2-4 phrases résumant les natures de données évoquées (textuelles, quantitatives, audiovisuelles, archives, etc.), sans décompte précis.

**Exposition préalable aux IA génératives.** 2-4 phrases sur le niveau global d'exposition du groupe (proportion approximative d'expérimentés / ponctuels / novices) et les usages mentionnés.

Sois concis, factuel, synthétique.""",
    )

    enquetes = call_llm(
        client,
        f"""Voici les enquêtes / données déjà analysées par les stagiaires :

{enquetes_block}

Produis 2 paragraphes courts en français, **sans titre principal**, **sans listes à puces**, chaque paragraphe commençant par son intitulé en gras suivi d'un point :

**Types d'enquêtes et de données récurrents.** Une à deux phrases résumant les principaux types observés.

**Méthodologies dominantes.** Un paragraphe court (3-5 phrases) résumant les approches (quantitatif / qualitatif / mixte) et les logiciels couramment cités.""",
    )

    pedago = call_llm(
        client,
        f"""Voici les motivations brutes des {len(records)} stagiaires :

{themes_block}

Et leurs commentaires supplémentaires :

{commentaires_block or '(aucun commentaire)'}

Produis une **synthèse pédagogique succincte** à destination des 4 intervenants : ce qu'il faut retenir du groupe pour bien calibrer la formation — hétérogénéité, attentes saillantes, pièges à éviter, 2-3 exemples qui résonneront avec le groupe.

Format : un seul bloc de 4 à 6 phrases maximum, en prose. **Pas de titre, pas de tableau, pas de liste à puces.**""",
        max_tokens=1024,
    )

    return {
        "motivations": _strip_leading_headers(motivations),
        "enquetes": _strip_leading_headers(enquetes),
        "pedago": _strip_leading_headers(pedago),
    }


def one_line_per_participant(client, records: list[dict]) -> dict[int, str]:
    block = "\n\n".join(
        f"[{i + 1}] {r['prenom']} {r['nom']} | {r['discipline'] or '?'} | "
        f"{(r['themes'] or '(pas de thèmes renseignés)')[:600]}"
        for i, r in enumerate(records)
    )
    text = call_llm(
        client,
        f"""Pour chacun des {len(records)} stagiaires ci-dessous, produis UNE phrase (maximum 25 mots) résumant ses thématiques de recherche et motivations principales.

Format de sortie STRICT : une ligne par participant, sous la forme exacte :
[N] résumé en une phrase

Ne saute aucun numéro. N'écris RIEN d'autre que ces lignes numérotées.

{block}""",
        max_tokens=4096,
    )

    summaries: dict[int, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("["):
            continue
        try:
            num_str, summary = line.split("]", 1)
            num = int(num_str.strip("[ "))
            summaries[num] = summary.strip(" :-—")
        except (ValueError, IndexError):
            continue
    return summaries


def render_markdown(stats: dict, llm_results: dict, records: list[dict], summaries: dict[int, str], has_llm: bool) -> str:
    out: list[str] = []
    a = out.append
    total = stats["total"]

    a("# Analyse des participants — QuantiLille 2026")
    a("")
    a("Module *Exploration et Applications des IA Génératives en Sciences Sociales* — 22-26 juin 2026.")
    a("")
    a("Ce rapport est généré automatiquement par `participants/analyze_participants.py` "
      "à partir du fichier `MaJ_QL26_Selection_IA_2026_05_11.csv`.")
    a("")

    a("## 1. Vue d'ensemble")
    a("")
    a(f"- **Total de candidatures dans le fichier** : {total}")
    for k, v in stats["selection"].most_common():
        a(f"- {k} : {v}")
    a("")

    a("## 2. Profil démographique")
    a("")
    if stats["age_median"] is not None:
        a(f"Âges (calculés depuis l'année de naissance) : médiane **{stats['age_median']} ans** "
          f"(min {stats['age_min']}, max {stats['age_max']}).")
    if stats["age_missing"]:
        a(f"Année de naissance non renseignée pour {stats['age_missing']} participant·e·s.")
    a("")
    a("| Tranche d'âge | Nombre |")
    a("|---|---|")
    for grp in sorted(stats["age_groups"].keys()):
        a(f"| {grp} | {stats['age_groups'][grp]} |")
    a("")

    a("## 3. Répartition disciplinaire")
    a("")
    a("| Discipline | Nombre |")
    a("|---|---|")
    for d, n in stats["disciplines"].most_common():
        a(f"| {d} | {n} |")
    a("")

    a("## 4. Compétences techniques (auto-déclarées)")
    a("")
    a("| Logiciel | Utilisateurs (Oui) | % du groupe |")
    a("|---|---|---|")
    for label, n in stats["softwares"].items():
        pct = (n / total * 100) if total else 0
        a(f"| {label} | {n} | {pct:.0f}% |")
    a("")
    a("> **Pour l'équipe pédagogique :** une majorité du groupe ne se déclare pas utilisatrice "
      "de Python ; R est nettement plus représenté. Le démarrage lundi/mardi doit accepter cette asymétrie.")
    a("")

    a("## 5. Universités représentées")
    a("")
    a("| Université | Nombre |")
    a("|---|---|")
    for u, n in sorted(stats["universities"].items(), key=lambda x: (-x[1], x[0])):
        a(f"| {u} | {n} |")
    a("")

    if has_llm:
        a("## 6. Synthèse des champs texte libre (analyse LLM)")
        a("")
        a("### 6.1. Motivations et thématiques de recherche")
        a("")
        a(llm_results["motivations"])
        a("")
        a("### 6.2. Données et enquêtes déjà manipulées")
        a("")
        a(llm_results["enquetes"])
        a("")
        a("### 6.3. Synthèse pédagogique pour les 4 intervenants")
        a("")
        a(llm_results["pedago"])
        a("")
    else:
        a("## 6. Synthèse des champs texte libre")
        a("")
        a("> ⚠ Analyse LLM non générée (`ANTHROPIC_API_KEY` absente). "
          "Voir `.env.example` à la racine du repo et relancer.")
        a("")

    a("## 7. Tour de table — fiche par participant")
    a("")
    a("Tableau prêt pour l'accueil du lundi matin. Une ligne par participant·e, dans l'ordre du CSV.")
    a("")
    a("| # | Prénom Nom | Université | Discipline | Python | R | Thématique en 1 ligne |")
    a("|---|---|---|---|---|---|---|")
    for i, r in enumerate(records):
        num = i + 1
        py = "✓" if r["python_oui"] else ""
        rr = "✓" if r["r_oui"] else ""
        if has_llm:
            summary = summaries.get(num, "_(résumé LLM manquant)_")
        else:
            summary = "_(synthèse LLM désactivée)_"
        nom_complet = f"{r['prenom']} {r['nom']}".strip()
        univ = r["universite"] or "?"
        disc = r["discipline"] or "?"
        if r["selection"].lower() == "desistement":
            nom_complet += " *(désistement)*"
        a(f"| {num} | {nom_complet} | {univ} | {disc} | {py} | {rr} | {summary} |")
    a("")

    a("---")
    a("*Ce rapport contient des données personnelles (noms, prénoms, affiliations) — usage interne pédagogique uniquement.*")
    a("")

    return "\n".join(out)


def main() -> int:
    load_dotenv(REPO_ROOT / ".env")

    if not CSV_PATH.exists():
        print(f"✗ CSV introuvable : {CSV_PATH}", file=sys.stderr)
        return 1

    df = load_data()
    stats = descriptive_stats(df)
    records = build_records(df)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    has_llm = bool(api_key) and not api_key.startswith("sk-ant-...")

    llm_results: dict = {}
    summaries: dict[int, str] = {}

    if has_llm:
        from anthropic import Anthropic

        client = Anthropic(api_key=api_key)
        print("→ Analyses LLM en cours (Claude Haiku 4.5)…")
        llm_results = analyze_text_globally(client, records)
        print("  ✓ synthèses globales générées")
        summaries = one_line_per_participant(client, records)
        print(f"  ✓ résumés individuels générés ({len(summaries)}/{len(records)})")
    else:
        print("⚠ ANTHROPIC_API_KEY absente — analyse LLM ignorée (rapport descriptif uniquement).")

    OUTPUT_PATH.write_text(
        render_markdown(stats, llm_results, records, summaries, has_llm),
        encoding="utf-8",
    )
    print(f"✓ Rapport écrit : {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
