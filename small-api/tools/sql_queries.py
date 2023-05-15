import config.sql_connection as conn
import pandas as pd

def get_everything():
    query= "SELECT * FROM salaries LIMIT 10;"
    engine= conn.connection_to_sql()
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def table_ten(one_table):
    query = f"SELECT * FROM  {one_table} LIMIT 10;"
    engine= conn.connection_to_sql()
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")




