# Easy Converter - Supported Conversions

Complete matrix of supported file format conversions.

## Image Conversions

All bidirectional conversions between:
- PNG (Portable Network Graphics)
- JPEG/JPG (Joint Photographic Experts Group)
- GIF (Graphics Interchange Format)
- BMP (Bitmap)
- TIFF/TIF (Tagged Image File Format)
- WebP (Web Picture format)
- ICO (Icon format)

**Total combinations**: 42 conversion pairs

**Examples**:
- PNG → JPEG, JPEG → PNG
- GIF → WebP, WebP → GIF
- BMP → PNG, PNG → BMP
- TIFF → JPEG, JPEG → TIFF

## Document Conversions

Supported formats:
- PDF (Portable Document Format)
- DOCX/DOC (Microsoft Word)
- TXT (Plain Text)
- MD/Markdown
- HTML/HTM
- RTF (Rich Text Format)
- ODT (OpenDocument Text)
- EPUB (Electronic Publication)

**Common conversions**:
- MD → PDF, PDF → DOCX
- DOCX → HTML, HTML → PDF
- TXT → DOCX, DOCX → TXT
- MD → HTML, HTML → MD
- EPUB → PDF, PDF → EPUB

## Spreadsheet Conversions

All bidirectional conversions between:
- XLSX/XLS (Microsoft Excel)
- CSV (Comma-Separated Values)
- TSV (Tab-Separated Values)
- ODS (OpenDocument Spreadsheet)

**Total combinations**: 12 conversion pairs

**Examples**:
- XLSX → CSV, CSV → XLSX
- XLS → TSV, TSV → XLS
- CSV → ODS, ODS → CSV

## Presentation Conversions

- PPTX → PDF
- PPT → PDF
- ODP → PDF

## Format Detection

The universal converter automatically detects file formats based on extensions and routes to the appropriate converter.

## Quality Options

For image conversions:
- Quality parameter (1-100) for JPEG and WebP
- Automatic transparency handling
- Optimization for web formats

## Notes

- PDF extraction quality depends on source document structure
- Image transparency converted to white background for JPEG
- Multi-sheet Excel files: use --sheet parameter to specify sheet
- Presentation conversions require LibreOffice installed
