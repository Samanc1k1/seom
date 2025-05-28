from pydantic import BaseModel

class CreateTenders(BaseModel):
    text: str

class UpdateTenders(BaseModel):
    ident: int
    text: str