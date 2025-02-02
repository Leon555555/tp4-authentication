from fastapi import Depends, HTTPException
from authentication.dependency_injection.persistences.token import verify_token

def logout_user(token: str = Depends(verify_token)):
    """
    Cierra la sesión de un usuario.
    """
    username = token.get("sub")
    if not username:
        raise HTTPException(status_code=401, detail="Token inválido")
    # Aquí podrías implementar la lógica para eliminar el token de Redis u otra base de datos.
    return {"message": "Sesión cerrada exitosamente"}
