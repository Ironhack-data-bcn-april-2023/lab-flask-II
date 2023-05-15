import pandas as pd
import config.sql_connection as conn

def get_everything():
    query = "SELECT * FROM employees LIMIT 10;"
    engine = conn.connection_to_sql()
    df = pd.read_sql_query(query, engine)
    return df.to_dict('employees')

def table_ten(ten):
    query = f"SELECT * FROM  {ten} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict("remployees")

