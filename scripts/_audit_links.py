"""Audit all portal links for broken references."""
import json, os, re
from pathlib import Path
from urllib.parse import unquote as url_unquote

WS = Path(r"c:\Users\sajivfra\Documents\IAO-JPNotebookPython")
SITE = WS / "_site"
CAP_DIR = SITE / "cap"

nav = json.loads((SITE / "nav.json").read_text(encoding="utf-8"))

# 1. Check nav.json summary link targets
print("=== Summary Link Audit ===")
for t in nav:
    tower = t.get("tower", "")
    l0 = t.get("l0_summary", "")
    if l0:
        target = WS / l0.replace("/", os.sep)
        if not target.exists():
            print(f"  MISSING L0: {l0}")
    for g in t.get("groups", []):
        l1 = g.get("l1_summary", "")
        if l1:
            target = WS / l1.replace("/", os.sep)
            if not target.exists():
                print(f"  MISSING L1: {l1}")

# 2. Check cap page doc-btn targets
print("\n=== Doc-Button Link Audit ===")
broken_docs = 0
total_docs = 0
for f in sorted(CAP_DIR.glob("*.html")):
    content = f.read_text(encoding="utf-8")
    for m in re.finditer(r'href="\.\./(.*?)"[^>]*class="doc-btn', content):
        href = m.group(1)
        decoded = url_unquote(href)
        target = WS / decoded.replace("/", os.sep)
        total_docs += 1
        if not target.exists():
            broken_docs += 1
            print(f"  BROKEN: {f.name} -> {href}")
print(f"Total doc-btns: {total_docs}, Broken: {broken_docs}")

# 3. Check for caps in nav.json without corresponding cap HTML
print("\n=== Cap File Audit ===")
missing_caps = 0
for t in nav:
    tower = t.get("tower", "")
    for g in t.get("groups", []):
        for c in g.get("caps", []):
            cid = c.get("id", "")
            if not cid:
                print(f"  MISSING ID: tower={tower} group={g.get('group')}")
                missing_caps += 1
                continue
            cap_file = CAP_DIR / f"{tower}-{cid}.html"
            if not cap_file.exists():
                print(f"  MISSING CAP: {cap_file.name}")
                missing_caps += 1
print(f"Missing cap files: {missing_caps}")

# 4. Check for spaces in doc-btn hrefs (URL encoding needed)
print("\n=== URL Encoding Check ===")
space_links = 0
for f in sorted(CAP_DIR.glob("*.html")):
    content = f.read_text(encoding="utf-8")
    for m in re.finditer(r'href="\.\./(.*?)"[^>]*class="doc-btn', content):
        href = m.group(1)
        if " " in href:
            space_links += 1
            if space_links <= 5:
                print(f"  SPACES: {f.name} -> {href[:80]}...")
print(f"Links with spaces: {space_links}")
