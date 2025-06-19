from fastapi import APIRouter, Depends, UploadFile
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from db import database
from functions.documents import add_documents, update_documents, delete_documents
from models.documents import Documents
from models.users import Users
from routers.login import get_current_user
from save_file import save_file
from schemas.documents import CreateDocument, UpdateDocuments
from utils.ident import check_ident

document_routers = APIRouter(tags=['Document'])

@document_routers.get('/get_documents')
def get_document(ident:int = None, db: Session = Depends(database))-> Page[CreateDocument]:
    if ident:
        return db.query(Documents).filter(Documents.id == ident).first()
    else:
        a = db.query(Documents).all()
        return paginate(a)


@document_routers.post('/create_document')
def addd_document(form: CreateDocument, db: Session = Depends(database), current_user: Users =Depends(get_current_user)):
    return add_documents(form, db, current_user)


@document_routers.put('/update_document')
def upd_document(forms: UpdateDocuments, db: Session = Depends(database), current_user: Users =Depends(get_current_user)):
     return update_documents(forms, db, current_user)


@document_routers.put('/document_file')
def file_upload(idents: int, file:UploadFile, db:Session = Depends(database)):
    check_ident(db, Documents, idents)
    file = save_file(file)
    db.query(Documents).filter(Documents.id == idents).update({Documents.file: file})
    db.commit()
    return {"massage": "fayl muvaffaqiyatli yuklandi"}


@document_routers.delete('/delete_document')
def del_news(idents:int, db: Session=Depends(database), current_user: Users =Depends(get_current_user)):
    return delete_documents(idents, db, current_user)