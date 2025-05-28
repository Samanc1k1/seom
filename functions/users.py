from models.users import Users
from routers.login import get_password_hash
from fastapi import HTTPException

from utils.ident import check_ident


def add_user(form, db):
    new_user = Users(
        name=form.name,
        username=form.username,
        password=get_password_hash(form.password),
        email=form.email,
        role="user"
    )
    db.add(new_user)
    db.commit()
    return {"massage": "Ro'yxatdan o'tdingiz"}


def update_user(form, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Users, form.ident)

        db.query(Users).filter(Users.id == form.ident).update({
            Users.name: form.name,
            Users.username: form.username,
            Users.password: get_password_hash(form.password),
            Users.email: form.email
        })
        db.commit()
        return {"massage": "User yangilandi"}


def delete_user(ident,db, current_user):
    if current_user.role == "admin":

        check_ident(db, Users, ident)

        db.query(Users).filter(Users.id == ident).delete()
        db.commit()
        return {"maasage": "User o'chirildi"}
    raise HTTPException(400, "Siz admin emassiz !!!")


def add_admin(form, db, current_user):
    if current_user.role == "admin":
        new_user = Users(
            name=form.name,
            username=form.username,
            password=get_password_hash(form.password),
            email=form.email,
            role="admin"
        )
        db.add(new_user)
        db.commit()
        return {"massage": f"{new_user.name} {new_user.role} bo'lib qo'shildi"}
    else:
        raise HTTPException(400, "Siz admin emassiz !!!")