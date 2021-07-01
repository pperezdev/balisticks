from sqlalchemy import Column, Text, Integer
from dataclasses import dataclass
from sqlalchemy.orm import declarative_base

Base = declarative_base()

@dataclass
class Properties(Base):
    __tablename__ = "Properties"

    Id_Properties: int
    Properties_Name: str

    Id_Properties = Column(Integer, primary_key=True)
    Properties_Name = Column(Text, nullable=False)