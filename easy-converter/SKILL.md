---
name: easy-converter
description: Universal file format converter for images, documents, spreadsheets, and presentations. Automatically detects formats and converts between PNG, JPEG, GIF, BMP, TIFF, WebP, ICO, PDF, DOCX, TXT, MD, HTML, RTF, EPUB, XLSX, CSV, TSV, PPTX and more. Use when users need to convert any file type to another format.
---

# Easy Converter

Universal file format converter supporting images, documents, spreadsheets, and presentations with automatic format detection.

## Quick Start

Convert any file with automatic format detection:

```bash
python scripts/universal_converter.py input.png output.jpg
python scripts/universal_converter.py document.md report.pdf
python scripts/universal_converter.py data.xlsx export.csv
python scripts/universal_converter.py slides.pptx presentation.pdf
```

## Supported Formats

### Images
PNG, JPEG/JPG, GIF, BMP, TIFF, WebP, ICO

### Documents
PDF, DOCX, DOC, TXT, Markdown, HTML, RTF, ODT, EPUB

### Spreadsheets
XLSX, XLS, CSV, TSV, ODS

### Presentations
PPTX, PPT, ODP (to PDF)

## Usage Patterns

### Pattern 1: Image Conversion

Convert between any image formats with quality control:

```bash
# Basic conversion
python scripts/convert_image.py photo.png photo.jpg

# High-quality conversion
python scripts/convert_image.py image.png image.webp --quality 95

# Transparency handling (automatic)
python scripts/convert_image.py logo.png logo.jpg  # White background added
```

**Supported conversions**: All bidirectional between PNG, JPEG, GIF, BMP, TIFF, WebP, ICO

### Pattern 2: Document Conversion

Convert documents while preserving formatting:

```bash
# Markdown to PDF
python scripts/convert_document.py readme.md output.pdf

# Word to HTML
python scripts/convert_document.py report.docx report.html

# HTML to Markdown
python scripts/convert_document.py page.html page.md

# Text to DOCX
python scripts/convert_document.py notes.txt notes.docx
```

**Supported conversions**: PDF, DOCX, DOC, TXT, MD, HTML, RTF, ODT, EPUB

### Pattern 3: Spreadsheet Conversion

Convert spreadsheets and data files:

```bash
# Excel to CSV
python scripts/convert_spreadsheet.py data.xlsx data.csv

# CSV to Excel
python scripts/convert_spreadsheet.py export.csv workbook.xlsx

# Specific sheet conversion
python scripts/convert_spreadsheet.py workbook.xlsx data.csv --sheet "Sales Data"

# TSV to Excel
python scripts/convert_spreadsheet.py data.tsv data.xlsx
```

**Supported conversions**: XLSX, XLS, CSV, TSV, ODS

### Pattern 4: Presentation Conversion

Convert presentations to PDF:

```bash
# PowerPoint to PDF
python scripts/convert_presentation.py slides.pptx slides.pdf
```

## Universal Converter

Auto-detects formats and routes to appropriate converter:

```bash
# Automatically determines conversion type
python scripts/universal_converter.py input.* output.*

# With options
python scripts/universal_converter.py photo.png photo.jpg --quality 90
python scripts/universal_converter.py data.xlsx data.csv --sheet "Sheet1"
```

## Implementation Guidelines

### When to Use Which Script

1. **`universal_converter.py`** - Default choice, handles all formats
2. **`convert_image.py`** - When you need fine control over image quality
3. **`convert_document.py`** - For document-specific conversions
4. **`convert_spreadsheet.py`** - When working with multi-sheet Excel files
5. **`convert_presentation.py`** - For presentation conversions

### Format Detection

The converter automatically detects formats from file extensions. No need to specify input/output types.

### Quality Considerations

- **Images**: Use `--quality` parameter (1-100) for JPEG/WebP
- **Documents**: Formatting preservation depends on source complexity
- **Spreadsheets**: Formulas converted to values in CSV/TSV
- **Presentations**: Vector graphics rasterized in PDF output

### Error Handling

All scripts provide clear error messages and exit codes:
- Exit 0: Success
- Exit 1: Conversion error
- Errors printed to stderr with ✗ symbol
- Success messages to stdout with ✓ symbol

## Dependencies

Required Python packages:
```bash
pip install Pillow pandas openpyxl
```

System dependencies:
```bash
# Install pandoc for document conversions
apt-get install pandoc

# Install LibreOffice for presentation conversions
apt-get install libreoffice
```

## Reference Documentation

See `references/conversion_matrix.md` for complete list of supported conversion pairs and format details.

## Transparency Handling

Images with transparency (PNG with alpha channel) are automatically converted:
- **To JPEG**: White background added
- **To formats supporting transparency**: Alpha channel preserved

## Batch Conversions

For batch conversions, call scripts in a loop:

```bash
for file in *.png; do
    python scripts/convert_image.py "$file" "${file%.png}.jpg"
done
```

## Common Use Cases

1. **Web optimization**: Convert images to WebP for smaller file sizes
2. **Documentation**: Convert Markdown to PDF for distribution
3. **Data export**: Convert Excel to CSV for universal compatibility
4. **Presentation sharing**: Convert PPTX to PDF for platform independence
5. **Format standardization**: Batch convert images to common format
