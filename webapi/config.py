from os import environ, path
from datetime import timedelta

basedir = path.abspath(path.dirname(__file__))

class Config:

    ##### FLASK #####
    PORT_SQL = 8082
    PORT_API = 5001
    HOST = "localhost"

    ##### DATABASE #####
    DB_USERNAME = "admin"
    DB_PASSWORD = "admin"
    # DB_HOST = "0.0.0.0"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "balisticks"
    # postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
    # postgresql+pypostgresql://user:password@host:port/dbname[?key=value&key=value...]
    WEBAPI_URI = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
    # WEBAPI_URI = "postgresql+pypostgresql://admin:admin@localhost:5432/balisticks"
    # WEBAPI_URI = "postgresql+pypostgresql://{0}:{1}@{2}:{3}/{4}".format(DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

    ##### SQLALCHEMY #####
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL',WEBAPI_URI)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False