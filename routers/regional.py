from fastapi import Depends, APIRouter, UploadFile
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from db import database
from functions.regional import add_regional, update_regional, delete_regional
from models.regional import Regional
from models.users import Users
from routers.login import get_current_user
from save_image import save_image
from schemas.regional import CreateRegional, UpdateRegional
from utils.ident import check_ident

regional_routers = APIRouter(tags=["Regional"])

@regional_routers.get('/get_regional')
def get_regional(ident:int = None, db: Session = Depends(database))-> Page[CreateRegional]:
    if ident:
        return db.query(Regional).filter(Regional.id == ident).first()
    else:
        a = db.query(Regional).all()
        return paginate(a)


@regional_routers.post('/create_regional')
def addd_regional(form: CreateRegional, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return add_regional(form, db, current_user)


@regional_routers.put('/update_regional')
def upd_regional(form: UpdateRegional, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return update_regional(form, db, current_user)


@regional_routers.put('/regional_image')
def images_upload(idents: int, file: UploadFile, db: Session = Depends(database)):
    check_ident(db, Regional, idents)
    image = save_image(file)
    db.query(Regional).filter(Regional.id == idents).update({Regional.image: image})
    db.commit()
    return {"Rasm muvaffaqiyatli yuklandi"}

@regional_routers.delete('/delete_regional')
def del_regional(ident: int, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return delete_regional(ident, db, current_user)
