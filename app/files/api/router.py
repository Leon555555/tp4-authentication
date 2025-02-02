from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Rutas de archivos funcionando correctamente"}
