from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from .models import Admin
from .schemas import AdminBase, AdminList
from models.user import User
from config.database import get_db
from providers.hash import generate_hash

adm = APIRouter()

@adm.post('/singup/admin', status_code=200, tags=['Admin'], response_model=AdminList)
async def create_admin(admin:AdminBase ,db: Session=Depends(get_db)):
    admin.password = generate_hash(admin.password)

    new_admin = Admin(username=admin.username,
                    password=admin.password,
                    email=admin.email,
                    name=admin.name,
                    phone=admin.phone,
                    types="A")
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

@adm.get('/admin', status_code=200, tags=['Admin'])
async def list_admin(db: Session=Depends(get_db)):
    admins = db.query(Admin).all()
    return adminsks

@adm.delete('/admin', status_code=200, tags=['Admin'])
async def delete_admin(self, id_admin):
        query = delete(Admin).where(Admin.id == id_admin)
        query2 = delete(User).where(User.id == id_admin)

        self.db.execute(query1)
        self.db.commit()
        self.db.execute(query2)
        self.db.commit()