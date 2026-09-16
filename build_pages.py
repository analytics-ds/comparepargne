# -*- coding: utf-8 -*-
"""Genere les pages fixes : a propos et mentions legales."""
import os, json
from common import *
from linkify import linkify

PAGES = [
dict(slug="a-propos", title="Qui sommes-nous : la méthode de Comparépargne",
 desc="Qui écrit les comparatifs de Comparépargne, d'où viennent les chiffres publiés, comment les contrats sont notés et comment le site est financé.",
 h1="Qui sommes-nous", lead="Comparépargne compare les contrats d'assurance vie, les PER et les placements d'épargne longue à partir des documents contractuels publiés par les assureurs. Voici d'où viennent les chiffres, comment les contrats sont notés et où signaler une erreur.",
 blocks=[
  ("h2","Ce que nous faisons"),
  ("p","Nous lisons les conditions générales et les notes d'information des contrats du marché, nous relevons les frais ligne par ligne, nous reprenons les rendements publiés par les assureurs et nous testons le parcours de souscription. Chaque comparatif indique la date de son relevé et la source de chaque chiffre."),
  ("h2","Comment nous notons"),
  ("p","Chaque contrat reçoit une note sur 10 sur quatre critères, puis une note globale pondérée. Les frais pèsent le plus lourd, parce qu'ils sont certains alors que le rendement ne l'est pas."),
  ("ul",["<b>Fonds en euros</b> : taux servi sur les trois derniers exercices, régularité et niveau de garantie du capital",
         "<b>Frais</b> : versement, gestion, arbitrage, frais courants des supports et frais d'arrérages",
         "<b>Supports</b> : nombre, qualité et lisibilité de la gamme d'unités de compte",
         "<b>Accessibilité</b> : premier versement, délai d'ouverture, présence d'un interlocuteur, délai de versement d'un rachat"]),
  ("h2","Qui édite ce site"),
  ("p","L'éditeur du site et le directeur de la publication sont indiqués dans les <a href=\"../mentions-legales/\">mentions légales</a>. Les comparatifs publiés ici sont une information générale et ne constituent pas un conseil en investissement personnalisé."),
  ("h2","Ce que nous ne faisons pas"),
  ("p","Nous ne donnons pas de conseil en investissement personnalisé et nous ne recommandons pas de contrat au regard d'une situation individuelle. Nos comparatifs sont une information générale. Le choix d'un contrat suppose de tenir compte de votre situation patrimoniale, de vos objectifs et de votre horizon, et gagne à être discuté avec un professionnel."),
  ("h2","Corrections et signalements"),
  ("p","Un chiffre erroné se corrige et se signale. Toute correction significative est datée en bas du comparatif concerné. Pour signaler une erreur, écrivez-nous à l'adresse indiquée dans les mentions légales."),
 ]),
dict(slug="mentions-legales", title="Mentions légales de Comparépargne",
 desc="Mentions légales, éditeur, hébergeur, propriété intellectuelle, données personnelles et avertissement sur la nature des informations publiées sur Comparépargne.",
 h1="Mentions légales", lead="Informations légales relatives au site Comparépargne et avertissement sur la portée des contenus publiés.",
 blocks=[
  ("h2","Éditeur du site"),
  ("p","À compléter avant mise en ligne : dénomination sociale, forme juridique, capital, siège social, numéro SIREN, numéro de TVA intracommunautaire, directeur de la publication et adresse de contact."),
  ("h2","Hébergement"),
  ("p","À compléter avant mise en ligne : nom, raison sociale et adresse de l'hébergeur du site."),
  ("h2","Nature des informations publiées"),
  ("p","Les contenus publiés sur ce site ont une vocation d'information générale. Ils ne constituent ni un conseil en investissement, ni une recommandation personnalisée, ni une offre de souscription. Les performances passées ne préjugent pas des performances futures. Les unités de compte présentent un risque de perte en capital, supporté intégralement par le souscripteur. Les règles fiscales citées sont celles en vigueur à la date de publication de chaque article et peuvent évoluer."),
  ("h2","Sources et mise à jour"),
  ("p","Les frais proviennent des conditions générales et des notes d'information des contrats cités. Les rendements proviennent des publications annuelles des assureurs. Les règles fiscales renvoient au code général des impôts et au code des assurances. Chaque page indique sa date de dernière mise à jour."),
  ("h2","Crédits photo"),
  ("p","Les photographies publiées sur ce site proviennent d'Unsplash et sont utilisées dans les conditions de la licence Unsplash. La liste des visuels et le lien vers chaque photographie d'origine sont tenus à jour dans le fichier <code>sources_photos.json</code> du site. Les signatures des assureurs affichées dans les classements sont des repères typographiques produits par nos soins et non les logos officiels de ces sociétés."),
  ("h2","Propriété intellectuelle"),
  ("p","Les textes, tableaux, classements et visuels publiés sur ce site sont protégés. Toute reproduction, même partielle, suppose une autorisation préalable. Les noms et marques des assureurs cités appartiennent à leurs titulaires respectifs et sont utilisés à seule fin d'identification dans un cadre comparatif."),
  ("h2","Données personnelles"),
  ("p","Les adresses collectées via le formulaire d'inscription à la lettre d'information servent uniquement à l'envoi de celle-ci. Elles ne sont ni revendues ni transmises à des tiers. Vous disposez d'un droit d'accès, de rectification et de suppression, exerçable à l'adresse de contact indiquée ci-dessus."),
 ]),
]

def render(p):
    R = "../"
    body = ""
    for kind, val in p["blocks"]:
        if kind == "h2":
            body += f"<h2>{val}</h2>"
        elif kind == "p":
            body += f"<p>{val}</p>"
        elif kind == "ul":
            body += "<ul>" + "".join(f"<li>{li}</li>" for li in val) + "</ul>"
    ld = json.dumps({"@context":"https://schema.org","@type":"WebPage","name":p["title"],
                     "description":p["desc"],"url":f'{SITE}/{p["slug"]}/',"inLanguage":"fr-FR",
                     "isPartOf":{"@type":"WebSite","name":NOM,"url":SITE}}, ensure_ascii=False)
    return f'''<!doctype html>
<html lang="fr">
<head>
{head(R, p["title"], p["desc"], canonical=f'{SITE}/{p["slug"]}/', extra='<script type="application/ld+json">' + ld + '</script>')}</head>
<body>

{header(R, scrolled=True)}

<section class="art-head" style="padding-top:120px">
  <div class="wrap">
    <div class="art-card">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="{R}">Accueil</a><i></i><span>{p["h1"]}</span></nav>
      <h1>{p["h1"]}</h1>
      <p class="art-lead">{p["lead"]}</p>
    </div>
  </div>
</section>

<section class="art-body">
  <div class="wrap">
    <article class="prose" style="max-width:820px;margin:0 auto">
      {body}
      {DISCLOSURE}
    </article>
  </div>
</section>

{footer(R)}

<script src="{R}assets/js/site.js?v=1"></script>
</body>
</html>
'''

if __name__ == "__main__":
    for p in PAGES:
        os.makedirs(p["slug"], exist_ok=True)
        open(os.path.join(p["slug"], "index.html"), "w", encoding="utf-8").write(linkify(render(p), "../"))
        print("ok", p["slug"])
