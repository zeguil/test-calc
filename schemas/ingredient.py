from pydantic import BaseModel,HttpUrl,constr
from pydantic.typing import Optional, Literal, List
from decouple import config


#serializer
class IngredientBase(BaseModel):
    id: Optional[int] = None
    name: str
    brand: str
    measure_unit: int

class Ingredient(IngredientBase):
    name: str
    brand: str
    measure_unit: int

    class Config:
        orm_mode = True












