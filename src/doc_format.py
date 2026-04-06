"""doc_format.py — Shared document formatting for all IAO pipeline documents.

Provides consistent title pages, TOC anchors, page breaks, footers, and styles
across SAD, RICEFW Register, Testing Register, and future document types.

Usage:
    from src.doc_format import DocFormatter
    fmt = DocFormatter(doc_type="RICEFW Register", subtitle="FPR Tower")
    md = fmt.title_page(title="FPR — RICEFW Register", context_lines=[...])
    md += fmt.toc(sections)
    md += fmt.page_break()
    md += section_content
    # After assembly:
    md = fmt.inject_footers(md)
"""

from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ══════════════════════════════════════════════════════════════
# Constants — shared across all document types
# ══════════════════════════════════════════════════════════════

PAGE_BREAK = '<div style="page-break-before: always;"></div>'

CANONICAL_STYLE = """\
<style>
@media print {
  @page { size: A4; margin: 0; }
  .mermaid { page-break-inside: avoid; break-inside: avoid; overflow: visible; }
  pre, table, blockquote { page-break-inside: avoid; break-inside: avoid; }
  h2, h3, h4 { page-break-after: avoid; break-after: avoid; }
  p { orphans: 3; widows: 3; }
  a[title="View full diagram"],
  a[title="Open full-size SVG"] {
    color: #0071c5 !important;
    text-decoration: underline !important;
    font-size: 10pt !important;
  }
}
.mermaid { overflow: visible; }
.mermaid svg { max-width: 100%; height: auto !important; }
.page-footer {
  padding-top: 8px;
  border-top: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  color: #888;
  margin-top: auto;
  padding: 6px 0;
  background: #fff;
}
@media print {
  .page-footer {
    display: none !important;
  }
}
.page-footer a { color: #00aeef; text-decoration: none; font-weight: 500; }
.page-footer a:hover { color: #0071c5; text-decoration: underline; }
nav.toc { margin: 16px 0 24px 0; }
nav.toc ol, nav.toc ul { list-style: none; padding-left: 0; margin: 0; }
nav.toc > ol > li { margin-bottom: 6px; font-weight: 600; font-size: 14px; }
nav.toc > ol > li > ul { padding-left: 28px; margin-top: 4px; }
nav.toc > ol > li > ul > li { font-weight: 400; font-size: 13px; margin-bottom: 2px; }
nav.toc a { color: #0071c5; text-decoration: none; }
nav.toc a:hover { text-decoration: underline; }
</style>"""


