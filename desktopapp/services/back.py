import requests
from config import *
import datetime
import json

class back:
    def __init__(self):
        ...

    def post_data(self, payload, name):
        try:
            return requests.post(f"http://{API_HOST}:{PORT_API}/api/create/{name}", data=payload)
        except:
            return "Error"

    def get_data(self, name):
        try:
            return json.load(requests.get(f"http://{API_HOST}:{PORT_API}/{name}"))
        except:
            return "Error"

    def insert_users(self, val):
        payload = {
            "pseudo": val[0] + val[1],
            "name": val[0],
            "surname": val[1],
            "mail": val[2],
            "phone": val[3],
            "password": val[6],
            "birthday": "2021-07-25 18:49:28.055818",
            "picture": "nothing",
            "banner": "nothing",
            "inscriptiondate": datetime.datetime.now()
        }

        return self.post_data(payload, "user")

    def insert_organisation(self, val):
        payload = {
            'user': val[0],
            'organisation': val[1],
            'name': val[2],
            "picture": "nothing",
            "banner": "nothing",
            "createdate": datetime.datetime.now()
        }

        return self.post_data(payload, "organisation")

    def insert_project(self, val):
        payload = {
            'user': val[0],
            'organisation': val[1],
            'libelle': val[2],
            "description": val[3],
            "picture": "nothing",
            "banner": "nothing"
        }

        return self.post_data(payload, "project")

    def insert_task(self, val):
        payload = {'name': val[0]}

        return self.post_data(payload, "task")
