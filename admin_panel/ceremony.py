from sqladmin import ModelView
from models.ceremony import Ceremony

class CeremonyAdmin(ModelView, model = Ceremony):
    column_list = [Ceremony.id, Ceremony.title, Ceremony.date, Ceremony.text]