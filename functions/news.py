from models.news import News
from fastapi import HTTPException
from utils.ident import check_ident


def add_news(form, db, current_user):
    if current_user.role == "admin":
        new_news = News(
            created_at=form.created_at,
            title=form.title,
            description=form.description,
            text=form.text
        )
        db.add(new_news)
        db.commit()
        return {'message': "Yangilik qo'shildi"}
    raise HTTPException(400, "Siz admin emassiz !!!")


def update_news(form, db, current_user):
    if current_user.role == "admin":

        check_ident(db, News, form.ident)

        db.query(News).filter(News.id == form.ident).update({
            News.created_at: form.created_at,
            News.title: form.title,
            News.description: form.description,
            News.text: form.text
        })
        db.commit()
        return {'massage': "News yangilandi"}
    else:
        raise HTTPException(400, "Siz admin emassiz !!!")


def delete_news(ident, db, current_user):
    if current_user.role == "admin":

        check_ident(db, News, ident)

        db.query(News).filter(News.id == ident).delete()
        db.commit()
        return {'messege': "Yangilik o'chirildi"}
    else:
        raise HTTPException(400, "Siz admin emassiz !!!")