# AV-Converter - Supported Conversions

Complete matrix of audio and video format conversions.

## Audio Formats

### Supported Formats
- **MP3** (MPEG Audio Layer 3)
- **WAV** (Waveform Audio)
- **FLAC** (Free Lossless Audio Codec)
- **AAC** (Advanced Audio Coding)
- **OGG/Vorbis**
- **M4A** (MPEG-4 Audio)
- **WMA** (Windows Media Audio)
- **AIFF** (Audio Interchange File Format)
- **OPUS** (Opus Interactive Audio)
- **AC3** (Dolby Digital)
- **ALAC** (Apple Lossless)
- **APE** (Monkey's Audio)
- **AMR** (Adaptive Multi-Rate)
- **DTS** (Digital Theater Systems)

### Audio Conversion Matrix
All bidirectional conversions supported between any audio formats.
**Total combinations**: 182+ conversion pairs

Common examples:
- MP3 ↔ WAV, FLAC ↔ MP3, AAC ↔ OGG
- M4A → MP3, WAV → FLAC, OGG → AAC
- WMA → MP3, AIFF → WAV, OPUS → MP3

## Video Formats

### Supported Formats
- **MP4** (MPEG-4 Part 14)
- **AVI** (Audio Video Interleave)
- **MKV** (Matroska Video)
- **MOV** (QuickTime Movie)
- **WMV** (Windows Media Video)
- **FLV** (Flash Video)
- **WebM** (Web Media)
- **MPEG/MPG** (Moving Picture Experts Group)
- **3GP** (3rd Generation Partnership)
- **M4V** (iTunes Video)
- **VOB** (DVD Video Object)
- **TS** (MPEG Transport Stream)
- **MTS/M2TS** (AVCHD Video)
- **DivX**
- **OGV** (Ogg Video)

### Video Conversion Matrix
All bidirectional conversions supported between any video formats.
**Total combinations**: 210+ conversion pairs

Common examples:
- MP4 ↔ AVI, MKV ↔ MP4, MOV ↔ AVI
- WebM → MP4, FLV → MP4, AVI → MKV
- MPEG → MP4, 3GP → MP4, VOB → MKV

## Video to Audio Extraction

Extract audio tracks from any video format to any audio format.
**Total combinations**: 210+ extraction pairs

Examples:
- MP4 → MP3, AVI → WAV, MKV → FLAC
- MOV → AAC, WebM → OGG, FLV → MP3
- Any video format → Any audio format

## Codec Support

### Video Codecs
- **H.264/AVC** (libx264) - Default, high compatibility
- **H.265/HEVC** (libx265) - Better compression
- **VP9** (libvpx-vp9) - WebM standard
- **VP8** (libvpx) - Older WebM
- **MPEG-4** - Legacy support
- **Xvid** - DivX alternative
- **Theora** - Ogg video

### Audio Codecs
- **AAC** - Default for most containers
- **MP3** (libmp3lame) - Universal compatibility
- **Vorbis** - OGG/WebM audio
- **OPUS** - Modern low-latency
- **AC3** - Surround sound
- **FLAC** - Lossless compression

## Quality Settings

### Audio Quality
- **Bitrate**: 64k, 128k, 192k (default), 256k, 320k
- **Sample Rate**: 22050, 44100 (CD quality), 48000 (professional), 96000 (Hi-Res)
- **Channels**: Mono (1), Stereo (2), 5.1 Surround

### Video Quality
- **Bitrate**: 1M (low), 2M (medium), 5M (high), 10M+ (very high)
- **Resolution**: 
  - 480p (854x480)
  - 720p HD (1280x720)
  - 1080p Full HD (1920x1080)
  - 1440p 2K (2560x1440)
  - 2160p 4K (3840x2160)
- **Frame Rate**: 24, 25, 30, 50, 60 fps

## Container vs Codec

- **Container** (file extension): Wrapper holding video/audio streams
- **Codec**: Compression method for the actual data

Example: MP4 container can use H.264, H.265, or MPEG-4 video codec

## Format Recommendations

### Best for Compatibility
- **Video**: MP4 with H.264 codec
- **Audio**: MP3 or AAC

### Best for Quality
- **Video**: MKV with H.265 codec
- **Audio**: FLAC (lossless) or high-bitrate AAC

### Best for Web
- **Video**: WebM with VP9 codec
- **Audio**: OPUS or AAC

### Best for Size
- **Video**: H.265/HEVC codec (smaller than H.264)
- **Audio**: OPUS (better than MP3 at same bitrate)

## Notes

- Video conversions preserve audio tracks
- Multiple audio tracks supported (MKV, MP4)
- Subtitle tracks preserved in MKV conversions
- Batch conversion supported via scripting
- FFmpeg handles all conversions internally
