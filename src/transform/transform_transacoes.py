
import pandas as pd
from pathlib import Path

def transform_transacoes(df):
    
    df = df.copy()
    
    df['dataMovimentacao'] = pd.to_datetime(df['dataMovimentacao'])
    
    df["transacaoMotivo"] = df["transacaoMotivo"].str.upper()
    
    df['tipoMovimento'] = df['valorMovimentacao'].apply(
        lambda x: 'CREDITO' if x > 0 else 'DEBITO'
    )
    
    df['valorAbsolutoMovimentacao'] = df['valorMovimentacao'].abs()
    
    df = df.drop_duplicates(subset=['NSU'])

    return df
