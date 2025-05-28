from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from functions.users import add_user, add_admin, update_user, delete_user
from models.users import Users
from routers.login import get_current_user
from schemas.users import CreateUser, UpdateUser

user_router = APIRouter(tags=["Users"])


@user_router.get('/get')
def get_user(db: Session = Depends(database)):
    return db.query(Users).all()


@user_router.post('/create')
def create_user(form: CreateUser, db: Session = Depends(database)):
    return add_user(form, db)


@user_router.put('/update_user')
def upd_user(form: UpdateUser, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return update_user(form, db, current_user)


@user_router.delete('/delete_user')
def del_user(ident: int, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return delete_user(ident, db, current_user)


@user_router.post('/create_admin')
def create_admin(form: CreateUser, db: Session = Depends(database), current_users: Users = Depends(get_current_user)):
    return add_admin(form, db, current_users)