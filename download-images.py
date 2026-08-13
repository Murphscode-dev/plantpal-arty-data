#!/usr/bin/env python3
"""
download-images.py

Downloads the images referenced in the articles and saves them under data/images/ with predictable filenames.
Run: python3 download-images.py
"""

import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("requests not installed. Run: pip install requests")
    sys.exit(1)

IMAGES = [
    ("https://images.unsplash.com/photo-1693070058300-78ab7421d392?q=80&w=1074", "data/images/ext-link-001-hero.jpg"),
    ("https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?q=80&w=1070", "data/images/ext-link-001-1.jpg"),
    ("https://images.unsplash.com/photo-1697342566063-a77aea25cc18?q=80&w=1071", "data/images/ext-link-001-2.jpg"),

    ("https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?q=80&w=1070", "data/images/ext-link-002-hero.jpg"),
    ("https://images.unsplash.com/photo-1591857177580-dc82b9ac4e1e?q=80&w=1000", "data/images/ext-link-002-1.jpg"),
    ("https://images.unsplash.com/photo-1601833256820-4fb291a66e0a?q=80&w=1000", "data/images/ext-link-002-2.jpg"),

    ("https://images.unsplash.com/photo-1697342566063-a77aea25cc18?q=80&w=1071", "data/images/ext-link-003-hero.jpg"),
    ("https://images.unsplash.com/photo-1592841200221-a6898f307baa?q=80&w=1000", "data/images/ext-link-003-1.jpg"),
    ("https://images.unsplash.com/photo-1631313335861-d44f363f6e03?q=80&w=1000", "data/images/ext-link-003-2.jpg"),
]

OUTPUT_DIR = Path("data/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

headers = {"User-Agent": "plantpal-arty-data downloader/1.0"}

errors = []
for url, outpath in IMAGES:
    outpath = Path(outpath)
    if outpath.exists():
        print(f"Skipped (exists): {outpath}")
        continue
    print(f"Downloading: {url} -> {outpath}")
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        outpath.write_bytes(r.content)
        print(f"Saved: {outpath} ({len(r.content)} bytes)")
    except Exception as e:
        print(f"ERROR downloading {url}: {e}")
        errors.append((url, str(e)))

if errors:
    print("\nCompleted with errors:")
    for u, e in errors:
        print(u, e)
    sys.exit(2)

print("\nAll images downloaded successfully.")
