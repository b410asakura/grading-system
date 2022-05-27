from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    staff_id: str
    first_name: str
    last_name: str
    email: EmailStr
    photo: str
    is_active: Optional[bool] = True
    is_superuser: bool = False
    is_student: bool = False
    is_professor: bool = False

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    password: str


class UserUpdate(BaseModel):
    staff_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    photo: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[str] = False
    is_student: Optional[bool] = False
    is_professor: Optional[bool] = False


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


class StudentProfilePartialUpdateSchema(BaseModel):
    user_id: Optional[int] = None
    program: Optional[str] = None
    advisor: Optional[str] = None


class Login(BaseModel):
    staff_id: int
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    staff_id: Optional[str] = None