from typing import Dict
import pandas as pd
import config
from csv_handler import read_csv

def normalize_headers() -> pd.DataFrame:
    """
    Normalize the header row of the dataframe:
    - Trim excess spaces from column names
    - Convert column names to title case
    
    Returns:
        DataFrame with normalized headers
    """
    df = read_csv(str(config.RAW_DATA_FILE))
    
    df_normalized = df.copy()
    new_columns: Dict[str, str] = {}
    
    for col in df_normalized.columns:
        trimmed_col = ' '.join(str(col).split())
        normalized_col = trimmed_col.title()
        new_columns[col] = normalized_col
    
    df_normalized.rename(columns=new_columns, inplace=True)
    
    return df_normalized
