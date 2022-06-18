from fastapi import APIRouter
from .users import user_router
from .foods import food_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=['users'])
router.include_router(food_router, prefix="/foods", tags=["foods"])
