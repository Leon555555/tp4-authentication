from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.authentication.api.router import router as auth_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="TP4 - Sistema de Autenticación",
    description="API de autenticación con JWT y Redis",
    version="1.0.0",
)

# Registrar las rutas del módulo de autenticación
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# Redireccionar desde "/" hacia "/docs"
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
