"""
Merges multiple CSV files by country code (derived from the first two
characters of each filename).  Returns a single DataFrame with all rows
combined and a ``Country_Code`` column identifying the source group.
"""
import pandas as pd
import config
from utils.csv_handler import read_csv


def merge_csv(file_path=None, uploaded_files=None):
    """Merge multiple CSV files grouped by country code.

    Parameters
    ----------
    file_path : str or None
        Unused (kept for pipeline convention). Falls back to
        ``config.RAW_DATA_FILE`` but multi-file merge requires
        *uploaded_files*.
    uploaded_files : list of UploadedFile, optional
        Streamlit ``UploadedFile`` objects to merge.

    Returns
    -------
    pd.DataFrame
        Concatenated DataFrame with an added ``Country_Code`` column.
    """
    file_path = file_path or config.RAW_DATA_FILE

    if not uploaded_files:
        # Single-file fallback: read the pipeline temp file as-is
        df = read_csv(str(file_path))
        return df

    frames = []
    for uf in uploaded_files:
        filename = uf.name
        if not filename.lower().endswith('.csv'):
            continue

        country_code = filename[:2].upper()

        try:
            df = pd.read_csv(uf, encoding='utf-16', sep='\t')
        except (UnicodeDecodeError, UnicodeError):
            uf.seek(0)
            df = pd.read_csv(uf, encoding='utf-8')

        df['Country_Code'] = country_code
        frames.append(df)

    if not frames:
        return pd.DataFrame()

    merged_df = pd.concat(frames, ignore_index=True, sort=False)
    return merged_df
