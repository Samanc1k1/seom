from fastapi import Depends, APIRouter, UploadFile
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from db import database
from functions.tenders import add_tender, update_tender, delete_tender
from models.tenders import Tenders
from models.users import Users
from routers.login import get_current_user
from save_image import save_image
from save_file import save_file
from schemas.tenders import CreateTenders, UpdateTenders
from utils.ident import check_ident

tender_router = APIRouter(tags=["Tenders"])

@tender_router.get("/get_tender")
def get_tender(ident:int = None, db: Session = Depends(database))-> Page[CreateTenders]:
    if ident:
        return db.query(Tenders).filter(Tenders.id == ident).first()
    else:
        a = db.query(Tenders).all()
        return paginate(a)


@tender_router.post("/create_tender")
def addd_tender(form: CreateTenders, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return add_tender(form, db, current_user)


@tender_router.put("/update_tender")
def upd_tender(form: UpdateTenders, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return update_tender(form, db, current_user)


@tender_router.put("/tender_image")
def image_uploaded(idents: int, file: UploadFile, db: Session = Depends(database)):
    check_ident(db, Tenders, idents)
    image = save_image(file)
    db.query(Tenders).filter(Tenders.id == idents).update({Tenders.image: image})
    db.commit()
    return {"massage": "Rasm muvaffaqiyatli yuklandi"}


@tender_router.delete("/tender_file")
def file_uploaded(idents: int, file:UploadFile, db:Session = Depends(database)):
    check_ident(db, Tenders, idents)
    file = save_file(file)
    db.query(Tenders).filter(Tenders.id == idents).update({Tenders.file: file})
    db.commit()
    return {"massage": "fayl muvaffaqiyatli yuklandi"}


@tender_router.delete("/delete_tender")
def del_tender(ident: int, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return delete_tender(ident, db, current_user)