#!/usr/bin/env python3
"""Extract a lightweight outline from a PDF for paper-to-course analysis."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SECTION_RE = re.compile(
    r"^\s*(abstract|introduction|related work|background|method|methods|approach|model|experiments?|results?|discussion|limitations?|conclusion|references)\s*$",
    re.IGNORECASE,
)


def read_pages(pdf_path: Path) -> list[str]:
    try:
        import pdfplumber  # type: ignore

        with pdfplumber.open(str(pdf_path)) as pdf:
            return [(page.extract_text() or "") for page in pdf.pages]
    except Exception:
        try:
            from pypdf import PdfReader  # type: ignore

            reader = PdfReader(str(pdf_path))
            return [(page.extract_text() or "") for page in reader.pages]
        except Exception as exc:  # pragma: no cover - environment-dependent
            raise SystemExit(
                "Could not extract PDF text. Install pdfplumber or pypdf, "
                "or use another PDF tool to extract text first."
            ) from exc


def clean_line(line: str) -> str:
    return re.sub(r"\s+", " ", line).strip()


def likely_title(first_page: str) -> str:
    lines = [clean_line(line) for line in first_page.splitlines()]
    lines = [line for line in lines if len(line) > 8]
    if not lines:
        return "Unknown title"
    return max(lines[:8], key=len)


def outline_pages(pages: list[str]) -> list[tuple[int, str]]:
    found: list[tuple[int, str]] = []
    for page_num, text in enumerate(pages, start=1):
        for raw in text.splitlines():
            line = clean_line(raw)
            if SECTION_RE.match(line):
                found.append((page_num, line))
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--chars-per-page", type=int, default=700)
    args = parser.parse_args()

    pages = read_pages(args.pdf)
    print(f"# PDF Outline: {args.pdf.name}")
    print(f"Pages: {len(pages)}")
    print(f"Likely title: {likely_title(pages[0] if pages else '')}")
    print()
    print("## Detected Sections")
    sections = outline_pages(pages)
    if sections:
        for page, title in sections:
            print(f"- p.{page}: {title}")
    else:
        print("- No obvious section headings detected.")
    print()
    print("## Page Previews")
    for page_num, text in enumerate(pages, start=1):
        preview = clean_line(text)[: args.chars_per_page]
        print(f"\n### Page {page_num}\n{preview}")


if __name__ == "__main__":
    main()
