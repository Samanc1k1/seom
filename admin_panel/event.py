from sqladmin import ModelView
from models.events import Event

class EventAdmin(ModelView, model = Event):
    column_list = [Event.id, Event.date, Event.title, Event.text]