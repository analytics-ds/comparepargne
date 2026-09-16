# -*- coding: utf-8 -*-
"""Genere le logo du site, les signatures des assureurs et les icones de sous-navigation.

Les photos du site sont telechargees par gen_photos.py. Ici on ne genere que le
vectoriel : logo, favicon, signatures typographiques des assureurs (a remplacer par
les logos officiels si les droits sont obtenus) et petites icones de sous-navigation.
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
           f'<text x="48" y="38" font-family="Inter,Helvetica,Arial,sans-serif" font-size="23" font-weight="700" '
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
           f'<text x="126" y="88" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-size="62" font-weight="700" letter-spacing="-2" fill="{ink}">Compar</text>'
           f'<text x="126" y="88" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-size="62" font-weight="700" fill="{accent}" '
           f'style="visibility:hidden">x</text>'
           f'<text x="352" y="88" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" font-size="62" font-weight="700" letter-spacing="-2" fill="{accent}">épargne</text>'
           f'</svg>')
    open(path, "w", encoding="utf-8").write(svg)

sitelogo("assets/logo/logo.svg", INK, GREEN)
sitelogo("assets/logo/logo-light.svg", "#FFFFFF", "#8FE3C2")
open("assets/logo/favicon.svg", "w", encoding="utf-8").write(
 f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{INK}"/>'
 f'<path d="M14 44 C 26 44, 30 24, 40 20" fill="none" stroke="{GREEN}" stroke-width="7" stroke-linecap="round"/>'
 f'<circle cx="44" cy="20" r="8" fill="{GREEN}"/></svg>')

# ------------------------------------------------------------------- icones
def icon(name, theme="vert"):
    acc = GREEN
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 56 56" width="56" height="56">'
           f'<rect width="56" height="56" rx="16" fill="{acc}" opacity=".14"/>'
           f'<path d="M12 38 C 22 38, 26 20, 36 16" fill="none" stroke="{acc}" stroke-width="4" stroke-linecap="round"/>'
           f'<circle cx="39" cy="16" r="5" fill="{acc}"/></svg>')
    open(f"assets/img/{name}.svg", "w", encoding="utf-8").write(svg)

for n in ["sub-av", "sub-fonds", "sub-frais", "sub-fisc", "sub-succession", "sub-per", "sub-retraite",
          "sub-isr", "sub-jeune", "sub-enfant", "sub-rachat", "sub-uc", "sub-simulateur", "sub-handicap",
          "sub-transmission", "sub-versement", "sub-gestion", "sub-impots", "sub-70ans", "sub-sortie",
          "sub-labels", "sub-climat", "sub-solidaire", "sub-profil", "sub-banque", "sub-enligne",
          "sub-garantie", "sub-arbitrage", "sub-pea", "sub-capital", "sub-deblocage", "sub-fiscal",
          "sub-clause", "sub-donation", "sub-notaire", "sub-entreprise"]:
    icon(n)

print("logo, signatures et icones generes")
