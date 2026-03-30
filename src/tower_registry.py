"""Centralized tower registry — single source of truth for tower metadata.

All scripts that need tower normalization, display names, ordering, or
Signavio name mappings should import from here instead of maintaining
their own hardcoded dictionaries.

Usage::

    from src.tower_registry import (
        normalize_tower,  # "03. FPR" → "FPR"
        TOWER_ORDER,      # ["FPR", "OTC-IF", ...]
        TOWER_DISPLAY,    # {"FPR": "Finance Plan to Report", ...}
        TOWER_INFO,       # {"FPR": {"name": ..., "icon": ..., ...}}
        SIGNAVIO_MAP,     # {"Finance Plan To Report": "FPR", ...}
    )
"""

from __future__ import annotations

import json
import re
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_REGISTRY_PATH = _ROOT / "config" / "tower_registry.json"

# ── Load registry ────────────────────────────────────────────────────────
def _load_registry() -> dict:
    with open(_REGISTRY_PATH, encoding="utf-8") as f:
        return json.load(f)

_REG = _load_registry()

# ── Derived lookups ──────────────────────────────────────────────────────

#: Ordered list of tower shortcodes (presentation order)
TOWER_ORDER: list[str] = list(_REG["towers"].keys())

#: Full tower info dicts keyed by shortcode
TOWER_INFO: dict[str, dict] = _REG["towers"]

#: Shortcode → display name
TOWER_DISPLAY: dict[str, str] = {
    sc: info["name"] for sc, info in _REG["towers"].items()
}

#: Signavio folder name → shortcode
SIGNAVIO_MAP: dict[str, str] = {}
for sc, info in _REG["towers"].items():
    for sname in info.get("signavio_names", []):
        SIGNAVIO_MAP[sname] = sc

#: Lowercase alias → shortcode (for normalizing Smartsheet / CSV tower names)
_ALIAS_MAP: dict[str, str] = {
    k.lower(): v for k, v in _REG.get("aliases", {}).items()
}

# Also add shortcodes themselves as lowercase aliases
for sc in _REG["towers"]:
    _ALIAS_MAP[sc.lower()] = sc

# ── Normalization ────────────────────────────────────────────────────────

# Strip leading "03. " or "09A. " numbering from Smartsheet tower names
_NUM_PREFIX_RE = re.compile(r"^\d+[a-zA-Z]?\.\s*")


def normalize_tower(raw: str) -> str:
    """Normalize a raw tower name to its canonical shortcode.

    Handles Smartsheet numbering prefixes, Signavio folder names,
    case variations, and common aliases.  Returns empty string if
    the name cannot be resolved.
    """
    key = _NUM_PREFIX_RE.sub("", raw.strip()).lower()
    return _ALIAS_MAP.get(key, "")


def reload():
    """Reload the registry from disk (useful after build_capability_master updates it)."""
    global _REG, TOWER_ORDER, TOWER_INFO, TOWER_DISPLAY, SIGNAVIO_MAP, _ALIAS_MAP
    _REG = _load_registry()
    TOWER_ORDER = list(_REG["towers"].keys())
    TOWER_INFO = _REG["towers"]
    TOWER_DISPLAY = {sc: info["name"] for sc, info in _REG["towers"].items()}
    SIGNAVIO_MAP = {}
    for sc, info in _REG["towers"].items():
        for sname in info.get("signavio_names", []):
            SIGNAVIO_MAP[sname] = sc
    _ALIAS_MAP = {k.lower(): v for k, v in _REG.get("aliases", {}).items()}
    for sc in _REG["towers"]:
        _ALIAS_MAP[sc.lower()] = sc
