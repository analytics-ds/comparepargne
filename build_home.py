# -*- coding: utf-8 -*-
"""Genere la page d'accueil de Comparepargne.

Usage : python3 build_home.py  (depuis le dossier comparepargne)
"""
import json
from common import *
from linkify import linkify

R = ""
TITLE = "Comparateur d'assurance vie et de PER 2026 : le classement des meilleurs contrats"
DESC = ("Comparatif d'assurance vie et de plan d'épargne retraite 2026 : rendement des fonds en euros, "
        "frais réels, choix des supports et fiscalité de 16 contrats comparés, de Groupama à Linxea.")

LOGOS = ["ggvie","linxea","boursobank","fortuneo","spirica","suravenir","maif","macsf",
         "generali","cnp","yomoni","nalo","axa"]
NOMS = {"ggvie":"Groupama Gan Vie","groupama":"Groupama","gan":"Gan","linxea":"Linxea","boursobank":"BoursoBank","fortuneo":"Fortuneo",
        "spirica":"Spirica","suravenir":"Suravenir","maif":"MAIF","macsf":"MACSF","generali":"Generali",
        "cnp":"CNP","yomoni":"Yomoni","nalo":"Nalo","credit-agricole":"Crédit Agricole","bnp":"BNP Paribas","axa":"AXA"}

# notes sur 10 : fonds en euros, frais, choix des supports, accessibilite, note globale
CONTRATS = {
 "Groupama Modulation": [9.0, 8.8, 8.4, 9.2, 9.1],
 "Gan Patrimoine":      [8.8, 8.5, 8.6, 8.6, 8.7],
 "Linxea Spirit 2":     [7.6, 8.6, 9.0, 8.4, 8.3],
 "BoursoVie":           [7.0, 8.2, 8.0, 8.6, 7.9],
 "Fortuneo Vie":        [7.2, 8.0, 7.8, 8.4, 7.8],
 "MACSF RES":           [8.2, 7.4, 6.4, 7.2, 7.5],
 "MAIF Responsable":    [7.4, 7.6, 6.8, 8.0, 7.4],
 "Contrat bancaire moyen": [5.8, 4.6, 5.4, 7.8, 5.9],
}
CRITS = [("Fonds en euros","rendement servi sur trois ans"),
         ("Frais","versement, gestion, arbitrage"),
         ("Choix des supports","nombre et qualité des unités de compte"),
         ("Accessibilité","versement minimum, souscription, service"),
         ("Note globale","moyenne pondérée")]

CLASSEMENT = [
 ("ggvie","Groupama Modulation","Le meilleur contrat du panel","Frais affichés au centime, souscription en ligne en quinze minutes, versement programmé dès 50 € par mois et un fonds en euros au-dessus du marché.","9,1","up","▲ +0,3"),
 ("ggvie","Gan Patrimoine","Le plus complet sur les supports","Gamme labellisée ISR de bout en bout, fonds en euros régulier sur trois exercices, accompagnement à la demande.","8,7","up","▲ +0,2"),
 ("linxea","Linxea Spirit 2","Le plus large en ligne","Gamme de plus de 1 000 supports, mais aucun accompagnement sur la clause bénéficiaire.","8,3","flat","= 0,0"),
 ("boursobank","BoursoVie","Le plus rapide à ouvrir","Souscription en dix minutes, gamme de supports plus courte, fonds en euros en retrait.","7,9","flat","= 0,0"),
 ("macsf","MACSF RES","Le plus limité en supports","Fonds en euros correct, mais une soixantaine d'unités de compte seulement.","7,5","down","▼ -0,1"),
]

FEAT = dict(href="assurance-vie/meilleure-assurance-vie/", img="une.jpg",
  alt="Rendez-vous entre une conseillère et un épargnant autour d'un contrat", tag="Classement",
  h2="Meilleure assurance vie 2026 : le comparatif de 16 contrats",
  p="Rendement des fonds en euros servi sur trois ans, frais lus dans les conditions générales, nombre de supports réellement accessibles et montant du premier versement. Le contrat le mieux noté est celui qui tient les quatre critères à la fois, pas celui qui gagne sur un seul.",
  meta="16 contrats comparés · 12 min de lecture · Mis à jour le 16 septembre 2026")

