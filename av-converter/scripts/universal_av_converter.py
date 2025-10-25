#!/usr/bin/env python3
"""
Universal audio/video converter - automatically detects and converts.
"""

import sys
from pathlib import Path
import argparse
import subprocess


# Format categories
AUDIO_FORMATS = {'mp3', 'wav', 'flac', 'aac', 'ogg', 'm4a', 'wma', 'aiff', 'opus', 'ac3', 'alac', 'ape', 'amr', 'dts'}
VIDEO_FORMATS = {'mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'mpeg', 'mpg', '3gp', 'm4v', 'vob', 'ts', 'mts', 'm2ts', 'divx', 'ogv'}


def get_converter_script(input_format: str, output_format: str) -> str:
    """Determine which converter script to use."""
    script_dir = Path(__file__).parent
    
    if input_format in AUDIO_FORMATS and output_format in AUDIO_FORMATS:
        return str(script_dir / 'convert_audio.py')
    elif input_format in VIDEO_FORMATS and output_format in AUDIO_FORMATS:
        return str(script_dir / 'extract_audio.py')
    elif input_format in VIDEO_FORMATS or output_format in VIDEO_FORMATS:
        return str(script_dir / 'convert_video.py')
    else:
        raise ValueError(f"Unsupported conversion: {input_format} → {output_format}")


def convert_file(input_path: str, output_path: str, **kwargs) -> None:
    """
    Universal audio/video converter.
    
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
    if 'bitrate' in kwargs and kwargs['bitrate']:
        cmd.extend(['--bitrate', kwargs['bitrate']])
    if 'resolution' in kwargs and kwargs['resolution']:
        cmd.extend(['--resolution', kwargs['resolution']])
    if 'fps' in kwargs and kwargs['fps']:
        cmd.extend(['--fps', str(kwargs['fps'])])
    if 'codec' in kwargs and kwargs['codec']:
        cmd.extend(['--codec', kwargs['codec']])
    if 'sample_rate' in kwargs and kwargs['sample_rate']:
        cmd.extend(['--sample-rate', str(kwargs['sample_rate'])])
    
    # Execute conversion
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"Conversion failed: {result.stderr}")
    
    # Print output from converter
    if result.stdout:
        print(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser(
        description='Universal audio/video converter - automatically detects formats'
    )
    parser.add_argument('input', help='Input file')
    parser.add_argument('output', help='Output file')
    parser.add_argument('--bitrate', help='Audio/video bitrate (e.g., 192k, 2M)')
    parser.add_argument('--resolution', help='Video resolution (e.g., 1920x1080)')
    parser.add_argument('--fps', type=int, help='Video frames per second')
    parser.add_argument('--codec', help='Video codec (e.g., libx264, libx265)')
    parser.add_argument('--sample-rate', type=int, help='Audio sample rate (Hz)')
    
    args = parser.parse_args()
    
    try:
        convert_file(
            args.input,
            args.output,
            bitrate=args.bitrate,
            resolution=args.resolution,
            fps=args.fps,
            codec=args.codec,
            sample_rate=args.sample_rate
        )
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
