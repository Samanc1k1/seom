from fastapi import Depends, APIRouter, UploadFile
from sqlalchemy.orm import Session
from db import database
from functions.tenders import add_tender, update_tender, delete_tender
from models.tenders import Tenders
from models.users import Users
from routers.login import get_current_user
from save_image3 import save_image3
from save_file2 import save_file2
from schemas.tenders import CreateTenders, UpdateTenders

tender_router = APIRouter(tags=["Tenders"])

@tender_router.get("/get_tender")
def get_tender(db: Session = Depends(database)):
    return db.query(Tenders).all()


@tender_router.post("/create_tender")
def addd_tender(form: CreateTenders, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return add_tender(form, db, current_user)


@tender_router.put("/update_tender")
def upd_tender(form: UpdateTenders, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return update_tender(form, db, current_user)


@tender_router.put("/update_image3")
def image_uploaded(idents: int, file: UploadFile, db: Session = Depends(database)):
    image = save_image3(file)
    db.query(Tenders).filter(Tenders.id == idents).update({Tenders.image: image})
    db.commit()
    return {"massage": "Rasm muvaffaqiyatli yuklandi"}


@tender_router.delete("/update_file2")
def file_uploaded(idents: int, file:UploadFile, db:Session = Depends(database)):
    file = save_file2(file)
    db.query(Tenders).filter(Tenders.id == idents).update({Tenders.file: file})
    db.commit()
    return {"massage": "fayl muvaffaqiyatli yuklandi"}


@tender_router.delete("/delete_tender")
def del_tender(ident: int, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return delete_tender(ident, db, current_user)