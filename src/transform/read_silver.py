
import pandas as pd
from pathlib import Path


def read_silver(table_name):
    path = Path(f'data/silver/{table_name}')
    
    files = sorted(path.glob('*.parquet'))
    
    if not files:
        raise FileNotFoundError('Nenhum arquivo encontrado na Silver')
    
    return pd.read_parquet(files[-1])