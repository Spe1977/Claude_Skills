#!/usr/bin/env python3
"""
Presentation format converter.
Supports: PPTX to PDF conversion
"""

import sys
import subprocess
from pathlib import Path
import argparse


def convert_presentation(input_path: str, output_path: str) -> None:
    """
    Convert presentation from one format to another.
    Currently supports PPTX to PDF using LibreOffice.
    
    Args:
        input_path: Path to input presentation file
        output_path: Path to output presentation file
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    input_format = input_file.suffix.lower().lstrip('.')
    output_format = output_file.suffix.lower().lstrip('.')
    
    # Use LibreOffice for conversion
    if output_format == 'pdf':
        # Convert to PDF using LibreOffice in headless mode
        output_dir = output_file.parent
        
        cmd = [
            'libreoffice',
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', str(output_dir),
            str(input_file)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise RuntimeError(f"LibreOffice conversion failed: {result.stderr}")
        
        # LibreOffice creates file with same name but .pdf extension
        temp_output = output_dir / f"{input_file.stem}.pdf"
        if temp_output != output_file and temp_output.exists():
            temp_output.rename(output_file)
        
        print(f"✓ Converted: {input_file.name} → {output_file.name}")
    else:
        raise ValueError(f"Unsupported conversion: {input_format} → {output_format}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert presentations (PPTX to PDF)'
    )
    parser.add_argument('input', help='Input presentation file')
    parser.add_argument('output', help='Output presentation file')
    
    args = parser.parse_args()
    
    try:
        convert_presentation(args.input, args.output)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
