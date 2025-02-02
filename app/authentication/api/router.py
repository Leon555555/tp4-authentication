from fastapi import APIRouter, HTTPException
from app.authentication.dependency_injection.persistences.token import (
    create_access_token, verify_token, invalidate_token
)
from app.authentication.dependency_injection.persistences.user_bo import (
    register_user, authenticate_user
)

router = APIRouter()

@router.post("/register")
def register(username: str, password: str, full_name: str):
    user_created = register_user(username, password, full_name)
    if not user_created:
        raise HTTPException(status_code=409, detail="Usuario ya registrado")
    return {"message": "Usuario registrado exitosamente"}

@router.post("/token")
def login(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/introspect")
def introspect(token: str):
    payload = verify_token(token)
    return {"username": payload.get("sub")}

@router.post("/logout")
def logout(token: str):
    invalidate_token(token)
    return {"message": "Sesión cerrada exitosamente"}
