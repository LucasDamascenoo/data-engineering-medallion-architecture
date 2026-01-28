


from src.extract.extract_transacoes_sqlserver import extract_transacoes
from src.extract.bronze_write import write_bronze

from src.transform.read_bronze import read_bronze
from src.transform.transform_transacoes import transform_transacoes
from src.transform.silver_writer import write_silver


def main():
    
    ## lendo bronze
    
    df = extract_transacoes()
    
    file_path = write_bronze(
        df=df,
        table_name = 'transacoes_clientes'
    )
    
    print(f"bronze salvo em {file_path}")
    
    
    ## lendo silver
    
    df_bronze = read_bronze('transacoes_clientes')
    df_silver = transform_transacoes(df_bronze)
    
    silver_path = write_silver(
        df=df_silver,
        table_name='transacoes_clientes'
    )
    
    print(f"Silver salva em: {silver_path}")
    
if __name__ == "__main__":
    main()

    
