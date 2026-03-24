import hmac
import hashlib
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.core.config import settings

SECRET_PEPPER = settings.secret_key.encode()


def hash_password(password: str) -> str:
    # PBKDF2 com SHA256
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        SECRET_PEPPER,
        200_000,
    ).hex()


def verify_password(plain: str, hashed: str) -> bool:
    calc = hash_password(plain)
    return hmac.compare_digest(calc, hashed)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def decode_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError:
        return None
