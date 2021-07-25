from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from .tasks import Tasks

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Workspaces(Base):
    __tablename__ = "workspaces"

    id: int
    libelle: str
    id_projects: int

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)

    # task = relationship("Task")

    id_projects = Column(Integer, ForeignKey('projects.id'))