from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc

from app.models import users
from config import *
from app import Base

engine = create_engine(Config.WEBAPI_URI)
Session = sessionmaker(bind=engine)
session = Session()

class UserOperation():

    def create(arr):
        
        object = users.Users(
            pseudo= arr["pseudo"],
            name=arr["name"],
            surname = arr["surname"],
            mail = arr["mail"],
            password = arr["password"],
            phone = arr["phone"],
            birthday = arr["birthday"],
            picture = arr["picture"],
            banner = arr["banner"],
            inscriptiondate = arr["inscriptiondate"]
        )

        session.add(object)
        session.commit()
        Base.metadata.clear()

    def select(data):
        result = session.query(users.Users).filter_by(id=data).all()
        return result