from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str
    username: str
    password: str
    email: str


class UpdateUser(BaseModel):
    ident:int
    name: str
    username: str
    password: str
    email: str

