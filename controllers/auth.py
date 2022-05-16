from fastapi import status, HTTPException, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User
from schemas.auth import Password, Login, LoginSuccess, ForgotPassword, ResetPassword
from providers.hash import verify_hash, generate_hash
from providers.access_token import create_access_token, verify_acess_token
from providers.emails import send_email
from jose import JWTError

class AuthController():
    def __init__(self, db: Session):
        self.db = db

    def token(self, login_data: Login):
        user = self.db.query(User).filter_by(username= login_data.username).first()

        if not user:
            raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
        
        valid_password = verify_hash(login_data.password, user.password)
        if not valid_password:
            raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

        # Gerar Token JWT
        new_token = create_access_token({'sub': user.username})
        return LoginSuccess(user=user, access_token=new_token)


    def change_password(self, psw: Password, user_id):
        user = self.db.query(User).filter_by(id=user_id).first()
        
        if user:

            valid_password = verify_hash(psw.password, user.password)

            if valid_password:
                user.password = generate_hash(psw.new_password)
                self.db.commit()
                return "Senha alterada com sucesso"
            
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Senha incorreta")

        raise HTTPException(status_code=404, detail="Usuário não existe")

    def forgot_password(self, psw:ForgotPassword):
        user = self.db.query(User).filter_by(email=psw.email).first()
        if user:
            email = user.email
            name = user.name
            new_token = create_access_token({'sub': user.username})

            send_email(token=new_token, email=email, name=name)
            return f"Email enviado para: {email}"

        raise HTTPException(status_code=404, detail="Email não cadastrado")

    def reset_password(self, token, psw: ResetPassword):
        
        username = verify_acess_token(token)
        
        if username:
            if  psw.new_password == psw.confirm_password:
                user = self.db.query(User).filter_by(username=username).first()
                user.password = generate_hash(psw.new_password)
                self.db.commit()
                return "Senha alterada com sucesso"

            raise HTTPException(status_code=400, detail="As senhas não coincidem")

        raise HTTPException(status_code=401, detail='Token inválido')


    def get_by_username(self, username) -> User:
        query = select(User).where(
            User.username == username)
        return self.db.execute(query).scalars().first()

