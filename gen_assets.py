# -*- coding: utf-8 -*-
"""Genere les visuels du site : logos texte des assureurs et illustrations SVG.

Aucun visuel n'est repris a un tiers : tout est dessine ici, en SVG, a partir
d'un motif de courbe d'epargne. Les logos sont de simples signatures
typographiques, a remplacer par les logos officiels si les droits sont obtenus.
"""
import os, math, random

os.makedirs("assets/logos", exist_ok=True)
os.makedirs("assets/img", exist_ok=True)
os.makedirs("assets/logo", exist_ok=True)

INK = "#0D1A14"; GREEN = "#0E9F6E"; SAND = "#F4F7F5"

# --------------------------------------------------------------------- logos
ASSUREURS = [
 ("groupama", "Groupama"), ("gan", "Gan"), ("linxea", "Linxea"),
 ("boursobank", "BoursoBank"), ("fortuneo", "Fortuneo"), ("spirica", "Spirica"),
 ("suravenir", "Suravenir"), ("maif", "MAIF"), ("macsf", "MACSF"),
 ("generali", "Generali"), ("cnp", "CNP"), ("yomoni", "Yomoni"),
 ("nalo", "Nalo"), ("credit-agricole", "Crédit Agricole"),
 ("bnp", "BNP Paribas"), ("axa", "AXA"), ("swisslife", "SwissLife"),
 ("placement-direct", "Placement-direct"),
]

def logo(slug, name):
    w, h = max(220, 22 * len(name) + 60), 60
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{name}">'
           f'<rect width="{w}" height="{h}" fill="none"/>'
           f'<circle cx="26" cy="30" r="11" fill="{GREEN}"/>'
           f'<path d="M20 32 l5 5 9-11" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<text x="48" y="38" font-family="Inter,Helvetica,Arial,sans-serif" font-size="22" font-weight="600" '
           f'letter-spacing="-0.4" fill="{INK}">{name}</text></svg>')
    open(f"assets/logos/{slug}.svg", "w", encoding="utf-8").write(svg)

for s, n in ASSUREURS:
    logo(s, n)

# --------------------------------------------------------------- logo du site
def sitelogo(path, ink, accent):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 133" width="620" height="133" role="img" aria-label="Comparépargne">'
           f'<g transform="translate(6,26)">'
           f'<path d="M0 74 C 22 74, 30 40, 48 32 S 74 48, 92 28" fill="none" stroke="{accent}" stroke-width="9" stroke-linecap="round"/>'
           f'<circle cx="92" cy="28" r="12" fill="{accent}"/></g>'
           f'<text x="126" y="88" font-family="Instrument Serif,Georgia,serif" font-size="70" fill="{ink}">Compar</text>'
           f'<text x="126" y="88" font-family="Instrument Serif,Georgia,serif" font-size="70" fill="{accent}" '
           f'style="visibility:hidden">x</text>'
           f'<text x="378" y="88" font-family="Instrument Serif,Georgia,serif" font-size="70" fill="{accent}">épargne</text>'
           f'</svg>')
    open(path, "w", encoding="utf-8").write(svg)

sitelogo("assets/logo/logo.svg", INK, GREEN)
sitelogo("assets/logo/logo-light.svg", "#FFFFFF", "#8FE3C2")
open("assets/logo/favicon.svg", "w", encoding="utf-8").write(
 f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{INK}"/>'
 f'<path d="M14 44 C 26 44, 30 24, 40 20" fill="none" stroke="{GREEN}" stroke-width="7" stroke-linecap="round"/>'
 f'<circle cx="44" cy="20" r="8" fill="{GREEN}"/></svg>')

# ------------------------------------------------------------- illustrations
THEMES = {
 "vert":   ("#0D1A14", "#0E9F6E", "#8FE3C2"),
 "sauge":  ("#16352A", "#2FB98A", "#D9F0E5"),
 "nuit":   ("#0B1F2A", "#1E8FA8", "#BFE6EF"),
 "terre":  ("#241C12", "#C08A3E", "#F0E0C6"),
 "prune":  ("#22142A", "#8A5CC0", "#E4D8F2"),
}

