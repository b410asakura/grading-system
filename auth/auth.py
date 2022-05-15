from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_sqlalchemy import db

from auth.JWT import create_access_token
from auth.hashing import Hash
from deps.oauth2 import get_current_active_superuser
from users import crud
from users.models import User
from users.schemas import UserCreateSchema, UserBaseSchema, SuperuserCreateSchema

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends()):
    user = db.session.query(User).filter(User.staff_id == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = create_access_token(data={"sub": user.staff_id})

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/create_user", response_model=UserBaseSchema)
def create_users(request: UserCreateSchema,
                 current_user: User = Depends(get_current_active_superuser)):
    return crud.create_users(request)


@router.post("/superuser")
def create_superuser(request: SuperuserCreateSchema):
    return crud.create_superuser(request)