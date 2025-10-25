# Easy Converter - Universal File Format Converter

Universal converter for images, documents, spreadsheets, and presentations with automatic format detection.

## Description

Easy Converter is a comprehensive skill that enables simple and automatic file conversion between different formats. Supports over 30 different formats and automatically detects the required conversion type.

## Supported Formats

### 📸 Images
- **Formats**: PNG, JPEG/JPG, GIF, BMP, TIFF, WebP, ICO
- **Conversions**: All bidirectional conversions (42 pairs)

### 📄 Documents
- **Formats**: PDF, DOCX, DOC, TXT, Markdown, HTML, RTF, ODT, EPUB
- **Conversions**: Formatting preservation

### 📊 Spreadsheets
- **Formats**: XLSX, XLS, CSV, TSV, ODS
- **Conversions**: All bidirectional conversions (12 pairs)

### 📽️ Presentations
- **Formats**: PPTX, PPT, ODP → PDF

## Conversion Examples

### Images
```
PNG ↔ JPEG    |  GIF ↔ WebP    |  BMP ↔ PNG
JPEG ↔ WebP   |  TIFF ↔ JPEG   |  PNG ↔ ICO
GIF ↔ BMP     |  WebP ↔ TIFF   |  And many more...
```

### Documents
```
Markdown → PDF       |  HTML → DOCX        |  TXT → PDF
DOCX → HTML         |  PDF → Markdown     |  RTF → DOCX
EPUB → PDF          |  HTML → Markdown    |  And many more...
```

### Spreadsheets
```
XLSX ↔ CSV     |  XLS ↔ TSV      |  CSV ↔ ODS
XLSX ↔ TSV     |  CSV ↔ XLS      |  ODS ↔ XLSX
```

### Presentations
```
PPTX → PDF     |  PPT → PDF      |  ODP → PDF
```

## Key Features

✅ **Automatic Detection**: Automatically recognizes formats from files
✅ **Quality Control**: Quality parameters for JPEG and WebP images (1-100)
✅ **Transparency Handling**: Automatic conversion for images with transparency
✅ **Multi-Sheet**: Support for multiple sheets in Excel
✅ **Batch Processing**: Multiple conversion capability
✅ **Format Preservation**: Maintains formatting when possible

## Quick Usage

```bash
# Automatic conversion (detects formats)
python scripts/universal_converter.py input.png output.jpg

# Image conversion with quality
python scripts/convert_image.py photo.png photo.webp --quality 95

# Document conversion
python scripts/convert_document.py readme.md report.pdf

# Spreadsheet conversion
python scripts/convert_spreadsheet.py data.xlsx data.csv

# Presentation conversion
python scripts/convert_presentation.py slides.pptx slides.pdf
```

## Available Scripts

1. **universal_converter.py** - Universal converter (recommended)
2. **convert_image.py** - Image conversion
3. **convert_document.py** - Document conversion
4. **convert_spreadsheet.py** - Spreadsheet conversion
5. **convert_presentation.py** - Presentation conversion

## Complete Conversion Matrix

### Images (42 pairs)
| From/To | PNG | JPEG | GIF | BMP | TIFF | WebP | ICO |
|---------|-----|------|-----|-----|------|------|-----|
| PNG     | -   | ✓    | ✓   | ✓   | ✓    | ✓    | ✓   |
| JPEG    | ✓   | -    | ✓   | ✓   | ✓    | ✓    | ✓   |
| GIF     | ✓   | ✓    | -   | ✓   | ✓    | ✓    | ✓   |
| BMP     | ✓   | ✓    | ✓   | -   | ✓    | ✓    | ✓   |
| TIFF    | ✓   | ✓    | ✓   | ✓   | -    | ✓    | ✓   |
| WebP    | ✓   | ✓    | ✓   | ✓   | ✓    | -    | ✓   |
| ICO     | ✓   | ✓    | ✓   | ✓   | ✓    | ✓    | -   |

### Documents (Common Conversions)
- Markdown → PDF, HTML, DOCX, TXT, RTF, EPUB
- PDF → DOCX, HTML, TXT, Markdown
- DOCX → PDF, HTML, TXT, Markdown, RTF, ODT
- HTML → PDF, DOCX, Markdown, TXT
- TXT → PDF, DOCX, HTML, Markdown

### Spreadsheets (12 pairs)
| From/To | XLSX | XLS | CSV | TSV | ODS |
|---------|------|-----|-----|-----|-----|
| XLSX    | -    | ✓   | ✓   | ✓   | ✓   |
| XLS     | ✓    | -   | ✓   | ✓   | ✓   |
| CSV     | ✓    | ✓   | -   | ✓   | ✓   |
| TSV     | ✓    | ✓   | ✓   | -   | ✓   |
| ODS     | ✓    | ✓   | ✓   | ✓   | -   |

## Common Use Cases

1. 🌐 **Web Optimization**: Convert images to WebP for reduced file sizes
2. 📚 **Documentation**: Convert Markdown to PDF for distribution
3. 📊 **Data Export**: Convert Excel to CSV for universal compatibility
4. 🎯 **Presentation Sharing**: Convert PPTX to PDF for platform independence
5. 🔄 **Standardization**: Batch convert files to a common format

## Dependencies

```bash
# Python packages
pip install Pillow pandas openpyxl

# System dependencies
apt-get install pandoc libreoffice
```

## Technical Notes

- **Transparency**: Images with transparency are converted with white background for JPEG
- **Excel Multi-Sheet**: Use `--sheet` parameter to specify the sheet
- **PDF Quality**: Depends on source document structure
- **Presentations**: Requires LibreOffice installed

## Complete Documentation

See `references/conversion_matrix.md` for the complete list of all supported conversion pairs.
