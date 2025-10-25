#!/usr/bin/env python3
"""
Document format converter supporting text and office documents.
Supports: PDF, DOCX, TXT, MD, HTML, RTF, and more.
"""

import sys
import subprocess
from pathlib import Path
import argparse


def convert_document(input_path: str, output_path: str) -> None:
    """
    Convert document from one format to another using pandoc.
    
    Args:
        input_path: Path to input document file
        output_path: Path to output document file
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine input and output formats
    input_format = input_file.suffix.lower().lstrip('.')
    output_format = output_file.suffix.lower().lstrip('.')
    
    # Map extensions to pandoc format names
    format_map = {
        'md': 'markdown',
        'markdown': 'markdown',
        'txt': 'plain',
        'html': 'html',
        'htm': 'html',
        'docx': 'docx',
        'doc': 'doc',
        'rtf': 'rtf',
        'odt': 'odt',
        'epub': 'epub',
        'pdf': 'pdf'
    }
    
    pandoc_input_format = format_map.get(input_format, input_format)
    pandoc_output_format = format_map.get(output_format, output_format)
    
    # Build pandoc command
    cmd = [
        'pandoc',
        str(input_file),
        '-f', pandoc_input_format,
        '-t', pandoc_output_format,
        '-o', str(output_file),
        '--standalone'
    ]
    
    # Add PDF-specific options
    if output_format == 'pdf':
        cmd.extend(['--pdf-engine=weasyprint'])
    
    # Execute conversion
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"Pandoc conversion failed: {result.stderr}")
    
    print(f"✓ Converted: {input_file.name} → {output_file.name}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert documents between formats (PDF, DOCX, TXT, MD, HTML, RTF, etc.)'
    )
    parser.add_argument('input', help='Input document file')
    parser.add_argument('output', help='Output document file')
    
    args = parser.parse_args()
    
    try:
        convert_document(args.input, args.output)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
