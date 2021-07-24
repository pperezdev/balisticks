from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Workspaces(Base):
    __tablename__ = "WORKSPACES"

    id: int
    libelle: str
    id_PROJECTS: int

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)

    task = relationship("TASK")

    id_PROJECTS = Column(Integer, ForeignKey('PROJECTS.id'))