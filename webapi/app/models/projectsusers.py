from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Projectsusers(Base):
    __tablename__ = "projectsusers"

    id: int
    id_users: int
    id_projects: int

    id = Column(Integer, primary_key=True)

    id_users = Column(Integer, ForeignKey('users.id'))
    id_projects = Column(Integer, ForeignKey('projects.id'))