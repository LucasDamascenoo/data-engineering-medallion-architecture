
## 🎯 Objetivo do Projeto

Construir um pipeline ETL que:

- Extraia dados de um banco **SQL Server**
- Persista dados crus na camada **Bronze**
- Transforme e padronize dados na camada **Silver**
- Separe responsabilidades entre extração, persistência, transformação e orquestração
- Utilize arquivos **Parquet** como formato de dados
- Seja reprocessável, organizado e escalável


## 🧱 Arquitetura Utilizada

### Arquitetura Medalhão

```text
Fonte (SQL Server)
        ↓
      Bronze
        ↓
      Silver
        ↓
      Gold

```

Camadas

**Bronze:**

- Contém dados crus extraídos diretamente do SQL Server

- Nenhuma transformação é aplicada

- Serve como fonte confiável para reprocessamento

- Persistido em formato Parquet

**Silver:**

- Contém dados limpos e padronizados

- Conversão de tipos de dados

- Padronização de campos textuais

- Criação de colunas derivadas (ex: tipoMovimento, valorAbsolutoMovimentacao)

- Remoção de duplicidades

- Camada confiável para consumo analítico
        
**Gold:**

- Contém dados agregados e estruturados para análise

- Aplicação de regras analíticas e métricas de negócio

- Base para dashboards, relatórios e consultas analíticas

 ## 📂 Estrutura do Projeto

```text
data-engineering-medallion-architecture/
│
├── src/
│   ├── connections/
│   │   └── sqlserver.py              # Conexão com SQL Server
│   │
│   ├── extract/
│   │   ├── extract_transacoes_sqlserver.py
│   │   └── bronze_writer.py         # Persistência Bronze
│   │
│   ├── transform/
│   │   ├── read_bronze.py
│   │   ├── transform_transacoes.py  # Transformações Silver
│   │   ├── transform_gold_transacoes.py # Transformações Gold
│   │   ├── write_silver.py
│   │   └── write_gold.py
│   │
│   └── __init__.py
│
├── configs/
│   └── db.yaml                      # Configurações de conexão
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── main.py                         # Orquestrador do pipeline
└── README.md


```


## Como Executar

Na raiz do projeto:

```Python

python main.py


```



##  Conclusão

Este projeto demonstra a implementação prática de um pipeline ETL completo utilizando a arquitetura medalhão, aplicando conceitos fundamentais de engenharia de dados como:

Extração confiável

Persistência intermediária

Transformações controladas

Estrutura analítica final

Servindo como base sólida para pipelines escaláveis e ambientes produtivos.