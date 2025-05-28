from sqlalchemy import Column, Integer, String, Text, DATE
from db import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATE, nullable=False)
    title = Column(String(100), nullable=False)
    text = Column(Text, nullable=False)