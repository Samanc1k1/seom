from sqlalchemy import Column, String, Text, Integer
from db import Base

class Regional(Base):
    __tablename__ = "regional_management"
    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String(255), nullable=True)
    title = Column(String(255), nullable=False)
    text = Column(Text, nullable=False)
    full_name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)