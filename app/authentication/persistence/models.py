from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {}  # Base de datos ficticia en memoria
