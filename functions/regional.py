from models.regional import Regional
from fastapi import HTTPException

from utils.ident import check_ident


def add_regional(form, db, current_user):
    if current_user.role == "admin":
        new_regional = Regional(
            title = form.title,
            text = form.text,
            full_name = form.full_name,
            phone = form.phone,
            address = form.address
        )
        db.add(new_regional)
        db.commit()
        return {"massage": "Regional qo'shildi"}
    raise HTTPException(400, "Siz admin emassiz")


def update_regional(form, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Regional, form.ident)

        db.query(Regional).filter(Regional.id == form.ident).update({
            Regional.title: form.title,
            Regional.text: form.text,
            Regional.full_name: form.full_name,
            Regional.phone: form.phone,
            Regional.address: form.address
        })
        db.commit()
        return {"massage": "Regional yangilandi"}
    else:
        raise HTTPException(400, "Siz admin emassiz !!!")


def delete_regional(ident, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Regional, ident)

        db.query(Regional).filter(Regional.id == ident).delete()
        db.commit()
        return {"massage": "Regional o'chirildi"}
    raise HTTPException(400, "Siz admin emassiz")
