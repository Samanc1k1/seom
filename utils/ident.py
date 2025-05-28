from fastapi import HTTPException


def check_ident(db, model, ident):
    item = db.query(model).filter(model.id == ident).first()
    if not item:
        raise HTTPException(404, "Bunday id mavjud emas")