class DocFormatter:
    """Generates consistent formatting elements for any IAO pipeline document."""

    def __init__(
        self,
        doc_type: str = "Architecture Document",
        subtitle: str = "TOGAF BDAT",
        gen_date: str | None = None,
        author: str = "Sajiv Francis",
        release: str = "R1 – R5",
        confidentiality: str = "IAO Architecture Pipeline — Intel Confidential",
        banner_path: str | None = None,
    ):
        self.doc_type = doc_type
        self.subtitle = subtitle
        self.gen_date = gen_date or datetime.now().strftime("%B %Y")
        self.author = author
        self.release = release
        self.confidentiality = confidentiality
        self.banner_path = banner_path  # Relative path to cover_banner.svg

    def title_page(
        self,
        title: str,
        context_lines: list[str] | None = None,
        output_filepath: Path | None = None,
    ) -> str:
        """Generate a title page with banner, title, subtitle, and metadata.

        Args:
            title: Main document title (e.g. "DS-020 — Product Costing")
            context_lines: Optional list of context strings (e.g. "Tower: FPR")
            output_filepath: If provided, computes relative banner path from this location
        """
        # Compute banner path
        banner = self.banner_path
        if not banner and output_filepath:
            banner = os.path.relpath(
                ROOT / "templates" / "assets" / "cover_banner.svg",
                output_filepath.parent,
            ).replace("\\", "/")

        lines = []
        if banner:
            lines.append(f'<div style="text-align:center; padding-top:20px;">')
            lines.append(f'  <img src="{banner}" alt="IAO Architecture" '
                         f'style="width:100%; border-radius:8px;" />')
        else:
            lines.append(f'<div style="text-align:center; padding-top:60px;">')

        lines.append(f'  <h1 style="font-size:36px; margin-top:24px;">{title}</h1>')
        lines.append(f'  <h2 style="font-size:24px;">{self.subtitle}</h2>')

        if context_lines:
            ctx = "<br/>\n  ".join(context_lines)
            lines.append(f'  <p style="font-size:18px; color:#555;">{ctx}</p>')

        lines.append(f'  <p style="font-size:14px; color:#888;">IAO Program · {self.release}<br/>')
        lines.append(f'  Generated: {self.gen_date}<br/>')
        lines.append(f'  {self.author}</p>')
        lines.append(f'  <p style="font-size:12px; color:#aaa;">{self.confidentiality}</p>')
        lines.append(f'</div>')
        lines.append(f'')
        lines.append(CANONICAL_STYLE)
        lines.append(f'')

        return "\n".join(lines) + "\n"

    def toc(self, sections: list[dict]) -> str:
        """Generate a Table of Contents from a section list.

        Args:
            sections: List of dicts with keys:
                - number: str (e.g. "1", "2.1")
                - title: str (e.g. "Executive Summary")
                - level: int (1=top, 2=sub, 3=subsub)
        """
        lines = [
            PAGE_BREAK,
            "",
            '<a id="toc"></a>',
            "",
            "## Table of Contents",
            "",
        ]
        for s in sections:
            anchor = self._make_anchor(s["number"], s["title"])
            indent = "   " * (s.get("level", 1) - 1)
            prefix = f'{s["number"]}.' if s.get("level", 1) == 1 else f'{s["number"]}'
            lines.append(f'{indent}- [{prefix} {s["title"]}](#{anchor})')
        lines.append("")

        return "\n".join(lines) + "\n"

    @staticmethod
    def page_break() -> str:
        """Return a page break marker."""
        return f"\n{PAGE_BREAK}\n\n"

    @staticmethod
    def section_heading(number: str, title: str, level: int = 2) -> str:
        """Return a section heading with page break before it.

        Args:
            number: Section number (e.g. "1", "2.1")
            title: Section title
            level: Heading level (2=##, 3=###)
        """
        hashes = "#" * level
        return f"{PAGE_BREAK}\n\n{hashes} {number} {title}\n\n"

    def inject_footers(self, content: str) -> str:
        """Split content on page breaks and inject numbered footers with TOC backlinks."""
        # Extract title from first <h1>
        title = ""
        m = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r'<[^>]+>', '', m.group(1)).replace("\n", " ").strip()

        # Ensure TOC anchor exists
        if '<a id="toc"></a>' not in content:
            content = content.replace(
                "## Table of Contents",
                '<a id="toc"></a>\n\n## Table of Contents',
                1,
            )

        # Remove any existing footers (idempotent)
        content = re.sub(r'<div class="page-footer">.*?</div>\n?', '', content)

        parts = content.split(PAGE_BREAK)
        if len(parts) <= 1:
            return content

        result = []
        for i, part in enumerate(parts[:-1]):
            page = i + 1
            footer = (
                f'<div class="page-footer">'
                f'<span>Page {page}</span>'
                f'<span><a href="#toc">\u2191 Back to TOC</a></span>'
                f'<span>{title}</span>'
                f'</div>\n'
                f'{PAGE_BREAK}'
            )
            result.append(part + footer)
        result.append(parts[-1])
        return "".join(result)

    @staticmethod
    def _make_anchor(number: str, title: str) -> str:
        """Create a markdown-compatible anchor from section number + title."""
        raw = f"{number} {title}".lower()
        raw = re.sub(r'[^a-z0-9\s-]', '', raw)
        return re.sub(r'\s+', '-', raw.strip())

    @staticmethod
    def completed_ricefw_context(
        total: int,
        completed: int,
        active: int,
        by_type: dict[str, int] | None = None,
    ) -> str:
        """Generate a compact RICEFW completion context block for the SAD.

        Shows a one-paragraph summary + compact metrics table so stakeholders
        understand the overall posture without showing per-object detail.
        """
        pct = (completed / total * 100) if total else 0
        lines = [
            f"> **RICEFW Completion Context:** {completed} of {total} objects "
            f"({pct:.0f}%) are complete. The {active} active items below require attention. "
            f"See the **RICEFW Register** for full detail including completed objects.",
            "",
        ]
        if by_type:
            lines.append("| Type | Completed | Active | Total |")
            lines.append("|------|----------:|-------:|------:|")
            type_labels = {
                "R": "Report", "I": "Interface", "C": "Conversion",
                "E": "Enhancement", "F": "Form", "W": "Workflow",
            }
            for code in ["R", "I", "C", "E", "F", "W"]:
                comp = by_type.get(f"{code}_completed", 0)
                act = by_type.get(f"{code}_active", 0)
                tot = comp + act
                if tot:
                    lines.append(f"| {type_labels.get(code, code)} ({code}) | {comp} | {act} | {tot} |")
            lines.append("")
        return "\n".join(lines) + "\n"
