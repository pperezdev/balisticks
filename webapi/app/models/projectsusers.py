from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Projectsusers(Base):
    __tablename__ = "PROJECTSUSERS"

    id: int
    id_USERS: int
    id_PROJECTS: int

    id = Column(Integer, primary_key=True)

    id_USERS = Column(Integer, ForeignKey('USERS.id'))
    id_PROJECTS = Column(Integer, ForeignKey('PROJECTS.id'))