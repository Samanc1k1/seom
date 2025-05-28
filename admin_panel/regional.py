from models.regional import Regional
from sqladmin import ModelView

class RegionalAdmin(ModelView, model = Regional):
    column_list = [Regional.id, Regional.title, Regional.text, Regional.full_name, Regional.phone, Regional.address]
