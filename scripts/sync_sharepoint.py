"""sync_sharepoint.py — Upload architecture docs & inputs to SharePoint Online.

Uses Microsoft Graph API with client-credentials (Azure AD app registration).
Credentials come from .env via src.config.

Usage:
    python sync_sharepoint.py --all                    # sync outputs for all towers
    python sync_sharepoint.py --tower FPR              # sync one tower
    python sync_sharepoint.py --all --include-inputs   # also sync input xlsx files
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import requests

WORKSPACE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE))

from src.config import cfg

TOWERS_DIR = WORKSPACE / "towers"
GRAPH_BASE = "https://graph.microsoft.com/v1.0"


def get_access_token() -> str:
    """Obtain an OAuth2 token via client_credentials grant."""
    if not all([cfg.sp_tenant_id, cfg.sp_client_id, cfg.sp_client_secret]):
        print("ERROR: SP_TENANT_ID, SP_CLIENT_ID, SP_CLIENT_SECRET must be set in .env")
        sys.exit(1)

    url = f"https://login.microsoftonline.com/{cfg.sp_tenant_id}/oauth2/v2.0/token"
    resp = requests.post(url, data={
        "grant_type": "client_credentials",
        "client_id": cfg.sp_client_id,
        "client_secret": cfg.sp_client_secret,
        "scope": "https://graph.microsoft.com/.default",
    }, timeout=30)
    resp.raise_for_status()
    return resp.json()["access_token"]


def get_site_id(token: str) -> str:
    """Resolve SharePoint site URL to a Graph site ID."""
    # Parse 'https://intel.sharepoint.com/sites/IAO-Architecture' into host + path
    from urllib.parse import urlparse
    parsed = urlparse(cfg.sp_site_url)
    host = parsed.hostname  # intel.sharepoint.com
    site_path = parsed.path.rstrip("/")  # /sites/IAO-Architecture

    url = f"{GRAPH_BASE}/sites/{host}:{site_path}"
    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
    resp.raise_for_status()
    return resp.json()["id"]


def get_drive_id(token: str, site_id: str) -> str:
    """Get the drive ID for the target document library."""
    url = f"{GRAPH_BASE}/sites/{site_id}/drives"
    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
    resp.raise_for_status()
    for drive in resp.json().get("value", []):
        if drive["name"] == cfg.sp_doc_library:
            return drive["id"]
    # Fallback to first drive
    drives = resp.json().get("value", [])
    if drives:
        return drives[0]["id"]
    print(f"ERROR: No drive found matching '{cfg.sp_doc_library}'")
    sys.exit(1)


def upload_file(token: str, drive_id: str, local_path: Path, remote_folder: str) -> bool:
    """Upload a single file to SharePoint via Graph API (up to 4 MB simple upload)."""
    filename = local_path.name
    remote_path = f"{remote_folder}/{filename}".replace("\\", "/")

    url = f"{GRAPH_BASE}/drives/{drive_id}/root:/{remote_path}:/content"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/octet-stream",
    }
    with open(local_path, "rb") as f:
        data = f.read()

    resp = requests.put(url, headers=headers, data=data, timeout=60)
    if resp.status_code in (200, 201):
        return True
    else:
        print(f"  FAILED {filename}: {resp.status_code} {resp.text[:200]}")
        return False


def sync_tower(token: str, drive_id: str, tower_short: str,
               include_inputs: bool = False) -> tuple[int, int]:
    """Upload outputs (and optionally inputs) for a tower. Returns (uploaded, failed)."""
    tower_dir = TOWERS_DIR / tower_short
    remote_base = f"{cfg.sp_target_folder}/{tower_short}"
    uploaded, failed = 0, 0

    # ── Output files (HTML, PDF, SVG) ──
    for cap_dir in tower_dir.rglob("output"):
        if not cap_dir.is_dir():
            continue
        files = (list(cap_dir.rglob("*.html"))
                 + list(cap_dir.rglob("*.pdf"))
                 + list(cap_dir.rglob("*.svg")))
        for fp in files:
            rel = fp.relative_to(tower_dir)
            remote_folder = f"{remote_base}/{rel.parent}".replace("\\", "/").rstrip("/.")
            ok = upload_file(token, drive_id, fp, remote_folder)
            if ok:
                uploaded += 1
            else:
                failed += 1
            time.sleep(0.2)

    # ── Input files (xlsx) — only when --include-inputs ──
    if include_inputs:
        for cap_dir in tower_dir.rglob("input"):
            if not cap_dir.is_dir():
                continue
            data_dir = cap_dir / "data"
            if not data_dir.is_dir():
                continue
            for fp in data_dir.glob("*.xlsx"):
                rel = fp.relative_to(tower_dir)
                remote_folder = f"{remote_base}/{rel.parent}".replace("\\", "/").rstrip("/.")
                ok = upload_file(token, drive_id, fp, remote_folder)
                if ok:
                    uploaded += 1
                else:
                    failed += 1
                time.sleep(0.2)

    if uploaded == 0 and failed == 0:
        print(f"  No files to sync for {tower_short}")

    return uploaded, failed


def main():
    parser = argparse.ArgumentParser(description="Sync architecture docs to SharePoint")
    parser.add_argument("--tower", type=str, help="Single tower shortcode")
    parser.add_argument("--all", action="store_true", help="Sync all towers")
    parser.add_argument("--include-inputs", action="store_true",
                        help="Also upload input/data/*.xlsx files (for initial bootstrap)")
    args = parser.parse_args()

    if not args.tower and not args.all:
        parser.print_help()
        sys.exit(1)

    print("Authenticating to Microsoft Graph...")
    token = get_access_token()

    print("Resolving SharePoint site...")
    site_id = get_site_id(token)
    drive_id = get_drive_id(token, site_id)
    print(f"  Site: {cfg.sp_site_url}")
    print(f"  Drive: {drive_id[:40]}...")
    if args.include_inputs:
        print("  Mode: outputs + input xlsx files")

    towers = []
    if args.all:
        towers = [d.name for d in TOWERS_DIR.iterdir() if d.is_dir()]
    elif args.tower:
        towers = [args.tower]

    total_up, total_fail = 0, 0
    for t in sorted(towers):
        print(f"\nSyncing {t}...")
        up, fail = sync_tower(token, drive_id, t, include_inputs=args.include_inputs)
        total_up += up
        total_fail += fail
        print(f"  {t}: {up} uploaded, {fail} failed")

    print(f"\n{'='*40}")
    print(f"Total: {total_up} uploaded, {total_fail} failed")


if __name__ == "__main__":
    main()
