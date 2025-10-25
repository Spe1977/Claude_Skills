#!/usr/bin/env python3
"""
Extract audio from video files using FFmpeg.
Converts video to audio-only formats.
"""

import sys
import subprocess
from pathlib import Path
import argparse


def extract_audio(input_path: str, output_path: str, bitrate: str = '192k') -> None:
    """
    Extract audio track from video file.
    
    Args:
        input_path: Path to input video file
        output_path: Path to output audio file
        bitrate: Audio bitrate (e.g., '128k', '192k', '320k')
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Build FFmpeg command
    cmd = [
        'ffmpeg',
        '-i', str(input_file),
        '-vn',  # Disable video
        '-b:a', bitrate,
        '-y'  # Overwrite output file
    ]
    
    # Add output file
    cmd.append(str(output_file))
    
    # Execute extraction
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg extraction failed: {result.stderr}")
    
    print(f"✓ Extracted audio: {input_file.name} → {output_file.name}")


def main():
    parser = argparse.ArgumentParser(
        description='Extract audio from video files'
    )
    parser.add_argument('input', help='Input video file')
    parser.add_argument('output', help='Output audio file')
    parser.add_argument('--bitrate', default='192k',
                       help='Audio bitrate (default: 192k)')
    
    args = parser.parse_args()
    
    try:
        extract_audio(args.input, args.output, args.bitrate)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
