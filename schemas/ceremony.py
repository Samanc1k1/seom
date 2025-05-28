from pydantic import BaseModel
from datetime import date


class CreateCeremony(BaseModel):
    title: str
    date: date
    text: str


class UpdateCeremony(BaseModel):
    ident: int
    title: str
    date: date
    text: str