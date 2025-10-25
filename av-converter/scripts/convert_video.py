#!/usr/bin/env python3
"""
Video format converter using FFmpeg.
Supports: MP4, AVI, MKV, MOV, WMV, FLV, WebM, MPEG, 3GP, and more.
"""

import sys
import subprocess
from pathlib import Path
import argparse


def convert_video(input_path: str, output_path: str, codec: str = 'libx264',
                 resolution: str = None, fps: int = None, bitrate: str = None) -> None:
    """
    Convert video from one format to another using FFmpeg.
    
    Args:
        input_path: Path to input video file
        output_path: Path to output video file
        codec: Video codec (libx264, libx265, libvpx-vp9, etc.)
        resolution: Resolution (e.g., '1920x1080', '1280x720')
        fps: Frames per second
        bitrate: Video bitrate (e.g., '2M', '5M')
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Build FFmpeg command
    cmd = [
        'ffmpeg',
        '-i', str(input_file),
        '-c:v', codec,
        '-c:a', 'aac',  # Standard audio codec
        '-y'  # Overwrite output file
    ]
    
    # Add optional parameters
    if resolution:
        width, height = resolution.split('x')
        cmd.extend(['-s', f'{width}x{height}'])
    
    if fps:
        cmd.extend(['-r', str(fps)])
    
    if bitrate:
        cmd.extend(['-b:v', bitrate])
    
    # Add output file
    cmd.append(str(output_file))
    
    # Execute conversion
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg conversion failed: {result.stderr}")
    
    print(f"✓ Converted: {input_file.name} → {output_file.name}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert video between formats (MP4, AVI, MKV, MOV, WebM, etc.)'
    )
    parser.add_argument('input', help='Input video file')
    parser.add_argument('output', help='Output video file')
    parser.add_argument('--codec', default='libx264',
                       help='Video codec (default: libx264)')
    parser.add_argument('--resolution',
                       help='Resolution (e.g., 1920x1080, 1280x720)')
    parser.add_argument('--fps', type=int,
                       help='Frames per second')
    parser.add_argument('--bitrate',
                       help='Video bitrate (e.g., 2M, 5M)')
    
    args = parser.parse_args()
    
    try:
        convert_video(args.input, args.output, args.codec,
                     args.resolution, args.fps, args.bitrate)
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
