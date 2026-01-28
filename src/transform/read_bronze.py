import pandas as pd
from pathlib import Path



def read_bronze(table_name):
    
    path = Path(f"data/bronze/{table_name}")
    files = sorted(path.glob('*.parquet'))
    
    
    if not files:
        raise FileNotFoundError("nenhum arquivo bronze encontrado")
    
    
    return pd.read_parquet(files[-1])

print(read_bronze('transacoes_clientes')) 
