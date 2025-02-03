from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """Basic test to check if the API root is accessible"""
    response = client.get("/")
    assert response.status_code == 200  # Acepta 200 OK como válido
    assert "TP4 - Sistema de Autenticación" in response.text  # Verifica contenido básico

def test_docs():
    """Test to check if the Swagger docs are accessible"""
    response = client.get("/docs")
    assert response.status_code == 200

def test_openapi_json():
    """Test to check if the OpenAPI JSON is accessible"""
    response = client.get("/openapi.json")
    assert response.status_code == 200
