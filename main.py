from fastapi import FastAPI
from fastapi_pagination import add_pagination
from sqladmin import Admin
from admin_panel.ceremony import CeremonyAdmin
from admin_panel.event import EventAdmin
from admin_panel.news import NewsAdmin
from admin_panel.document import DocumentAdmin
from admin_panel.regional import RegionalAdmin
from admin_panel.management import ManagementAdmin
from admin_panel.tenders import TenderAdmin
from routers.ceremony import ceremony_routers
from routers.news import news_routers
from routers.documents import document_routers
from routers.regional import regional_routers
from routers.management import management_routers
from routers.events import event_routers
from routers.tenders import tender_router
from routers.users import user_router
from routers.login import login_router
from db import engine, Base
from starlette.middleware.sessions import SessionMiddleware
from routers.login import SECRET_KEY
from admin_panel.login import AdminAuth
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url='/')

add_pagination(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)

app.mount("/images", StaticFiles(directory="images"), name="images")

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

app.include_router(user_router)
app.include_router(login_router)
app.include_router(news_routers)
app.include_router(document_routers)
app.include_router(regional_routers)
app.include_router(management_routers)
app.include_router(event_routers)
app.include_router(tender_router)
app.include_router(ceremony_routers)


authentication_backend = AdminAuth(secret_key=SECRET_KEY)
admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_model_view(NewsAdmin)
admin.add_model_view(DocumentAdmin)
admin.add_model_view(RegionalAdmin)
admin.add_model_view(ManagementAdmin)
admin.add_model_view(EventAdmin)
admin.add_model_view(TenderAdmin)
admin.add_model_view(CeremonyAdmin)