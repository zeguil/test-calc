from sqlalchemy import String, Column, Integer, Boolean, ForeignKey, DateTime

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.database import Base
from .user import User
from sqlalchemy.sql import func
from datetime import datetime

class Recipe(Base):
    __tablename__="recipe"

    id = Column(Integer, primary_key=True)
    #todo  user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', name='fk_user'))
    user_id = Column(Integer, ForeignKey('users.id', name='fk_user'))
    user = relationship('User', back_populates='recipes')
    name = Column(String, nullable=False, unique=True, index=True)
    culture = Column(String, nullable=False, index=True)
    last_modified = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    # last_modified = Column(DateTime, onupdate=datetime.now, server_default=datetime.now)
#? ingedients = relationship('Ingredient', back_populates='recipe')
    
class FavoriteRecipe(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True, index=True)
    #todo user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', name='fk_user_fav'))
    user_id = Column(Integer, ForeignKey(
        'users.id', name='fk_user_fav'))
    recipe_id = Column(Integer, ForeignKey(
        'recipe.id', name='fk_recipe'))
    
    user = relationship('User', back_populates='favorites')
    recipe = relationship('Recipe')