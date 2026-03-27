"""Centralized configuration loader for IAO Architecture Pipeline.

Reads credentials and settings from .env (via python-dotenv) and
exposes them as a typed Config dataclass.  Every script that needs
API credentials should::

    from src.config import cfg
    token = cfg.smartsheet_token
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

# Walk upward to find .env next to this repo root
_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")


def _env(key: str, default: str = "") -> str:
    return os.environ.get(key, default)


@dataclass(frozen=True)
class Config:
    # ── Smartsheet ──────────────────────────────────────────
    smartsheet_token: str = field(default_factory=lambda: _env("SMARTSHEET_TOKEN"))

    # ── IAPM ────────────────────────────────────────────────
    iapm_bearer_token: str = field(default_factory=lambda: _env("IAPM_BEARER_TOKEN"))

    # ── BIC ─────────────────────────────────────────────────
    bic_auth_token: str = field(default_factory=lambda: _env("BIC_AUTH_TOKEN"))

    # ── SAP BI0 (Intel Foundry) ─────────────────────────────
    sap_bi0_host: str = field(default_factory=lambda: _env("SAP_BI0_HOST", "https://sapbi0ci.intel.com:8220"))
    sap_bi0_client: str = field(default_factory=lambda: _env("SAP_BI0_CLIENT", "200"))
    sap_bi0_user: str = field(default_factory=lambda: _env("SAP_BI0_USER"))
    sap_bi0_pass: str = field(default_factory=lambda: _env("SAP_BI0_PASS"))
    sap_bi0_auth_method: str = field(default_factory=lambda: _env("SAP_BI0_AUTH_METHOD", "negotiate"))

    # ── SAP DI0 (Intel Products) ────────────────────────────
    sap_di0_host: str = field(default_factory=lambda: _env("SAP_DI0_HOST", "https://sapdi0ci.intel.com:8220"))
    sap_di0_client: str = field(default_factory=lambda: _env("SAP_DI0_CLIENT", "200"))
    sap_di0_user: str = field(default_factory=lambda: _env("SAP_DI0_USER"))
    sap_di0_pass: str = field(default_factory=lambda: _env("SAP_DI0_PASS"))
    sap_di0_auth_method: str = field(default_factory=lambda: _env("SAP_DI0_AUTH_METHOD", "negotiate"))

    # ── SharePoint ──────────────────────────────────────────
    sp_tenant_id: str = field(default_factory=lambda: _env("SP_TENANT_ID"))
    sp_client_id: str = field(default_factory=lambda: _env("SP_CLIENT_ID"))
    sp_client_secret: str = field(default_factory=lambda: _env("SP_CLIENT_SECRET"))
    sp_site_url: str = field(default_factory=lambda: _env("SP_SITE_URL"))
    sp_doc_library: str = field(default_factory=lambda: _env("SP_DOC_LIBRARY", "Shared Documents"))
    sp_target_folder: str = field(default_factory=lambda: _env("SP_TARGET_FOLDER", "Architecture/SAD"))

    # ── Paths ───────────────────────────────────────────────
    root: Path = _ROOT


# Singleton — import and use directly: ``from src.config import cfg``
cfg = Config()

__version__ = "0.2.0"
