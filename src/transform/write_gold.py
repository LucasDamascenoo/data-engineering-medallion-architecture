
from datetime import datetime
from pathlib import Path


def write_gold(df,table_name):
    
    totay = datetime.today().strftime('%Y-%m-%d')
    path= Path(f'data/gold/{table_name}')
    
    path.mkdir(parents=True, exist_ok=True)
    
    file_path = path / f'{table_name}_{totay}.parquet'
    
    df.to_parquet(file_path,index=False)
    
    return file_path