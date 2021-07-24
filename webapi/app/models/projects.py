from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from app import Base 

@dataclass
class Projects(Base):
    __tablename__ = "PROJECTS"

    id: int
    libelle: str
    description: str
    picture: str
    banner: str
    id_ORGANISATIONS: int
    id_USERS: int


    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    picture = Column(String(50), nullable=False)
    banner = Column(String(50), nullable=False)
    
    id_ORGANISATIONS = Column(Integer, ForeignKey('ORGANISATIONS.id'))
    id_USERS = Column(Integer, ForeignKey('USERS.id'))

    projectuser = relationship("Projectsusers")
    task = relationship("Tasks")