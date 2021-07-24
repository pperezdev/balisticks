from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from .projectsusers import Projectsusers
from .tasks import Tasks

from app import Base 

@dataclass
class Projects(Base):
    __tablename__ = "projects"

    id: int
    libelle: str
    description: str
    picture: str
    banner: str
    id_organisations: int
    id_users: int


    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    picture = Column(String(50), nullable=False)
    banner = Column(String(50), nullable=False)
    
    id_organisations = Column(Integer, ForeignKey('organisations.id'))
    id_users = Column(Integer, ForeignKey('users.id'))

    projectuser = relationship("Projectsusers")
    task = relationship("Tasks")