"""iapm_lookup.py — Build IAPM system lookup from IAPM_All_Solutions.csv.

Provides system name → IAPM metadata mapping used by mermaid_builder.py to:
  - Resolve IAPM IDs and URLs from flow CSV system names
  - Determine lifecycle status (Deployed, Developing, End of Life, etc.)
  - Supply tooltip text for Mermaid click events

Extraction mode pivot:
  POC  — reads from data/iapm/IAPM_All_Solutions.csv (manual export)
  Prod — will call IAPM REST API via src/iapm_client.py (not yet built)
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# Default IAPM base URL for generating application links
IAPM_BASE_URL = "https://iapm.intel.com/#/app/"

# Status classification for Mermaid styling
STATUS_CLASSES = {
    "Deployed":           "deployed",
    "Deployed-Legal Hold": "deployed",
    "Developing":         "developing",
    "Planning":           "developing",
    "Registration":       "developing",
    "End of Life":        "eol",
    "Canceled":           "eol",
}


@dataclass
class IAPMApp:
    """A single IAPM application record."""
    app_id: str
    name: str
    acronym: str
    status: str
    product_owner: str = ""
    product_owner_email: str = ""
    business_owner: str = ""
    hosting_type: str = ""
    iao_tower: str = ""

    @property
    def url(self) -> str:
        return f"{IAPM_BASE_URL}{self.app_id}" if self.app_id else ""

    @property
    def style_class(self) -> str:
        return STATUS_CLASSES.get(self.status, "noMatch")

    @property
    def status_label(self) -> str:
        """Short label for Mermaid node annotations."""
        if self.status == "Developing":
            return "DEV"
        if self.status == "End of Life":
            return "EOL"
        if self.status == "Planning":
            return "DEV"
        return ""


class IAPMLookup:
    """Lookup table: system name/acronym → IAPMApp.

    Matching priority:
      1. Exact acronym match (case-insensitive)
      2. Exact name match (case-insensitive)
      3. IAPM URL ID extraction (from flow CSV IAPM URL columns)
    """

    def __init__(self) -> None:
        self._by_id: dict[str, IAPMApp] = {}
        self._by_acronym: dict[str, IAPMApp] = {}
        self._by_name: dict[str, IAPMApp] = {}
        self._loaded = False

    @property
    def app_count(self) -> int:
        return len(self._by_id)

    def load_csv(self, csv_path: str) -> None:
        """Load IAPM_All_Solutions.csv into lookup tables."""
        path = Path(csv_path)
        if not path.exists():
            raise FileNotFoundError(f"IAPM CSV not found: {csv_path}")

        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                app = IAPMApp(
                    app_id=(row.get("applicationId") or "").strip(),
                    name=(row.get("applicationNm") or "").strip(),
                    acronym=(row.get("applicationAcronymNm") or "").strip(),
                    status=(row.get("applicationLifecycleStatusNm") or "").strip(),
                    product_owner=(row.get("productOwnerNm") or "").strip(),
                    product_owner_email=(row.get("productOwnerEmailTxt") or "").strip(),
                    business_owner=(row.get("businessOwnerNm") or "").strip(),
                    hosting_type=(row.get("applicationHostingTypeNm") or "").strip(),
                    iao_tower=(row.get("idmAccelerationOfficeTowerClassificationNm") or "").strip(),
                )
                if app.app_id:
                    self._by_id[app.app_id] = app
                if app.acronym:
                    self._by_acronym[app.acronym.lower()] = app
                if app.name:
                    self._by_name[app.name.lower()] = app
        self._loaded = True

    def find_by_name(self, system_name: str) -> Optional[IAPMApp]:
        """Look up by system name or acronym."""
        if not system_name:
            return None
        key = system_name.strip().lower()
        # Strip status annotations that may appear in CSV system names
        clean = re.sub(r"\s*\((?:DEV|EOL|N/A|Developing|End of Life)\)\s*$", "", key, flags=re.IGNORECASE)
        return self._by_acronym.get(clean) or self._by_name.get(clean)

    def find_by_id(self, app_id: str) -> Optional[IAPMApp]:
        """Look up by IAPM application ID."""
        return self._by_id.get(str(app_id).strip()) if app_id else None

    def find_by_url(self, iapm_url: str) -> Optional[IAPMApp]:
        """Extract IAPM ID from a URL like https://iapm.intel.com/#/app/41275."""
        if not iapm_url:
            return None
        m = re.search(r"/app/(\d+)", iapm_url)
        if m:
            return self.find_by_id(m.group(1))
        return None

    def resolve(self, system_name: str, iapm_url: str = "") -> Optional[IAPMApp]:
        """Best-effort resolve: try URL first (most precise), then name."""
        return self.find_by_url(iapm_url) or self.find_by_name(system_name)
