import json
import os
import tempfile
import pytest
from app import app, DATA_FILE

@pytest.fixture
def client():
    # Creamos un archivo temporal para no pisar usuarios reales
    db_fd, temp_path = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.config['DATA_FILE'] = temp_path  # parcheamos la ruta

    # Inicializamos archivo vacío
    with open(temp_path, 'w') as f:
        f.write('[]')

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.remove(temp_path)

# --------------------
# TESTS
# --------------------

def test_crear_usuario_exitoso(client):
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "username": "testuser",
        "password": "1234"
    }
    response = client.post('/api/usuarios', json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["email"] == payload["email"]
    assert "id" in data

def test_usuario_email_duplicado(client):
    payload = {
        "name": "User One",
        "email": "dup@example.com",
        "username": "userone",
        "password": "pass"
    }
    client.post('/api/usuarios', json=payload)
    # Intento duplicar
    response = client.post('/api/usuarios', json=payload)
    assert response.status_code == 409
    data = response.get_json()
    assert "email" in data["error"]

def test_usuario_campos_faltantes(client):
    payload = {
        "name": "",
        "email": "",
        "username": "",
        "password": ""
    }
    response = client.post('/api/usuarios', json=payload)
    assert response.status_code == 400
    assert "Faltan campos" in response.get_json()["error"]

def test_falta_contraseña(client):
    payload = {
        "name": "NoPass",
        "email": "nopass@example.com",
        "username": "nopassuser",
        "password": ""
    }
    response = client.post('/api/usuarios', json=payload)
    assert response.status_code == 400
    assert "Faltan campos" in response.get_json()["error"]

def test_email_case_insensitive(client):
    payload = {
        "name": "CaseTest",
        "email": "mayus@example.com",
        "username": "casetest",
        "password": "1234"
    }
    client.post('/api/usuarios', json=payload)

    # Ahora repetimos el email en mayúsculas
    payload["email"] = "MAYUS@EXAMPLE.COM"
    response = client.post('/api/usuarios', json=payload)
    assert response.status_code == 409
    assert "email" in response.get_json()["error"]

def test_falta_username(client):
    payload = {
        "name": "NoUser",
        "email": "nouser@example.com",
        "username": "",
        "password": "1234"
    }
    response = client.post('/api/usuarios', json=payload)
    assert response.status_code == 400
    assert "Faltan campos" in response.get_json()["error"]

#LOGIN

def test_login_exitoso(client):
    # Registramos un usuario
    payload = {
        "name": "Login User",
        "email": "login@example.com",
        "username": "loginuser",
        "password": "1234"
    }
    client.post('/api/usuarios', json=payload)

    # Probamos login
    response = client.post('/login', data={
        "email": "login@example.com",
        "password": "1234"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Alta de Usuario" in response.data  # confirmamos que entró al panel

def test_login_fallido(client):
    response = client.post('/login', data={
        "email": "fake@example.com",
        "password": "wrong"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Email o contrase" in response.data  # parte del mensaje de error
