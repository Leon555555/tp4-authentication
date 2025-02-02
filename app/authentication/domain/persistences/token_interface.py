import redis
from datetime import timedelta

# Configuración de Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def save_token(username: str, token: str, expires: timedelta):
    """
    Guarda un token asociado a un usuario en Redis.
    """
    redis_client.setex(username, int(expires.total_seconds()), token)

def get_token(username: str):
    """
    Obtiene un token asociado a un usuario desde Redis.
    """
    return redis_client.get(username)

def delete_token(username: str):
    """
    Elimina un token asociado a un usuario desde Redis.
    """
    redis_client.delete(username)
