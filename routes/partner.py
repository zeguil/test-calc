from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.partner import PartnerController
from schemas.partner import PartnerBase, PartnerUpdate, PartnerList, PartnerDetail
from schemas.auth import Password
from controllers.auth import AuthController
from config.database import get_db
from providers.hash import generate_hash
from pydantic.typing import List
from providers.utils import logged_user,is_admin
from schemas.auth import SimpleUser



partner = APIRouter()


@partner.get('/partners', status_code=200, tags=['Partner'], response_model=List[PartnerList])
async def get_all_partners(user: SimpleUser = Depends(is_admin), db: Session = Depends(get_db)):
    partners = PartnerController(db).get_all_partners()
    return partners

@partner.get('/profile/partner/', status_code=200, tags=['Partner'], response_model=PartnerList)
async def get_partner(user: SimpleUser = Depends(logged_user), db: Session=Depends(get_db)):
    partner = PartnerController(db).get_partner(user.id)
    return partner

@partner.post('/singup/partner', status_code=201, tags=['Partner'], response_model=PartnerList)
async def create_partner(partner:PartnerBase ,db: Session=Depends(get_db)):
    partner.password = generate_hash(partner.password)
    new_partner = PartnerController(db).create_partner(partner)
    return new_partner

@partner.delete('/partner', tags=['Partner'])
async def delete_partner(user: SimpleUser = Depends(logged_user), db: Session=Depends(get_db)):
    return PartnerController(db).delete_partner(user.id)

@partner.put('/partner', tags=['Partner'], response_model=PartnerList)
async def update_partner(partner:PartnerUpdate, user: SimpleUser = Depends(logged_user), db: Session=Depends(get_db)):
    return PartnerController(db).update_partner(id_partner=user.id, partner=partner)
    
