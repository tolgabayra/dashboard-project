from database import SessionLocal
from model import User
from util.helper import Helper

db = SessionLocal()

class AuthService:
    @staticmethod
    def login(email: str, password: str):
        user = User.query.filter_by(email=email).first()
        if user is None:
            return False
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def register(payload: str):
        user = User(
            name = payload["name"],
            email = payload["email"],
            password = Helper.generate_hash_password(payload["password"])
        )

        
    