# Comparépargne

Média comparateur de l'assurance vie, du PER et de l'épargne longue, aux couleurs de Groupama Gan Vie.
Site statique, sans dépendance ni build : les pages HTML sont générées par des
scripts Python et servies telles quelles. Titres en Bricolage Grotesque, texte en Inter,
photographies Unsplash.

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
| `assets/img/*.jpg` | Photographies Unsplash, téléchargées par `gen_photos.py` |
| `assets/logos/` | Logos officiels des assureurs + `neutre.svg`, origines dans `sources_logos.json` |
| `assets/img/sub-*.svg`, `assets/logo/` | Icônes et logo du site (`gen_assets.py`) |
| `sources_photos.json` | Une entrée par visuel : URL source, dimensions, recadrage, lien de crédit |

## Régénérer le site

```bash
python3 build_all.py       # accueil + catégories + articles + pages fixes + sitemap
```

Ou script par script : `build_home.py`, `build_categories.py`, `build_articles.py`,
`build_pages.py`, `build_sitemap.py`. Les photos se retéléchargent avec `python3 gen_photos.py`, le vectoriel avec `python3 gen_assets.py`.

Le contenu des articles vit dans `contenus_*.py`, une rubrique par fichier, assemblés
par `contenus.py`. `common.py` porte l'en-tête, le menu, le pied de page et la mention
d'information. `linkify.py` branche les liens internes : un lien reste en `#` tant que
l'article correspondant n'existe pas, ce qui évite les liens morts.

## Avant mise en ligne publique

1. **Décider de la ligne éditeur.** Le classement place Groupama Gan Vie en tête sur les
   cinq rubriques, avec le logo de la marque. Les affirmations d'indépendance (« aucun
   assureur ne finance ce comparatif ») ont donc été retirées du site : elles seraient
   fausses. Reste à trancher qui est déclaré éditeur dans les mentions légales.
2. **Remplacer les chiffres du panel par des relevés réels.** Les notes, frais, rendements
   et montants publiés sont des valeurs de démonstration construites sur des ordres de
   grandeur de marché. Sur un sujet financier, ils doivent être relevés contrat par contrat
   dans les conditions générales avant toute publication.
3. **Vérifier les règles fiscales à la date de publication** (abattements, taux du
   prélèvement forfaitaire, taux des prélèvements sociaux, seuil de 150 000 €).
4. **Logos des assureurs.** `assets/logos/` contient les logos officiels, récupérés sur
   Wikimedia Commons ou sur le site de chaque marque, avec leur origine dans
   `sources_logos.json`. Ils sont reproduits pour identifier les contrats comparés.
   `neutre.svg` sert aux lignes génériques (Livret A, contrat bancaire moyen) qui ne
   doivent porter le logo d'aucune marque réelle. Le logo GGVIE est affiché en couleur,
   les concurrents en niveaux de gris.
5. **Vérifier les crédits photo.** Les photographies viennent d'Unsplash et sont utilisées
   sous licence Unsplash. `sources_photos.json` garde le lien vers chaque photo d'origine.
6. **Compléter les mentions légales** : éditeur, directeur de publication, hébergeur, contact.
7. **Mettre `SITE` dans `common.py`** sur le domaine définitif, puis `python3 build_all.py`.

## Développement local

```bash
python3 -m http.server 8791
```