SIDE = [("rendement-frais/meilleur-fonds-euros/","rend-1.jpg","Fonds en euros","Meilleur fonds en euros 2026 : les rendements servis, contrat par contrat","9 min de lecture"),
        ("per-retraite/meilleur-per/","per-1.jpg","Retraite","Meilleur PER 2026 : le comparatif de 12 plans d'épargne retraite","11 min de lecture"),
        ("fiscalite-succession/fiscalite-assurance-vie/","fisc-1.jpg","Fiscalité","Fiscalité de l'assurance vie en 2026 : ce que vous payez vraiment à chaque retrait","10 min de lecture"),
        ("rendement-frais/frais-assurance-vie/","rend-2.jpg","Frais","Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats","8 min de lecture")]

TILES = [("assurance-vie","Assurance vie","14 comparatifs"),
         ("rendement-frais","Rendement et frais","11 comparatifs"),
         ("per-retraite","PER et retraite","9 comparatifs"),
         ("fiscalite-succession","Fiscalité et succession","8 comparatifs")]

POSTS = [("assurance-vie/ouvrir-assurance-vie-debutant/","av-2.jpg","Assurance vie","Où ouvrir une assurance vie quand on débute : banque, assureur ou courtier","3 circuits","9 min"),
         ("assurance-vie/assurance-vie-ou-livret-a/","av-3.jpg","Épargne","Assurance vie ou Livret A : où placer son épargne en 2026","2 placements","8 min"),
         ("per-retraite/per-ou-assurance-vie/","per-3.jpg","Retraite","PER ou assurance vie : lequel choisir pour préparer sa retraite","2 enveloppes","9 min"),
         ("epargne-responsable/assurance-vie-isr/","isr-1.jpg","ISR","Meilleure assurance vie ISR 2026 : les contrats qui tiennent leur promesse","9 contrats","10 min")]

def jsonld():
    org = {"@context":"https://schema.org","@type":"Organization","name":NOM,"url":SITE,
           "description":BASELINE,"logo":f"{SITE}/assets/logo/logo.svg"}
    site = {"@context":"https://schema.org","@type":"WebSite","name":NOM,"url":SITE,"inLanguage":"fr-FR"}
    items = {"@context":"https://schema.org","@type":"ItemList","name":"Classement des contrats d'épargne",
             "itemListOrder":"https://schema.org/ItemListOrderDescending","numberOfItems":len(CLASSEMENT),
             "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,
               "description":f"Note {sc}/10. {b}. {why}"} for i,(_,n,b,why,sc,_,_) in enumerate(CLASSEMENT)]}
    return "".join('<script type="application/ld+json">'+json.dumps(d,ensure_ascii=False)+"</script>\n"
                   for d in (org,site,items))

side = "".join(f'''
        <a class="side-item" href="{h}">
          <img src="assets/img/{img}" alt="" width="96" height="80" loading="lazy">
          <div><span class="eyebrow">{k}</span><h3>{t}</h3><small>{m}</small></div>
        </a>''' for h,img,k,t,m in SIDE)

tiles = "".join(f'''
      <a class="tile" href="{s}/"><img src="assets/img/cat-{s}.jpg" alt="{n}" width="760" height="720" loading="lazy"><span class="tile-label"><span><strong>{n}</strong><em>{c}</em></span><span class="arrow">{ARROW}</span></span></a>''' for s,n,c in TILES)

rank = "".join(f'''
      <div class="rank-row"><span class="pos{" first" if i==0 else ""}">0{i+1}</span><img src="{logo_src("", logo)}" alt="{n}" width="120" height="33"><div class="why"><b>{b}</b>{why}</div><div class="score"><b>{sc}</b><small>/10</small><span class="chip{"" if cls=="up" else " "+cls}">{chip}</span></div></div>''' for i,(logo,n,b,why,sc,cls,chip) in enumerate(CLASSEMENT))

