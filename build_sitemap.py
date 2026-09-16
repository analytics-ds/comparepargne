# -*- coding: utf-8 -*-
"""Genere sitemap.xml et robots.txt a partir des pages presentes sur le disque."""
import os, datetime
from common import SITE

today = datetime.date.today().isoformat()
urls = [("", "1.0")]
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "assets", "__pycache__", ".playwright-cli")]
    if root == "." or "index.html" not in files:
        continue
    path = os.path.relpath(root, ".").replace(os.sep, "/") + "/"
    urls.append((path, "0.8" if path.count("/") == 1 else "0.7"))

body = "".join(f'  <url><loc>{SITE}/{p}</loc><lastmod>{today}</lastmod>'
               f'<priority>{prio}</priority></url>\n' for p, prio in sorted(urls))
open("sitemap.xml", "w", encoding="utf-8").write(
 '<?xml version="1.0" encoding="UTF-8"?>\n'
 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + '</urlset>\n')
open("robots.txt", "w", encoding="utf-8").write(
 f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print(f"ok sitemap.xml ({len(urls)} URL) et robots.txt")
