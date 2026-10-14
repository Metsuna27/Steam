from fastapi import APIRouter, Request
from pydantic import BaseModel, EmailStr, Field

from app.services.user_service import register_user, login_user

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


class UserSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


@router.post("/register", status_code=201)
def register(user: UserSchema):
    return register_user(user.email, user.password)


@router.post("/login")
def login(user: UserSchema):
    return login_user(user.email, user.password)


@router.get("/me")
def get_current_user(request: Request):
    return {
        "user_id": request.state.user_id
    }