# -*- coding: utf-8 -*-
"""Genere les articles de Comparepargne, GEO friendly.

Structure d'un article : encart En bref (reponse directe), sommaire, sections H2 avec
listes et tableaux, podium, verdict, methodologie, FAQ, articles lies, mention
d'information, et les donnees structurees Article + FAQPage + ItemList + BreadcrumbList.

Le contenu vit dans contenus.py, ce fichier ne porte que le rendu.

Usage : python3 build_articles.py  (depuis le dossier comparepargne)
"""
import os, json, re
from common import *
from linkify import linkify
from contenus import ARTICLES

def strip(t):
    return re.sub(r"<[^>]+>", "", t).replace("&amp;", "&").replace("&nbsp;", " ").strip()

def render_table(t, R):
    head = "".join(f"<th>{h}</th>" for h in t["head"])
    rows = ""
    for r in t["rows"]:
        best = len(r) > len(t["head"]) and r[-1] == 1
        cells = r[:len(t["head"])]
        tds = ""
        for i, c in enumerate(cells):
            if i == 0:
                badge = "<span class='badge'>Notre choix</span>" if best else ""
                tds += f'<td class="brand">{c}{badge}</td>'
            elif i == 1 and "Note" in t["head"][1]:
                tds += f'<td class="note{" best" if best else ""}">{c}</td>'
            else:
                tds += f"<td>{c}</td>"
        rows += f"<tr>{tds}</tr>"
    note = f'<div class="table-note">{t["note"]}</div>' if t.get("note") else ""
    return f'<div class="table-wrap"><div class="table-scroll"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>{note}</div>'

def render_podium(a, R):
    out = ""
    for i, (logo, name, label, detail, score) in enumerate(a["podium"]):
        out += (f'<div class="pod{" first" if i==0 else ""}"><span class="rank">0{i+1}</span>'
                f'<img src="{R}assets/logos/{logo}.svg" alt="{strip(name)}" width="120" height="33">'
                f'<b>{label}</b><span>{detail}</span>'
                f'<span class="sc">{score}<span style="font-size:13px;opacity:.6">/10</span></span></div>')
    return f'<div class="podium">{out}</div>'

def render_body(a, R):
    html = ""
    for s in a["sections"]:
        html += f'<h2 id="{s["id"]}">{s["h2"]}</h2>'
        for kind, val in s["body"]:
            if kind == "p":
                html += f"<p>{val}</p>"
            elif kind == "h3":
                html += f"<h3>{val}</h3>"
            elif kind == "ul":
                html += "<ul>" + "".join(f"<li>{li}</li>" for li in val) + "</ul>"
            elif kind == "ol":
                html += "<ol>" + "".join(f"<li>{li}</li>" for li in val) + "</ol>"
            elif kind == "img":
                html += (f'<figure><img src="{R}assets/img/{val["src"]}" alt="{val["alt"]}" '
                         f'width="1200" height="700" loading="lazy"><figcaption>{val["cap"]}</figcaption></figure>')
            elif kind == "quote":
                html += f"<blockquote><p>{val}</p></blockquote>"
            elif kind == "table":
                html += render_table(a["table"], R)
            elif kind == "table2":
                html += render_table(val, R)
            elif kind == "podium":
                html += render_podium(a, R)
    return html

def jsonld(a):
    url = f'{SITE}/{a["cat"]}/{a["slug"]}/'
    art = {
      "@context": "https://schema.org", "@type": "Article",
      "headline": strip(a["title"]), "description": strip(a["desc"]),
      "datePublished": a["date"], "dateModified": a["date"],
      "inLanguage": "fr-FR", "mainEntityOfPage": {"@type": "WebPage", "@id": url},
      "image": f'{SITE}/assets/img/{a["img"]}',
      "author": {"@type": "Organization", "name": NOM, "url": SITE},
      "publisher": {"@type": "Organization", "name": NOM, "url": SITE,
                    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo/logo.svg"}},
      "articleSection": CATS[a["cat"]]["nom"],
    }
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
      "mainEntity": [{"@type": "Question", "name": strip(q),
        "acceptedAnswer": {"@type": "Answer", "text": strip(r)}} for q, r in a["faq"]]}
    items = {"@context": "https://schema.org", "@type": "ItemList",
      "name": strip(a["title"]), "itemListOrder": "https://schema.org/ItemListOrderDescending",
      "numberOfItems": len(a["table"]["rows"]),
      "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": strip(r[0]),
        "description": f'Note {r[1]}/10. {strip(r[-2])}.'} for i, r in enumerate(a["table"]["rows"])]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE},
      {"@type": "ListItem", "position": 2, "name": CATS[a["cat"]]["nom"], "item": f'{SITE}/{a["cat"]}/'},
      {"@type": "ListItem", "position": 3, "name": strip(a["h1"])}]}
    return "".join('<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>\n"
                   for d in (art, faq, items, crumbs))

