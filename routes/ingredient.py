from fastapi import APIRouter, Depends, status
from schemas.ingredient import IngredientBase
from config.database import get_db
from controllers.ingredient import IngredientController
from sqlalchemy.orm import Session
from providers.utils import logged_user
from schemas.auth import SimpleUser

ingredient = APIRouter()


@ingredient.get('/ingredients', tags=["ingredient"],status_code=200)
async def get_all_ingredients(db: Session = Depends(get_db)):
    ingredients = IngredientController(db).get_all_ingredients()
    return ingredients
    

@ingredient.get('/ingredients/{ingredient_id}', tags=["ingredient"], status_code=200)
async def get_ingredient(ingredient_id:int, db: Session = Depends(get_db)):
    ingredient = IngredientController(db).get_ingredient(ingredient_id)
    return ingredient
    

@ingredient.post('/farmers', tags=["farmer"], status_code=201)
async def create_farmer(farmer: IngredientBase, db: Session = Depends(get_db)):
    new_farmer = IngredientController(db).create_farmer(farmer)
    return new_farmer
    

@ingredient.put('/ingredients/{ingredient_id}', tags=["ingredient"], status_code=200)
async def update_ingredient(ingredient_id:int, ingredient:IngredientBase, db: Session = Depends(get_db)):
    IngredientController(db).update_ingredient(ingredient=ingredient, ingredient_id=ingredient_id)
    

@ingredient.delete('/ingredients/{ingredient_id}', tags=["ingredient"], status_code=200)
async def delete_ingredient(ingredient_id:int, db: Session = Depends(get_db)):
    IngredientController(db).delete_ingredient(ingredient_id)
    return {"status": 200}

