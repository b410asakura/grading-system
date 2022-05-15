from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from users import crud
from users.models import User
from auth import JWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return JWT.verify_token(data, credentials_exception)


def get_current_active_superuser(current_user: User = Depends(get_current_user)):

    if not crud.is_superuser(current_user, User):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user





