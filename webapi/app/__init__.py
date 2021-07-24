from flask import Flask
from datetime import date, datetime
from config import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

app = Flask(__name__, instance_relative_config=False)

def create_app(app=app):
    engine = create_engine(Config.WEBAPI_URI)

    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes
        Base.metadata.create_all(bind=engine, checkfirst=True)
        return app