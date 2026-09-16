# -*- coding: utf-8 -*-
"""Assemble le contenu des articles, une rubrique par fichier.

Les montants et les notes proviennent de notre releve de septembre 2026, les regles
fiscales du code general des impots et du code des assurances en vigueur a cette date.
"""
from contenus_assurance_vie import ARTICLES as AV
from contenus_rendement import ARTICLES as REND
from contenus_fiscalite import ARTICLES as FISC
from contenus_retraite import ARTICLES as PER
from contenus_responsable import ARTICLES as ISR

ARTICLES = AV + REND + FISC + PER + ISR
