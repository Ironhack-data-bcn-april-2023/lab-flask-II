import sqlalchemy as alch # python -m pip install --upgrade 'sqlalchemy<2.0'
from dotenv import load_dotenv
import os

load_dotenv()

def connection_to_sql ():
    password=os.getenv("password")
    dbName = "empoyees"
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine



