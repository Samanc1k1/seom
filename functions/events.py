from models.events import Event
from fastapi import HTTPException
from utils.ident import check_ident


def add_event(form, db, current_user):
    if current_user.role == "admin":
        new_event = Event(
            date = form.date,
            title = form.title,
            text = form.text
        )
        db.add(new_event)
        db.commit()
        return {"massage": "Yangi event qo'shildi"}
    raise HTTPException(400, "Siz admin emassiz !!!")


def update_event(form, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Event, form.ident)

        db.query(Event).filter(Event.id == form.ident).update({
            Event.date: form.date,
            Event.title: form.title,
            Event.text: form.text
        })
        db.commit()
        return {"massage": "Event yangilandi"}
    raise HTTPException(400, "Siz admin emassiz !!!")


def delete_event(ident, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Event, ident)

        db.query(Event).filter(Event.id == ident).delete()
        db.commit()
        return {"massage": "Event o'chirildi"}
    raise HTTPException(400, "Siz admin emassiz")