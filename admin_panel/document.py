from models.documents import Documents
from sqladmin import ModelView

class DocumentAdmin(ModelView, model = Documents):
    column_list = [Documents.id, Documents.doc_date, Documents.title, Documents.text]