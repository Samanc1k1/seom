from sqlalchemy import Column, Integer, String, Text, DATE
from db import Base

class Ceremony(Base):
    __tablename__ = "ceremony"
    id = Column(Integer, autoincrement=True, primary_key=True)
    image = Column(String(255), nullable=True)
    title = Column(String(255), nullable=False)
    date = Column(DATE, nullable=False)
    text = Column(Text, nullable=False)