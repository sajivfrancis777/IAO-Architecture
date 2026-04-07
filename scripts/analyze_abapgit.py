"""analyze_abapgit.py — Parse abapGit-exported ABAP source for clean core analysis.

Scans an abapGit repository directory (or multiple) and produces:
  1. Object inventory (programs, classes, function modules, CDS views, etc.)
  2. Clean core scorecard (released-API usage, deprecated patterns, direct table access)
  3. Integration point analysis (RFC destinations, HTTP calls, IDoc types)
  4. Data access patterns (table reads/writes, CDS views, authority checks)
  5. Per-tower JSON report + Markdown clean core assessment

Expects standard abapGit directory layout:
    <repo>/src/
        zcl_*.clas.abap       → ABAP OO classes
        z*.prog.abap          → Reports / programs
        z*.fugr.*.abap        → Function modules
        z*.ddls.asddls        → CDS views (ABAP CDS)
        z*.tabl.xml           → Table definitions
        z*.enho.abap          → Enhancements
        z*.clas.testclasses.abap → Unit tests
        ...

Usage:
    python scripts/analyze_abapgit.py <path-to-abapgit-repo>
    python scripts/analyze_abapgit.py <path> --tower FPR
    python scripts/analyze_abapgit.py <path> --all-towers   # scan subdirs as tower packages
    python scripts/analyze_abapgit.py <path> --output data/abapgit/
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# ── Object type detection by file suffix ─────────────────────────

OBJECT_TYPE_MAP: dict[str, str] = {
    ".clas.abap": "Class",
    ".clas.locals_imp.abap": "Class (Local)",
    ".clas.locals_def.abap": "Class (Local Def)",
    ".clas.testclasses.abap": "Unit Test",
    ".prog.abap": "Report/Program",
    ".fugr.abap": "Function Group",
    ".func.abap": "Function Module",
    ".ddls.asddls": "CDS View",
    ".ddls.asddle": "CDS Entity",
    ".dcls.asdcls": "CDS Access Control",
    ".tabl.xml": "Table/Structure",
    ".dtel.xml": "Data Element",
    ".doma.xml": "Domain",
    ".ttyp.xml": "Table Type",
    ".enho.abap": "Enhancement Implementation",
    ".enhs.xml": "Enhancement Spot",
    ".intf.abap": "Interface",
    ".xslt.xml": "XSLT Transformation",
    ".msag.xml": "Message Class",
    ".nrob.xml": "Number Range",
    ".srvb.xml": "Service Binding",
    ".srvd.xml": "Service Definition",
    ".bdef.asbdef": "Behavior Definition (RAP)",
    ".smim.xml": "MIME Object",
    ".sicf.xml": "ICF Service",
    ".auth.xml": "Authorization Object",
}

# ── Clean Core pattern detection ─────────────────────────────────

# Deprecated / non-clean-core patterns
DEPRECATED_PATTERNS: list[tuple[str, str, str]] = [
    # (regex, finding_id, description)
    (r"\bCALL\s+FUNCTION\s+'RFC_", "RFC_CALL", "Direct RFC function call"),
    (r"\bCALL\s+FUNCTION\s+'BAPI_", "BAPI_CALL", "Direct BAPI call (check if released)"),
    (r"\bCALL\s+FUNCTION\s+'", "FM_CALL", "Function module call (verify released API)"),
    (r"\bCALL\s+TRANSACTION\b", "CALL_TRANSACTION", "CALL TRANSACTION (classic UI navigation)"),
    (r"\bSUBMIT\b", "SUBMIT", "SUBMIT report (classic batch/report chaining)"),
    (r"\bCALL\s+SCREEN\b", "CALL_SCREEN", "CALL SCREEN (classic Dynpro UI)"),
    (r"\bSELECTION-SCREEN\b", "SELECTION_SCREEN", "SELECTION-SCREEN (classic report UI)"),
    (r"\bMODIFICATION\b.*\bADJUSTMENT\b", "MODIFICATION", "Modification adjustment marker"),
    (r"\bSELECT\b.*\bFROM\b\s+(?!z|Z)", "STD_TABLE_READ", "SELECT from standard SAP table (check released CDS)"),
    (r"\bUPDATE\b\s+(?!z|Z)\w+\b", "STD_TABLE_WRITE", "UPDATE on standard SAP table"),
    (r"\bINSERT\b\s+(?!z|Z)\w+\b\s+FROM\b", "STD_TABLE_INSERT", "INSERT into standard SAP table"),
    (r"\bDELETE\b\s+FROM\s+(?!z|Z)\w+\b", "STD_TABLE_DELETE", "DELETE from standard SAP table"),
    (r"\bEXEC\s+SQL\b", "NATIVE_SQL", "Native SQL (non-portable)"),
    (r"\bSYSTEM-CALL\b", "SYSTEM_CALL", "SYSTEM-CALL (kernel-level access)"),
    (r"\bGENERATE\s+SUBROUTINE\b", "DYNAMIC_GEN", "Dynamic code generation"),
    (r"\bMODIFY\s+SCREEN\b", "MODIFY_SCREEN", "MODIFY SCREEN (classic Dynpro manipulation)"),
]

# Positive / clean-core patterns
CLEAN_PATTERNS: list[tuple[str, str, str]] = [
    (r"\bCL_ABAP_", "ABAP_CLEAN_API", "Uses CL_ABAP_* released class"),
    (r"\bCL_BCS\b", "BCS_API", "Business Communication Services (released)"),
    (r"\bCL_HTTP_CLIENT\b", "HTTP_CLIENT", "CL_HTTP_CLIENT for outbound HTTP"),
    (r"\bIF_HTTP_", "HTTP_HANDLER", "HTTP handler interface (ICF)"),
    (r"\b@AbapCatalog\b", "CDS_ANNOTATION", "CDS view annotation (modern data model)"),
    (r"\bdefine\s+(root\s+)?view\s+entity\b", "CDS_VIEW_ENTITY", "CDS View Entity (RAP-ready)"),
    (r"\bdefine\s+behavior\b", "RAP_BDEF", "RAP Behavior Definition"),
    (r"\bRaising\b.*\bCX_", "EXCEPTION_CLASS", "Uses exception classes (clean error handling)"),
    (r"\bCLASS\b.*\bFOR\s+TESTING\b", "UNIT_TEST", "Has unit test class"),
    (r"\bCL_AUNIT_", "AUNIT_FRAMEWORK", "Uses ABAP Unit framework"),
    (r"\bXCO_", "XCO_LIB", "Uses XCO library (released clean-core API)"),
    (r"\bCL_GUI_ALV_GRID\b", "ALV_CLASSIC", "Classic ALV Grid (consider Fiori migration)"),
]

# Integration point patterns
INTEGRATION_PATTERNS: list[tuple[str, str, str]] = [
    (r"\bDESTINATION\s+'([^']+)'", "RFC_DEST", "RFC destination"),
    (r"\bCALL\s+FUNCTION\s+'([^']+)'\s+DESTINATION", "RFC_REMOTE", "Remote function call"),
    (r"\bcl_http_client\s*=>\s*create_by_destination", "HTTP_DEST", "Outbound HTTP via destination"),
    (r"\bcl_http_client\s*=>\s*create_by_url", "HTTP_URL", "Outbound HTTP via URL"),
    (r"\bIDOC_TYPE\s*=\s*'([^']+)'", "IDOC_TYPE", "IDoc type reference"),
    (r"\bEDI_DC40\b", "IDOC_CONTROL", "IDoc control record access"),
    (r"\bCL_PROXY_CLIENT\b", "PROXY_CLIENT", "XI/PI proxy client"),
    (r"\bCL_REST_HTTP_CLIENT\b", "REST_CLIENT", "REST HTTP client"),
    (r"\b/IWBEP/", "ODATA_GATEWAY", "OData Gateway component"),
    (r"\bCL_BCS\b.*\bSEND\b", "EMAIL_SEND", "Email sending via BCS"),
    (r"\bAMQP\b|MQTT\b|EVENT_MESH\b", "EVENT_MESH", "Event/messaging integration"),
]

# Data access patterns
DATA_ACCESS_PATTERNS: list[tuple[str, str]] = [
    (r"\bSELECT\b.*\bFROM\s+(\w+)\b", "READ"),
    (r"\bUPDATE\b\s+(\w+)\b", "WRITE"),
    (r"\bINSERT\b\s+(\w+)\b", "INSERT"),
    (r"\bDELETE\b\s+FROM\s+(\w+)\b", "DELETE"),
    (r"\bMODIFY\b\s+(\w+)\b", "MODIFY"),
]

# Authority check
AUTH_PATTERN = re.compile(r"AUTHORITY-CHECK\s+OBJECT\s+'(\w+)'", re.IGNORECASE)


# ── Data classes ─────────────────────────────────────────────────

@dataclass
class AbapObject:
    name: str
    object_type: str
    file_path: str
    line_count: int = 0
    has_unit_test: bool = False


@dataclass
class Finding:
    finding_id: str
    description: str
    file: str
    line_no: int
    matched_text: str
    category: str  # "deprecated", "clean", "integration"


@dataclass
class DataAccess:
    table_name: str
    access_type: str  # READ, WRITE, INSERT, DELETE, MODIFY
    file: str
    line_no: int


@dataclass
class TowerAnalysis:
    tower: str
    package: str
    scan_path: str
    scan_date: str
    objects: list[AbapObject] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    data_accesses: list[DataAccess] = field(default_factory=list)
    auth_objects: list[str] = field(default_factory=list)
    integration_values: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))

    # Computed summaries
    object_type_counts: dict[str, int] = field(default_factory=dict)
    deprecated_count: int = 0
    clean_count: int = 0
    clean_core_score: float = 0.0
    tables_accessed: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))


# ── Scanner ──────────────────────────────────────────────────────

def _detect_object_type(file_path: Path) -> str | None:
    """Determine ABAP object type from file name suffix."""
    name = file_path.name.lower()
    for suffix, obj_type in sorted(OBJECT_TYPE_MAP.items(), key=lambda x: -len(x[0])):
        if name.endswith(suffix.lower()):
            return obj_type
    return None


def _extract_object_name(file_path: Path) -> str:
    """Extract object name from abapGit filename."""
    name = file_path.stem
    # Remove known suffixes: .clas, .prog, .fugr, .func, etc.
    for suffix in (".clas", ".prog", ".fugr", ".func", ".ddls", ".dcls",
                   ".tabl", ".dtel", ".doma", ".ttyp", ".enho", ".enhs",
                   ".intf", ".xslt", ".msag", ".nrob", ".srvb", ".srvd",
                   ".bdef", ".smim", ".sicf", ".auth",
                   ".locals_imp", ".locals_def", ".testclasses"):
        if name.lower().endswith(suffix):
            name = name[: -len(suffix)]
    return name.upper()


def _is_abap_source(file_path: Path) -> bool:
    """Check if file contains ABAP source code."""
    return file_path.suffix.lower() in (".abap", ".asddls", ".asddle", ".asdcls", ".asbdef")


def scan_abap_source(file_path: Path) -> tuple[int, list[Finding], list[DataAccess], list[str]]:
    """Scan a single ABAP source file for patterns."""
    findings: list[Finding] = []
    data_accesses: list[DataAccess] = []
    auth_objects: list[str] = []
    line_count = 0

    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return 0, findings, data_accesses, auth_objects

    lines = text.splitlines()
    line_count = len(lines)
    rel_path = str(file_path)

    for line_no, line in enumerate(lines, 1):
        stripped = line.strip()
        # Skip comments
        if stripped.startswith("*") or stripped.startswith('"'):
            continue

        # Deprecated patterns
        for pattern, fid, desc in DEPRECATED_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append(Finding(
                    finding_id=fid, description=desc, file=rel_path,
                    line_no=line_no, matched_text=stripped[:120], category="deprecated",
                ))

        # Clean patterns
        for pattern, fid, desc in CLEAN_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append(Finding(
                    finding_id=fid, description=desc, file=rel_path,
                    line_no=line_no, matched_text=stripped[:120], category="clean",
                ))

        # Integration patterns (capture group values)
        for pattern, fid, desc in INTEGRATION_PATTERNS:
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                findings.append(Finding(
                    finding_id=fid, description=desc, file=rel_path,
                    line_no=line_no, matched_text=stripped[:120], category="integration",
                ))

        # Data access
        for pattern, access_type in DATA_ACCESS_PATTERNS:
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                table_name = m.group(1).upper()
                # Skip obvious non-tables (INTO, APPENDING, etc.)
                if table_name not in ("INTO", "APPENDING", "TABLE", "CORRESPONDING", "SINGLE", "UP"):
                    data_accesses.append(DataAccess(
                        table_name=table_name, access_type=access_type,
                        file=rel_path, line_no=line_no,
                    ))

        # Authority checks
        m = AUTH_PATTERN.search(line)
        if m:
            auth_objects.append(m.group(1))

    return line_count, findings, data_accesses, auth_objects


def analyze_directory(scan_path: Path, tower: str = "", package: str = "") -> TowerAnalysis:
    """Analyze all ABAP objects in an abapGit export directory."""
    analysis = TowerAnalysis(
        tower=tower or _infer_tower(scan_path),
        package=package or scan_path.name.upper(),
        scan_path=str(scan_path),
        scan_date=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )

    # Find all source files under src/
    src_dir = scan_path / "src"
    if not src_dir.exists():
        # Try scanning the directory itself (flat layout)
        src_dir = scan_path

    all_files = list(src_dir.rglob("*"))
    test_files: set[str] = set()

    # Pass 1: Inventory objects
    for fp in all_files:
        if not fp.is_file():
            continue
        obj_type = _detect_object_type(fp)
        if obj_type is None:
            continue

        obj_name = _extract_object_name(fp)

        # Track test classes
        if obj_type == "Unit Test":
            test_files.add(obj_name)
            continue

        # Only add primary object file (skip locals, etc.)
        if obj_type in ("Class (Local)", "Class (Local Def)"):
            continue

        line_count = 0
        if _is_abap_source(fp):
            try:
                line_count = len(fp.read_text(encoding="utf-8", errors="replace").splitlines())
            except Exception:
                pass

        analysis.objects.append(AbapObject(
            name=obj_name, object_type=obj_type,
            file_path=str(fp.relative_to(scan_path)), line_count=line_count,
        ))

    # Mark objects that have unit tests
    for obj in analysis.objects:
        if obj.name in test_files:
            obj.has_unit_test = True

    # Pass 2: Scan source for patterns
    for fp in all_files:
        if fp.is_file() and _is_abap_source(fp):
            _lc, findings, data_accesses, auth_objs = scan_abap_source(fp)
            analysis.findings.extend(findings)
            analysis.data_accesses.extend(data_accesses)
            analysis.auth_objects.extend(auth_objs)

    # Compute summaries
    type_counter: Counter[str] = Counter()
    for obj in analysis.objects:
        type_counter[obj.object_type] += 1
    analysis.object_type_counts = dict(type_counter.most_common())

    analysis.deprecated_count = sum(1 for f in analysis.findings if f.category == "deprecated")
    analysis.clean_count = sum(1 for f in analysis.findings if f.category == "clean")

    total_patterns = analysis.deprecated_count + analysis.clean_count
    if total_patterns > 0:
        analysis.clean_core_score = round(
            (analysis.clean_count / total_patterns) * 100, 1
        )

    # Table access summary
    for da in analysis.data_accesses:
        analysis.tables_accessed[da.access_type].add(da.table_name)

    # Extract integration point values
    for f in analysis.findings:
        if f.category == "integration":
            analysis.integration_values[f.finding_id].append(f.matched_text)

    analysis.auth_objects = sorted(set(analysis.auth_objects))

    return analysis


def _infer_tower(path: Path) -> str:
    """Infer tower from directory/package name convention."""
    name = path.name.upper()
    tower_prefixes = {
        "FPR": "FPR", "ZFPR": "FPR", "ZIDM_FPR": "FPR",
        "OTC_IF": "OTC-IF", "ZOTC_IF": "OTC-IF", "ZIDM_OTC_IF": "OTC-IF",
        "OTC_IP": "OTC-IP", "ZOTC_IP": "OTC-IP", "ZIDM_OTC_IP": "OTC-IP",
        "FTS_IF": "FTS-IF", "ZFTS_IF": "FTS-IF", "ZIDM_FTS_IF": "FTS-IF",
        "FTS_IP": "FTS-IP", "ZFTS_IP": "FTS-IP", "ZIDM_FTS_IP": "FTS-IP",
        "PTP": "PTP", "ZPTP": "PTP", "ZIDM_PTP": "PTP",
        "MDM": "MDM", "ZMDM": "MDM", "ZIDM_MDM": "MDM",
        "E2E": "E2E", "ZE2E": "E2E", "ZIDM_E2E": "E2E",
    }
    for prefix, tower in tower_prefixes.items():
        if prefix in name:
            return tower
    return "Unknown"


# ── Output: JSON report ─────────────────────────────────────────

def _serializable(analysis: TowerAnalysis) -> dict:
    """Convert analysis to JSON-serializable dict."""
    d = {
        "tower": analysis.tower,
        "package": analysis.package,
        "scan_path": analysis.scan_path,
        "scan_date": analysis.scan_date,
        "summary": {
            "total_objects": len(analysis.objects),
            "object_type_counts": analysis.object_type_counts,
            "total_source_lines": sum(o.line_count for o in analysis.objects),
            "objects_with_tests": sum(1 for o in analysis.objects if o.has_unit_test),
            "test_coverage_pct": round(
                (sum(1 for o in analysis.objects if o.has_unit_test) / len(analysis.objects) * 100)
                if analysis.objects else 0, 1
            ),
            "clean_core_score": analysis.clean_core_score,
            "deprecated_findings": analysis.deprecated_count,
            "clean_findings": analysis.clean_count,
            "integration_points": sum(1 for f in analysis.findings if f.category == "integration"),
            "auth_objects_used": len(analysis.auth_objects),
        },
        "objects": [asdict(o) for o in sorted(analysis.objects, key=lambda x: (x.object_type, x.name))],
        "deprecated_findings": [
            asdict(f) for f in analysis.findings if f.category == "deprecated"
        ],
        "clean_findings": [
            asdict(f) for f in analysis.findings if f.category == "clean"
        ],
        "integration_findings": [
            asdict(f) for f in analysis.findings if f.category == "integration"
        ],
        "data_access": {
            access_type: sorted(tables)
            for access_type, tables in analysis.tables_accessed.items()
        },
        "auth_objects": analysis.auth_objects,
    }
    return d


# ── Output: Markdown clean core assessment ───────────────────────

def generate_markdown(analysis: TowerAnalysis) -> str:
    """Generate a Markdown clean core assessment document."""
    lines: list[str] = []
    _a = lines.append

    _a(f"# Clean Core Assessment — {analysis.tower} Tower")
    _a("")
    _a(f"**SAP Package**: `{analysis.package}`  ")
    _a(f"**Scan Date**: {analysis.scan_date}  ")
    _a(f"**Source Path**: `{analysis.scan_path}`  ")
    _a("")

    # Summary
    s = _serializable(analysis)["summary"]
    _a("## 1. Executive Summary")
    _a("")
    _a(f"| Metric | Value |")
    _a(f"|--------|-------|")
    _a(f"| Total Objects | {s['total_objects']} |")
    _a(f"| Total Source Lines | {s['total_source_lines']:,} |")
    _a(f"| Clean Core Score | **{s['clean_core_score']}%** |")
    _a(f"| Objects with Unit Tests | {s['objects_with_tests']} ({s['test_coverage_pct']}%) |")
    _a(f"| Deprecated Pattern Hits | {s['deprecated_findings']} |")
    _a(f"| Clean Pattern Hits | {s['clean_findings']} |")
    _a(f"| Integration Points | {s['integration_points']} |")
    _a(f"| Auth Objects Used | {s['auth_objects_used']} |")
    _a("")

    # Score interpretation
    score = analysis.clean_core_score
    if score >= 80:
        _a("> **Assessment**: Strong clean core alignment. Minor refactoring recommended.")
    elif score >= 50:
        _a("> **Assessment**: Moderate clean core alignment. Targeted refactoring needed for deprecated patterns.")
    elif score > 0:
        _a("> **Assessment**: Significant clean core gaps. Comprehensive refactoring plan required.")
    else:
        _a("> **Assessment**: No pattern data collected — manual review recommended.")
    _a("")

    # Object Inventory
    _a("## 2. Object Inventory")
    _a("")
    _a("| Type | Count |")
    _a("|------|-------|")
    for otype, count in analysis.object_type_counts.items():
        _a(f"| {otype} | {count} |")
    _a("")

    _a("### Object Detail")
    _a("")
    _a("| Object Name | Type | Lines | Unit Test |")
    _a("|-------------|------|------:|:---------:|")
    for obj in sorted(analysis.objects, key=lambda x: (x.object_type, x.name)):
        test = "Yes" if obj.has_unit_test else "—"
        _a(f"| `{obj.name}` | {obj.object_type} | {obj.line_count:,} | {test} |")
    _a("")

    # Clean Core Findings
    _a("## 3. Clean Core Analysis")
    _a("")

    # Deprecated
    dep_counter: Counter[str] = Counter()
    for f in analysis.findings:
        if f.category == "deprecated":
            dep_counter[f.finding_id] += 1

    if dep_counter:
        _a("### 3.1 Deprecated / Non-Clean Patterns")
        _a("")
        _a("| Pattern | Count | Impact | Description |")
        _a("|---------|------:|--------|-------------|")
        impact_map = {
            "STD_TABLE_READ": "Medium", "STD_TABLE_WRITE": "High",
            "STD_TABLE_INSERT": "High", "STD_TABLE_DELETE": "High",
            "CALL_TRANSACTION": "Medium", "CALL_SCREEN": "High",
            "SELECTION_SCREEN": "Medium", "NATIVE_SQL": "High",
            "SUBMIT": "Low", "RFC_CALL": "Medium", "BAPI_CALL": "Low",
            "FM_CALL": "Medium", "SYSTEM_CALL": "High", "DYNAMIC_GEN": "High",
            "MODIFY_SCREEN": "Medium", "MODIFICATION": "High",
        }
        descs = {p[1]: p[2] for p in DEPRECATED_PATTERNS}
        for fid, count in dep_counter.most_common():
            impact = impact_map.get(fid, "Medium")
            desc = descs.get(fid, fid)
            _a(f"| `{fid}` | {count} | {impact} | {desc} |")
        _a("")
    else:
        _a("### 3.1 Deprecated / Non-Clean Patterns")
        _a("")
        _a("No deprecated patterns detected.")
        _a("")

    # Clean
    clean_counter: Counter[str] = Counter()
    for f in analysis.findings:
        if f.category == "clean":
            clean_counter[f.finding_id] += 1

    if clean_counter:
        _a("### 3.2 Clean Core Patterns Used")
        _a("")
        _a("| Pattern | Count | Description |")
        _a("|---------|------:|-------------|")
        descs = {p[1]: p[2] for p in CLEAN_PATTERNS}
        for fid, count in clean_counter.most_common():
            _a(f"| `{fid}` | {count} | {descs.get(fid, fid)} |")
        _a("")

    # Data Access
    _a("## 4. Data Access Patterns")
    _a("")
    for access_type in ("READ", "WRITE", "INSERT", "DELETE", "MODIFY"):
        tables = analysis.tables_accessed.get(access_type, set())
        if tables:
            custom = sorted(t for t in tables if t.startswith("Z") or t.startswith("Y"))
            standard = sorted(t for t in tables if not (t.startswith("Z") or t.startswith("Y")))
            _a(f"### 4.{list(('READ','WRITE','INSERT','DELETE','MODIFY')).index(access_type)+1} {access_type}")
            _a("")
            if standard:
                _a(f"**Standard SAP tables** ({len(standard)}): " + ", ".join(f"`{t}`" for t in standard[:30]))
                if len(standard) > 30:
                    _a(f"  ... and {len(standard) - 30} more")
            if custom:
                _a(f"**Custom tables** ({len(custom)}): " + ", ".join(f"`{t}`" for t in custom[:30]))
            _a("")

    # Integration Points
    _a("## 5. Integration Points")
    _a("")
    int_counter: Counter[str] = Counter()
    for f in analysis.findings:
        if f.category == "integration":
            int_counter[f.finding_id] += 1
    if int_counter:
        _a("| Type | Count | Description |")
        _a("|------|------:|-------------|")
        descs = {p[1]: p[2] for p in INTEGRATION_PATTERNS}
        for fid, count in int_counter.most_common():
            _a(f"| `{fid}` | {count} | {descs.get(fid, fid)} |")
        _a("")
    else:
        _a("No integration points detected.")
        _a("")

    # Authorization Objects
    _a("## 6. Authorization Objects")
    _a("")
    if analysis.auth_objects:
        _a("| Auth Object |")
        _a("|-------------|")
        for ao in analysis.auth_objects:
            _a(f"| `{ao}` |")
        _a("")
    else:
        _a("No explicit AUTHORITY-CHECK statements found.")
        _a("")

    # Recommendations
    _a("## 7. Recommendations")
    _a("")
    recs: list[str] = []
    if dep_counter.get("STD_TABLE_WRITE", 0) + dep_counter.get("STD_TABLE_INSERT", 0) > 0:
        recs.append("**Replace direct standard table writes** with released APIs or custom CDS-based services")
    if dep_counter.get("STD_TABLE_READ", 0) > 10:
        recs.append("**Migrate standard table SELECTs** to released CDS views where available")
    if dep_counter.get("CALL_SCREEN", 0) + dep_counter.get("SELECTION_SCREEN", 0) > 0:
        recs.append("**Plan Fiori migration** for classic Dynpro/selection-screen UIs")
    if dep_counter.get("RFC_CALL", 0) > 0:
        recs.append("**Review RFC destinations** — consider migration to CPI/Event Mesh integration")
    if s["test_coverage_pct"] < 30:
        recs.append("**Improve unit test coverage** — current coverage is below 30%")
    if dep_counter.get("NATIVE_SQL", 0) > 0:
        recs.append("**Eliminate native SQL** — replace with Open SQL/CDS for portability")
    if not recs:
        recs.append("Code appears well-aligned with clean core principles. Continue monitoring.")

    for i, rec in enumerate(recs, 1):
        _a(f"{i}. {rec}")
    _a("")

    _a("---")
    _a(f"*Generated by IAO Architecture Pipeline — {analysis.scan_date}*")
    _a("")

    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze abapGit ABAP source for clean core assessment")
    parser.add_argument("path", type=Path, help="Path to abapGit repository root (or parent dir with --all-towers)")
    parser.add_argument("--tower", default="", help="Tower shortcode (FPR, OTC-IF, etc.)")
    parser.add_argument("--all-towers", action="store_true",
                        help="Treat each subdirectory as a separate tower package")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output directory (default: data/abapgit/)")
    args = parser.parse_args()

    workspace = Path(__file__).resolve().parent.parent
    output_dir = args.output or (workspace / "data" / "abapgit")
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.all_towers:
        # Each subdirectory is a package/tower
        subdirs = sorted(d for d in args.path.iterdir() if d.is_dir() and not d.name.startswith("."))
        print(f"Scanning {len(subdirs)} package directories under {args.path}...")
        for sub in subdirs:
            print(f"\n{'=' * 60}")
            print(f"Analyzing: {sub.name}")
            analysis = analyze_directory(sub)
            _write_outputs(analysis, output_dir)
    else:
        print(f"Analyzing: {args.path}")
        analysis = analyze_directory(args.path, tower=args.tower)
        _write_outputs(analysis, output_dir)

    print(f"\nDone. Reports written to {output_dir}/")


def _write_outputs(analysis: TowerAnalysis, output_dir: Path) -> None:
    """Write JSON report and Markdown assessment."""
    slug = f"{analysis.tower}-{analysis.package}".replace(" ", "_")

    # JSON report
    json_path = output_dir / f"{slug}-analysis.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(_serializable(analysis), f, indent=2, default=str)
    print(f"  JSON: {json_path}")

    # Markdown assessment
    md_path = output_dir / f"{slug}-clean-core.md"
    md_path.write_text(generate_markdown(analysis), encoding="utf-8")
    print(f"  Markdown: {md_path}")

    s = _serializable(analysis)["summary"]
    print(f"  Objects: {s['total_objects']}  |  Lines: {s['total_source_lines']:,}  |  "
          f"Clean Core: {s['clean_core_score']}%  |  Tests: {s['test_coverage_pct']}%")


if __name__ == "__main__":
    main()
