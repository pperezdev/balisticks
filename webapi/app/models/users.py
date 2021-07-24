from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Users(Base):
    __tablename__ = "USERS"

    id: int
    pseudo: str
    name: str
    surname: str
    mail: str
    password: str
    phone: str
    birthday: datetime
    picture: str
    banner: str
    inscriptiondate: datetime

    id = Column(Integer, primary_key=True)
    pseudo = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    mail = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    phone = Column(String(10), nullable=False)

    birthday = Column(
        DateTime(timezone=True),
        index=False,
        unique=False,
        nullable=False
    )

    picture = Column(String(10), nullable=False)
    banner = Column(String(10), nullable=False)

    inscriptiondate = Column(
        DateTime(timezone=True),
        index=False,
        unique=False,
        nullable=False
    )

    project = relationship("Projects")
    projectuser = relationship("Projectsusers")
    organisationuser = relationship("Organisationsusers")
    usertask = relationship("Userstasks")