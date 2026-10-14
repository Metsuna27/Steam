import os
import jwt

from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from pwdlib import PasswordHash

from app.repositories.user_repository import (
    find_user_by_email,
    create_user
)

password_hash = PasswordHash.recommended()

SECRET_KEY = os.environ["JWT_SECRET"]
ALGORITHM = "HS256"


def register_user(email: str, password: str):

    email = email.strip().lower()

    if find_user_by_email(email):
        raise HTTPException(
            status_code=409,
            detail="Utilisateur déjà existant"
        )

    hashed_password = password_hash.hash(password)

    user = {
        "email": email,
        "password": hashed_password
    }

    try:
        user_id = create_user(user)
    except Exception as exc:
        from pymongo.errors import DuplicateKeyError

        if isinstance(exc, DuplicateKeyError):
            raise HTTPException(
                status_code=409,
                detail="Utilisateur déjà existant"
            ) from exc
        raise

    return {
        "id": user_id,
        "email": email
    }


def login_user(email: str, password: str):

    email = email.strip().lower()
    user = find_user_by_email(email)

    if not user or not password_hash.verify(
        password,
        user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Email ou mot de passe incorrect"
        )

    expiration = datetime.now(timezone.utc) + timedelta(hours=1)

    token = jwt.encode(
        {
            "sub": str(user["_id"]),
            "exp": expiration
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }