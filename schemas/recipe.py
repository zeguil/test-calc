from pydantic import BaseModel, constr, Field
from pydantic.typing import Optional, List
from datetime import datetime
from .ingredient import Ingredient
from schemas.auth import SimpleUser


#serializer
class RecipeBase(BaseModel):
    id: Optional[int] = None
    name: str
    culture: str
    user_id: Optional[int]
    user: Optional[SimpleUser]
    # proportion_mixA: List[Ingredient] = []
    # proportion_mixB: List[Ingredient] = []
    # proportion_mixC: List[Ingredient] = []


class RecipeList(RecipeBase):
    name: str
    culture: str

    class Config:
        orm_mode = True


    class Config:
        orm_mode = True

        
class Favorites(BaseModel):
    id: Optional[int] = None
    
    user_id: Optional[int]
    recipe_id: Optional[int]

    user: Optional[SimpleUser]
    recipe: Optional[RecipeList]

    class Config:
        orm_mode = True