from sqladmin import ModelView
from models.tenders import Tenders

class TenderAdmin(ModelView, model = Tenders):
    column_list = [Tenders.id, Tenders.text]