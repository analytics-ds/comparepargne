# Comparépargne

Média comparateur indépendant de l'assurance vie, du PER et de l'épargne longue.
Site statique, sans dépendance ni build : les pages HTML sont générées par des
scripts Python et servies telles quelles.

Construit sur le modèle du média Comparamode, avec le corpus GGVIE (50 mots-clés,
5 clusters, relevés ChatGPT / Gemini / AI Overviews de `AO/ggvie-geo`) comme carte
éditoriale.

## Structure

| Chemin | Rôle |
|---|---|
| `index.html` | Accueil : hero, bandeau assureurs, comparateur de 2 contrats, simulateur d'épargne, classement, méthode |
| `assurance-vie/`, `rendement-frais/`, `fiscalite-succession/`, `per-retraite/`, `epargne-responsable/` | Pages catégorie |
| `<catégorie>/<slug>/` | Articles comparatifs (11 publiés) |
| `a-propos/`, `mentions-legales/` | Pages fixes |
| `assets/css/site.css` | Feuille de style unique |
| `assets/js/site.js` | Zoom du hero, bandeau défilant, header au scroll |
| `assets/img/`, `assets/logos/`, `assets/logo/` | Visuels SVG générés, signatures des assureurs, logo du site |

## Régénérer le site

```bash
python3 build_all.py       # accueil + catégories + articles + pages fixes + sitemap
```

Ou script par script : `build_home.py`, `build_categories.py`, `build_articles.py`,
`build_pages.py`, `build_sitemap.py`. Les visuels se régénèrent avec `gen_assets.py`.

Le contenu des articles vit dans `contenus_*.py`, une rubrique par fichier, assemblés
par `contenus.py`. `common.py` porte l'en-tête, le menu, le pied de page et la mention
d'information. `linkify.py` branche les liens internes : un lien reste en `#` tant que
l'article correspondant n'existe pas, ce qui évite les liens morts.

## Avant mise en ligne publique

1. **Remplacer les chiffres du panel par des relevés réels.** Les notes, frais, rendements
   et montants publiés sont des valeurs de démonstration construites sur des ordres de
   grandeur de marché. Sur un sujet financier, ils doivent être relevés contrat par contrat
   dans les conditions générales avant toute publication.
2. **Vérifier les règles fiscales à la date de publication** (abattements, taux du
   prélèvement forfaitaire, taux des prélèvements sociaux, seuil de 150 000 €).
3. **Remplacer les signatures d'assureurs** de `assets/logos/` par les logos officiels si
   les droits sont obtenus, ou les conserver telles quelles : ce sont de simples
   signatures typographiques produites par `gen_assets.py`.
4. **Compléter les mentions légales** : éditeur, directeur de publication, hébergeur, contact.
5. **Mettre `SITE` dans `common.py`** sur le domaine définitif, puis `python3 build_all.py`.

## Développement local

```bash
python3 -m http.server 8791
```
