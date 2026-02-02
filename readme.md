# Data Pipeline

A data processing application for cleaning and transforming CSV and Excel files. Run steps in sequence from a Streamlit UI, preview results, and download the output.

## Features

- **Normalize headers** — Trim whitespace and convert column names to title case.
- **Remove duplicates** — Drop duplicate rows, optionally by selected columns.
- **Add date metadata** — Detect a date column (e.g. `date`, `date_published`) and add Year, Month, Day, and Quarter.
- **Translate columns** — Translate selected text columns to a target language (e.g. English) with optional source auto-detection and similarity grouping to reduce API calls.

Input formats: CSV, Excel (`.xlsx`, `.xls`). Output: CSV or Excel download.

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

## Installation

From the project root:

```bash
pip install -r requirements.txt
```

## Usage

Start the Streamlit app:

```bash
python main.py
```

Or run Streamlit directly:

```bash
streamlit run app.py
```

Then:

1. Upload a CSV or Excel file.
2. In the sidebar, select one or more steps (or "Run all steps").
3. Configure options for "Remove duplicates" (columns) and "Translate columns" (columns, target/source language) if used.
4. Click **Run pipeline**, review the preview table, and use **Download CSV** or **Download Excel** to save the result.

## Project structure

```
project-root/
  main.py              # Entry point; launches Streamlit app
  app.py               # Streamlit UI and pipeline orchestration
  config.py            # Paths, encodings, delimiters
  requirements.txt
  data/
    raw/               # Default location for raw input files (CLI usage)
    output/            # Default output location (CLI usage)
  src/
    cleaning/
      normalize_headers.py
      removing_duplicates.py
    transformation/
      add_dates_metadata.py
      translate_columns.py
    utils/
      csv_handler.py   # CSV/Excel read and write helpers
```

## Configuration

Edit `config.py` to change:

- `PROJECT_ROOT`, `DATA_DIR`, `OUTPUT_DATA_DIR`, `RAW_DATA_DIR`
- `RAW_DATA_FILE` (default input for script/CLI usage)
- `CSV_ENCODINGS`, `CSV_DELIMITERS` used when reading CSV

## License

Rythmos DB
