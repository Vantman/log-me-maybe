import requests

# Lista de usuarios de prueba
usuarios = [
    {
        "name": "Juan Pérez",
        "email": "juan.perez@example.com",
        "username": "juanp"
    },
    {
        "name": "María López",
        "email": "maria.lopez@example.com",
        "username": "marial"
    }
]

# URL de la API de prueba
url = "https://jsonplaceholder.typicode.com/users"

# Enviar POST para cada usuario
for usuario in usuarios:
    print(f"\n👤 Enviando usuario: {usuario['email']}...")

    response = requests.post(url, json=usuario)

    # ✅ Validaciones
    assert response.status_code == 201, f"❌ Status esperado: 201, recibido: {response.status_code}"
    assert "application/json" in response.headers.get("Content-Type", ""), "❌ Respuesta no es JSON"
    
    data = response.json()

    # Aserción simple: validar que el nombre recibido coincida con el enviado
    assert data.get("name") == usuario["name"], f"❌ Nombre recibido: {data.get('name')} no coincide con el enviado: {usuario['name']}"

    # ✅ Mostrar resultados legibles
    print("✅ Usuario creado correctamente.")
    print(f"🔢 ID generado: {data.get('id')}")
    print(f"📧 Email: {data.get('email')}")
    print(f"🧾 Headers: {response.headers['Content-Type']}")
