#!/usr/bin/env python3
"""
Spreadsheet format converter.
Supports: XLSX, XLS, CSV, TSV, ODS
"""

import sys
from pathlib import Path
import pandas as pd
import argparse


def convert_spreadsheet(input_path: str, output_path: str, sheet_name: str = None) -> None:
    """
    Convert spreadsheet from one format to another.
    
    Args:
        input_path: Path to input spreadsheet file
        output_path: Path to output spreadsheet file
        sheet_name: Name of sheet to convert (for multi-sheet files)
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine input format and read file
    input_format = input_file.suffix.lower().lstrip('.')
    output_format = output_file.suffix.lower().lstrip('.')
    
    # Read input file
    read_kwargs = {}
    if sheet_name:
        read_kwargs['sheet_name'] = sheet_name
    
    if input_format in ['xlsx', 'xls']:
        df = pd.read_excel(input_file, **read_kwargs)
    elif input_format == 'csv':
        df = pd.read_csv(input_file)
    elif input_format == 'tsv':
        df = pd.read_csv(input_file, sep='\t')
    elif input_format == 'ods':
        df = pd.read_excel(input_file, engine='odf', **read_kwargs)
    else:
        raise ValueError(f"Unsupported input format: {input_format}")
    
    # Write output file
    if output_format in ['xlsx', 'xls']:
        df.to_excel(output_file, index=False, engine='openpyxl')
    elif output_format == 'csv':
        df.to_csv(output_file, index=False)
    elif output_format == 'tsv':
        df.to_csv(output_file, sep='\t', index=False)
    elif output_format == 'ods':
        df.to_excel(output_file, index=False, engine='odf')
    else:
        raise ValueError(f"Unsupported output format: {output_format}")
    
    print(f"✓ Converted: {input_file.name} → {output_file.name}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert spreadsheets between formats (XLSX, XLS, CSV, TSV, ODS)'
    )
    parser.add_argument('input', help='Input spreadsheet file')
    parser.add_argument('output', help='Output spreadsheet file')
    parser.add_argument('--sheet', help='Sheet name to convert (for multi-sheet files)')
    
    args = parser.parse_args()
    
    try:
        convert_spreadsheet(args.input, args.output, args.sheet)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
