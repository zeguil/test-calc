from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Column, Integer, Boolean, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

#? from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

class User(Base):
    __tablename__ = "users"

    #todo id = db.Column(UUID(as_uuid=True), primary_key=True, index=True)
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, index=True)
    types = Column(String(1), index=True)
    recipes = relationship('Recipe', back_populates='user')
    favorites = relationship('FavoriteRecipe', back_populates='user')


    __mapper_args__ = {
        'polymorphic_on':types
    }


    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User {0}>".format(self.username)

class Farmer(User):
    __tablename__ = "farmers"

    #todo id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True, index=True)
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    active_user = Column(Boolean, index=True)
    automation_client = Column(Boolean)
    

    __mapper_args__ = {
        'polymorphic_identity':"F",
    }

    def __repr__(self):
        return f"<Paciente {self.username}>"

class Partner(User):
    __tablename__ = "partners"
    
    #todo id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True, index=True)
    id = Column(Integer, ForeignKey('users.id'), primary_key=True, index=True)
    brand = Column(String, unique=True, index=True)
    logo_img = Column(String)
    website = Column(String, unique=True, index=True)
    __mapper_args__ = {
        'polymorphic_identity':"P",
    }

def __repr__(self):
    return f"<Partner {self.username}>"


