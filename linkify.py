# -*- coding: utf-8 -*-
"""Table des articles publies et remplacement automatique des href="#".

Chaque generateur appelle linkify() avant d'ecrire un fichier. Un lien reste en "#"
tant que l'article correspondant n'existe pas, ce qui evite les liens morts.
"""
import re

# fragment de titre  ->  chemin de l'article depuis la racine du site
LINKS = [
 ("Meilleure assurance vie 2026",              "assurance-vie/meilleure-assurance-vie/"),
 ("Où ouvrir une assurance vie",               "assurance-vie/ouvrir-assurance-vie-debutant/"),
 ("Assurance vie ou Livret A",                 "assurance-vie/assurance-vie-ou-livret-a/"),
 ("Meilleur fonds en euros 2026",              "rendement-frais/meilleur-fonds-euros/"),
 ("Frais d'assurance vie",                     "rendement-frais/frais-assurance-vie/"),
 ("Gestion pilotée",                           "rendement-frais/gestion-pilotee-assurance-vie/"),
 ("Fiscalité de l'assurance vie en 2026",      "fiscalite-succession/fiscalite-assurance-vie/"),
 ("Clause bénéficiaire",                       "fiscalite-succession/clause-beneficiaire/"),
 ("Meilleur PER 2026",                         "per-retraite/meilleur-per/"),
 ("PER ou assurance vie",                      "per-retraite/per-ou-assurance-vie/"),
 ("Meilleure assurance vie ISR",               "epargne-responsable/assurance-vie-isr/"),
]

_A = re.compile(r'<a([^>]*?)href="#"([^>]*?)>(.*?)</a>', re.S)

def linkify(html, prefix=""):
    """Remplace href="#" par l'URL de l'article quand le libelle du lien le designe."""
    def sub(m):
        before, after, inner = m.group(1), m.group(2), m.group(3)
        for frag, url in LINKS:
            if frag in inner:
                return f'<a{before}href="{prefix}{url}"{after}>{inner}</a>'
        return m.group(0)
    return _A.sub(sub, html)
