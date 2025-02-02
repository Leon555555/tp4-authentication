from authentication.persistence.models import fake_users_db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(username: str):
    """
    Obtiene un usuario por su nombre desde la base de datos simulada.
    """
    return fake_users_db.get(username)

def create_user(username: str, password: str, full_name: str):
    """
    Crea un nuevo usuario y lo guarda en la base de datos simulada.
    """
    if username in fake_users_db:
        return False
    fake_users_db[username] = {
        "username": username,
        "hashed_password": pwd_context.hash(password),
        "full_name": full_name
    }
    return True
