from datetime import date
from pydantic import BaseModel


class Foods(BaseModel):
    food_id: str
    name: str

    class Config:
        orm_mode = True


class Garages(BaseModel):
    user_id: str
    food_id: str
    quantity: int
    limit_at: date
    thumbnail_url: str


class GarageResponse(BaseModel):
    food_id: str
    name: str
    quantity: int
    limit_at: date
    thumbnail_url: str

    class Config:
        orm_mode = True


class Recipes(BaseModel):
    title: str
    recipe_thumbnail: str
    recipe_url: str


class FoodName(BaseModel):
    name: str
