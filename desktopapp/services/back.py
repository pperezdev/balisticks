import requests
from config import *

class back:
    def __init__(self):
        ...

    def post_data(self, payload, name):
        try:
            return requests.post(f"{API_HOST}:{PORT_API}/{name}/", data=payload)
        except:
            return "Error"


    def insert_users(self, val):
        payload = {'name': val[0],
                   'surname': val[1],
                   'mail': val[2],
                   'phone': val[3],
                   'password': val[6]}

        return self.post_data(payload, "user")

    def insert_organisation(self, val):
        payload = {'name': val[0]}

        return self.post_data(payload, "organisation")

    def insert_project(self, val):
        payload = {'name': val[0]}

        return self.post_data(payload, "project")

    def insert_task(self, val):
        payload = {'name': val[0]}

        return self.post_data(payload, "task")