posts = "".join(f'''
      <a class="post" href="{h}"><img src="assets/img/{img}" alt="" width="800" height="560" loading="lazy"><div class="post-body"><span class="eyebrow">{k}</span><h3>{t}</h3><span class="meta">{n} <i></i> {d}</span></div></a>''' for h,img,k,t,n,d in POSTS)

marquee = "".join(f'<img src="{logo_src("", l)}" alt="{NOMS[l]}">' for l in LOGOS)

HTML = f'''<!doctype html>
<html lang="fr">
<head>
{head(R, TITLE, DESC, canonical=SITE + "/", extra=jsonld())}</head>
<body>

{header(R)}

<section class="hero hero-split">
  <div class="wrap hero-inner">
    <div class="hero-grid">
      <div>
        <h1>Le classement 2026 des meilleures <em>assurances vie</em></h1>
        <p>Quelle assurance vie ouvrir en 2026 ? Nous comparons 16 contrats sur le rendement servi par leur fonds en euros, les frais réellement prélevés, le choix des supports et le montant du premier versement.</p>
        <div class="btns">
          <a class="btn-pill" href="#comparatifs">Voir les comparatifs <span class="circ">{ARROW}</span></a>
          <a class="btn-link" href="#simulateur">Simuler mon épargne</a>
        </div>
      </div>
      <figure class="hero-figure">
        <div class="hero-portrait">
          <img src="assets/img/hero-portrait.jpg" alt="Conseillère en gestion de patrimoine devant un immeuble de bureaux" width="900" height="1200" fetchpriority="high">
          <figcaption class="hero-quote">
            <b>Des chiffres pris à la source</b>
            <span>Les frais viennent des conditions générales, les rendements des publications annuelles des assureurs, et chaque comparatif indique la date de son relevé.</span>
          </figcaption>
        </div>
      </figure>
    </div>
  </div>
</section>

<section class="brands" id="assureurs">
  <div class="brands-head">Les assureurs et les contrats que nous suivons chaque trimestre</div>
  <div class="marquee"><div class="marquee-track" id="logoTrack">{marquee}</div></div>
</section>

<section class="featured" id="comparatifs">
  <div class="wrap">
    <div class="section-head">
      <div><h2>Le comparatif d'épargne du mois</h2></div>
      <a class="btn btn-ghost" href="#derniers">Tous les comparatifs</a>
    </div>
    <div class="feat-grid">
      <a class="feat-main" href="{FEAT["href"]}">
        <img src="assets/img/{FEAT["img"]}" alt="{FEAT["alt"]}" width="1300" height="860">
        <div class="feat-body">
          <span class="tag">{FEAT["tag"]}</span>
          <h2>{FEAT["h2"]}</h2>
          <p>{FEAT["p"]}</p>
          <span class="feat-meta">{FEAT["meta"]}</span>
        </div>
      </a>
      <div class="feat-side">{side}
      </div>
    </div>
  </div>
</section>

<section class="tool" id="outil">
  <div class="wrap">
    <div class="tool-card">
      <div class="tool-intro">
        <h2>Comparez deux contrats d'épargne en un clic</h2>
        <p>Choisissez deux contrats, nous affichons leurs notes sur nos cinq critères, calculées à partir des rendements publiés et des frais lus dans les conditions générales.</p>
        <div class="selects">
          <div class="select"><select id="brandA" aria-label="Premier contrat"></select></div>
          <span class="vs">VS</span>
          <div class="select"><select id="brandB" aria-label="Second contrat"></select></div>
        </div>
        <p class="tool-note">Notes sur 10 établies sur nos relevés de septembre 2026. Les performances passées ne préjugent pas des performances futures.</p>
      </div>
      <div class="compare">
        <div class="cmp-head"><span>Critère</span><b id="nameA"></b><b id="nameB"></b></div>
        <div id="rows"></div>
        <div class="verdict"><b id="verdict"></b><span id="verdictSub"></span></div>
      </div>
    </div>
  </div>
</section>

<section class="tool" id="simulateur" style="padding-top:0">
  <div class="wrap">
    <div class="tool-card">
      <div class="tool-intro">
        <h2>Combien votre épargne rapporte-t-elle sur huit ans ?</h2>
        <p>Le capital de départ, l'effort mensuel, la durée et le rendement annuel moyen. Nous calculons le capital atteint, les intérêts produits et le total versé, avant fiscalité.</p>
        <div class="sim-grid">
          <div><label for="simCap">Capital de départ</label><input id="simCap" type="number" value="10000" min="0" step="500"></div>
          <div><label for="simMens">Versement mensuel</label><input id="simMens" type="number" value="200" min="0" step="10"></div>
          <div><label for="simDur">Durée (années)</label><input id="simDur" type="number" value="8" min="1" max="40"></div>
        </div>
        <div class="sim-grid" style="grid-template-columns:1fr 1fr">
          <div><label for="simTaux">Rendement annuel moyen</label><input id="simTaux" type="number" value="3" min="0" max="12" step="0.1"></div>
          <div><label for="simFrais">Frais de gestion annuels</label><input id="simFrais" type="number" value="0.7" min="0" max="3" step="0.05"></div>
        </div>
        <p class="tool-note">Calcul à rendement constant, frais de gestion déduits chaque année, hors prélèvements sociaux et hors impôt. Un fonds en euros ne garantit pas un rendement futur et une unité de compte peut perdre de la valeur.</p>
      </div>
      <div class="compare">
        <div class="sim-out">
          <div class="sim-card"><span>Capital atteint</span><b class="num" id="outCap">–</b></div>
          <div class="sim-card"><span>Total versé</span><b class="num" id="outVers">–</b></div>
          <div class="sim-card"><span>Intérêts produits</span><b class="num" id="outInt">–</b></div>
        </div>
        <div class="sim-out" style="grid-template-columns:1fr">
          <div class="sim-card"><span>Ce que les frais vous coûtent sur la période</span><b class="num" id="outFrais">–</b></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cats" id="categories">
  <div class="wrap">
    <div class="section-head">
      <div><h2>Nos comparatifs par sujet</h2><p>Le bon contrat dépend de ce que vous cherchez : un rendement, une fiscalité, une transmission ou une retraite.</p></div>
    </div>
    <div class="grid4">{tiles}
    </div>
  </div>
</section>

<section class="ranking" id="classement">
  <div class="wrap rank-grid">
    <div class="rank-intro">
      <h2>Les contrats d'épargne les mieux notés en septembre 2026</h2>
      <p>Note globale sur 10, moyenne pondérée de nos cinq critères. Le classement bouge à chaque publication de rendement et à chaque mise à jour des conditions générales.</p>
      <a class="btn btn-dark" href="#methode">Voir la méthode de notation</a>
    </div>
    <div class="rank-list">{rank}
    </div>
  </div>
</section>

<section class="posts" id="derniers">
  <div class="wrap">
    <div class="section-head">
      <div><h2>Derniers comparatifs publiés</h2></div>
      <a class="btn btn-ghost" href="assurance-vie/">Tous les comparatifs</a>
    </div>
    <div class="grid4">{posts}
    </div>
  </div>
</section>

<section class="method" id="methode">
  <div class="wrap">
    <div class="method-head">
      <h2>Comment nous comparons les contrats d'épargne</h2>
      <p>Tout part de documents publics, vérifiables un par un : conditions générales, notes d'information, publications annuelles des assureurs et documents d'informations clés des supports.</p>
    </div>
    <div class="steps">
      <div class="step"><span class="n">01</span><h3>Nous lisons les conditions générales</h3><p>Frais de versement, de gestion, d'arbitrage et de sortie en rente, ligne par ligne, sur le document contractuel et non sur la page commerciale.</p></div>
      <div class="step"><span class="n">02</span><h3>Nous reprenons les rendements publiés</h3><p>Le taux servi par chaque fonds en euros, net de frais de gestion et brut de prélèvements sociaux, sur les trois derniers exercices.</p></div>
      <div class="step"><span class="n">03</span><h3>Nous testons le parcours réel</h3><p>Montant du premier versement, durée de la souscription en ligne, montant minimal d'un versement programmé et délai réel de versement d'un rachat partiel, avis clients à l'appui.</p></div>
    </div>
    {DISCLOSURE}
  </div>
</section>

{newsletter()}

{footer(R)}

<script src="assets/js/site.js?v=1"></script>
<script>
(function(){{
  var contrats={json.dumps(CONTRATS, ensure_ascii=False)};
  var crits={json.dumps(CRITS, ensure_ascii=False)};
  var A=document.getElementById('brandA'),B=document.getElementById('brandB');
  Object.keys(contrats).forEach(function(n){{A.add(new Option(n,n));B.add(new Option(n,n));}});
  A.value="Groupama Modulation";B.value="Linxea Spirit 2";
  function fmt(v){{return v.toFixed(1).replace('.',',');}}
  function render(){{
    var a=A.value,b=B.value,ra=contrats[a],rb=contrats[b],wins=0,rows='';
    document.getElementById('nameA').textContent=a;document.getElementById('nameB').textContent=b;
    crits.forEach(function(c,i){{
      var va=ra[i],vb=rb[i],wa=va>vb,wb=vb>va; if(i<4&&wa)wins++;
      rows+='<div class="cmp-row"><div class="crit">'+c[0]+'<small>'+c[1]+'</small></div>'
        +'<div class="bar'+(wa?' win':'')+'"><div class="track"><div class="fill" style="width:'+(va*10)+'%"></div></div><span class="val">'+fmt(va)+'</span></div>'
        +'<div class="bar'+(wb?' win':'')+'"><div class="track"><div class="fill" style="width:'+(vb*10)+'%"></div></div><span class="val">'+fmt(vb)+'</span></div></div>';
    }});
    document.getElementById('rows').innerHTML=rows;
    var v=document.getElementById('verdict'),s=document.getElementById('verdictSub');
    if(a===b){{v.textContent='Choisissez deux contrats différents';s.textContent='';return;}}
    var lead=ra[4]>rb[4]?a:rb[4]>ra[4]?b:null;
    v.textContent=lead?lead+' l\\u2019emporte':'Égalité parfaite';
    s.textContent=lead?(lead===a?wins:4-wins)+' critères sur 4, note globale '+fmt(lead===a?ra[4]:rb[4])+' contre '+fmt(lead===a?rb[4]:ra[4]):'Même note globale sur nos relevés';
  }}
  A.addEventListener('change',render);B.addEventListener('change',render);render();
}})();
(function(){{
  var ids=['simCap','simMens','simDur','simTaux','simFrais'],el={{}};
  ids.forEach(function(i){{el[i]=document.getElementById(i);}});
  if(!el.simCap)return;
  var eur=new Intl.NumberFormat('fr-FR',{{style:'currency',currency:'EUR',maximumFractionDigits:0}});
  function calc(){{
    var c=+el.simCap.value||0,m=+el.simMens.value||0,n=Math.max(1,+el.simDur.value||1),
        t=(+el.simTaux.value||0)/100,f=(+el.simFrais.value||0)/100;
    var net=Math.pow(1+t,1/12)-1, fm=Math.pow(1-f,1/12)-1, r=net+fm;
    var cap=c, brut=c, rb=Math.pow(1+t,1/12)-1;
    for(var i=0;i<n*12;i++){{cap=cap*(1+r)+m; brut=brut*(1+rb)+m;}}
    var verse=c+m*n*12;
    document.getElementById('outCap').textContent=eur.format(cap);
    document.getElementById('outVers').textContent=eur.format(verse);
    document.getElementById('outInt').textContent=eur.format(cap-verse);
    document.getElementById('outFrais').textContent=eur.format(brut-cap);
  }}
  ids.forEach(function(i){{el[i].addEventListener('input',calc);}});calc();
}})();
</script>
</body>
</html>
'''

if __name__ == "__main__":
    open("index.html", "w", encoding="utf-8").write(linkify(HTML, ""))
    print("ok index.html")
