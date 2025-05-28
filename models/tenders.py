from sqlalchemy import Column, Integer, String, Text
from db import Base

class Tenders(Base):
    __tablename__ = "tenders"
    id = Column(Integer, autoincrement=True, primary_key=True)
    image = Column(String(255), nullable=True)
    text = Column(Text, nullable=False)
    file = Column(String(255), nullable=True)