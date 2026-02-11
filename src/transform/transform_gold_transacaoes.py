import pandas as pd


def transform_gold_transacoes(df):

    df_gold = (
        df.groupby(
            ["dataMovimentacao", "idCliente", "tipoMovimento"]
        )
        .agg(
            totalMovimentado=("valorMovimentacao", "sum"),
            quantidadeTransacoes=("NSU", "count"),
            valorMedio=("valorMovimentacao", "mean"),
        )
        .reset_index()
    )

    return df_gold