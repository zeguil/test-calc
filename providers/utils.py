import re
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from controllers.auth import AuthController
from config.database import get_db
from providers.access_token import verify_acess_token

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

async def logged_user(token: str = Depends(oauth2_schema),
                         db: Session = Depends(get_db)):
    exeception_401 = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    try:
        username = verify_acess_token(token)
    except JWTError:
        raise exeception_401

    if not username:
        raise exeception_401

    user = AuthController(db).get_by_username(username)

    if not user:
        raise exeception_401

    return user

async def is_admin(token: str = Depends(oauth2_schema),
                         db: Session = Depends(get_db)):
    exeception_401 = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    try:
        username = verify_acess_token(token)
    except JWTError:
        raise exeception_401

    if not username:
        raise exeception_401

    user = AuthController(db).get_by_username(username)

    if not user:
        raise exeception_401

    if user.types != "A":
        raise HTTPException(status_code=401, detail="You don't have permission")
        
    return True

def admin_or_farmer(token: str = Depends(oauth2_schema),
                         db: Session = Depends(get_db)):
    exeception_401 = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    try:
        username = verify_acess_token(token)
    except JWTError:
        raise exeception_401

    if not username:
        raise exeception_401
    
    user = AuthController(db).get_by_username(username)
    
    if user.types != "P":
        raise HTTPException(status_code=401, detail="You don't have permission")
        
    return True

def admin_or_partner(token: str = Depends(oauth2_schema),
                         db: Session = Depends(get_db)):
    exeception_401 = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    try:
        username = verify_acess_token(token)
    except JWTError:
        raise exeception_401

    if not username:
        raise exeception_401
    
    user = AuthController(db).get_by_username(username)
    
    if user.types != "F":
        raise HTTPException(status_code=401, detail="You don't have permission")
        
    return True

    

