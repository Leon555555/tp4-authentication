from passlib.context import CryptContext

# Contexto de hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Base de datos simulada
fake_users_db = {}

def register_user(username: str, password: str, full_name: str):
    hashed_password = pwd_context.hash(password)
    fake_users_db[username] = {"username": username, "full_name": full_name, "password": hashed_password}

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not pwd_context.verify(password, user["password"]):
        return None
    return user
