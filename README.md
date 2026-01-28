
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
Dados crus, sem regras de negócio, persistidos exatamente como vêm da fonte.

**Silver:**
Dados limpos, tipados, padronizados e deduplicados, prontos para consumo analítico.
        
**Gold:**

 ## 📂 Estrutura do Projeto

```text
data-engineering-medallion-architecture/
│
├── src/
│   ├── connections/
│   │   └── sqlserver.py
│   │
│   ├── extract/
│   │   ├── extract_transacoes_sqlserver.py
│   │   └── bronze_writer.py
│   │
│   ├── transform/
│   │   ├── read_bronze.py
│   │   ├── transform_transacoes.py
│   │   └── write_silver.py
│   │
│   └── __init__.py
│
├── configs/
│   └── db.yaml
│
├── data/
│   ├── bronze/
│   └── silver/
│
├── main.py
└── README.md


```

