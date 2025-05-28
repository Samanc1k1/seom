from pydantic import BaseModel


class CreateRegional(BaseModel):
    title: str
    text: str
    full_name: str
    phone: str
    address: str


class UpdateRegional(BaseModel):
    ident: int
    title: str
    text: str
    full_name: str
    phone: str
    address: str