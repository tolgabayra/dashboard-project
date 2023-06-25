import hashlib

class Helper:
    @staticmethod
    def generate_hash_password(password: str):
        return hashlib.sha256(password.encode()).hexdigest()
    
    