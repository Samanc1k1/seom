from models.tenders import Tenders
from fastapi import HTTPException
from utils.ident import check_ident

def add_tender(form, db, current_user):
    if current_user.role == "admin":
        new_tender = Tenders(
            text = form.text
        )
        db.add(new_tender)
        db.commit()
        return {"massage": "Yangi tender qo'shildi"}
    raise HTTPException(400, "Siz admin emassiz")


def update_tender(form, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Tenders, form.ident)

        db.query(Tenders).filter(Tenders.id == form.ident).update({
            Tenders.text: form.text
        })
        db.commit()
        return {"massage": "Tender yangilandi"}
    raise HTTPException(400, "Siz admin emassiz")


def delete_tender(ident, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Tenders, ident)

        db.query(Tenders).filter(Tenders.id == ident).delete()
        db.commit()
        return {"massage": "Tender o'chirildi"}
    raise HTTPException(400, "Siz admin emassiz")