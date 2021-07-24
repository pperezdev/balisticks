# from flask import Flask
from config import Config
from app import app
from api.bdd_project import *
from flask import jsonify
import datetime

@app.route("/")
def hello_world():
    print(datetime.datetime.now())
    return "<p>WEB API</p>"

@app.route("/api/create/<table_name>/<value>")
def apiCreate(table_name, value):

    splitValue = value.split(";")

    if table_name == "project":
        ProjectOperation().create(splitValue)
        return "projet insérer"

@app.route("/api/select/<value>")
def apiSelect(value):

    castValue = int(value)
    result = ProjectOperation.select(castValue)
    return jsonify(result)