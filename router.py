from fastapi import APIRouter, Depends
from typing import Annotated
from schema import UserSchema
from dependencies import get_current_user

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("/me", response_model=UserSchema)
def get_current_user_info(current_user = Depends(get_current_user)):
    """
    Получение данных текущего пользователя.
    :param user: Текущий авторизованный пользователь
    :return: Данные пользователя по схеме UserSchema
    """
    return UserSchema(
        id=current_user.id,
        name=current_user.name,
    )
