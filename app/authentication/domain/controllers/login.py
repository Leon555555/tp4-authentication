from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from authentication.dependency_injection.persistences.user_bo import authenticate_user
from authentication.dependency_injection.persistences.token import create_access_token

def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Autentica un usuario y genera un token de acceso.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}
