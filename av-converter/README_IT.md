# AV-Converter - Convertitore Universale Audio/Video

Convertitore universale per formati audio e video con FFmpeg.

## Formati Supportati

### 🎵 Audio (14 formati)
MP3, WAV, FLAC, AAC, OGG, M4A, WMA, AIFF, OPUS, AC3, ALAC, APE, AMR, DTS

### 🎬 Video (15 formati)
MP4, AVI, MKV, MOV, WMV, FLV, WebM, MPEG, MPG, 3GP, M4V, VOB, TS, MTS, DivX

## Esempi di Conversione

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

### Estrazione Audio da Video
```
MP4 → MP3     |  AVI → WAV     |  MKV → FLAC
MOV → AAC     |  WebM → OGG    |  Qualsiasi Video → Qualsiasi Audio
```

## Funzionalità

✅ **Rilevamento Automatico**: Riconosce formati da estensioni file
✅ **Controllo Qualità**: Bitrate audio (64k-320k), video (1M-10M+)
✅ **Scaling Risoluzione**: 480p, 720p, 1080p, 4K
✅ **Selezione Codec**: H.264, H.265, VP9, AAC, MP3
✅ **Estrazione Audio**: Estrai tracce audio da qualsiasi video
✅ **Frame Rate**: 24, 30, 60 fps
✅ **Sample Rate**: 22050, 44100, 48000, 96000 Hz

## Utilizzo Rapido

```bash
# Conversione automatica
python scripts/universal_av_converter.py input.mp4 output.avi

# Conversione audio
python scripts/convert_audio.py canzone.flac canzone.mp3 --bitrate 320k

# Conversione video
python scripts/convert_video.py video.avi video.mp4 --codec libx264

# Estrazione audio
python scripts/extract_audio.py film.mp4 colonna-sonora.mp3
```

## Script Disponibili

1. **universal_av_converter.py** - Convertitore universale (consigliato)
2. **convert_audio.py** - Conversione audio con controllo qualità
3. **convert_video.py** - Conversione video con opzioni codec/risoluzione
4. **extract_audio.py** - Estrazione audio da video

## Matrice Conversioni Complete

### Audio (182+ coppie)
Tutte le conversioni bidirezionali tra 14 formati audio

**Esempi comuni**:
- MP3 ↔ WAV, FLAC ↔ MP3, AAC ↔ OGG
- M4A → MP3, WAV → FLAC, OGG → AAC
- WMA → MP3, AIFF → WAV, OPUS → MP3

### Video (210+ coppie)
Tutte le conversioni bidirezionali tra 15 formati video

**Esempi comuni**:
- MP4 ↔ AVI, MKV ↔ MP4, MOV ↔ AVI
- WebM → MP4, FLV → MP4, AVI → MKV
- MPEG → MP4, 3GP → MP4, VOB → MKV

### Video → Audio (210+ estrazioni)
Estrai audio da qualsiasi video in qualsiasi formato audio

## Parametri Qualità

### Audio
- **Bitrate**: 64k, 128k, 192k (default), 256k, 320k
- **Sample Rate**: 22050, 44100 (CD), 48000 (professionale), 96000 (Hi-Res)
- **Canali**: Mono (1), Stereo (2)

### Video
- **Bitrate**: 1M (basso), 2M (medio), 5M (alto), 10M+ (molto alto)
- **Risoluzione**:
  - 480p (854x480)
  - 720p HD (1280x720)
  - 1080p Full HD (1920x1080)
  - 1440p 2K (2560x1440)
  - 2160p 4K (3840x2160)
- **Frame Rate**: 24, 25, 30, 50, 60 fps

### Codec Video
- **H.264/AVC** (libx264) - Compatibilità massima (default)
- **H.265/HEVC** (libx265) - Compressione migliore
- **VP9** (libvpx-vp9) - Standard WebM

## Esempi Dettagliati

### Conversione Audio
```bash
# Qualità massima MP3
python scripts/convert_audio.py input.flac output.mp3 --bitrate 320k

# Sample rate professionale
python scripts/convert_audio.py audio.m4a audio.wav --sample-rate 48000

# Lossless a lossy
python scripts/convert_audio.py musica.flac musica.aac --bitrate 256k
```

### Conversione Video
```bash
# HD con H.264
python scripts/convert_video.py video.mkv video.mp4 --codec libx264 --resolution 1920x1080

# 60fps ad alta qualità
python scripts/convert_video.py clip.mov clip.mp4 --fps 60 --bitrate 5M

# WebM per web
python scripts/convert_video.py video.mp4 video.webm --codec libvpx-vp9
```

### Estrazione Audio
```bash
# Estrai MP3 da video
python scripts/extract_audio.py film.mp4 audio.mp3

# Alta qualità FLAC
python scripts/extract_audio.py video.mkv colonna-sonora.flac

# Bitrate personalizzato
python scripts/extract_audio.py clip.avi audio.mp3 --bitrate 256k
```

## Raccomandazioni Formato

### Migliore Compatibilità
- **Video**: MP4 con codec H.264
- **Audio**: MP3 o AAC

### Migliore Qualità
- **Video**: MKV con codec H.265
- **Audio**: FLAC (lossless) o AAC ad alto bitrate

### Migliore per Web
- **Video**: WebM con codec VP9
- **Audio**: OPUS o AAC

### Migliore Dimensione File
- **Video**: Codec H.265/HEVC (più piccolo di H.264)
- **Audio**: OPUS (migliore di MP3 a pari bitrate)

## Casi d'Uso Comuni

1. 🎵 **Libreria Musicale**: Converti collezione FLAC in MP3 per dispositivi portatili
2. 📀 **Archiviazione Video**: Converti DVD (VOB) in MP4 per storage
3. 🌐 **Pubblicazione Web**: Converti video in WebM per consegna web ottimale
4. 🎙️ **Produzione Podcast**: Estrai audio da video interviste
5. 🔄 **Standardizzazione**: Converti formati misti in MP4/MP3

## Conversioni Batch

```bash
# Converti tutti i FLAC in MP3
for file in *.flac; do
    python scripts/convert_audio.py "$file" "${file%.flac}.mp3" --bitrate 320k
done

# Converti tutti gli AVI in MP4
for file in *.avi; do
    python scripts/convert_video.py "$file" "${file%.avi}.mp4"
done
```

## Dipendenze

```bash
# Installa FFmpeg
apt-get install ffmpeg  # Ubuntu/Debian
brew install ffmpeg     # MacOS

# Verifica installazione
ffmpeg -version
```

## Documentazione Completa

Consulta `references/conversion_matrix.md` per:
- Matrice completa compatibilità formati
- Raccomandazioni codec
- Guida impostazioni qualità
- Spiegazioni container vs codec

## Note Tecniche

- Le conversioni video preservano tracce audio
- Supporto per tracce audio multiple (MKV, MP4)
- Tracce sottotitoli preservate in conversioni MKV
- FFmpeg gestisce tutte le conversioni internamente
