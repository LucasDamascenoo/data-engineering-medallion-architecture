#%%

from datetime import datetime
from pathlib import Path
import pandas as pd


def write_bronze(df,table_name):
    
    today = datetime.today().strftime('%Y-%m-%d')
    
    path = Path(f'data/bronze/{table_name}')
    path.mkdir(parents=True, exist_ok=True)
    
    file_path = path  / f"{table_name}_{today}.parquet"
    
    df.to_parquet(file_path, index=False)
    
    return file_path


