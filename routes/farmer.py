from pydantic.typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.farmer import FarmerController
from schemas.farmer import FarmerBase, FarmerUpdate, FarmerList, FarmerDetail
from schemas.auth import Password
from controllers.auth import AuthController
from config.database import get_db
from providers.hash import generate_hash
from providers.utils import logged_user, is_admin
from schemas.auth import SimpleUser


farmer = APIRouter()


@farmer.get('/farmers', status_code=200, tags=['Farmer'], response_model=List[FarmerList])
async def get_all_farmers(user: SimpleUser = Depends(is_admin), db: Session = Depends(get_db)):
    farmers = FarmerController(db).get_all_farmers()
    return farmers

@farmer.get('/profile/farmer', status_code=200, tags=['Farmer'], response_model=FarmerDetail)
async def get_farmer(user: SimpleUser = Depends(logged_user), db: Session=Depends(get_db)):
    
    farmer = FarmerController(db).get_farmer(user.id)
    return farmer

@farmer.post('/singup/farmer', status_code=201, tags=['Farmer'], response_model=FarmerList)
async def create_farmer(farmer:FarmerBase ,db: Session=Depends(get_db)):
    farmer.password = generate_hash(farmer.password)
    new_farmer = FarmerController(db).create_farmer(farmer)
    return new_farmer

@farmer.put('/farmer', tags=['Farmer'])
async def update_farmer(farmer:FarmerUpdate, user: SimpleUser = Depends(logged_user), db: Session=Depends(get_db)):
    
    farmer = FarmerController(db).update_farmer(id_farmer=user.id, farmer=farmer)
    return farmer

@farmer.delete('/farmer', tags=['Farmer'])
async def delete_farmer(user: SimpleUser = Depends(logged_user), db: Session=Depends(get_db)):
    
    FarmerController(db).delete_farmer(user.id)
    return {"msg": "deletado"}
