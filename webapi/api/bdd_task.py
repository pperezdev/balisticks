from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc

from app.models import tasks
from config import *
from app import Base

engine = create_engine(Config.WEBAPI_URI)
Session = sessionmaker(bind=engine)
session = Session()

class TaskOperation():

    def create(arr):

        object = tasks.Tasks(
            libelle = arr["libelle"],
            createddate = arr["createddate"],
            id_workspaces = arr["workspace"],
            id_projects = arr["project"]
        )
        
        session.add(object)
        session.commit()
        Base.metadata.clear()

    def select(data):
        result = session.query(tasks.Tasks).filter_by(id=data).all()
        return result