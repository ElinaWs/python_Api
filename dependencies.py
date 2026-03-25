from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from schema import UserSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return UserSchema(
        id=1,
        name="Elina",
        email="elina@example.com"
    )