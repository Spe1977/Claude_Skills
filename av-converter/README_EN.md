# AV-Converter - Universal Audio/Video Converter

Universal converter for audio and video formats powered by FFmpeg.

## Supported Formats

### 🎵 Audio (14 formats)
MP3, WAV, FLAC, AAC, OGG, M4A, WMA, AIFF, OPUS, AC3, ALAC, APE, AMR, DTS

### 🎬 Video (15 formats)
MP4, AVI, MKV, MOV, WMV, FLV, WebM, MPEG, MPG, 3GP, M4V, VOB, TS, MTS, DivX

## Conversion Examples

### Audio
```
MP3 ↔ WAV     |  FLAC ↔ MP3    |  AAC ↔ OGG
M4A → MP3     |  WAV → FLAC    |  OGG → AAC
WMA → MP3     |  AIFF → WAV    |  OPUS → MP3
```

### Video
```
MP4 ↔ AVI     |  MKV ↔ MP4     |  MOV ↔ AVI
WebM → MP4    |  FLV → MP4     |  AVI → MKV
MPEG → MP4    |  3GP → MP4     |  VOB → MKV
```

### Video to Audio Extraction
```
MP4 → MP3     |  AVI → WAV     |  MKV → FLAC
MOV → AAC     |  WebM → OGG    |  Any Video → Any Audio
```

## Features

✅ **Automatic Detection**: Recognizes formats from file extensions
✅ **Quality Control**: Audio bitrate (64k-320k), video bitrate (1M-10M+)
✅ **Resolution Scaling**: 480p, 720p, 1080p, 4K
✅ **Codec Selection**: H.264, H.265, VP9, AAC, MP3
✅ **Audio Extraction**: Extract audio tracks from any video
✅ **Frame Rate**: 24, 30, 60 fps
✅ **Sample Rate**: 22050, 44100, 48000, 96000 Hz

## Quick Usage

```bash
# Automatic conversion
python scripts/universal_av_converter.py input.mp4 output.avi

# Audio conversion
python scripts/convert_audio.py song.flac song.mp3 --bitrate 320k

# Video conversion
python scripts/convert_video.py video.avi video.mp4 --codec libx264

# Audio extraction
python scripts/extract_audio.py movie.mp4 soundtrack.mp3
```

## Available Scripts

1. **universal_av_converter.py** - Universal converter (recommended)
2. **convert_audio.py** - Audio conversion with quality control
3. **convert_video.py** - Video conversion with codec/resolution options
4. **extract_audio.py** - Audio extraction from video

## Complete Conversion Matrix

### Audio (182+ pairs)
All bidirectional conversions between 14 audio formats

**Common examples**:
- MP3 ↔ WAV, FLAC ↔ MP3, AAC ↔ OGG
- M4A → MP3, WAV → FLAC, OGG → AAC
- WMA → MP3, AIFF → WAV, OPUS → MP3

### Video (210+ pairs)
All bidirectional conversions between 15 video formats

**Common examples**:
- MP4 ↔ AVI, MKV ↔ MP4, MOV ↔ AVI
- WebM → MP4, FLV → MP4, AVI → MKV
- MPEG → MP4, 3GP → MP4, VOB → MKV

### Video → Audio (210+ extractions)
Extract audio from any video to any audio format

## Quality Parameters

### Audio
- **Bitrate**: 64k, 128k, 192k (default), 256k, 320k
- **Sample Rate**: 22050, 44100 (CD quality), 48000 (professional), 96000 (Hi-Res)
- **Channels**: Mono (1), Stereo (2)

### Video
- **Bitrate**: 1M (low), 2M (medium), 5M (high), 10M+ (very high)
- **Resolution**:
  - 480p (854x480)
  - 720p HD (1280x720)
  - 1080p Full HD (1920x1080)
  - 1440p 2K (2560x1440)
  - 2160p 4K (3840x2160)
- **Frame Rate**: 24, 25, 30, 50, 60 fps

### Video Codecs
- **H.264/AVC** (libx264) - Maximum compatibility (default)
- **H.265/HEVC** (libx265) - Better compression
- **VP9** (libvpx-vp9) - WebM standard

## Detailed Examples

### Audio Conversion
```bash
# Maximum quality MP3
python scripts/convert_audio.py input.flac output.mp3 --bitrate 320k

# Professional sample rate
python scripts/convert_audio.py audio.m4a audio.wav --sample-rate 48000

# Lossless to lossy
python scripts/convert_audio.py music.flac music.aac --bitrate 256k
```

### Video Conversion
```bash
# HD with H.264
python scripts/convert_video.py video.mkv video.mp4 --codec libx264 --resolution 1920x1080

# 60fps high quality
python scripts/convert_video.py clip.mov clip.mp4 --fps 60 --bitrate 5M

# WebM for web
python scripts/convert_video.py video.mp4 video.webm --codec libvpx-vp9
```

### Audio Extraction
```bash
# Extract MP3 from video
python scripts/extract_audio.py movie.mp4 audio.mp3

# High quality FLAC
python scripts/extract_audio.py video.mkv soundtrack.flac

# Custom bitrate
python scripts/extract_audio.py clip.avi audio.mp3 --bitrate 256k
```

## Format Recommendations

### Best Compatibility
- **Video**: MP4 with H.264 codec
- **Audio**: MP3 or AAC

### Best Quality
- **Video**: MKV with H.265 codec
- **Audio**: FLAC (lossless) or high-bitrate AAC

### Best for Web
- **Video**: WebM with VP9 codec
- **Audio**: OPUS or AAC

### Best File Size
- **Video**: H.265/HEVC codec (smaller than H.264)
- **Audio**: OPUS (better than MP3 at same bitrate)

## Common Use Cases

1. 🎵 **Music Library**: Convert FLAC collection to MP3 for portable devices
2. 📀 **Video Archival**: Convert DVDs (VOB) to MP4 for storage
3. 🌐 **Web Publishing**: Convert videos to WebM for optimal web delivery
4. 🎙️ **Podcast Production**: Extract audio from video interviews
5. 🔄 **Standardization**: Batch convert mixed formats to MP4/MP3

## Batch Conversions

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

## Dependencies

```bash
# Install FFmpeg
apt-get install ffmpeg  # Ubuntu/Debian
brew install ffmpeg     # MacOS

# Check installation
ffmpeg -version
```

## Complete Documentation

See `references/conversion_matrix.md` for:
- Complete format compatibility matrix
- Codec recommendations
- Quality settings guide
- Container vs codec explanations

## Technical Notes

- Video conversions preserve audio tracks
- Multiple audio tracks supported (MKV, MP4)
- Subtitle tracks preserved in MKV conversions
- FFmpeg handles all conversions internally
