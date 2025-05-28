from sqladmin import ModelView
from models.news import News


class NewsAdmin(ModelView, model = News):
    column_list = [News.id, News.created_at, News.title, News.description, News.text]
