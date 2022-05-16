from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from config.database import get_db
from schemas.recipe import RecipeBase, RecipeList
from schemas.auth import SimpleUser, Password
from controllers.recipe import RecipeController
from providers.utils import logged_user, is_admin, admin_or_farmer


recipe = APIRouter()


@recipe.get('/recipes', tags=["recipe"],status_code=200)
async def get_all_recipes(user: SimpleUser = Depends(logged_user),db: Session = Depends(get_db)):
    return RecipeController(db).get_all_recipes()
     
    

@recipe.get('/recipes/{recipe_id}', tags=["recipe"], status_code=200, response_model=RecipeList)
async def get_recipe(recipe_id:int, user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    recipes = RecipeController(db).get_recipe(recipe_id)
    return recipes
    

@recipe.post('/recipe', tags=["recipe"], status_code=201)
async def create_recipes(recipe: RecipeBase, db: Session = Depends(get_db), user: SimpleUser = Depends(logged_user)):
    user_id = user.id
    return RecipeController(db).create_recipe(recipe, user_id)
    
    

@recipe.put('/recipes/{recipe_id}', tags=["recipe"], status_code=200)
async def update_recipe(recipe_id:int, recipe:RecipeList, user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    response = RecipeController(db).update_recipe(recipe=recipe, recipe_id=recipe_id, user_id=user.id)
    return response
    

@recipe.delete('/recipes/{recipe_id}', tags=["recipe"], status_code=200)
async def delete_recipe(recipe_id:int, user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    response = RecipeController(db).delete_recipe(recipe_id, user.id)
    return response

@recipe.get('/myrecipes', tags=["recipe"], status_code=200)
async def my_recipes(user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    user_id = user.id
    recipe = await RecipeController(db).get_my_recipes(user_id)
    return recipe


#*#############################################################################################################

@recipe.get('/recipes/favorites', tags=["recipe"], status_code=200)
async def favorite_recipes(user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    user_id= user.id
    recipes = await RecipeController(db).my_favorites(user_id)
    return recipes


@recipe.post('/recipes/favorites/{recipe_id}', tags=["recipe"], status_code=200)
async def favorite_recipes(recipe_id:int, user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    user_id= user.id
    recipes = await RecipeController(db).add_favorite(recipe_id, user_id)
    return recipes


@recipe.delete('/recipes/favorites/{recipe_id}', tags=["recipe"], status_code=200)
async def delete_favorite(recipe_id:int, user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    user_id= user.id
    recipes = RecipeController(db).delete_favorite(user_id, recipe_id)
    return recipes
