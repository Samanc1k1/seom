from sqladmin import ModelView
from models.management import Management

class ManagementAdmin(ModelView, model = Management):
    column_list = [Management.id, Management.full_name, Management.phone, Management.position, Management.free_day, Management.about, Management.authority]
