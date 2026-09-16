# -*- coding: utf-8 -*-
"""Regenere tout le site : accueil, categories, articles, sitemap."""
import subprocess, sys
for s in ("build_home.py", "build_categories.py", "build_articles.py", "build_pages.py", "build_sitemap.py"):
    subprocess.run([sys.executable, s], check=True)
