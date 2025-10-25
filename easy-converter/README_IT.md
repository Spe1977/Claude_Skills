# Easy Converter - Convertitore Universale di File

Convertitore universale per immagini, documenti, fogli di calcolo e presentazioni con rilevamento automatico del formato.

## Descrizione

Easy Converter è una skill completa che permette di convertire file tra diversi formati in modo semplice e automatico. Supporta oltre 30 formati diversi e rileva automaticamente il tipo di conversione necessaria.

## Formati Supportati

### 📸 Immagini
- **Formati**: PNG, JPEG/JPG, GIF, BMP, TIFF, WebP, ICO
- **Conversioni**: Tutte le conversioni bidirezionali (42 coppie)

### 📄 Documenti
- **Formati**: PDF, DOCX, DOC, TXT, Markdown, HTML, RTF, ODT, EPUB
- **Conversioni**: Preservazione della formattazione

### 📊 Fogli di Calcolo
- **Formati**: XLSX, XLS, CSV, TSV, ODS
- **Conversioni**: Tutte le conversioni bidirezionali (12 coppie)

### 📽️ Presentazioni
- **Formati**: PPTX, PPT, ODP → PDF

## Esempi di Conversioni Possibili

### Immagini
```
PNG ↔ JPEG    |  GIF ↔ WebP    |  BMP ↔ PNG
JPEG ↔ WebP   |  TIFF ↔ JPEG   |  PNG ↔ ICO
GIF ↔ BMP     |  WebP ↔ TIFF   |  E molte altre...
```

### Documenti
```
Markdown → PDF       |  HTML → DOCX        |  TXT → PDF
DOCX → HTML         |  PDF → Markdown     |  RTF → DOCX
EPUB → PDF          |  HTML → Markdown    |  E molte altre...
```

### Fogli di Calcolo
```
XLSX ↔ CSV     |  XLS ↔ TSV      |  CSV ↔ ODS
XLSX ↔ TSV     |  CSV ↔ XLS      |  ODS ↔ XLSX
```

### Presentazioni
```
PPTX → PDF     |  PPT → PDF      |  ODP → PDF
```

## Funzionalità Principali

✅ **Rilevamento Automatico**: Riconosce automaticamente i formati dai file
✅ **Controllo Qualità**: Parametri di qualità per immagini JPEG e WebP (1-100)
✅ **Gestione Trasparenza**: Conversione automatica per immagini con trasparenza
✅ **Multi-Sheet**: Supporto per fogli multipli in Excel
✅ **Batch Processing**: Possibilità di conversioni multiple
✅ **Preservazione Formato**: Mantiene formattazione quando possibile

## Utilizzo Rapido

```bash
# Conversione automatica (rileva i formati)
python scripts/universal_converter.py input.png output.jpg

# Conversione immagini con qualità
python scripts/convert_image.py foto.png foto.webp --quality 95

# Conversione documenti
python scripts/convert_document.py readme.md report.pdf

# Conversione fogli di calcolo
python scripts/convert_spreadsheet.py dati.xlsx dati.csv

# Conversione presentazioni
python scripts/convert_presentation.py slides.pptx slides.pdf
```

## Script Disponibili

1. **universal_converter.py** - Convertitore universale (consigliato)
2. **convert_image.py** - Conversione immagini
3. **convert_document.py** - Conversione documenti
4. **convert_spreadsheet.py** - Conversione fogli di calcolo
5. **convert_presentation.py** - Conversione presentazioni

## Matrice Completa delle Conversioni

### Immagini (42 coppie)
| Da/A | PNG | JPEG | GIF | BMP | TIFF | WebP | ICO |
|------|-----|------|-----|-----|------|------|-----|
| PNG  | -   | ✓    | ✓   | ✓   | ✓    | ✓    | ✓   |
| JPEG | ✓   | -    | ✓   | ✓   | ✓    | ✓    | ✓   |
| GIF  | ✓   | ✓    | -   | ✓   | ✓    | ✓    | ✓   |
| BMP  | ✓   | ✓    | ✓   | -   | ✓    | ✓    | ✓   |
| TIFF | ✓   | ✓    | ✓   | ✓   | -    | ✓    | ✓   |
| WebP | ✓   | ✓    | ✓   | ✓   | ✓    | -    | ✓   |
| ICO  | ✓   | ✓    | ✓   | ✓   | ✓    | ✓    | -   |

### Documenti (Conversioni Comuni)
- Markdown → PDF, HTML, DOCX, TXT, RTF, EPUB
- PDF → DOCX, HTML, TXT, Markdown
- DOCX → PDF, HTML, TXT, Markdown, RTF, ODT
- HTML → PDF, DOCX, Markdown, TXT
- TXT → PDF, DOCX, HTML, Markdown

### Fogli di Calcolo (12 coppie)
| Da/A | XLSX | XLS | CSV | TSV | ODS |
|------|------|-----|-----|-----|-----|
| XLSX | -    | ✓   | ✓   | ✓   | ✓   |
| XLS  | ✓    | -   | ✓   | ✓   | ✓   |
| CSV  | ✓    | ✓   | -   | ✓   | ✓   |
| TSV  | ✓    | ✓   | ✓   | -   | ✓   |
| ODS  | ✓    | ✓   | ✓   | ✓   | -   |

## Casi d'Uso Comuni

1. 🌐 **Ottimizzazione Web**: Converti immagini in WebP per dimensioni ridotte
2. 📚 **Documentazione**: Converti Markdown in PDF per distribuzione
3. 📊 **Esportazione Dati**: Converti Excel in CSV per compatibilità universale
4. 🎯 **Condivisione Presentazioni**: Converti PPTX in PDF per indipendenza dalla piattaforma
5. 🔄 **Standardizzazione**: Converti lotti di file in un formato comune

## Dipendenze

```bash
# Pacchetti Python
pip install Pillow pandas openpyxl

# Dipendenze di sistema
apt-get install pandoc libreoffice
```

## Note Tecniche

- **Trasparenza**: Le immagini con trasparenza vengono convertite con sfondo bianco per JPEG
- **Excel Multi-Sheet**: Usa il parametro `--sheet` per specificare il foglio
- **Qualità PDF**: Dipende dalla struttura del documento sorgente
- **Presentazioni**: Richiede LibreOffice installato

## Documentazione Completa

Consulta `references/conversion_matrix.md` per l'elenco completo di tutte le coppie di conversione supportate.
