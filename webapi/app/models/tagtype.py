from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
import datetime
from dataclasses import dataclass
from sqlalchemy.orm import relationship


from sqlalchemy.sql.sqltypes import DateTime


from app import Base 

@dataclass
class Tagtype(Base):
    __tablename__ = "TAGTYPE"

    id: int
    libelle: str

    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)

    tag = relationship("Tags")