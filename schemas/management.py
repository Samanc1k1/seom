from pydantic import BaseModel


class CreateManagement(BaseModel):
    full_name:str
    phone:str
    position:str
    free_day:str
    about:str
    authority:str

class UpdateManagement(BaseModel):
    ident:int
    full_name:str
    phone:str
    position:str
    free_day:str
    about:str
    authority:str