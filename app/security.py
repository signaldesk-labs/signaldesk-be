import bcrypt
import jwt

SECRET = "local-development-secret"

def hash_password(raw: str) -> str:
    return bcrypt.hashpw(raw.encode(), bcrypt.gensalt()).decode()

def verify_password(raw: str, hashed: str) -> bool:
    return bcrypt.checkpw(raw.encode(), hashed.encode())

def issue_token(subject: str, scope: str = "user") -> str:
    return jwt.encode({"sub": subject, "scope": scope}, SECRET, algorithm="HS256")
