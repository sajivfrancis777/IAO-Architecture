"""gen_pdf.py -- Convert generated Architecture MD files to styled HTML + PDF.

Produces:
  1. Standalone HTML with embedded CSS (viewable in any browser)
  2. PDF via the HTML (uses Markdown -> HTML -> fpdf2 pipeline)

Usage:
    python gen_pdf.py                     # all towers (HTML + PDF)
    python gen_pdf.py --tower FPR         # single tower
    python gen_pdf.py --tower FPR --cap DS-020
    python gen_pdf.py --html-only         # skip PDF, just produce HTML
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.fenced_code import FencedCodeExtension

WORKSPACE = Path(__file__).resolve().parent.parent
os.chdir(str(WORKSPACE))

# CSS for print-friendly, professional-looking architecture documents
DOCUMENT_CSS = """
@page {
    size: A4;
    margin: 0;   /* zero margin suppresses browser default header/footer */
}
body {
    font-family: "Segoe UI", Calibri, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1a1a1a;
    max-width: 210mm;
    margin: 0 auto;
    padding: 15mm;
    background: #fff;
}
h1 {
    font-size: 22pt;
    color: #00285a;
    border-bottom: 3px solid #0071c5;
    padding-bottom: 8px;
    margin-top: 30px;
    page-break-before: always;
}
h1:first-of-type { page-break-before: avoid; }
h2 {
    font-size: 16pt;
    color: #00285a;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4px;
    margin-top: 24px;
    page-break-after: avoid;
    break-after: avoid;
}
h3 {
    font-size: 13pt;
    color: #0071c5;
    margin-top: 18px;
    page-break-after: avoid;
    break-after: avoid;
}
h4 {
    font-size: 11pt;
    color: #333;
    margin-top: 14px;
    page-break-after: avoid;
    break-after: avoid;
}
p {
    orphans: 3;
    widows: 3;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
}
th {
    background: #00285a;
    color: #fff;
    font-weight: 600;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #00285a;
}
td {
    padding: 5px 8px;
    border: 1px solid #ddd;
    vertical-align: top;
}
tr:nth-child(even) td { background: #f5f8fc; }
tr:hover td { background: #e8f0fe; }
code {
    font-family: "Cascadia Code", "Consolas", monospace;
    font-size: 9pt;
    background: #f0f0f0;
    padding: 1px 4px;
    border-radius: 3px;
}
pre {
    background: #1e1e1e;
    color: #d4d4d4;
    padding: 12px;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 8.5pt;
    line-height: 1.4;
    page-break-inside: avoid;
    break-inside: avoid;
}
pre code { background: none; padding: 0; color: inherit; }
blockquote {
    border-left: 4px solid #0071c5;
    background: #f5f8fc;
    margin: 12px 0;
    padding: 8px 16px;
    color: #333;
    page-break-inside: avoid;
    break-inside: avoid;
}
.mermaid-placeholder {
    background: #f5f8fc;
    border: 1px dashed #0071c5;
    border-radius: 4px;
    padding: 16px;
    margin: 12px 0;
    text-align: center;
    color: #666;
    font-style: italic;
}
.mermaid {
    background: #fafbfd;
    border: 1px solid #e0e4ea;
    border-radius: 6px;
    padding: 16px 12px;
    margin: 12px 0;
    overflow: visible;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
}
.mermaid svg {
    max-width: 100%;
    height: auto;
    max-height: 85vh;
}
.header-bar {
    background: #00285a;
    color: #fff;
    padding: 16px 24px;
    margin: -15mm -15mm 20px -15mm;
    font-size: 9pt;
}
.header-bar h1 {
    color: #fff;
    border: none;
    margin: 0;
    padding: 0;
    font-size: 20pt;
    page-break-before: avoid;
}
.header-bar .subtitle { color: #a8c7e8; font-size: 10pt; }
.footer {
    font-size: 8pt;
    color: #888;
    text-align: center;
    margin-top: 30px;
    padding-top: 10px;
    border-top: 1px solid #ddd;
}
.page-section {
    display: flex;
    flex-direction: column;
    min-height: calc(100vh - 40px);
    box-sizing: border-box;
}
.page-footer {
    margin-top: auto;
    padding-top: 8px;
    border-top: 1px solid #ddd;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 9pt;
    color: #888;
    padding: 6px 12px;
    background: #fff;
}
.page-footer a { color: #0071c5; text-decoration: none; }
.page-footer a:hover { text-decoration: underline; }
a { color: #0071c5; text-decoration: none; }
a:hover { text-decoration: underline; }
hr { border: none; border-top: 1px solid #ccc; margin: 20px 0; }
strong { color: #00285a; }

/* ---- Floating PDF download button ---- */
.pdf-download-btn {
    position: fixed;
    top: 72px;
    right: 24px;
    z-index: 9999;
    background: #00285a;
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 12px;
    font-family: "Segoe UI", Arial, sans-serif;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    transition: background 0.2s;
}
.pdf-download-btn:hover { background: #0071c5; }

@media print {
    body { padding: 20mm 15mm; max-width: none; }
    .header-bar { margin: 0 0 20px 0; }
    .no-print, .pdf-download-btn { display: none !important; }
    h1, h2, h3, h4 { page-break-after: avoid; break-after: avoid; }
    table, pre, blockquote { page-break-inside: avoid; break-inside: avoid; }
    p { orphans: 3; widows: 3; }

    /* Page sections: auto height in print — page-break divs handle pagination */
    .page-section {
        min-height: auto;
        display: block;
    }
    .page-footer { page-break-inside: avoid; break-inside: avoid; }

    /* Mermaid diagrams: constrain to page, avoid spill-over to next page */
    .mermaid {
        page-break-inside: avoid;
        break-inside: avoid;
        overflow: visible;
        max-height: 85vh;
        margin: 8px 0;
    }
    .mermaid svg {
        max-width: 100%;
        max-height: 80vh;
        height: auto;
        width: auto;
    }

    /* Diagram links: visible + clickable in PDF */
    a[title="View full diagram"],
    a[title="Open full-size SVG"] {
        color: #0071c5 !important;
        text-decoration: underline !important;
        font-size: 10pt !important;
    }

    /* Tighten spacing in print for professional PDF output */
    h2 { margin-top: 18px; margin-bottom: 8px; }
    h3 { margin-top: 14px; margin-bottom: 6px; }
    h4 { margin-top: 10px; margin-bottom: 4px; }
    table { margin: 8px 0; }
    blockquote { margin: 8px 0; padding: 6px 14px; }
}
"""

MERMAID_JS = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" crossorigin="anonymous">
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.esm.min.mjs';
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    securityLevel: 'loose',
    flowchart: {
      curve: 'basis',
      padding: 16,
      nodeSpacing: 50,
      rankSpacing: 60,
      useMaxWidth: true
    },
    themeVariables: {
      primaryColor: '#e8f0fe',
      primaryBorderColor: '#0071c5',
      primaryTextColor: '#1a1a1a',
      lineColor: '#37474F',
      secondaryColor: '#f5f8fc',
      tertiaryColor: '#fff',
      fontSize: '14px',
      fontFamily: 'Segoe UI, Arial, sans-serif'
    }
  });
</script>
<script>
  // Open rendered Mermaid diagram as full-size SVG in a new browser tab.
  // Works on SharePoint, GitHub Pages, localhost — no file system dependency.
  document.addEventListener('click', function(e) {
    var link = e.target.closest('a[title="Open full-size SVG"]');
    if (!link) return;
    // Walk backwards from the link div to find the preceding .mermaid container
    var container = link.closest('div');
    var prev = container;
    while (prev && prev.previousElementSibling) {
      prev = prev.previousElementSibling;
      if (prev.classList && prev.classList.contains('mermaid')) break;
    }
    if (!prev || !prev.classList.contains('mermaid')) return;
    var svgEl = prev.querySelector('svg');
    if (!svgEl) return;
    e.preventDefault();
    // Clone SVG with full dimensions for standalone viewing
    var clone = svgEl.cloneNode(true);
    clone.removeAttribute('style');
    clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    var svgXml = new XMLSerializer().serializeToString(clone);
    var blob = new Blob([svgXml], {type: 'image/svg+xml'});
    window.open(URL.createObjectURL(blob), '_blank');
  });
</script>
"""

_PAGE_BREAK_HTML = '<div style="page-break-before: always;"></div>'


def _wrap_page_sections(html_body: str) -> str:
    """Wrap each page-break section in a <div class="page-section"> flex container.

    This pushes the .page-footer to the bottom of each page via CSS flex
    (margin-top: auto).  Must be called AFTER markdown conversion — doing
    this at the Markdown stage would cause Python-Markdown to skip processing
    inside block-level HTML elements.
    """
    parts = re.split(
        r'<div style="page-break-before:\s*always;\s*">\s*</div>',
        html_body,
    )
    if len(parts) <= 1:
        return html_body

    wrapped = []
    for i, part in enumerate(parts):
        wrapped.append(f'<div class="page-section">\n{part}\n</div>')
        if i < len(parts) - 1:
            wrapped.append(_PAGE_BREAK_HTML)
    return "\n".join(wrapped)


def md_to_html(md_content: str, title: str = "", md_path: Path | None = None) -> str:
    """Convert Markdown content to a standalone HTML document."""
    # Convert mermaid code blocks to <div class="mermaid"> for Mermaid.js rendering.
    # The JS library renders full, interactive diagrams in the browser.
    # SVG and Mermaid Live links below each diagram are preserved from the MD source.
    def replace_mermaid(match):
        code = match.group(1).strip()
        return f'<div class="mermaid">\n{code}\n</div>'

    processed = re.sub(
        r'```mermaid\s*\n(.*?)```',
        replace_mermaid,
        md_content,
        flags=re.DOTALL,
    )

    # Fix legacy overflow:hidden in embedded <style> blocks from older MD files.
    # These clip Mermaid diagrams when printing to PDF.
    processed = processed.replace('overflow: hidden', 'overflow: visible')
    processed = processed.replace('overflow-x: auto; overflow-y: auto', 'overflow: visible')

    # Fix legacy position:fixed on page footers — causes stacking in multi-page docs.
    # Replace with flex-based margin-top:auto positioning inside page-section containers.
    processed = re.sub(
        r'\.page-footer\s*\{[^}]*position:\s*fixed[^}]*\}',
        '.page-footer { margin-top:auto; padding-top:8px; border-top:1px solid #ddd; '
        'display:flex; justify-content:space-between; align-items:center; '
        'font-size:11px; color:#888; padding:6px 12px; background:#fff; }',
        processed,
    )
    # Also fix the @media print block for page-footer
    processed = re.sub(
        r'@media\s+print\s*\{\s*\.page-footer\s*\{[^}]*position:\s*fixed[^}]*\}\s*\}',
        '@media print { .page-footer { page-break-inside:avoid; break-inside:avoid; } }',
        processed,
    )

    # Convert MD to HTML
    extensions = [
        TableExtension(),
        TocExtension(permalink=False, toc_depth="1-4"),
        FencedCodeExtension(),
        "markdown.extensions.sane_lists",
        "markdown.extensions.smarty",
    ]
    html_body = markdown.markdown(processed, extensions=extensions)

    # Post-processing: wrap each page section in a flex container
    # so that footers are pushed to the bottom of each page.
    # This MUST happen after markdown conversion — wrapping raw Markdown
    # in <div> tags causes Python-Markdown to skip Markdown processing
    # inside the block-level HTML elements.
    html_body = _wrap_page_sections(html_body)

    # Wrap in full HTML document
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{DOCUMENT_CSS}</style>
    {MERMAID_JS}
</head>
<body>
<button class="pdf-download-btn" onclick="window.print()" title="Print / Save as PDF">&#128196; Download PDF</button>
{html_body}
<div class="footer">
    IAO Architecture Document | Intel IDM 2.0 | Generated by IAO Architecture Pipeline
</div>
</body>
</html>"""
    return html


def convert_file(md_path: Path, html_only: bool = False) -> tuple[Path | None, Path | None]:
    """Convert a single MD file to HTML (and optionally PDF)."""
    md_content = md_path.read_text(encoding="utf-8")
    # Build a readable title from the filename
    title = md_path.stem
    for suffix in ("-Architecture", "-RICEFW-Tracker", "-Testing-Report"):
        title = title.replace(suffix, "")
    title = title.strip()

    html_content = md_to_html(md_content, title, md_path)

    # Write HTML next to the MD
    html_path = md_path.with_suffix(".html")
    html_path.write_text(html_content, encoding="utf-8")

    pdf_path = None
    if not html_only:
        # Try to generate PDF
        pdf_path = _html_to_pdf(html_path, md_path.with_suffix(".pdf"))

    return html_path, pdf_path


def _html_to_pdf(html_path: Path, pdf_path: Path) -> Path | None:
    """Convert HTML to PDF. Returns path if successful, None otherwise."""
    # Try weasyprint first (best quality)
    try:
        from weasyprint import HTML
        HTML(filename=str(html_path)).write_pdf(str(pdf_path))
        return pdf_path
    except ImportError:
        pass
    except Exception:
        pass

    # Try pdfkit (wkhtmltopdf wrapper)
    try:
        import pdfkit
        pdfkit.from_file(str(html_path), str(pdf_path),
                         options={"encoding": "UTF-8", "page-size": "A4",
                                  "margin-top": "20mm", "margin-bottom": "20mm"})
        return pdf_path
    except ImportError:
        pass
    except Exception:
        pass

    # Fallback: no PDF library available
    return None


def discover_md_files(tower: str | None = None, cap: str | None = None) -> list[Path]:
    """Find all generated Architecture, RICEFW, and Testing MD files."""
    towers_dir = WORKSPACE / "towers"
    md_files = []
    patterns = ("-Architecture.md", "-RICEFW-Tracker.md", "-Testing-Report.md")

    for root, dirs, files in os.walk(str(towers_dir)):
        for f in files:
            if any(f.endswith(pat) for pat in patterns):
                p = Path(root) / f
                if tower and tower.upper() not in str(p).upper():
                    continue
                if cap and cap.upper() not in f.upper():
                    continue
                md_files.append(p)

    return sorted(md_files)


def main():
    parser = argparse.ArgumentParser(description="Convert Architecture MD files to HTML/PDF")
    parser.add_argument("--tower", help="Single tower shortcode")
    parser.add_argument("--cap", help="Single capability ID")
    parser.add_argument("--html-only", action="store_true", help="Only generate HTML (skip PDF)")
    args = parser.parse_args()

    md_files = discover_md_files(args.tower, args.cap)
    print(f"Found {len(md_files)} MD files (Architecture + RICEFW + Testing)")

    html_count = 0
    pdf_count = 0
    pdf_attempted = not args.html_only
    pdf_lib = None

    for md_path in md_files:
        rel = md_path.relative_to(WORKSPACE)
        html_path, pdf_path = convert_file(md_path, args.html_only)
        if html_path:
            html_count += 1
        if pdf_path:
            pdf_count += 1
            if not pdf_lib:
                pdf_lib = "available"
        print(f"  {rel.parts[1]:8s} {md_path.stem:30s} HTML={'OK' if html_path else 'FAIL':4s} {'PDF=' + ('OK' if pdf_path else 'SKIP') if pdf_attempted else ''}")

    print(f"\nResults:")
    print(f"  HTML files generated: {html_count}")
    if pdf_attempted:
        if pdf_count > 0:
            print(f"  PDF files generated: {pdf_count}")
        else:
            print(f"  PDF generation: no PDF library available")
            print(f"  To enable PDF generation, install one of:")
            print(f"    pip install weasyprint    (recommended, best quality)")
            print(f"    pip install pdfkit        (requires wkhtmltopdf)")
            print(f"  Or use the HTML files: open in browser -> Print -> Save as PDF")
    print(f"\n  TIP: HTML files include Mermaid.js for live diagram rendering.")
    print(f"  Open any .html file in a browser and use Ctrl+P to print/save as PDF.")


if __name__ == "__main__":
    main()
