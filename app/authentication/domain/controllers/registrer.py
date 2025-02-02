from fastapi import HTTPException
from authentication.persistence.models import fake_users_db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(username: str, password: str, full_name: str):
    """
    Registra un nuevo usuario en la base de datos.
    """
    if username in fake_users_db:
        raise HTTPException(status_code=409, detail="El usuario ya existe")
    fake_users_db[username] = {
        "username": username,
        "hashed_password": pwd_context.hash(password),
        "full_name": full_name
    }
    return {"message": "Usuario registrado exitosamente"}

