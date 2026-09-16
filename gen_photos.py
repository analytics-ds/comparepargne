# -*- coding: utf-8 -*-
"""Telecharge les photos du site depuis Unsplash et les ecrit dans assets/img.

Les URL sources sont figees dans sources_photos.json, une entree par visuel, avec
la page de credit du photographe. Les images sont servies par le CDN Unsplash aux
dimensions demandees (recadrage sur les visages quand il y en a).

Usage : python3 gen_photos.py
"""
import json, os, urllib.request

SRC = json.load(open("sources_photos.json", encoding="utf-8"))
os.makedirs("assets/img", exist_ok=True)

def download(name, url, w, h, crop="faces,entropy"):
    full = f"{url}?w={w}&h={h}&fit=crop&crop={crop}&q=78&fm=jpg"
    req = urllib.request.Request(full, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=40).read()
    open(f"assets/img/{name}", "wb").write(data)
    return len(data)

if __name__ == "__main__":
    total = 0
    for name, meta in SRC.items():
        try:
            n = download(name, meta["url"], meta["w"], meta["h"], meta.get("crop", "faces,entropy"))
            total += n
            print(f"ok {name} ({n // 1024} Ko)")
        except Exception as e:
            print(f"ECHEC {name} : {e}")
    print(f"{len(SRC)} visuels, {total // 1024 // 1024} Mo")
