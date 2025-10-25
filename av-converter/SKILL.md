---
name: av-converter
description: Universal audio and video format converter with FFmpeg. Converts between all major formats including MP3, WAV, FLAC, AAC, OGG, MP4, AVI, MKV, MOV, WebM and more. Supports audio extraction from video, quality control, resolution scaling, and codec selection. Use when users need audio/video format conversion or audio extraction.
---

# AV-Converter

Universal audio and video converter supporting 30+ formats with automatic detection and quality control.

## Quick Start

```bash
# Automatic conversion
python scripts/universal_av_converter.py input.mp4 output.avi

# Audio conversion
python scripts/convert_audio.py song.flac song.mp3 --bitrate 320k

# Video conversion
python scripts/convert_video.py video.avi video.mp4 --codec libx264

# Extract audio from video
python scripts/extract_audio.py movie.mp4 soundtrack.mp3
```

## Supported Formats

### Audio (14 formats)
MP3, WAV, FLAC, AAC, OGG, M4A, WMA, AIFF, OPUS, AC3, ALAC, APE, AMR, DTS

### Video (15 formats)
MP4, AVI, MKV, MOV, WMV, FLV, WebM, MPEG, MPG, 3GP, M4V, VOB, TS, MTS, DivX

## Usage Patterns

### Pattern 1: Audio Conversion

Convert between any audio formats:

```bash
# Basic conversion
python scripts/convert_audio.py input.flac output.mp3

# High-quality conversion
python scripts/convert_audio.py song.wav song.mp3 --bitrate 320k

# Professional sample rate
python scripts/convert_audio.py audio.m4a audio.wav --sample-rate 48000

# Lossless to lossy
python scripts/convert_audio.py music.flac music.aac --bitrate 256k
```

**Parameters**:
- `--bitrate`: 64k, 128k, 192k (default), 256k, 320k
- `--sample-rate`: 22050, 44100, 48000, 96000 Hz

### Pattern 2: Video Conversion

Convert between any video formats with quality control:

```bash
# Basic conversion
python scripts/convert_video.py input.avi output.mp4

# HD conversion with H.264
python scripts/convert_video.py video.mkv video.mp4 --codec libx264 --resolution 1920x1080

# High-quality 60fps
python scripts/convert_video.py clip.mov clip.mp4 --fps 60 --bitrate 5M

# WebM for web
python scripts/convert_video.py video.mp4 video.webm --codec libvpx-vp9
```

**Parameters**:
- `--codec`: libx264 (default), libx265, libvpx-vp9
- `--resolution`: 1280x720, 1920x1080, 3840x2160
- `--fps`: 24, 30, 60
- `--bitrate`: 1M, 2M, 5M, 10M

### Pattern 3: Audio Extraction

Extract audio tracks from video files:

```bash
# Extract to MP3
python scripts/extract_audio.py movie.mp4 audio.mp3

# High-quality extraction
python scripts/extract_audio.py video.mkv soundtrack.flac

# Custom bitrate
python scripts/extract_audio.py clip.avi audio.mp3 --bitrate 256k
```

### Pattern 4: Universal Converter

Auto-detects format and routes to appropriate converter:

```bash
# Detects audio-to-audio
python scripts/universal_av_converter.py song.flac song.mp3 --bitrate 320k

# Detects video-to-video
python scripts/universal_av_converter.py clip.avi clip.mp4 --codec libx264

# Detects video-to-audio
python scripts/universal_av_converter.py movie.mp4 audio.mp3 --bitrate 192k
```

## Implementation Guidelines

### Script Selection

1. **`universal_av_converter.py`** - Default choice, handles all conversions
2. **`convert_audio.py`** - Audio-specific with quality control
3. **`convert_video.py`** - Video-specific with codec/resolution options
4. **`extract_audio.py`** - Dedicated audio extraction from video

### Format Detection

Automatic detection based on file extensions. Supports:
- Audio → Audio: Direct conversion
- Video → Video: Transcode with quality preservation
- Video → Audio: Extract audio track

### Quality Recommendations

**Audio**:
- Music archival: FLAC (lossless)
- General use: MP3 320k or AAC 256k
- Streaming: AAC 192k or OPUS 128k
- Voice: MP3 128k

**Video**:
- Archival: MKV with H.265, bitrate 10M+
- Sharing: MP4 with H.264, bitrate 5M
- Web: WebM with VP9, bitrate 2M
- Mobile: MP4 with H.264 at 720p

### Codec Selection

**Video Codecs**:
- `libx264` - Best compatibility (default)
- `libx265` - Better compression, newer devices
- `libvpx-vp9` - WebM standard, excellent quality

**Audio Codecs** (automatically selected based on format):
- AAC for MP4/M4A
- MP3 for .mp3 files
- Vorbis for OGG/WebM
- OPUS for modern apps

### Common Conversions

```bash
# 4K to 1080p
python scripts/convert_video.py 4k.mp4 1080p.mp4 --resolution 1920x1080

# Multiple audio formats from video
python scripts/extract_audio.py movie.mkv audio.mp3
python scripts/extract_audio.py movie.mkv audio.flac

# Web optimization
python scripts/convert_video.py large.mp4 optimized.webm --codec libvpx-vp9 --bitrate 2M
```

## Dependencies

FFmpeg must be installed:
```bash
# Ubuntu/Debian
apt-get install ffmpeg

# MacOS
brew install ffmpeg

# Check installation
ffmpeg -version
```

## Error Handling

All scripts provide clear feedback:
- Exit 0: Success
- Exit 1: Conversion error
- Success: ✓ symbol with filenames
- Errors: ✗ symbol with details in stderr

## Batch Conversions

Process multiple files:

```bash
# Convert all FLACs to MP3
for file in *.flac; do
    python scripts/convert_audio.py "$file" "${file%.flac}.mp3" --bitrate 320k
done

# Convert all AVIs to MP4
for file in *.avi; do
    python scripts/convert_video.py "$file" "${file%.avi}.mp4"
done
```

## Reference Documentation

See `references/conversion_matrix.md` for:
- Complete format compatibility matrix
- Codec recommendations
- Quality settings guide
- Container vs codec explanations

## Common Use Cases

1. **Music Library**: Convert FLAC collection to MP3 for portable devices
2. **Video Archival**: Convert DVDs (VOB) to MP4 for storage
3. **Web Publishing**: Convert videos to WebM for optimal web delivery
4. **Podcast Production**: Extract audio from video interviews
5. **Format Standardization**: Batch convert mixed formats to MP4/MP3
