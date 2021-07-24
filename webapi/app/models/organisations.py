from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Organisations(Base):
    __tablename__ = "ORGANISATIONS"

    id: int
    name: str
    picture: str
    banner: str
    creationdate: datetime

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    picture = Column(String(10), nullable=False)
    banner = Column(String(10), nullable=False)

    creationdate = Column(
        DateTime(timezone=True),
        index=False,
        unique=False,
        nullable=False
    )

    project = relationship("Projects")
    organisationuser = relationship("Organisationsusers")  