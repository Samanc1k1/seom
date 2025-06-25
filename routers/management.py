from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from db import database
from functions.management import add_management, update_management, delete_management
from models.management import Management
from models.users import Users
from routers.login import get_current_user
from save_image import save_image
from schemas.management import CreateManagement, UpdateManagement
from utils.ident import check_ident

management_routers = APIRouter(tags=["Management"])

@management_routers.get("/get_management")
def get_management(page:int, limit:int, db: Session = Depends(database)):
    offset = (page - 1) * limit
    return db.query(Management).limit(limit).offset(offset).all()


@management_routers.post("/create_management")
def addd_management(form: CreateManagement, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return add_management(form , db, current_user)


@management_routers.put("/update_management")
def upd_management(form: UpdateManagement, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return update_management(form, db, current_user)


@management_routers.put("/management_image")
def image_upload(idents: int, file: UploadFile, db: Session = Depends(database)):
    check_ident(db, Management, idents)
    image = save_image(file)
    db.query(Management).filter(Management.id == idents).update({Management.image: image})
    db.commit()
    return {"massage": "Rasm muvaffaqiyatli yuklandi"}


@management_routers.delete("/delete_management")
def del_management(idents: int, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return delete_management(idents, db, current_user)