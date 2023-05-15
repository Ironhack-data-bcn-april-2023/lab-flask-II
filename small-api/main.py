from flask import Flask
import requests
import random
import config.sql_connection as conn
import tools.sql_queries as queries

app = Flask(__name__)

@app.route("/everything-employees")
def example():
    return queries.get_everything()

@app.route("/table/<tablename>")
def example_table (tablename):
    return queries.table_ten(tablename)

if __name__ == "__main__":
    app.run(port=8000, debug=False)