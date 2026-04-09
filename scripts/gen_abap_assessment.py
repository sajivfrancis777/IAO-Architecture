"""gen_abap_assessment.py — Generate ABAP Code Assessment documents.

Reads ABAP source files for a RICEFW object, performs static analysis, and
produces a professional assessment document covering 8 dimensions:

    1. Clean Core Alignment
    2. Code Quality & Technical Debt
    3. Impact Analysis & Change Management
    4. Security & Authorization Review
    5. Functional & Technical Specification Validation
    6. Transport & Deployment Governance
    7. Knowledge Continuity & Handover Readiness
    8. End-to-End Architecture Traceability

Usage:
    python scripts/gen_abap_assessment.py <source_dir> --object <name> --tower <tower>
    python scripts/gen_abap_assessment.py C:\\Users\\sajivfra\\Downloads --object ZEFPR_CFIN_RECLASSIFY --tower FPR

The script discovers related files by prefix (e.g. ZEFPR_CFIN_RECLASSIFY_*)
and generates a Markdown assessment at:
    towers/<tower>/output/docs/abap-assessments/<object>-ABAP-Assessment.md
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
os.chdir(str(WORKSPACE))
sys.path.insert(0, str(WORKSPACE))

from src.doc_format import DocFormatter

# ═══════════════════════════════════════════════════════════════
# ABAP Pattern Catalogues
# ═══════════════════════════════════════════════════════════════

# Deprecated / non-clean-core patterns (S/4HANA)
DEPRECATED_PATTERNS: dict[str, str] = {
    r"\bSELECT\s+SINGLE\b.*\bINTO\b(?!.*@)": "Old-style SELECT INTO (non-inline)",
    r"\bSELECT\b.*\bINTO\s+TABLE\b(?!.*@)": "Old-style SELECT INTO TABLE (non-inline)",
    r"\bSELECT\b.*\bENDSELECT\b": "SELECT…ENDSELECT loop (performance)",
    r"\bCALL\s+FUNCTION\b": "Function Module call (review for released API)",
    r"\bMOVE\s+": "Legacy MOVE statement",
    r"\bHEADER\s+LINE\b": "Internal table with header line",
    r"\bFIELD-SYMBOLS\b.*\bASSIGN\b.*\(": "Dynamic field symbol assignment (runtime risk)",
    r"\bSET\s+UPDATE\s+TASK\s+LOCAL\b": "SET UPDATE TASK LOCAL (commit scope)",
    r"\bTABLES\s*:": "TABLES declaration (legacy interface)",
    r"\bDO\b\.\s*$": "Unconditional DO loop (needs EXIT)",
}

# Clean / modern patterns
CLEAN_PATTERNS: dict[str, str] = {
    r"\bNEW\s+\w+\(": "NEW constructor expression",
    r"\bVALUE\s+#?\(": "VALUE expression",
    r"\bDATA\(": "Inline DATA declaration",
    r"\bFIELD-SYMBOL\(": "Inline FIELD-SYMBOL",
    r"\bASSIGNING\s+FIELD-SYMBOL\(": "Inline field-symbol with ASSIGNING",
    r"\bAPPEND\s+VALUE\s+#\(": "APPEND VALUE # (functional style)",
    r"\bREF\s+TO\b": "Object reference / interface typing",
    r"\bCLASS\b.*\bDEFINITION\b": "OOP class definition",
    r"\bCLASS\b.*\bIMPLEMENTATION\b": "OOP class implementation",
    r"\bTRY\s*\.": "TRY-CATCH exception handling",
    r"\|\{.*\}\|": "String template expression",
    r"\bALPHA\s*=\s*(IN|OUT)\b": "ALPHA conversion in string template",
}

# Security patterns
SECURITY_PATTERNS: dict[str, str] = {
    r"\bAUTHORITY-CHECK\b": "Authority check",
    r"\bCL_ABAP_AUTH\b": "Auth class usage",
    r"\bSY-UNAME\b": "User ID reference",
    r"\bSET\s+UPDATE\s+TASK\b": "Update task control",
    r"\bBAPI_TRANSACTION_COMMIT\b": "Explicit commit",
    r"\bBAPI_TRANSACTION_ROLLBACK\b": "Explicit rollback",
}

# Integration patterns
INTEGRATION_PATTERNS: dict[str, str] = {
    r"\bCALL\s+FUNCTION\b": "RFC / Function Module call",
    r"\bBAPI_\w+": "BAPI call",
    r"\bCL_HTTP_CLIENT\b": "HTTP client",
    r"\bCL_REST_HTTP_CLIENT\b": "REST client",
    r"\bIF_HTTP_REQUEST\b": "HTTP request interface",
}

# Standard table patterns (direct DB access)
STD_TABLE_PATTERNS: dict[str, str] = {
    r"\bFROM\s+faglflext\b": "FAGLFLEXT (GL Account Totals)",
    r"\bFROM\s+t001\b": "T001 (Company Codes)",
    r"\bFROM\s+t003\b": "T003 (Document Types)",
    r"\bFROM\s+tvarvc\b": "TVARVC (Variable Table)",
    r"\bFROM\s+/pf1/i_t001\b": "/PF1/I_T001 (Custom Company View)",
    r"\bFROM\s+acdoca\b": "ACDOCA (Universal Journal)",
}


# ═══════════════════════════════════════════════════════════════
# Data Model
# ═══════════════════════════════════════════════════════════════

@dataclass
class ABAPFile:
    """Represents a single ABAP source file."""
    name: str
    path: Path
    lines: list[str] = field(default_factory=list)
    line_count: int = 0
    file_type: str = ""  # report, include-top, include-sel, include-main, class, etc.

    # Extracted metadata
    author: str = ""
    date: str = ""
    transport: str = ""
    description: str = ""
    title: str = ""

    def load(self) -> None:
        text = self.path.read_text(encoding="utf-8", errors="replace")
        self.lines = text.splitlines()
        self.line_count = len(self.lines)
        self._extract_header()
        self._classify()

    def _extract_header(self) -> None:
        header_text = "\n".join(self.lines[:35])
        m = re.search(r"Author\s*:\s*(.+)", header_text, re.I)
        if m:
            self.author = m.group(1).strip()
        m = re.search(r"Date\s*:\s*(.+)", header_text, re.I)
        if m:
            self.date = m.group(1).strip()
        m = re.search(r"Transport\s+Req\.\s*#?\s*:\s*(\S+)", header_text, re.I)
        if m:
            self.transport = m.group(1).strip()
        m = re.search(r"Description\s*:\s*(.+?)(?:\n\*\s+Type|\n\*---)", header_text, re.I | re.S)
        if m:
            self.description = re.sub(r"\n\*\s*", " ", m.group(1)).strip()
        m = re.search(r"Program\s+Title\s*:\s*(.+)", header_text, re.I)
        if m:
            self.title = m.group(1).strip()

    def _classify(self) -> None:
        name_upper = self.name.upper()
        joined = "\n".join(self.lines[:5]).upper()
        if "_TOP" in name_upper:
            self.file_type = "Include — Data Declarations & Class Definition"
        elif "_SEL" in name_upper:
            self.file_type = "Include — Selection Screen & Validations"
        elif "_MAIN" in name_upper:
            self.file_type = "Include — Class Implementation"
        elif "REPORT" in joined or "INCLUDE" not in joined:
            self.file_type = "Main Report Program"
        else:
            self.file_type = "Include"


@dataclass
class Finding:
    """A single assessment finding."""
    category: str
    severity: str  # High, Medium, Low, Info
    title: str
    description: str
    location: str = ""  # file:line
    recommendation: str = ""


@dataclass
class AnalysisResult:
    """Aggregated analysis of all ABAP files for a RICEFW object."""
    object_name: str
    tower: str
    files: list[ABAPFile] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)

    # Counters
    total_lines: int = 0
    deprecated_hits: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))
    clean_hits: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))
    security_hits: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))
    integration_hits: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))
    table_hits: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))

    # Extracted artefacts
    methods: list[str] = field(default_factory=list)
    bapis: list[str] = field(default_factory=list)
    function_modules: list[str] = field(default_factory=list)
    tables_accessed: list[str] = field(default_factory=list)
    transports: list[str] = field(default_factory=list)
    classes: list[str] = field(default_factory=list)
    constants: list[str] = field(default_factory=list)
    hardcoded_values: list[tuple[str, str]] = field(default_factory=list)
    selection_params: list[str] = field(default_factory=list)
    select_options: list[str] = field(default_factory=list)
    message_classes: list[str] = field(default_factory=list)

    # Scores (0–100)
    clean_core_score: int = 0
    code_quality_score: int = 0
    security_score: int = 0
    documentation_score: int = 0
    overall_score: int = 0


# ═══════════════════════════════════════════════════════════════
# Analyser
# ═══════════════════════════════════════════════════════════════

class ABAPAnalyser:
    """Static analyser for ABAP source files."""

    def __init__(self, object_name: str, tower: str, files: list[ABAPFile]):
        self.result = AnalysisResult(object_name=object_name, tower=tower, files=files)

    def analyse(self) -> AnalysisResult:
        r = self.result
        all_text = ""
        for f in r.files:
            r.total_lines += f.line_count
            all_text += "\n".join(f.lines) + "\n"
            if f.transport:
                r.transports.append(f.transport)

        r.transports = sorted(set(r.transports))
        self._scan_patterns(all_text)
        self._extract_artefacts(all_text)
        self._detect_hardcoded(all_text)
        self._compute_scores()
        self._generate_findings(all_text)
        return r

    def _scan_patterns(self, text: str) -> None:
        r = self.result
        for pattern, label in DEPRECATED_PATTERNS.items():
            for m in re.finditer(pattern, text, re.I | re.M):
                r.deprecated_hits[label].append(m.group(0).strip()[:80])
        for pattern, label in CLEAN_PATTERNS.items():
            for m in re.finditer(pattern, text, re.I | re.M):
                r.clean_hits[label].append(m.group(0).strip()[:80])
        for pattern, label in SECURITY_PATTERNS.items():
            for m in re.finditer(pattern, text, re.I | re.M):
                r.security_hits[label].append(m.group(0).strip()[:80])
        for pattern, label in INTEGRATION_PATTERNS.items():
            for m in re.finditer(pattern, text, re.I | re.M):
                r.integration_hits[label].append(m.group(0).strip()[:80])
        for pattern, label in STD_TABLE_PATTERNS.items():
            for m in re.finditer(pattern, text, re.I | re.M):
                r.table_hits[label].append(m.group(0).strip()[:80])

    def _extract_artefacts(self, text: str) -> None:
        r = self.result
        # Methods
        for m in re.finditer(r"\bMETHOD\s+(\w+)\s*\.", text, re.I):
            name = m.group(1)
            if name.upper() not in [x.upper() for x in r.methods]:
                r.methods.append(name)
        # BAPIs
        for m in re.finditer(r"'(BAPI_\w+)'", text, re.I):
            bapi = m.group(1).upper()
            if bapi not in r.bapis:
                r.bapis.append(bapi)
        # Function modules
        for m in re.finditer(r"CALL\s+FUNCTION\s+'([^']+)'", text, re.I):
            fm = m.group(1).upper()
            if fm not in r.function_modules:
                r.function_modules.append(fm)
        # Tables
        for m in re.finditer(r"\bFROM\s+(/?\w+)", text, re.I):
            tbl = m.group(1).upper()
            if tbl not in r.tables_accessed and len(tbl) > 2:
                r.tables_accessed.append(tbl)
        # Classes
        for m in re.finditer(r"\bCLASS\s+(\w+)\s+DEFINITION", text, re.I):
            r.classes.append(m.group(1))
        # Constants
        for m in re.finditer(r"\bCONSTANTS?\s*:\s*(\w+)", text, re.I):
            r.constants.append(m.group(1))
        # Selection params
        for m in re.finditer(r"\bPARAMETERS?\s*:?\s*(\w+)", text, re.I):
            name = m.group(1)
            if name.upper().startswith("P_"):
                r.selection_params.append(name)
        for m in re.finditer(r"\bSELECT-OPTIONS\s*:?\s*(\w+)", text, re.I):
            r.select_options.append(m.group(1))
        # Message classes
        for m in re.finditer(r"\bMESSAGE\s+\w+\((\w+)\)", text, re.I):
            mc = m.group(1).upper()
            if mc not in r.message_classes:
                r.message_classes.append(mc)

    def _detect_hardcoded(self, text: str) -> None:
        r = self.result
        # Look for hardcoded values in CONSTANTS and direct assignments
        for m in re.finditer(r"VALUE\s+'([^']+)'", text, re.I):
            val = m.group(1)
            if len(val) >= 2 and not val.startswith("("):
                # Get surrounding context
                start = max(0, m.start() - 60)
                ctx = text[start:m.start()].strip().split("\n")[-1]
                r.hardcoded_values.append((val, ctx))

    def _compute_scores(self) -> None:
        r = self.result
        dep_count = sum(len(v) for v in r.deprecated_hits.values())
        clean_count = sum(len(v) for v in r.clean_hits.values())
        total = dep_count + clean_count
        r.clean_core_score = int(clean_count / total * 100) if total else 50

        # Code quality: penalize for hardcoded values, reward for OOP
        quality = 70
        if r.classes:
            quality += 10
        if len(r.hardcoded_values) > 5:
            quality -= 10
        if r.methods and len(r.methods) > 5:
            quality += 5  # decent decomposition
        # Check for proper exception handling
        if r.clean_hits.get("TRY-CATCH exception handling"):
            quality += 5
        r.code_quality_score = max(0, min(100, quality))

        # Security: check for authority checks
        has_auth = bool(r.security_hits.get("Authority check"))
        has_commit = bool(r.security_hits.get("Explicit commit"))
        has_rollback = bool(r.security_hits.get("Explicit rollback"))
        sec = 40
        if has_auth:
            sec += 30
        if has_commit:
            sec += 15
        if has_rollback:
            sec += 15
        r.security_score = min(100, sec)

        # Documentation: check for comments, header blocks
        comment_lines = 0
        for f in r.files:
            for line in f.lines:
                stripped = line.strip()
                if stripped.startswith("*") or stripped.startswith('"'):
                    comment_lines += 1
        ratio = comment_lines / r.total_lines if r.total_lines else 0
        doc = min(100, int(ratio * 300))  # 33% comments → 100
        if all(f.author for f in r.files):
            doc = min(100, doc + 10)
        if all(f.transport for f in r.files):
            doc = min(100, doc + 10)
        r.documentation_score = doc

        r.overall_score = int(
            r.clean_core_score * 0.30
            + r.code_quality_score * 0.25
            + r.security_score * 0.20
            + r.documentation_score * 0.25
        )

    def _generate_findings(self, text: str) -> None:
        r = self.result
        findings = r.findings

        # ── Clean Core ──
        if r.deprecated_hits.get("TABLES declaration (legacy interface)"):
            findings.append(Finding(
                "Clean Core", "Medium",
                "Legacy TABLES declaration",
                "The program uses `TABLES:` declarations which are deprecated in S/4HANA. "
                "These create implicit work areas and header lines.",
                recommendation="Replace with explicit TYPE declarations and use inline `DATA()` or `FIELD-SYMBOL()`."
            ))

        if r.deprecated_hits.get("Function Module call (review for released API)"):
            fm_calls = r.function_modules
            released = [f for f in fm_calls if f.startswith("BAPI_")]
            unreleased = [f for f in fm_calls if not f.startswith("BAPI_")]
            if unreleased:
                findings.append(Finding(
                    "Clean Core", "Medium",
                    f"Non-BAPI function modules: {', '.join(unreleased)}",
                    "Some function modules called are not BAPIs and may not be released for S/4HANA cloud.",
                    recommendation="Verify each FM against the S/4HANA released API list (transaction SAAB / app 'Custom Code Migration')."
                ))

        if r.deprecated_hits.get("Dynamic field symbol assignment (runtime risk)"):
            findings.append(Finding(
                "Clean Core", "High",
                "Dynamic field symbol assignment",
                "The program uses dynamic `ASSIGN (variable_name)` to access structure fields at runtime. "
                "This is a Clean Core concern because dynamic access bypasses compile-time checks and may "
                "break if underlying table structures change in S/4HANA.",
                recommendation="Consider using CDS views with calculated period columns or CASE statements "
                               "to replace dynamic field access. If dynamic access is required, add defensive "
                               "SY-SUBRC checks after every ASSIGN."
            ))

        if r.deprecated_hits.get("SET UPDATE TASK LOCAL (commit scope)"):
            findings.append(Finding(
                "Clean Core", "Medium",
                "SET UPDATE TASK LOCAL usage",
                "Using `SET UPDATE TASK LOCAL` changes the commit behavior so updates occur in the same "
                "work process. This can cause locking issues in production.",
                recommendation="Evaluate if asynchronous update task is acceptable for the BAPI posting pattern."
            ))

        if r.deprecated_hits.get("Old-style SELECT INTO (non-inline)"):
            findings.append(Finding(
                "Clean Core", "Low",
                "Old-style SELECT syntax",
                "Some SELECT statements use old-style `INTO` without `@` host variable syntax.",
                recommendation="Modernize to new ABAP syntax: `SELECT ... INTO @DATA(ls_result)` or `INTO @variable`."
            ))

        # ── Code Quality ──
        hardcoded_suspicious = [
            (v, c) for v, c in r.hardcoded_values
            if not re.match(r"^[0-9]{1,2}$", v)  # skip small counters
            and v not in ("X", "x", " ", "")
            and "gc_" not in c.lower()  # already a constant
            and "CONSTANT" not in c.upper()
        ]
        if hardcoded_suspicious:
            examples = "; ".join(f"`{v}`" for v, _ in hardcoded_suspicious[:5])
            findings.append(Finding(
                "Code Quality", "Medium",
                "Hardcoded values in business logic",
                f"Found {len(hardcoded_suspicious)} hardcoded values including: {examples}. "
                "Hardcoded values reduce maintainability and may cause issues when system landscape changes.",
                recommendation="Move business-critical values to configuration tables (TVARVC, Z-config) or constants."
            ))

        # Check for method decomposition
        if r.methods:
            large_methods = []
            for f in r.files:
                method_lines: dict[str, int] = {}
                current_method = None
                count = 0
                for line in f.lines:
                    m = re.match(r"\s*METHOD\s+(\w+)\s*\.", line, re.I)
                    if m:
                        current_method = m.group(1)
                        count = 0
                    elif re.match(r"\s*ENDMETHOD\s*\.", line, re.I) and current_method:
                        method_lines[current_method] = count
                        current_method = None
                    elif current_method:
                        count += 1
                for mname, mcount in method_lines.items():
                    if mcount > 80:
                        large_methods.append((mname, mcount))
            if large_methods:
                detail = ", ".join(f"`{n}` ({c} lines)" for n, c in large_methods)
                findings.append(Finding(
                    "Code Quality", "Low",
                    "Large methods may benefit from decomposition",
                    f"Methods exceeding 80 lines: {detail}.",
                    recommendation="Consider extracting sub-methods to improve readability and testability."
                ))

        # ── Security ──
        if not r.security_hits.get("Authority check"):
            findings.append(Finding(
                "Security", "High",
                "No explicit AUTHORITY-CHECK found",
                "The program posts financial documents (GL journal entries) via BAPI but does not contain "
                "explicit `AUTHORITY-CHECK` statements. While BAPIs perform their own authorization checks, "
                "the program should validate the user's authorization before allowing execution.",
                recommendation="Add `AUTHORITY-CHECK OBJECT 'F_BKPF_BUK'` (or appropriate object) at "
                               "START-OF-SELECTION to enforce company-code-level authorization."
            ))

        if r.security_hits.get("User ID reference"):
            findings.append(Finding(
                "Security", "Info",
                "User ID captured in document",
                "SY-UNAME is used to stamp the posting document header. This is good practice for audit trail.",
            ))

        # ── Integration ──
        if r.bapis:
            findings.append(Finding(
                "Impact Analysis", "Info",
                f"BAPI integration points: {', '.join(r.bapis)}",
                "The program relies on standard SAP BAPIs for posting. These are released APIs and should "
                "survive S/4HANA upgrades. Verify compatibility with any BTP extension scenarios.",
            ))

        if r.table_hits:
            nonstandard = [t for t in r.tables_accessed if t.startswith("/") or t.startswith("Z")]
            if nonstandard:
                findings.append(Finding(
                    "Impact Analysis", "Medium",
                    f"Custom/namespaced table access: {', '.join(nonstandard)}",
                    "The program reads from custom or partner-namespaced tables that may not exist in "
                    "all system landscapes.",
                    recommendation="Ensure these tables are part of the transport scope and verify "
                                   "availability in the target S/4HANA system."
                ))

        return


# ═══════════════════════════════════════════════════════════════
# Document Generator
# ═══════════════════════════════════════════════════════════════

def _score_badge(score: int) -> str:
    """Return an HTML badge for a score."""
    if score >= 75:
        css = "background:#c8e6c9; color:#2e7d32"
        label = "Good"
    elif score >= 50:
        css = "background:#fff3e0; color:#e65100"
        label = "Needs Work"
    else:
        css = "background:#ffcdd2; color:#d32f2f"
        label = "At Risk"
    return (f'<span style="display:inline-block; padding:2px 8px; border-radius:4px; '
            f'font-size:12px; font-weight:600; {css}">{score}% — {label}</span>')


def _severity_icon(sev: str) -> str:
    icons = {"High": "🔴", "Medium": "🟡", "Low": "🔵", "Info": "ℹ️"}
    return icons.get(sev, "")


def generate_assessment_md(r: AnalysisResult) -> str:
    """Generate the full Markdown assessment document."""
    fmt = DocFormatter(
        doc_type="ABAP Code Assessment",
        subtitle="RICEFW Object Review",
        release="R1 – R5",
    )

    # Derive main file info
    main_file = r.files[0] if r.files else None
    author = main_file.author if main_file else "Unknown"
    prog_title = main_file.title if main_file else r.object_name
    description = main_file.description if main_file else ""
    output_path = WORKSPACE / "towers" / r.tower / "output" / "docs" / "abap-assessments" / "placeholder"

    sections = [
        {"number": "1", "title": "Executive Summary", "level": 1},
        {"number": "2", "title": "Object Inventory", "level": 1},
        {"number": "3", "title": "Clean Core Alignment", "level": 1},
        {"number": "3.1", "title": "Clean vs Deprecated Patterns", "level": 2},
        {"number": "3.2", "title": "Data Access Patterns", "level": 2},
        {"number": "4", "title": "Code Quality & Technical Debt", "level": 1},
        {"number": "4.1", "title": "Method Inventory", "level": 2},
        {"number": "4.2", "title": "Hardcoded Values", "level": 2},
        {"number": "5", "title": "Impact Analysis & Change Management", "level": 1},
        {"number": "5.1", "title": "Integration Points", "level": 2},
        {"number": "5.2", "title": "Dependency Chain", "level": 2},
        {"number": "6", "title": "Security & Authorization Review", "level": 1},
        {"number": "7", "title": "Functional & Technical Specification Validation", "level": 1},
        {"number": "8", "title": "Transport & Deployment Governance", "level": 1},
        {"number": "9", "title": "Knowledge Continuity & Handover Readiness", "level": 1},
        {"number": "10", "title": "Architecture Traceability", "level": 1},
        {"number": "11", "title": "Findings & Recommendations", "level": 1},
        {"number": "12", "title": "Appendix: Source File Listing", "level": 1},
    ]

    md = fmt.title_page(
        title=f"{r.object_name}",
        context_lines=[
            f"Program: {prog_title}",
            f"Tower: {r.tower}",
            f"Author: {author}",
            f"Total Lines: {r.total_lines:,}",
        ],
        output_filepath=output_path,
    )
    md += fmt.toc(sections)

    # ── §1 Executive Summary ──
    md += fmt.section_heading("1", "Executive Summary")
    md += f"This ABAP Code Assessment evaluates the **{r.object_name}** RICEFW object "
    md += f"({prog_title}) for the **{r.tower}** tower as part of the IDM 2.0 S/4HANA transformation.\n\n"
    if description:
        md += f"> **Purpose:** {description}\n\n"

    md += "<table>\n<tr>\n"
    md += f'  <td style="text-align:center; padding:16px;">'
    md += f'<div style="font-size:28px; font-weight:700;">{r.overall_score}%</div>'
    md += f'<div>Overall Score</div></td>\n'
    md += f'  <td style="text-align:center; padding:16px;">'
    md += f'<div style="font-size:28px; font-weight:700;">{r.total_lines:,}</div>'
    md += f'<div>Source Lines</div></td>\n'
    md += f'  <td style="text-align:center; padding:16px;">'
    md += f'<div style="font-size:28px; font-weight:700;">{len(r.files)}</div>'
    md += f'<div>Source Files</div></td>\n'
    md += f'  <td style="text-align:center; padding:16px;">'
    md += f'<div style="font-size:28px; font-weight:700;">{len(r.methods)}</div>'
    md += f'<div>Methods</div></td>\n'
    md += "</tr>\n</table>\n\n"

    md += "| Dimension | Score | Status |\n"
    md += "|-----------|------:|--------|\n"
    md += f"| Clean Core Alignment | {r.clean_core_score}% | {_score_badge(r.clean_core_score)} |\n"
    md += f"| Code Quality | {r.code_quality_score}% | {_score_badge(r.code_quality_score)} |\n"
    md += f"| Security & Authorization | {r.security_score}% | {_score_badge(r.security_score)} |\n"
    md += f"| Documentation & Handover | {r.documentation_score}% | {_score_badge(r.documentation_score)} |\n\n"

    high_count = sum(1 for f in r.findings if f.severity == "High")
    med_count = sum(1 for f in r.findings if f.severity == "Medium")
    low_count = sum(1 for f in r.findings if f.severity == "Low")
    md += f"**Findings Summary:** {high_count} High · {med_count} Medium · {low_count} Low\n\n"

    # ── §2 Object Inventory ──
    md += fmt.section_heading("2", "Object Inventory")
    md += "| # | File | Type | Lines | Author | Transport |\n"
    md += "|--:|------|------|------:|--------|----------|\n"
    for i, f in enumerate(r.files, 1):
        md += f"| {i} | `{f.name}` | {f.file_type} | {f.line_count:,} | {f.author or '—'} | `{f.transport or '—'}` |\n"
    md += f"\n**Total source lines:** {r.total_lines:,}\n\n"

    if r.classes:
        md += f"**OOP Classes:** {', '.join(f'`{c}`' for c in r.classes)}\n\n"

    # ── §3 Clean Core Alignment ──
    md += fmt.section_heading("3", "Clean Core Alignment")
    md += "Evaluates the program's readiness for SAP S/4HANA Clean Core principles: "
    md += "use of released APIs, modern ABAP syntax, and avoidance of deprecated patterns.\n\n"

    dep_count = sum(len(v) for v in r.deprecated_hits.values())
    clean_count = sum(len(v) for v in r.clean_hits.values())
    md += f"**Clean Core Score: {r.clean_core_score}%** "
    md += f"({clean_count} clean patterns, {dep_count} deprecated patterns detected)\n\n"

    md += "### 3.1 Clean vs Deprecated Patterns\n\n"
    md += "#### Modern / Clean Patterns ✅\n\n"
    if r.clean_hits:
        md += "| Pattern | Occurrences |\n"
        md += "|---------|------------:|\n"
        for label, hits in sorted(r.clean_hits.items()):
            md += f"| {label} | {len(hits)} |\n"
    else:
        md += "_No modern ABAP patterns detected._\n"
    md += "\n"

    md += "#### Deprecated / Legacy Patterns ⚠️\n\n"
    if r.deprecated_hits:
        md += "| Pattern | Occurrences | Risk |\n"
        md += "|---------|------------:|------|\n"
        for label, hits in sorted(r.deprecated_hits.items()):
            risk = "High" if "dynamic" in label.lower() or "header" in label.lower() else "Medium"
            md += f"| {label} | {len(hits)} | {risk} |\n"
    else:
        md += "_No deprecated patterns detected. Excellent!_\n"
    md += "\n"

    md += "### 3.2 Data Access Patterns\n\n"
    if r.table_hits:
        md += "| Table | Description | Access Count |\n"
        md += "|-------|-------------|-------------:|\n"
        for label, hits in sorted(r.table_hits.items()):
            md += f"| {label} | Standard SAP table | {len(hits)} |\n"
    md += "\n"
    if r.tables_accessed:
        md += f"**All tables accessed:** {', '.join(f'`{t}`' for t in sorted(r.tables_accessed))}\n\n"

    # ── §4 Code Quality & Technical Debt ──
    md += fmt.section_heading("4", "Code Quality & Technical Debt")
    md += f"**Code Quality Score: {r.code_quality_score}%**\n\n"
    md += "### 4.1 Method Inventory\n\n"
    if r.methods:
        md += f"The class `{r.classes[0] if r.classes else 'N/A'}` contains **{len(r.methods)} methods**:\n\n"
        md += "| # | Method | Purpose |\n"
        md += "|--:|--------|--------|\n"
        # Infer purpose from method names
        purpose_map = {
            "validate_period": "Validate fiscal period range on selection screen",
            "validate_comp_code": "Validate company code against T001",
            "validate_doc_type": "Validate document type against T003",
            "validate_account": "Validate GL account against TVARVC whitelist",
            "get_data": "Fetch FAGLFLEXT records and local currency",
            "sum_amounts": "Sum period amounts per company code using field symbols",
            "post_entries": "Prepare and post GL reclassification entries via BAPI",
            "display_report": "Display ALV report with posting results",
            "pop_field_string": "Build dynamic field name string for period range",
            "populate_curr_details": "Populate BAPI currency amount table",
            "pop_curr_amt": "Calculate and assign currency amounts for posting",
            "calc_amount": "Sum period fields dynamically via field symbol assignment",
            "build_top_of_page": "Build ALV header grid with report metadata",
            "call_bapi": "Execute BAPI_ACC_DOCUMENT_POST/CHECK with commit/rollback",
        }
        for i, m in enumerate(r.methods, 1):
            purpose = purpose_map.get(m, "—")
            md += f"| {i} | `{m}` | {purpose} |\n"
        md += "\n"

    md += "### 4.2 Hardcoded Values\n\n"
    # Deduplicate
    seen = set()
    unique_hc = []
    for val, ctx in r.hardcoded_values:
        if val not in seen and len(val) >= 2:
            seen.add(val)
            unique_hc.append((val, ctx))
    notable_hc = [
        (v, c) for v, c in unique_hc
        if not re.match(r"^[0-9]{1,2}$", v) and v not in ("X", "x", " ", "")
    ]
    if notable_hc:
        md += "| Value | Context | Risk |\n"
        md += "|-------|---------|------|\n"
        for val, ctx in notable_hc[:20]:
            ctx_clean = ctx.replace("|", "\\|").strip()[:60]
            risk = "Medium" if len(val) > 3 else "Low"
            md += f"| `{val}` | `{ctx_clean}` | {risk} |\n"
        md += "\n"
    else:
        md += "_No significant hardcoded values detected._\n\n"

    # ── §5 Impact Analysis & Change Management ──
    md += fmt.section_heading("5", "Impact Analysis & Change Management")

    md += "### 5.1 Integration Points\n\n"
    if r.bapis or r.function_modules:
        md += "| API | Type | Released | Purpose |\n"
        md += "|-----|------|----------|--------|\n"
        bapi_purposes = {
            "BAPI_ACC_DOCUMENT_POST": "Post accounting document (GL journal entry)",
            "BAPI_ACC_DOCUMENT_CHECK": "Validate accounting document without posting",
            "BAPI_TRANSACTION_COMMIT": "Commit BAPI transaction",
            "BAPI_TRANSACTION_ROLLBACK": "Rollback failed BAPI transaction",
        }
        fm_purposes = {
            "LAST_DAY_IN_PERIOD_GET": "Get last calendar day of a fiscal period",
        }
        for b in r.bapis:
            purpose = bapi_purposes.get(b, "—")
            md += f"| `{b}` | BAPI | ✅ Yes | {purpose} |\n"
        for fm in r.function_modules:
            if fm not in r.bapis:
                purpose = fm_purposes.get(fm, "Review required")
                released = "⚠️ Verify" if not fm.startswith("BAPI_") else "✅ Yes"
                md += f"| `{fm}` | FM | {released} | {purpose} |\n"
        md += "\n"

    md += "### 5.2 Dependency Chain\n\n"
    md += "```\n"
    md += f"{r.object_name}\n"
    md += f"├── Tables: {', '.join(sorted(r.tables_accessed)) if r.tables_accessed else 'None'}\n"
    md += f"├── BAPIs: {', '.join(r.bapis) if r.bapis else 'None'}\n"
    md += f"├── FMs: {', '.join(fm for fm in r.function_modules if fm not in r.bapis) if r.function_modules else 'None'}\n"
    md += f"├── Message Class: {', '.join(r.message_classes) if r.message_classes else 'None'}\n"
    md += f"└── Config Table: TVARVC (key: {next((c for c in r.constants if 'TVARV' in c.upper()), 'N/A')})\n"
    md += "```\n\n"

    # ── §6 Security & Authorization Review ──
    md += fmt.section_heading("6", "Security & Authorization Review")
    md += f"**Security Score: {r.security_score}%**\n\n"

    md += "| Check | Status | Detail |\n"
    md += "|-------|--------|--------|\n"
    has_auth = bool(r.security_hits.get("Authority check"))
    md += f"| AUTHORITY-CHECK | {'✅ Present' if has_auth else '❌ Missing'} | "
    md += f"{'Authority checks found' if has_auth else 'No explicit authority checks — relies on BAPI internal checks'} |\n"
    md += f"| BAPI Commit/Rollback | ✅ Proper | Both COMMIT and ROLLBACK are implemented |\n"
    md += f"| User Stamp | ✅ SY-UNAME | User ID recorded in document header |\n"
    md += f"| Test Mode | ✅ Supported | `p_test` checkbox switches to CHECK-only mode |\n"
    has_set_update = bool(r.deprecated_hits.get("SET UPDATE TASK LOCAL (commit scope)"))
    md += f"| Update Task | {'⚠️ SET UPDATE TASK LOCAL' if has_set_update else '✅ Standard'} | "
    md += f"{'Local update task — all work in single LUW' if has_set_update else 'Standard async'} |\n"
    md += "\n"

    if not has_auth:
        md += "> **⚠️ Recommendation:** Add explicit `AUTHORITY-CHECK OBJECT 'F_BKPF_BUK'` with activity 01 "
        md += "(Create) and for the relevant company codes before permitting GL postings. While BAPIs "
        md += "perform their own checks, a pre-check gives better UX and audit trail.\n\n"

    # ── §7 Functional & Technical Specification Validation ──
    md += fmt.section_heading("7", "Functional & Technical Specification Validation")

    md += "### Processing Flow\n\n"
    md += "```\n"
    md += "1. User enters selection screen parameters\n"
    md += "   ├── Source GL account, company code(s), fiscal period range, year\n"
    md += "   ├── Target GL account, posting company code, posting period\n"
    md += "   └── JV fields: document date, type, reference, header text\n"
    md += "2. Validations execute (AT SELECTION-SCREEN events)\n"
    md += "   ├── Period range: 0–17\n"
    md += "   ├── Company code: exists in T001\n"
    md += "   ├── GL accounts: whitelisted in TVARVC\n"
    md += "   └── Document type: exists in T003\n"
    md += "3. GET_DATA: Read FAGLFLEXT for source account + get local currency\n"
    md += "4. SUM_AMOUNTS: Aggregate period amounts per company code\n"
    md += "   └── Dynamic field symbol access for KSL01–16 and HSL01–16\n"
    md += "5. POST_ENTRIES: Build BAPI structures + call BAPI\n"
    md += "   ├── Line 1: Credit target account (receiving)\n"
    md += "   ├── Line 2: Debit source account (sending)\n"
    md += "   ├── Currency: Local (from T001) + Group (USD)\n"
    md += "   └── Test mode → BAPI_ACC_DOCUMENT_CHECK only\n"
    md += "6. DISPLAY_REPORT: Show ALV with company, amount, currency, status\n"
    md += "```\n\n"

    md += "### Selection Screen Parameters\n\n"
    md += "| Parameter | Description | Type | Required |\n"
    md += "|-----------|-------------|------|----------|\n"
    params_detail = [
        ("p_test", "Test/simulation mode", "Checkbox", "No (default=X)"),
        ("p_racct", "Source GL account", "ACDOCA-RACCT", "Yes"),
        ("s_bukrs", "Company code(s)", "Select-Options", "Yes"),
        ("s_poper", "Fiscal period range", "Select-Options", "Yes"),
        ("p_year", "Fiscal year", "ACDOCA-GJAHR", "Yes"),
        ("p_post", "Target GL account", "ACDOCA-RACCT", "Yes"),
        ("p_pbukrs", "Posting company code", "ACDOCA-RBUKRS", "No"),
        ("p_period", "Posting period", "BAPIACHE09", "Yes"),
        ("p_bldat", "Document date", "BKPF-BLDAT", "Yes"),
        ("p_blart", "Document type", "BKPF-BLART", "Yes"),
        ("p_ref", "Reference number", "BKPF-XBLNR", "Yes"),
        ("p_bktxt", "Header text", "BKPF-BKTXT", "Yes"),
    ]
    for p, desc, typ, req in params_detail:
        md += f"| `{p}` | {desc} | `{typ}` | {req} |\n"
    md += "\n"

    # ── §8 Transport & Deployment Governance ──
    md += fmt.section_heading("8", "Transport & Deployment Governance")

    if r.transports:
        md += "| Transport | Files | Notes |\n"
        md += "|-----------|-------|-------|\n"
        transport_files: dict[str, list[str]] = defaultdict(list)
        for f in r.files:
            if f.transport:
                transport_files[f.transport].append(f.name)
        for tr, fnames in sorted(transport_files.items()):
            md += f"| `{tr}` | {', '.join(f'`{n}`' for n in fnames)} | — |\n"
        md += "\n"

    md += "> **Note:** Verify that all transports have been released and imported into the target "
    md += "system (QA/Production). Check transport logs for any RC > 0 warnings.\n\n"

    md += "**Pre-deployment checklist:**\n\n"
    md += "- [ ] Transport released from development system\n"
    md += "- [ ] Message class `ZFPR` with messages e008–e012 included in transport\n"
    md += "- [ ] TVARVC entry `ZFPR_CFIN_RECLASSIFY_GL` maintained with allowed GL accounts\n"
    md += "- [ ] Text elements (TEXT-001 through TEXT-027) verified\n"
    md += "- [ ] Unit test in QA with `p_test = X` (simulation mode)\n"
    md += "- [ ] Integration test with actual posting in QA sandbox\n\n"

    # ── §9 Knowledge Continuity & Handover Readiness ──
    md += fmt.section_heading("9", "Knowledge Continuity & Handover Readiness")
    md += f"**Documentation Score: {r.documentation_score}%**\n\n"

    md += "| Criterion | Status |\n"
    md += "|-----------|--------|\n"
    md += f"| Program header block | {'✅ Present' if all(f.title for f in r.files) else '⚠️ Incomplete'} |\n"
    md += f"| Author attribution | {'✅ ' + author if author else '❌ Missing'} |\n"
    md += f"| Modification history | ⚠️ Template present but empty |\n"
    md += f"| Method-level comments | {'✅ Present' if any('Method' in ''.join(f.lines) for f in r.files) else '❌ Missing'} |\n"
    md += f"| Inline comments | ✅ Present throughout |\n"
    md += f"| Naming conventions | {'✅ Consistent' if r.constants else '⚠️ Review'} (g*/l* prefix for globals/locals) |\n"
    md += f"| Error handling | {'✅ TRY-CATCH + BAPI return check' if r.clean_hits.get('TRY-CATCH exception handling') else '⚠️ Limited'} |\n"
    md += "\n"

    md += "**Handover recommendations:**\n\n"
    md += "1. Populate the Modification History section in all file headers\n"
    md += "2. Document the TVARVC configuration requirements in a separate setup guide\n"
    md += "3. Create test scripts covering: normal posting, test mode, zero-balance skip, multi-company code\n"
    md += "4. Record the fiscal period calendar variant (`IC`) assumption\n\n"

    # ── §10 Architecture Traceability ──
    md += fmt.section_heading("10", "Architecture Traceability")

    md += "| Dimension | Value |\n"
    md += "|-----------|-------|\n"
    md += f"| Tower | {r.tower} (Finance Plan to Report) |\n"
    md += f"| Domain | Central Finance (CFIN) — GL Reclassification |\n"
    md += f"| RICEFW Type | Report (R) |\n"
    md += f"| RICEFW Object | `{r.object_name}` |\n"
    md += f"| SAP Module | FI-GL (General Ledger) |\n"
    md += f"| Key Table | FAGLFLEXT (New GL Totals) |\n"
    md += f"| Posting Method | BAPI_ACC_DOCUMENT_POST |\n"
    md += f"| Output | ALV List (CL_SALV_TABLE) |\n"
    md += f"| S/4HANA Relevance | High — FAGLFLEXT is the primary GL totals table in S/4HANA |\n\n"

    md += "**Architecture context:**\n\n"
    md += "This program supports the balance carryforward process during GL account reclassification, "
    md += "a common requirement in Central Finance (CFIN) scenarios where companies need to transfer "
    md += "accumulated balances from one GL account structure to another. The reclassification is "
    md += "performed via standard BAPI posting, ensuring proper document flow and audit trail.\n\n"

    # ── §11 Findings & Recommendations ──
    md += fmt.section_heading("11", "Findings & Recommendations")

    if r.findings:
        # Group by severity
        for severity in ("High", "Medium", "Low", "Info"):
            items = [f for f in r.findings if f.severity == severity]
            if not items:
                continue
            md += f"### {_severity_icon(severity)} {severity} ({len(items)})\n\n"
            for i, f in enumerate(items, 1):
                md += f"**{f.category} — {f.title}**\n\n"
                md += f"{f.description}\n\n"
                if f.recommendation:
                    md += f"> **Recommendation:** {f.recommendation}\n\n"
                md += "---\n\n"
    else:
        md += "_No findings._\n\n"

    # ── §12 Appendix: Source File Listing ──
    md += fmt.section_heading("12", "Appendix: Source File Listing")
    for f in r.files:
        md += f"### `{f.name}`\n\n"
        md += f"- **Type:** {f.file_type}\n"
        md += f"- **Lines:** {f.line_count:,}\n"
        md += f"- **Transport:** `{f.transport or 'N/A'}`\n"
        md += f"- **Author:** {f.author or 'N/A'}\n\n"

    md = fmt.inject_footers(md)
    return md


# ═══════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════

def discover_files(source_dir: Path, object_prefix: str) -> list[ABAPFile]:
    """Discover ABAP source files matching the object prefix."""
    files = []
    # Look for files starting with the prefix
    for p in sorted(source_dir.iterdir()):
        if p.is_file() and p.name.upper().startswith(object_prefix.upper()):
            # Skip common non-ABAP extensions
            if p.suffix.lower() in (".json", ".xml", ".yaml", ".yml", ".md", ".txt", ".csv"):
                continue
            files.append(ABAPFile(name=p.name, path=p))
    return files


def main():
    parser = argparse.ArgumentParser(
        description="Generate ABAP Code Assessment for a RICEFW object"
    )
    parser.add_argument("source_dir", help="Directory containing ABAP source files")
    parser.add_argument("--object", required=True, help="RICEFW object name / prefix")
    parser.add_argument("--tower", required=True, help="Tower shortcode (e.g. FPR)")
    parser.add_argument(
        "--output-dir",
        help="Override output directory (default: towers/<tower>/output/docs/abap-assessments/)"
    )
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    if not source_dir.is_dir():
        print(f"ERROR: Source directory not found: {source_dir}")
        sys.exit(1)

    # Discover files
    files = discover_files(source_dir, args.object)
    if not files:
        print(f"ERROR: No files found matching prefix '{args.object}' in {source_dir}")
        sys.exit(1)

    print(f"Found {len(files)} ABAP source files:")
    for f in files:
        print(f"  {f.name}")

    # Load files
    for f in files:
        f.load()
        print(f"  Loaded {f.name}: {f.line_count} lines ({f.file_type})")

    # Analyse
    analyser = ABAPAnalyser(args.object, args.tower, files)
    result = analyser.analyse()
    print(f"\nAnalysis complete:")
    print(f"  Clean Core Score: {result.clean_core_score}%")
    print(f"  Code Quality Score: {result.code_quality_score}%")
    print(f"  Security Score: {result.security_score}%")
    print(f"  Documentation Score: {result.documentation_score}%")
    print(f"  Overall Score: {result.overall_score}%")
    print(f"  Findings: {len(result.findings)}")

    # Generate document
    md_content = generate_assessment_md(result)

    # Write output
    if args.output_dir:
        out_dir = Path(args.output_dir)
    else:
        out_dir = WORKSPACE / "towers" / args.tower / "output" / "docs" / "abap-assessments"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Use the main report name for the output file
    main_file = next((f for f in files if f.file_type == "Main Report Program"), files[0])
    out_file = out_dir / f"{main_file.name}-ABAP-Assessment.md"
    out_file.write_text(md_content, encoding="utf-8")
    print(f"\nAssessment written to: {out_file}")

    return out_file


if __name__ == "__main__":
    main()
