# from flask import Flask
from app.models.workspaces import Workspaces
from flask import request
from config import Config
from app import app

from api.bdd_project import *
from api.bdd_users import *
from api.bdd_organisation import *
from api.bdd_task import *
from api.bdd_projectuser import *
from api.bdd_organisationuser import *
from api.bdd_workspace import *


import json

from flask import jsonify
import datetime
import requests

@app.route("/test")
def test():
    url = "http://localhost:5001/api/create/workspace"

    jsondata = {
        "libelle": "workspace",
        "project": 4
    }

    # jsondata = {
    #     "libelle": "task",
    #     "createddate": datetime.datetime.now(),
    #     "workspace": None,
    #     "project": 4
    # }

    test = requests.post(url, data=jsondata)
    return str(test.content)
    return "POST succeed"

@app.route("/")
def hello_world():
    print(datetime.datetime.now())
    return "<p>WEB API</p>"

@app.route("/api/create/<table_name>", methods=["GET","POST"])
def apiCreate(table_name):

    if request.method == "POST":
        content = request.data
        content = request.get_json()

        if table_name == "user":
            UserOperation.create(content)
            return "user inséré"

        if table_name == "organisation":
            OrganisationOperation.create(content)
            OrganisationuserOperation.create(content)
            return "organisation inséré"

        if table_name == "project":
            ProjectOperation.create(content)
            ProjectuserOperation.create(content)
            return "projet inséré"

        if table_name == "task":
            TaskOperation.create(content)
            return "task inséré"
        
        if table_name == "workspace":
            WorkspaceOperation.create(content)
            return "workspace inséré"

@app.route("/api/select/<table_name>/<value>", methods=["GET"])
def apiSelect(table_name, value):

    castValue = int(value)

    if request.method == "GET":
        if table_name == "user":
            return jsonify(UserOperation.select(castValue))
        if table_name == "organisation":
            return jsonify(OrganisationOperation.select(castValue))
        if table_name == "project":
            return jsonify(ProjectOperation.select(castValue))
        if table_name == "task":
            return jsonify(TaskOperation.select(castValue))
        if table_name == "workspace":
            return jsonify(WorkspaceOperation.select(castValue))