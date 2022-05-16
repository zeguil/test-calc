from config.database import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

class Ingredient(Base):
    __tablename__="ingredient"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True, index=True)
    brand = Column(String(20), nullable=False, index=True)
    measure_unit = Column(Integer)
    # recipe_id = Column(Integer, ForeignKey('ingredient.id', name='fk_ingredient'), nullable=False)
    # recipe = relationship('Recipe', back_populates='ingredients')

# relação de proportions com IngredientKs