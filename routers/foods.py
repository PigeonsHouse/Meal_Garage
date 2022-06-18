from datetime import date
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from cruds.foods import create_food, get_foods_list, delete_food_by_id, update_garage
from utils.utils import get_current_user
from utils.scraping import scraping_data
from schemas.foods import GarageResponse, Recipes

food_router = APIRouter()


@food_router.post('', response_model=GarageResponse)
async def post_food(name: str, quantity: int, limit_at: date, thumbnail_url: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    garage_res = create_food(
        db, name, quantity, limit_at, user_id, thumbnail_url)
    return garage_res


@food_router.get('', response_model=List[GarageResponse])
async def get_foods(db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    garage_list = get_foods_list(db, user_id)
    return garage_list


@food_router.put('/{food_id}', response_model=GarageResponse)
async def update_food(food_id: str, quantity: int, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    garage = update_garage(db, quantity, food_id, user_id)
    return garage


@food_router.delete('/{food_id}')
async def delete_food(food_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    delete_food_by_id(db, food_id, user_id)
    return {'detail': 'OK'}


@food_router.get('/{recipe_name}', response_model=List[Recipes])
async def get_recipe_by_name(recipe_name: str):
    res = scraping_data(recipe_name)
    return res


@food_router.get('/recipes')
async def get_recipes():
    pass
