from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from functions.events import add_event, update_event, delete_event
from schemas.events import CreateEvent, UpdateEvent
from models.events import Event
from models.users import Users
from routers.login import get_current_user

event_routers = APIRouter(tags=["/Events"])


@event_routers.get("/get_event")
def get_event(db: Session = Depends(database)):
    return db.query(Event).all()


@event_routers.post("/create_event")
def addd_event(form: CreateEvent, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return add_event(form, db, current_user)


@event_routers.put("/update_event")
def upd_event(form: UpdateEvent, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return update_event(form, db, current_user)


@event_routers.delete("/delete_event")
def del_event(ident: int, db: Session = Depends(database), current_user: Users = Depends(get_current_user)):
    return delete_event(ident, db, current_user)