from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Organisationsusers(Base):
    __tablename__ = "ORGANISATIONSUSERS"

    id: int
    id_ORGANISATIONS: int
    id_USERS: int

    id = Column(Integer, primary_key=True)

    id_ORGANISATIONS = Column(Integer, ForeignKey('ORGANISATIONS.id'))
    id_USERS = Column(Integer, ForeignKey('USERS.id'))