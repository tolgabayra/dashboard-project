import hashlib
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Helper:
    @staticmethod
    def generate_hash_password(password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(password: str, hashed_password: str):
        generated_hash = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password == generated_hash
    
    @staticmethod
    def generate_access_token(payload: dict, expires_delta: timedelta):
        to_encode = payload.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    

    @staticmethod
    def generate_refresh_token(payload: dict, expires_delta: timedelta):
        to_encode = payload.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(days=7)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt