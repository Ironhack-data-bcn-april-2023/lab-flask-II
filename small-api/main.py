from flask import Flask
import requests
import random
import tools.sql_queries as sql
import config.sql_connection as conn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_int():
    return str(random.randint(0, 10))


@app.route("/everything-employees")
def example():
    return sql.get_everything()


@app.route("/table/<one_table>")
def table(one_table):
    return str(sql.table_ten(one_table))


if __name__ == "__main__":
    app.run(port=9000, debug=False)