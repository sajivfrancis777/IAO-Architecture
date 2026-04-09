"""system_master — Shared loader for config/system_master.yaml.

Provides approved dropdown options and system → DB/platform defaults
for enrichment, diagram generation, and Input Portal registry.
"""

from __future__ import annotations

from pathlib import Path
from functools import lru_cache
from typing import NamedTuple

import yaml

_CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "system_master.yaml"


class SystemDefault(NamedTuple):
    db: str
    platform: str


@lru_cache(maxsize=1)
def _load_raw() -> dict:
    with open(_CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def db_labels() -> list[str]:
    """Return ordered list of approved database platform labels."""
    return [d["label"] for d in _load_raw().get("databases", [])]


def platform_labels() -> list[str]:
    """Return ordered list of approved tech platform labels."""
    return [p["label"] for p in _load_raw().get("platforms", [])]


@lru_cache(maxsize=1)
def system_defaults() -> dict[str, SystemDefault]:
    """Return {system_name: SystemDefault(db, platform)} lookup."""
    raw = _load_raw().get("system_defaults", {})
    return {
        name: SystemDefault(db=vals.get("db", ""), platform=vals.get("platform", ""))
        for name, vals in raw.items()
    }


def infer_db(system_name: str) -> str:
    """Return the default database for a system, or empty string."""
    sd = system_defaults().get(system_name)
    return sd.db if sd else ""


def infer_platform(system_name: str) -> str:
    """Return the default platform for a system, or empty string."""
    sd = system_defaults().get(system_name)
    return sd.platform if sd else ""
