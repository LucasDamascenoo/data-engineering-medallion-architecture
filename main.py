


from src.extract.extract_transacoes_sqlserver import extract_transacoes
from src.extract.bronze_write import write_bronze

def main():
    
    df = extract_transacoes()
    
    file_path = write_bronze(
        df=df,
        table_name = 'transacoes_clientes'
    )
    
    print(f"bronze salvo em {file_path}")
    
    
if __name__ == "__main__":
    main()

    
