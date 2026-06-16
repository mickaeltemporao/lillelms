# Crédits des images — J2 matin

Un sous-dossier par notebook : `m1/` (module 1, perspective historique) et `m2/` (module 2, fondamentaux ML).

## Images d'ouverture

| Fichier | Sujet | Auteur | Licence | Source |
|---|---|---|---|---|
| `m1/m1-opener.jpg` | Pions de couleur devant une urne | générée par IA (ChatGPT / OpenAI), par l'intervenant | sortie OpenAI, réutilisable par son créateur | image générée par IA |
| `m2/m2-opener.jpg` | Palais de justice | cygnus921 | CC BY 2.0 | Flickr, via Openverse — `live.staticflickr.com/3893/14731880797` |

Images redimensionnées (largeur 1000 px) pour alléger le dépôt.

## Schémas de concepts (générés)

- `m1/` : `m1-symbolic.png`, `m1-ml.png`, `m1-dl.png`, `m1-transformers.png`, `m1-generative.png`
- `m2/` : `m2-feature.png`, `m2-cleaning.png`, `m2-split.png`, `m2-overfitting.png`, `m2-confusion.png`, `m2-regression.png`

Générés par [`make_schemas.py`](make_schemas.py) (matplotlib), aucune dépendance à une image externe, reproductibles :

```bash
uv run python ressources/j2/1_matin/img/make_schemas.py
```
