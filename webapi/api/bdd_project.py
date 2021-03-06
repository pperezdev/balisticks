# from webapi.app.models.projects import Projects
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc
from sqlalchemy.sql.functions import user

from app.models import projects
from config import *
from app import Base

engine = create_engine(Config.WEBAPI_URI)
Session = sessionmaker(bind=engine)
session = Session()

class ProjectOperation():

    def create(arr):
        
        object = projects.Projects(
            libelle = arr["libelle"],
            description = arr["description"],
            picture = arr["picture"],
            banner = arr["banner"],
            id_organisations = arr["organisation"],
            id_users = arr["user"]    
        )
        
        session.add(object)
        session.commit()
        Base.metadata.clear()

    def select(data):
        result = session.query(projects.Projects).filter_by(id=data).all()
        return result