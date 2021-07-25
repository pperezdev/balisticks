# from webapi.app.models.projects import Projects
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc

from app.models import organisations
from config import *
from app import Base

engine = create_engine(Config.WEBAPI_URI)
Session = sessionmaker(bind=engine)
session = Session()

class OrganisationOperation():

    def create(arr):

        object = organisations.Organisations(
            name = arr["name"],
            picture = arr["picture"],
            banner = arr["banner"],
            createddate = arr["createddate"]
        )
        session.add(object)
        session.commit()
        Base.metadata.clear()

    def select(data):
        result = session.query(organisations.Organisations).filter_by(id=data).all()
        return result