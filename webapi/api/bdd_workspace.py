from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc

from app.models import workspaces
from config import *
from app import Base

engine = create_engine(Config.WEBAPI_URI)
Session = sessionmaker(bind=engine)
session = Session()

class WorkspaceOperation():

    def create(arr):
        
        object = workspaces.Workspaces(
            libelle= arr["libelle"],
            id_projects=arr["project"]
        )

        session.add(object)
        session.commit()
        Base.metadata.clear()

    def select(data):
        result = session.query(workspaces.Workspaces).filter_by(id=data).all()
        return result