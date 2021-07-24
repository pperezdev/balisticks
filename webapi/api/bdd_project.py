from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc

from app.models import projects
from config import *
from app import Base

engine = create_engine(Config.WEBAPI_URI)
Session = sessionmaker(bind=engine)
session = Session()

class ProjectOperation():

    def create(arr):

        lib = arr[0]
        desc = arr[1]
        pic = arr[2]
        ban = arr[3]
        id_orga = arr[4]
        id_use = arr[5]

        # lib, desc, pic, ban, id_orga, id_use
        object = projects.Projects(lib, desc, pic, ban, id_orga, id_use)
        session.add(object)
        session.commit()
        Base.metadata.clear()

    def getInfo():
        return "ok"
