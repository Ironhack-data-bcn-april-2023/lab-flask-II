
import requests
from flask import Flask, jsonify, request
import random
import config.sql_connection as conn
import tools.sql_queries as queries
import pandas as pd

app = Flask(__name__)

@app.route("/everything-employees")
def employees_full ():
    return queries.get_everything()

@app.route("/table/<tablename>")
def one_table (tablename):
    return queries.table_ten(tablename)

if __name__ == "__main__":
     app.run(port=9000, debug=False)