from fastapi import APIRouter, Depends, UploadFile
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from db import database
from functions.ceremony import add_ceremony, update_ceremony, delete_ceremony
from models.ceremony import Ceremony
from models.users import Users
from routers.login import get_current_user
from save_image import save_image
from schemas.ceremony import CreateCeremony, UpdateCeremony

ceremony_routers = APIRouter(tags=["Ceremony"])

@ceremony_routers.get("/get_ceremony")
def get_ceremony(ident:int = None, db: Session = Depends(database))-> Page[CreateCeremony]:
    if ident:
        return db.query(Ceremony).filter(Ceremony.id == ident).first()
    else:
        a = db.query(Ceremony).all()
        return paginate(a)



@ceremony_routers.post("/create_ceremony")
def create_ceremony(form: CreateCeremony, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return add_ceremony(form, db, current_user)


@ceremony_routers.put("/update_ceremony")
def upd_ceremony(form: UpdateCeremony, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return update_ceremony(form, db, current_user)


@ceremony_routers.put("/ceremony_image")
def image_uploaded(idents: int, file: UploadFile, db: Session = Depends(database)):
    image = save_image(file)
    db.query(Ceremony).filter(Ceremony.id == idents).update({Ceremony.image: image})
    db.commit()
    return {"massage": "Rasm muvaffaqiyatli yuklandi"}


@ceremony_routers.delete("/delete_ceremony")
def del_ceremony(ident: int, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return delete_ceremony(ident, db, current_user)