from models.documents import Documents
from fastapi import HTTPException

from utils.ident import check_ident

def add_documents(form, db, current_user):
    if current_user.role == "admin":
        new_documents = Documents(
            doc_date=form.doc_date,
            title=form.title,
            text=form.text
        )
        db.add(new_documents)
        db.commit()
        return {"massage": "Document qo'shildi"}
    raise HTTPException(400, "Siz admin emassiz !!!")


def update_documents(form, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Documents, form.ident)

        db.query(Documents).filter(Documents.id == form.ident).update({
            Documents.doc_date : form.doc_date,
            Documents.title : form.title,
            Documents.text : form.text
        })
        db.commit()
        return {"massage": "Document yangilandi"}
    else:
        raise HTTPException(400, "Siz admin emassiz !!!")


def delete_documents(ident, db, current_user):
    if current_user.role == "admin":

        check_ident(db, Documents, ident)

        db.query(Documents).filter(Documents.id == ident).delete()
        db.commit()
        return {"massage": "Document o'chirildi"}
    raise HTTPException(400, "Siz admin emassiz !!!")