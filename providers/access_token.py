from datetime import datetime, timedelta
from jose import jwt

# JOSE Config vars
SECRET_KEY = "uma senha qualquer"
ALGORITHM = "HS256"
EXPIRES_IN_MINUTES = 30

def create_access_token(data_base: dict):
    data = data_base.copy()
    expires = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)

    data.update({'exp': expires})

    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

def verify_acess_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')

