from sqlalchemy.orm import Session
from schemas.partner import PartnerBase,PartnerUpdate
from models.user import Partner, User
from sqlalchemy import delete, update


class PartnerController():
    def __init__(self, db:Session):
        self.db = db

    def create_partner(self, partner: PartnerBase):
        partner = Partner(username=partner.username,
                                    password=partner.password,
                                    email=partner.email,
                                    name=partner.name,
                                    phone=partner.phone,
                                    types="P",
                                    brand=partner.brand,
                                    website=partner.website,
                                    logo_img=partner.logo_img
                                    )
        self.db.add(partner)
        self.db.commit()
        self.db.refresh(partner)
        return partner

    def get_all_partners(self):
        partners = self.db.query(Partner).all()
        return partners

    def delete_partner(self, id_partner):
        query = delete(Partner).where(Partner.id == id_partner)
        query2 = delete(User).where(User.id == id_partner)

        self.db.execute(query)
        self.db.commit()
        self.db.execute(query2)
        self.db.commit()
        return {"msg": "Partner deleted"}

    def get_partner(self, id_partner):
        partners = self.db.query(Partner).filter_by(id=id_partner).first()
        return partners

    def update_partner(self, id_partner, partner: PartnerUpdate):
        query = update(Partner).where(Partner.id==id_partner).values(
                                    website=partner.website,
                                    logo_img=partner.logo_img,
                                    brand=partner.brand)
        query2 = update(User).where(User.id==id_partner).values(
                                    username=partner.username,
                                    email=partner.email,
                                    name=partner.name,
                                    phone=partner.phone,
                                    )
        self.db.execute(query)
        self.db.commit()
        self.db.execute(query2)
        self.db.commit()
        return partner