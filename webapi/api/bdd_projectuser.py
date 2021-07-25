# from webapi.app.models.projects import Projects
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc

from app.models import projectsusers
from config import *
from app import Base

engine = create_engine(Config.WEBAPI_URI)
Session = sessionmaker(bind=engine)
session = Session()

class ProjectuserOperation():

    def create(arr):
    
        object = projectsusers.Projectsusers(
            id_users = arr["user"],
            id_projects = arr["project"]
        )
        
        session.add(object)
        session.commit()
        Base.metadata.clear()

    def select(data):
        result = session.query(projectsusers.Projectsusers).filter_by(id=data).all()
        return result