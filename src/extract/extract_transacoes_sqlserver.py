

import pandas as pd

from src.connections.sqlserver import get_sqlserver_connection


def extract_transacoes():
    conn = get_sqlserver_connection()

    query = """
        SELECT *
        FROM dbo.transacoes_clientes
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df




