from sqlalchemy import Column, Integer, String, DATE, Text
from db import Base

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String(255), nullable=True)
    created_at = Column(DATE, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    text = Column(Text, nullable=False)