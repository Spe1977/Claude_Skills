#!/usr/bin/env python3
"""
Image format converter supporting all major image formats.
Supports: PNG, JPEG, GIF, BMP, TIFF, WebP, ICO, and more.
"""

import sys
from pathlib import Path
from PIL import Image
import argparse


def convert_image(input_path: str, output_path: str, quality: int = 95) -> None:
    """
    Convert image from one format to another.
    
    Args:
        input_path: Path to input image file
        output_path: Path to output image file
        quality: Quality for JPEG/WebP (1-100, default 95)
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Open and convert image
    img = Image.open(input_file)
    
    # Handle transparency for formats that don't support it
    output_format = output_file.suffix.lower().lstrip('.')
    if output_format in ['jpg', 'jpeg'] and img.mode in ['RGBA', 'LA', 'P']:
        # Convert RGBA to RGB with white background
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = background
    
    # Save with appropriate parameters
    save_kwargs = {}
    if output_format in ['jpg', 'jpeg']:
        save_kwargs['quality'] = quality
        save_kwargs['optimize'] = True
    elif output_format == 'webp':
        save_kwargs['quality'] = quality
        save_kwargs['method'] = 6  # Best compression
    elif output_format == 'png':
        save_kwargs['optimize'] = True
    elif output_format == 'ico':
        # ICO files support multiple sizes
        img.save(output_file, format='ICO', sizes=[(256, 256)])
        print(f"✓ Converted: {input_file.name} → {output_file.name}")
        return
    
    img.save(output_file, **save_kwargs)
    print(f"✓ Converted: {input_file.name} → {output_file.name}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert images between formats (PNG, JPEG, GIF, BMP, TIFF, WebP, ICO)'
    )
    parser.add_argument('input', help='Input image file')
    parser.add_argument('output', help='Output image file')
    parser.add_argument('--quality', type=int, default=95,
                       help='Quality for JPEG/WebP (1-100, default: 95)')
    
    args = parser.parse_args()
    
    try:
        convert_image(args.input, args.output, args.quality)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
