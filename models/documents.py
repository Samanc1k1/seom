from sqlalchemy import Column, String, Integer, DATE, Text
from db import Base

class Documents(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    doc_date = Column(DATE, nullable=False)
    title = Column(String(255), nullable=False)
    text = Column(Text, nullable=False)
    file = Column(String(255), nullable=True)