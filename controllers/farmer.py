from sqlalchemy.orm import Session
from schemas.farmer import FarmerBase
from models.user import Farmer,User
from sqlalchemy import delete, update
from providers.emails import validEmail
from fastapi import HTTPException

class FarmerController():
    def __init__(self, db:Session):
        self.db = db

    def create_farmer(self, farmer: FarmerBase):
        
        if not validEmail(farmer.email):
            raise HTTPException(status_code=400,detail="Email is invalid")
            
        new_farmer = Farmer(username=farmer.username,
                                    password=farmer.password,
                                    email=farmer.email,
                                    name=farmer.name,
                                    phone=farmer.phone,
                                    types="F",
                                    active_user=True,
                                    automation_client=True
                                    )
        self.db.add(new_farmer)
        self.db.commit()
        self.db.refresh(new_farmer)
        return new_farmer

    def get_all_farmers(self):
        farmers = self.db.query(Farmer).all()
        return farmers

    def delete_farmer(self, id_farmer):
        query = delete(Farmer).where(Farmer.id == id_farmer)
        query2 = delete(User).where(User.id == id_farmer)

        self.db.execute(query1)
        self.db.commit()
        self.db.execute(query2)
        self.db.commit()

    def get_farmer(self, id_farmer):
        farmers = self.db.query(Farmer).filter_by(id=id_farmer).first()
        return farmers

    def update_farmer(self, id_farmer, farmer: FarmerBase):
        query = update(Farmer).where(Farmer.id==id_farmer).values(
                                    active_user=farmer.active_user,
                                    automation_client=farmer.automation_client)

        query2 = update(User).where(User.id==id_farmer).values(
                                    username=farmer.username,
                                    email=farmer.email,
                                    name=farmer.name,
                                    phone=farmer.phone,)
        self.db.execute(query)
        self.db.commit()
        self.db.execute(query2)
        self.db.commit()
        return farmer