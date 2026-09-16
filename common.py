# -*- coding: utf-8 -*-
"""Briques partagees par les trois generateurs : en-tete, menu, pied de page, mentions.

Un seul endroit pour le menu et le pied de page : si une categorie change de nom,
elle change partout.
"""

SITE = "https://analytics-ds.github.io/comparepargne"  # domaine reel a brancher avant mise en ligne
NOM = "Comparépargne"
BASELINE = "Le comparateur indépendant de l'assurance vie, du PER et de l'épargne longue."

CATS = {
 "assurance-vie":        dict(menu="Assurance vie",  nom="Assurance vie"),
 "rendement-frais":      dict(menu="Rendement",      nom="Rendement et frais"),
 "fiscalite-succession": dict(menu="Fiscalité",      nom="Fiscalité et succession"),
 "per-retraite":         dict(menu="Retraite",       nom="PER et retraite"),
 "epargne-responsable":  dict(menu="Épargne responsable", nom="Épargne responsable"),
}

ICON_SEARCH = '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M16 16l5 5"/></svg>'
BURGER = ('<svg width="22" height="14" viewBox="0 0 22 14" fill="none" stroke="#111" stroke-width="1.7">'
          '<path d="M0 1h22M0 7h22M0 13h22"/></svg>')
ARROW = '<svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1'
         '&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')

def head(R, title, desc, canonical=None, extra=""):
    can = f'\n<link rel="canonical" href="{canonical}">' if canonical else ""
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{can}
<meta property="og:site_name" content="{NOM}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
{FONTS}
<link rel="icon" href="{R}assets/logo/favicon.svg" type="image/svg+xml">
<meta name="theme-color" content="#0D1A14">
<link rel="stylesheet" href="{R}assets/css/site.css?v=1">
{extra}'''

def header(R, current=None, scrolled=False):
    menu = "".join(
      f'      <li><a href="{R}{s}/"' +
      (' style="text-decoration:underline;text-underline-offset:6px"' if s == current else '') +
      f'>{c["menu"]}</a></li>\n' for s, c in CATS.items())
    return f'''<header{' class="scrolled"' if scrolled else ''}>
  <div class="wrap nav">
    <a class="logo" href="{R or './'}" aria-label="{NOM}, accueil"><img class="l-light" src="{R}assets/logo/logo-light.svg" alt="{NOM}" width="620" height="133"><img class="l-dark" src="{R}assets/logo/logo.svg" alt="" aria-hidden="true" width="620" height="133"></a>
    <ul class="menu">
{menu}    </ul>
    <div class="nav-actions">
      <a class="iconbtn" href="{R}#outil" aria-label="Rechercher">{ICON_SEARCH}</a>
      <a class="btn btn-dark" href="{R}#outil">Comparer 2 contrats</a>
      <button class="burger" aria-label="Menu">{BURGER}</button>
    </div>
  </div>
</header>'''

def newsletter(titre="Recevez chaque comparatif d'épargne avant tout le monde"):
    return f'''<section class="news" id="newsletter">
  <div class="wrap">
    <div class="news-card">
      <div>
        <h2>{titre}</h2>
        <p>Un email par mois : les rendements servis dès leur publication, les hausses de frais repérées dans les conditions générales et les nouveaux comparatifs.</p>
      </div>
      <div>
        <form class="form" onsubmit="return false">
          <input type="email" placeholder="Votre adresse email" aria-label="Adresse email" required>
          <button class="btn btn-accent" type="submit">Je m'inscris</button>
        </form>
        <p class="form-note">Pas de publicité, pas de revente de fichier, désinscription en un clic.</p>
      </div>
    </div>
  </div>
</section>'''

def footer(R):
    cats = "".join(f'<li><a href="{R}{s}/">{c["nom"]}</a></li>' for s, c in CATS.items())
    return f'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand"><a class="logo" href="{R or './'}" aria-label="{NOM}, accueil"><img src="{R}assets/logo/logo.svg" alt="{NOM}" width="620" height="133" loading="lazy"></a><p>{BASELINE} Nous relevons, nous comparons, nous classons. Nous ne vendons aucun contrat.</p></div>
      <div><h4>Comparatifs</h4><ul>{cats}</ul></div>
      <div><h4>Outils</h4><ul><li><a href="{R}#outil">Comparer deux contrats</a></li><li><a href="{R}#simulateur">Simulateur d'épargne</a></li><li><a href="{R}#classement">Le classement du mois</a></li><li><a href="{R}#methode">Notre méthode</a></li></ul></div>
      <div><h4>À propos</h4><ul><li><a href="{R}#methode">Comment nous comparons</a></li><li><a href="{R}a-propos/">Qui sommes-nous</a></li><li><a href="{R}a-propos/#corrections">Signaler une erreur</a></li><li><a href="{R}mentions-legales/">Mentions légales</a></li></ul></div>
    </div>
    <div class="foot-bottom"><span>© 2026 {NOM}. Comparateur indépendant de l'épargne longue.</span><span>Information non contractuelle, ne constitue pas un conseil en investissement.</span></div>
  </div>
</footer>'''

DISCLOSURE = ('<div class="disclosure"><b>Information, pas conseil.</b> Les chiffres publiés ici sont des relevés '
              'de marché, mis à jour à la date indiquée sous chaque tableau. Ils ne préjugent pas des performances '
              'futures et ne constituent pas une recommandation personnalisée. Les rendements des fonds en euros '
              'sont nets de frais de gestion et bruts de prélèvements sociaux, les unités de compte présentent un '
              'risque de perte en capital.</div>')
