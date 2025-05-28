from pydantic import BaseModel
from datetime import date

class CreateEvent(BaseModel):
    date: date
    title: str
    text: str


class UpdateEvent(BaseModel):
    ident: int
    date: date
    title: str
    text: str