"""
Configuration file for the RDB application.
Contains file paths, settings, and other configuration constants.
"""

import sys
from pathlib import Path

if str(Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent))
    
_utils_dir = Path(__file__).parent / "src" / "utils"
if str(_utils_dir) not in sys.path:
    sys.path.insert(0, str(_utils_dir))

PROJECT_ROOT = Path(__file__).parent

DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DATA_DIR = DATA_DIR / "output"
RAW_DATA_DIR = DATA_DIR / "raw"

RAW_DATA_FILE = RAW_DATA_DIR / "test.csv"

CSV_ENCODINGS = ['utf-8', 'utf-8-sig', 'latin1', 'cp1252']
CSV_DELIMITERS = ['\t', ',', ';']

for directory in [DATA_DIR, OUTPUT_DATA_DIR, RAW_DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
