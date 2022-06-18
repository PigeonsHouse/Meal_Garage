from datetime import date
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from db.model import Food, Garage
from schemas.foods import GarageResponse


def create_food(db: Session, name: str, quantity: int, limit_at: date, user_id: str, thumbnail_url: str) -> GarageResponse:
    same_name_food = db.query(Food).filter(Food.name == name).first()
    if same_name_food is None:
        food_orm = Food(
            name=name
        )
        db.add(food_orm)
        db.commit()
        db.refresh(food_orm)
        garage_orm = Garage(
            user_id=user_id,
            food_id=food_orm.food_id,
            quantity=quantity,
            limit_at=limit_at,
            thumbnail_url=thumbnail_url
        )
        db.add(garage_orm)
        db.commit()
        db.refresh(garage_orm)
        return GarageResponse(
            food_id=food_orm.food_id,
            name=food_orm.name,
            quantity=garage_orm.quantity,
            limit_at=garage_orm.limit_at,
            thumbnail_url=garage_orm.thumbnail_url
        )
    else:
        garage = db.query(Garage).filter(
            Garage.food_id == same_name_food.food_id, Garage.user_id == user_id).first()
        if garage is None:
            garage_orm = Garage(
                user_id=user_id,
                food_id=same_name_food.food_id,
                quantity=quantity,
                limit_at=limit_at,
                thumbnail_url=thumbnail_url
            )
            db.add(garage_orm)
            db.commit()
            db.refresh(garage_orm)
            return GarageResponse(
                food_id=same_name_food.food_id,
                name=same_name_food.name,
                quantity=garage_orm.quantity,
                limit_at=garage_orm.limit_at,
                thumbnail_url=garage_orm.thumbnail_url
            )
        else:
            garage.quantity += quantity
            db.commit()

            return GarageResponse(
                food_id=same_name_food.food_id,
                name=same_name_food.name,
                quantity=garage.quantity,
                limit_at=garage.limit_at,
                thumbnail_url=garage.thumbnail_url
            )


def get_foods_list(db: Session, user_id: str) -> List[GarageResponse]:
    foods = db.query(Food.food_id, Food.name, Garage.quantity, Garage.limit_at, Garage.thumbnail_url).filter(
        Food.food_id == Garage.food_id, Garage.user_id == user_id).all()
    res_list = list(map(GarageResponse.from_orm, foods))
    return res_list


def delete_food_by_id(db: Session, food_id: str, user_id: str):
    garage_orm = db.query(Garage).filter(
        Garage.food_id == food_id, Garage.user_id == user_id).first()
    if garage_orm is None:
        raise HTTPException(status_code=400, detail="food not exist")
    db.delete(garage_orm)
    db.commit()

    return
