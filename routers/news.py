from fastapi import APIRouter, Depends, UploadFile
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from db import database
from functions.news import add_news, update_news, delete_news
from models.news import News
from models.users import Users
from routers.login import get_current_user
from save_image import save_image
from schemas.news import CreateNews, UpdateNews
from utils.ident import check_ident


news_routers = APIRouter(tags=['Yangilik'])

@news_routers.get('/get_news')
def get_news(ident:int = None, db: Session = Depends(database))-> Page[CreateNews]:
    if ident:
        return db.query(News).filter(News.id == ident).first()
    else:
        a = db.query(News).all()
        return paginate(a)


@news_routers.post('/create_news')
def addd_news(form: CreateNews, db: Session = Depends(database), current_user: Users =Depends(get_current_user)):
    return add_news(form, db, current_user)


@news_routers.put('/update_news')
def upd_news(forms: UpdateNews, db: Session = Depends(database), current_user: Users =Depends(get_current_user)):
     return update_news(forms, db, current_user)


@news_routers.put('/news_images')
def image_uploads(idents: int, file:UploadFile, db:Session = Depends(database)):
    check_ident(db, News, idents)
    image = save_image(file)
    db.query(News).filter(News.id == idents).update({News.image: image})
    db.commit()
    return {"massage": "Rasm muvaffaqiyatli yuklandi"}


@news_routers.delete('/delete_news')
def del_news(idents:int, db: Session=Depends(database), current_user: Users =Depends(get_current_user)):
    return delete_news(idents, db, current_user)