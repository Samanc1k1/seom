from models.management import Management
from fastapi import HTTPException
from utils.ident import check_ident

def add_management(form, db, current_user):
    if current_user.role == "admin":
        new_management = Management(
            full_name = form.full_name,
            phone = form.phone,
            position = form.position,
            free_day = form.free_day,
            about = form.about,
            authority = form.authority
        )
        db.add(new_management)
        db.commit()
        return {"massage": "Management qo'shildi"}
    raise HTTPException(400, "Siz admin emassiz !!!")


def update_management(form, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Management, form.ident)

        db.query(Management).filter(Management.id == form.ident).update({
            Management.full_name: form.full_name,
            Management.phone: form.phone,
            Management.position: form.position,
            Management.free_day: form.free_day,
            Management.about: form.about,
            Management.authority: form.authority
        })
        db.commit()
        return {"massage": "Management yangilandi"}
    raise HTTPException(400, "Siz admin emassiz !!!")


def delete_management(ident, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Management, ident)

        db.query(Management).filter(Management.id == ident).delete()
        db.commit()
        return {"massage": "Management o'chirildi"}
    raise HTTPException(400, "Siz admin emassiz !!!")