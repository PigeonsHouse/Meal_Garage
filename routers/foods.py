from datetime import date
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from cruds.foods import create_food, get_foods_list, delete_food_by_id
from utils import get_current_user
from schemas.foods import GarageResponse

food_router = APIRouter()


@food_router.post('/', response_model=GarageResponse)
async def post_food(name: str, quantity: int, limit_at: date, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    garage_res = create_food(db, name, quantity, limit_at, user_id)
    return garage_res


@food_router.get('/', response_model=List[GarageResponse])
async def get_foods(db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    garage_list = get_foods_list(db, user_id)
    return garage_list


@food_router.delete('/{food_id}')
async def delete_food(food_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    delete_food_by_id(db, food_id, user_id)
    return {'detail': 'OK'}


# @food_router.get('/recipe')
# async def get_recipe():
#     pass
