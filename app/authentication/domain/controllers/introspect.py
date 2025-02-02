from fastapi import HTTPException, Depends
from authentication.dependency_injection.persistences.token import verify_token
from authentication.persistence.models import fake_users_db

def introspect_user(token: str = Depends(verify_token)):
    """
    Verifica si un token es válido y obtiene información del usuario asociado.
    """
    username = token.get("sub")
    if not username or username not in fake_users_db:
        raise HTTPException(status_code=401, detail="Token inválido o usuario no encontrado")
    return {"username": username, "message": "Token válido"}
