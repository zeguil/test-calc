from sqlalchemy.orm import Session
from schemas.recipe import RecipeBase, RecipeList
from models.recipe import Recipe,FavoriteRecipe
from models.user import User
from fastapi import status, HTTPException
from sqlalchemy import delete, update, select
from sqlalchemy import func

class RecipeController():
    def __init__(self, db: Session):
        self.db = db

    def create_recipe(self, recipe: RecipeBase, user_id:int):
        new_recipe = Recipe(
            name = recipe.name,
            culture = recipe.culture,
            user_id = user_id,
            # proportion_mixA = recipe.proportion_mixA,
            # proportion_mixB = recipe.proportion_mixB,
            # proportion_mixC = recipe.proportion_mixC,
        )
        self.db.add(new_recipe)
        self.db.commit()
        self.db.refresh(new_recipe)
        return new_recipe

    def get_all_recipes(self):
        recipes = self.db.query(Recipe).all()
        return recipes

    async def get_recipe(self, recipe_id):
        recipe = await self.db.query(Recipe).filter_by(id=recipe_id).first()
        return recipe

    def update_recipe(self, recipe_id:int, recipe:RecipeList, user_id:int):
        get_recipe = self.db.query(Recipe).filter(Recipe.id == recipe_id).first()
        
        if get_recipe is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Receita não existe")
        
        owner = self.db.query(Recipe).filter(Recipe.user_id == user_id).first()
        admin = self.db.query(User).filter(User.id == user_id).first()
        
        if owner or admin.types == "A":
            query = update(Recipe).where(
                Recipe.id == recipe_id
            ).values(
                    name = recipe.name,
                    culture = recipe.culture,
                    # proportion_mixA = recipe.proportion_mixA,
                    # proportion_mixB = recipe.proportion_mixB,
                    # proportion_mixC = recipe.proportion_mixC, 
                    )
                        
            self.db.execute(query)
            self.db.commit()
            return recipe
        return HTTPException(status_code=401, detail="Usuário não é o criador da receira")

    def delete_recipe(self, recipe_id:int, user_id:int):
        recipe = self.db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if recipe is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
        
        owner = self.db.query(Recipe).filter(Recipe.user_id == user_id).first()
        admin = self.db.query(User).filter(User.id == user_id).first()
        
        
        if owner or admin.types == "A":
            recipe = self.db.query(Recipe).filter(Recipe.id == recipe_id).first()
            favorite = self.db.query(FavoriteRecipe).filter(FavoriteRecipe.recipe_id == recipe_id).first()
            
            if favorite is None:
                self.db.delete(recipe)
                self.db.commit()
                return {'msg': "Receita deletada"}
            else:
                self.db.delete(favorite)
                self.db.commit()
                self.db.delete(recipe)
                self.db.commit()
                return {'msg': "Receita deletada"}
        
        return HTTPException(status_code=401, detail='Usuário não é o criador da receira')
    
    async def get_my_recipes(self, user_id):
        recipes = self.db.query(Recipe).filter(Recipe.user_id == user_id).all()
        
        if recipes:
            return recipes
        return HTTPException(status_code=404, detail='Usuário não tem receitas cadastradas')
    
    async def add_favorite(self, recipe_id, user_id):
        favorite = FavoriteRecipe(user_id=user_id, recipe_id=recipe_id)
        self.db.add(favorite)
        self.db.commit()
        self.db.refresh(favorite)
        return favorite
    
    # ! rever
    async def my_favorites(self, user_id:int):
        favorites = self.db.query(FavoriteRecipe).filter(FavoriteRecipe.user_id == user_id).all()
        return favorites
    
    async def delete_favorite(self, user_id:int, favorite_id):
        favorite = self.db.query(FavoriteRecipe).filter(FavoriteRecipe.user_id == user_id).first()
        
        return {'msg': f"Receita {favorite.name} removida de favoritos"}