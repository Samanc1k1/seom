from pydantic import BaseModel
from datetime import date

class CreateDocument(BaseModel):
    doc_date: date
    title: str
    text: str


class UpdateDocuments(BaseModel):
    ident: int
    doc_date: date
    title: str
    text: str