def illus(name, w, h, theme="vert", seed=0, bars=True):
    bg, acc, pale = THEMES[theme]
    rnd = random.Random(seed or sum(map(ord, name)))
    pts, n = [], 7
    for i in range(n + 1):
        x = w * i / n
        y = h * (0.72 - 0.42 * (i / n) ** 1.2 + rnd.uniform(-0.07, 0.07))
        pts.append((x, max(h * 0.12, min(h * 0.86, y))))
    d = f"M{pts[0][0]:.0f},{pts[0][1]:.0f}"
    for i in range(1, len(pts)):
        x0, y0 = pts[i - 1]; x1, y1 = pts[i]
        d += f" C{(x0+x1)/2:.0f},{y0:.0f} {(x0+x1)/2:.0f},{y1:.0f} {x1:.0f},{y1:.0f}"
    area = d + f" L{w},{h} L0,{h} Z"
    b = ""
    if bars:
        bw = w / 26
        for i in range(9):
            bh = h * (0.10 + 0.055 * i + rnd.uniform(0, 0.05))
            x = w * 0.06 + i * bw * 1.9
            b += (f'<rect x="{x:.0f}" y="{h-bh:.0f}" width="{bw:.0f}" height="{bh:.0f}" rx="{bw/2:.0f}" '
                  f'fill="{pale}" opacity="{0.18+0.05*i:.2f}"/>')
    dots = "".join(f'<circle cx="{w*(0.08+0.115*i):.0f}" cy="{h*0.18+((i*37)%int(h*0.2)):.0f}" r="3" fill="{pale}" opacity=".35"/>'
                   for i in range(8))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
           f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
           f'<stop offset="0" stop-color="{bg}"/><stop offset="1" stop-color="{acc}" stop-opacity=".55"/></linearGradient>'
           f'<linearGradient id="a" x1="0" y1="0" x2="0" y2="1">'
           f'<stop offset="0" stop-color="{pale}" stop-opacity=".55"/><stop offset="1" stop-color="{pale}" stop-opacity="0"/>'
           f'</linearGradient></defs>'
           f'<rect width="{w}" height="{h}" fill="url(#g)"/>{b}{dots}'
           f'<path d="{area}" fill="url(#a)"/>'
           f'<path d="{d}" fill="none" stroke="{pale}" stroke-width="{max(3,h/120):.0f}" stroke-linecap="round"/>'
           f'<circle cx="{pts[-1][0]-6:.0f}" cy="{pts[-1][1]:.0f}" r="{max(7,h/60):.0f}" fill="{pale}"/>'
           f'</svg>')
    open(f"assets/img/{name}.svg", "w", encoding="utf-8").write(svg)

def icon(name, theme="vert"):
    bg, acc, pale = THEMES[theme]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 56 56" width="56" height="56">'
           f'<rect width="56" height="56" rx="16" fill="{acc}" opacity=".14"/>'
           f'<path d="M12 38 C 22 38, 26 20, 36 16" fill="none" stroke="{acc}" stroke-width="4" stroke-linecap="round"/>'
           f'<circle cx="39" cy="16" r="5" fill="{acc}"/></svg>')
    open(f"assets/img/{name}.svg", "w", encoding="utf-8").write(svg)

BIG = [("hero-bg", 2400, 1400, "vert"), ("une", 1300, 860, "sauge"), ("method", 1200, 700, "nuit")]
for n, w, h, t in BIG:
    illus(n, w, h, t)

CATIMG = [("assurance-vie", "vert"), ("rendement-frais", "sauge"), ("fiscalite-succession", "nuit"),
          ("per-retraite", "terre"), ("epargne-responsable", "prune")]
for slug, t in CATIMG:
    illus(f"cat-{slug}", 760, 720, t)
    illus(f"cat-{slug}-hero", 2000, 900, t)

FAM = {"av": "vert", "rend": "sauge", "fisc": "nuit", "per": "terre", "isr": "prune"}
for fam, t in FAM.items():
    for i in range(1, 7):
        illus(f"{fam}-{i}", 800, 560, t, seed=hash(fam) % 999 + i)
    for i in (1, 2):
        illus(f"in-{fam}-{i}", 1200, 700, t, seed=hash(fam) % 777 + i * 13)
for i in range(1, 7):
    illus(f"art-{i}", 800, 560, list(THEMES)[i % 5], seed=100 + i)

for n in ["sub-av", "sub-fonds", "sub-frais", "sub-fisc", "sub-succession", "sub-per", "sub-retraite",
          "sub-isr", "sub-jeune", "sub-enfant", "sub-rachat", "sub-uc", "sub-simulateur", "sub-handicap",
          "sub-transmission", "sub-versement", "sub-gestion", "sub-impots", "sub-70ans", "sub-sortie",
          "sub-labels", "sub-climat", "sub-solidaire", "sub-profil", "sub-banque", "sub-enligne",
          "sub-garantie", "sub-arbitrage", "sub-pea", "sub-capital", "sub-deblocage", "sub-fiscal",
          "sub-clause", "sub-donation", "sub-notaire", "sub-entreprise"]:
    icon(n)

print("assets generes")
