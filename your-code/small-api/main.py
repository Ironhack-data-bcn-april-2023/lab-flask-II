import requests
import random
from flask import Flask
from flask import Flask, request, jsonify
import tools.quer as queries

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello world!"
@app.route('/random-number')

def random_int():
    return str(random.randint(0,10))

@app.route("/everything-employees")
def employees_full():
    return queries.get_everything()

@app.route("/table/<tablename>")
def one_table (tablename):
    return queries.table_ten(tablename)

if __name__ == "__main__":
     app.run(port=9000, debug=False)
