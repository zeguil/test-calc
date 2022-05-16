from fastapi import FastAPI
from sqladmin import Admin, ModelAdmin
from fastapi.middleware.cors import CORSMiddleware
from routes.farmer import farmer
from routes.partner import partner
from routes.recipe import recipe
from routes.auth import login
from config.database import create_db, engine
from models.user import Farmer, Partner
from admin.models import Admin as Adm
from admin.routes import adm

create_db()

app = FastAPI()
admin = Admin(app, engine)

#* origins = ['http://localhost:8080']

#* app.add_middleware(
#*     CORSMiddleware,
#*     allow_origins=origins,
#*     allow_credentials=True,
#*     allow_methods=["*"],
#*     allow_headers=["*"]
# )

app.include_router(farmer)
app.include_router(partner)
app.include_router(adm)
app.include_router(login)
app.include_router(recipe)

class FarmerAdmin(ModelAdmin, model=Farmer):
    column_list = [Farmer.id,Farmer.username, Farmer.name, Farmer.email, Farmer.phone, Farmer.active_user, Farmer.automation_client]

class PartnerAdmin(ModelAdmin, model=Partner):
    column_list = [Partner.id,Partner.username, Partner.name, Partner.email, Partner.phone, Partner.brand, Partner.website]

class Admins(ModelAdmin, model=Adm):
    column_list = [Adm.id,Adm.username, Adm.name, Adm.email]

admin.register_model(Admins)
admin.register_model(FarmerAdmin)
admin.register_model(PartnerAdmin)



# documentação sqladmin
#https://aminalaee.github.io/sqladmin/authentication/