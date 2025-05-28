from sqlalchemy import Column, Integer, String, JSON
from db import Base

class Management(Base):
    __tablename__ = "management"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    position = Column(String(50), nullable=False)
    image = Column(String(250), nullable=True)
    free_day = Column(String(50), nullable=False)
    about = Column(String(255), nullable=False)
    authority = Column(JSON, nullable=False)