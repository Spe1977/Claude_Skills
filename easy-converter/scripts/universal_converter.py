#!/usr/bin/env python3
"""
Universal file converter - automatically detects formats and converts.
Supports images, documents, spreadsheets, and presentations.
"""

import sys
from pathlib import Path
import argparse
import subprocess


# Format categories
IMAGE_FORMATS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'ico'}
DOCUMENT_FORMATS = {'pdf', 'docx', 'doc', 'txt', 'md', 'markdown', 'html', 'htm', 'rtf', 'odt', 'epub'}
SPREADSHEET_FORMATS = {'xlsx', 'xls', 'csv', 'tsv', 'ods'}
PRESENTATION_FORMATS = {'pptx', 'ppt', 'odp'}


def get_converter_script(input_format: str, output_format: str) -> str:
    """Determine which converter script to use."""
    script_dir = Path(__file__).parent
    
    if input_format in IMAGE_FORMATS and output_format in IMAGE_FORMATS:
        return str(script_dir / 'convert_image.py')
    elif input_format in DOCUMENT_FORMATS or output_format in DOCUMENT_FORMATS:
        return str(script_dir / 'convert_document.py')
    elif input_format in SPREADSHEET_FORMATS and output_format in SPREADSHEET_FORMATS:
        return str(script_dir / 'convert_spreadsheet.py')
    elif input_format in PRESENTATION_FORMATS or (input_format in PRESENTATION_FORMATS and output_format == 'pdf'):
        return str(script_dir / 'convert_presentation.py')
    else:
        raise ValueError(f"Unsupported conversion: {input_format} → {output_format}")


def convert_file(input_path: str, output_path: str, **kwargs) -> None:
    """
    Universal file converter.
    
    Args:
        input_path: Path to input file
        output_path: Path to output file
        **kwargs: Additional arguments passed to specific converters
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Detect formats
    input_format = input_file.suffix.lower().lstrip('.')
    output_format = output_file.suffix.lower().lstrip('.')
    
    if not input_format or not output_format:
        raise ValueError("Input and output files must have extensions")
    
    # Get appropriate converter script
    converter_script = get_converter_script(input_format, output_format)
    
    # Build command
    cmd = ['python3', converter_script, str(input_file), str(output_file)]
    
    # Add optional arguments
    if 'quality' in kwargs and kwargs['quality']:
        cmd.extend(['--quality', str(kwargs['quality'])])
    if 'sheet' in kwargs and kwargs['sheet']:
        cmd.extend(['--sheet', kwargs['sheet']])
    
    # Execute conversion
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"Conversion failed: {result.stderr}")
    
    # Print output from converter
    if result.stdout:
        print(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser(
        description='Universal file converter - automatically detects and converts between formats'
    )
    parser.add_argument('input', help='Input file')
    parser.add_argument('output', help='Output file')
    parser.add_argument('--quality', type=int, help='Quality for image conversion (1-100)')
    parser.add_argument('--sheet', help='Sheet name for spreadsheet conversion')
    
    args = parser.parse_args()
    
    try:
        convert_file(
            args.input,
            args.output,
            quality=args.quality,
            sheet=args.sheet
        )
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
