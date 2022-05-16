from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from config.database import get_db
from providers.hash import generate_hash
from providers.utils import logged_user
from controllers.auth import AuthController
from schemas.auth import Login, LoginSuccess, SimpleUser, Password, ForgotPassword, ResetPassword

login = APIRouter()

@login.post('/token', tags=["Auth"], response_model=LoginSuccess)
async def sing_in(login_data: Login, db: Session = Depends(get_db)):
    return AuthController(db).token(login_data)

@login.get('/me', tags=["Auth"], response_model=SimpleUser)
async def me(user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    return user

@login.put('/change-password', tags=["Auth"], status_code=200)
async def change_password(password: Password, user: SimpleUser = Depends(logged_user), db: Session = Depends(get_db)):
    return AuthController(db).change_password(psw=password, user_id=user.id)

@login.post('/reset-password', tags=["Auth"], status_code=200)
async def forgot_password(password: ForgotPassword, db: Session = Depends(get_db)):
    return AuthController(db).forgot_password(psw=password)

@login.post('/reset-password/{token}', tags=["Auth"], status_code=200)
async def reset_password(token, user: ResetPassword, db: Session = Depends(get_db)):
    return AuthController(db).reset_password(token=token, psw=user)

# Criar rota pra receber token de mudança de senha
     

