# from flask import Flask
from config import Config
from app import app
from api.bdd_project import *

@app.route("/")
def hello_world():
    return "<p>WEB API</p>"

@app.route("/api/create/<table_name>/<value>")
def api(table_name, value):

    # value = value.split(";")

    # if table_name == "project":
    #     ProjectOperation().create(value)
        return "projet insérer"