from pydantic import BaseModel
from datetime import date

class CreateNews(BaseModel):
    created_at: date
    title: str
    description: str
    text: str


class UpdateNews(BaseModel):
    ident: int
    created_at: date
    title: str
    description: str
    text: str