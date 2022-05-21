from typing import Optional, List

from pydantic import BaseModel, EmailStr

from users.models import Role


class UserBaseSchema(BaseModel):
    staff_id: str
    first_name: str
    last_name: str
    email: EmailStr
    photo: str
    is_active: Optional[bool] = True
    is_superuser: bool = False
    role: Role

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    password: str


class UserUpdate(UserBaseSchema):
    password: Optional[str] = None


class UserInDBBase(UserBaseSchema):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class SuperuserCreateSchema(BaseModel):
    staff_id: int
    password: str


class StudentProfileSchema(BaseModel):
    user_id: int
    program: str
    advisor: str


class Login(BaseModel):
    staff_id: int
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    staff_id: Optional[str] = None