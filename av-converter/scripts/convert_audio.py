#!/usr/bin/env python3
"""
Audio format converter using FFmpeg.
Supports: MP3, WAV, FLAC, AAC, OGG, M4A, WMA, AIFF, OPUS, AC3, ALAC, and more.
"""

import sys
import subprocess
from pathlib import Path
import argparse


def convert_audio(input_path: str, output_path: str, bitrate: str = '192k', 
                 sample_rate: int = None) -> None:
    """
    Convert audio from one format to another using FFmpeg.
    
    Args:
        input_path: Path to input audio file
        output_path: Path to output audio file
        bitrate: Audio bitrate (e.g., '128k', '192k', '320k')
        sample_rate: Sample rate in Hz (e.g., 44100, 48000)
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Build FFmpeg command
    cmd = [
        'ffmpeg',
        '-i', str(input_file),
        '-b:a', bitrate,
        '-y'  # Overwrite output file
    ]
    
    # Add sample rate if specified
    if sample_rate:
        cmd.extend(['-ar', str(sample_rate)])
    
    # Add output file
    cmd.append(str(output_file))
    
    # Execute conversion
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg conversion failed: {result.stderr}")
    
    print(f"✓ Converted: {input_file.name} → {output_file.name}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert audio between formats (MP3, WAV, FLAC, AAC, OGG, M4A, etc.)'
    )
    parser.add_argument('input', help='Input audio file')
    parser.add_argument('output', help='Output audio file')
    parser.add_argument('--bitrate', default='192k',
                       help='Audio bitrate (default: 192k)')
    parser.add_argument('--sample-rate', type=int,
                       help='Sample rate in Hz (e.g., 44100, 48000)')
    
    args = parser.parse_args()
    
    try:
        convert_audio(args.input, args.output, args.bitrate, args.sample_rate)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
