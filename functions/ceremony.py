from models.ceremony import Ceremony
from fastapi import HTTPException
from utils.ident import check_ident


def add_ceremony(form, db, current_user):
    if current_user.role == "admin":
       new_ceremony = Ceremony(
           title = form.title,
           date = form.date,
           text = form.text
       )
       db.add(new_ceremony)
       db.commit()
       return {"massage": "Ceremony qo'shildi"}
    raise HTTPException(400, "Siz admin emassiz")


def update_ceremony(form, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Ceremony, form.ident)

        db.query(Ceremony).filter(Ceremony.id == form.ident).update({
            Ceremony.title: form.title,
            Ceremony.date: form.date,
            Ceremony.text: form.text
        })
        db.commit()
        return {"massage": "Ceremony yangilandi"}
    raise HTTPException(400, "Siz admin emassiz")


def delete_ceremony(ident, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Ceremony, ident)

        db.query(Ceremony).filter(Ceremony.id == ident).delete()
        db.commit()
        return {"massage": "Ceremony o'chirildi"}
    raise HTTPException(400, "Siz admin emassiz")