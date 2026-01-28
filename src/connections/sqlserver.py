
from pathlib import Path
import yaml
import pyodbc

def get_sqlserver_connection():
    base_dir = Path(__file__).resolve().parents[2]
    config_path = base_dir / "configs" / "db.yaml"

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    sql_cfg = cfg["sqlserver"]

    conn_str = (
        f"DRIVER={{{sql_cfg['driver']}}};"
        f"SERVER={sql_cfg['server']};"
        f"DATABASE={sql_cfg['database']};"
    )

    if sql_cfg.get("trusted_connection") == "yes":
        conn_str += "Trusted_Connection=yes;"
    else:
        conn_str += f"UID={sql_cfg['user']};PWD={sql_cfg['password']};"

    return pyodbc.connect(conn_str)