METHODE = '''      <div class="method-box">
        <h2>Notre méthode</h2>
        <p>Ce comparatif repose sur des documents publics, vérifiables un par un.</p>
        <ul>
          <li>Les frais sont relevés dans les conditions générales et la note d'information de chaque contrat, pas sur la page commerciale</li>
          <li>Les rendements sont ceux publiés par l'assureur au titre du dernier exercice clos, nets de frais de gestion et bruts de prélèvements sociaux</li>
          <li>Les règles fiscales citées renvoient au code général des impôts et au code des assurances en vigueur à la date de mise à jour</li>
          <li>Le parcours de souscription est testé sur chaque contrat : premier versement, délai d'ouverture, délai de versement d'un rachat partiel</li>
          <li>Aucun assureur ne finance ce comparatif, ne nous rémunère et ne le relit avant publication. Nous ne distribuons aucun contrat</li>
        </ul>
      </div>'''

def render(a):
    R = "../../"
    toc = "".join(f'<li><a href="#{s["id"]}">{strip(s["h2"])}</a></li>' for s in a["sections"])
    brief = "".join(f"<li>{b}</li>" for b in a["brief"])
    faq = "".join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{r}</p></details>'
                  for i, (q, r) in enumerate(a["faq"]))
    verdict = "".join(f"<p>{p}</p>" for p in a["verdict"]["body"])
    related = "".join(
        f'<a class="post big" href="#"><img src="{R}assets/img/{img}" alt="" width="800" height="560" loading="lazy">'
        f'<div class="post-body"><span class="eyebrow">{k}</span><h3>{t}</h3></div></a>'
        for c, img, k, t in a["related"])
    win_logo, win_name, win_label, win_detail, win_score = a["podium"][0]
    nom_cat = CATS[a["cat"]]["nom"]
    return f'''<!doctype html>
<html lang="fr">
<head>
{head(R, a["title"], a["desc"], canonical=f'{SITE}/{a["cat"]}/{a["slug"]}/', extra=jsonld(a))}<meta property="og:type" content="article">
</head>
<body>

{header(R, current=a["cat"], scrolled=True)}

<section class="art-hero">
  <img src="{R}assets/img/{a["img"]}" alt="{a["img_alt"]}" width="1300" height="731" fetchpriority="high">
</section>

<section class="art-head">
  <div class="wrap">
    <div class="art-card">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="{R}">Accueil</a><i></i><a href="{R}{a["cat"]}/">{nom_cat}</a><i></i><span>{strip(a["h1"])}</span></nav>
      <h1>{a["h1"]}</h1>
      <p class="art-lead">{a["lead"]}</p>
      <div class="art-meta">
        <span class="art-author"><span>C</span><b>La rédaction {NOM}</b></span>
        <span>Mis à jour le <b>{a["date_fr"]}</b></span>
        <span><b>{a["reading"]} min</b> de lecture</span>
        <span><b>{a["nb"]}</b> {a["nb_label"]}</span>
      </div>
    </div>
  </div>
</section>

<section class="art-body">
  <div class="wrap art-cols">
    <article class="prose">

      <div class="brief">
        <h2>En bref</h2>
        <p class="answer">{a["brief_answer"]}</p>
        <ul>{brief}</ul>
      </div>

      <details class="toc">
        <summary>Sommaire</summary>
        <ol>{toc}</ol>
      </details>

      {render_body(a, R)}

      <div class="verdict-box">
        <h2>{a["verdict"]["h2"]}</h2>
        {verdict}
      </div>

      <h2 id="faq">Questions fréquentes</h2>
      <div class="faq" style="padding:0">{faq}</div>

{METHODE}

      {DISCLOSURE}
    </article>

    <aside class="aside">
      <div class="aside-card">
        <h3>Notre choix</h3>
        <div class="aside-win"><img src="{R}assets/logos/{win_logo}.svg" alt="{strip(win_name)}" width="120" height="33"><b>{win_score}</b></div>
        <p>{win_label}. {win_detail}.</p>
        <a class="btn btn-dark" href="{R}#outil" style="width:100%;justify-content:center">Comparer 2 contrats</a>
      </div>
      <div class="aside-card">
        <h3>Dans ce dossier</h3>
        <div class="aside-links">{"".join(f'<a href="#{s["id"]}">{strip(s["h2"])}</a>' for s in a["sections"])}<a href="#faq">Questions fréquentes</a></div>
      </div>
      <div class="aside-card dark">
        <h3>Simulateur</h3>
        <p>Capital, versement mensuel, durée et frais : ce que votre épargne produit sur la période.</p>
        <a class="btn btn-accent" href="{R}#simulateur" style="width:100%;justify-content:center">Lancer le calcul</a>
      </div>
    </aside>
  </div>
</section>

<section class="related">
  <div class="wrap">
    <div class="section-head"><h2>À lire ensuite</h2><a class="btn btn-ghost" href="{R}{a["cat"]}/">Tous les dossiers {nom_cat.lower()}</a></div>
    <div class="grid3">{related}</div>
  </div>
</section>

{footer(R)}

<script src="{R}assets/js/site.js?v=1"></script>
</body>
</html>
'''

if __name__ == "__main__":
    for a in ARTICLES:
        d = os.path.join(a["cat"], a["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(linkify(render(a), "../../"))
        print("ok", d)
