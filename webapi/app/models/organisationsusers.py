from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Organisationsusers(Base):
    __tablename__ = "organisationsusers"

    id: int
    id_organisations: int
    id_users: int

    id = Column(Integer, primary_key=True)

    id_organisations = Column(Integer, ForeignKey('organisations.id'))
    id_users = Column(Integer, ForeignKey('users.id'))