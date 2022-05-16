from sqlalchemy.orm import Session
from schemas.ingredient import IngredientBase 
from models.ingredient import Ingredient
from fastapi import status, HTTPException
from sqlalchemy import delete, update

class IngredientController():
    async def __init__(self, db: Session):
        self.db = db

    async def create_ingredient(self, ingredient: IngredientBase):
        new_ingredient = await Ingredient(
            name = ingredient.name,
            brand = ingredient.brand,
            measure_unit = ingredient.measure_unit,
            # recipe_id = ingredient.recipe_id
        )
        await self.db.add(new_ingredient)
        await self.db.commit()
        await self.db.refresh(new_ingredient)
        return new_ingredient

    async def get_all_ingredients(self):
        ingredients = await self.db.query(Ingredient).all()
        return ingredients

    async def get_ingredient(self, ingredient_id):
        ingredient = await self.db.query(Ingredient).filter_by(id=ingredient_id).first()
        return ingredient

    async def update_ingredient(self, ingredient_id:int, ingredient:IngredientBase):
        query = await update_ingredient(Ingredient).where(
            Ingredient.id == ingredient_id
        ).values(
                name = ingredient.name,
                brand = ingredient.brand,
                measure_unit = ingredient.measure_unit,
                recipe_id = ingredient.recipe_id)
                     
        await self.db.execute(query)
        await self.db.commit()
        return ingredient

    async def delete_ingredient(self, ingredient_id:int):
        ingredient = await query(Ingredient).filter(Ingredient.id == ingredient_id).first()

        if ingredient is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
        
        await self.db.delete(ingredient)
        await self.db.commit()
        return ingredient