# 🎤🔐 Log Me Maybe 🎶

> _Hey, I just met you... and this is crazy..._  
> _But here’s my email, so login maybe?_ 🔐🎶

---

## 🧪 Challenge: Automatización de API REST para crear usuarios

Este proyecto cumple con los requisitos del challenge solicitado:

- ✅ Realiza un request `POST` a una API REST  
- ✅ Valida la respuesta (`status code`, contenido del `body`, headers)  
- ✅ Contiene aserciones simples  
- ✅ Muestra los resultados de forma clara y legible en el navegador 
- ✅ Automatizar pruebas

---

## ⚙️ Tecnología utilizada

- Python 3.12  
- Flask como servidor web/API  
- HTML + JavaScript (`fetch`) para el frontend  
- JSON como base de datos local simulada (`usuarios.json`)

---

## 📂 Estructura del proyecto

log-me-maybe/
├── app.py # Backend Flask
├── test_app.py # Pruebas automatizadas con pytest
├── usuarios.json # Archivo donde se guardan los usuarios
├── .gitignore
├── README.md
└── templates/
├── index.html # Formulario para crear usuarios
└── login.html # Página de login con branding

---

## 🚀 Cómo ejecutar el proyecto

### 1. Instalar dependencias:
python -m pip install flask

### 2. Ejecutar el servidor:
python app.py

### 3. Abrir el navegador:
👉 http://127.0.0.1:5000

---

✅ ¿Qué hace el sistema?
🧑‍💻 Backend (app.py)
Expone un endpoint POST en /api/usuarios

Valida que:

No falten campos

No se repita el email

Guarda los usuarios en usuarios.json

Devuelve respuestas con códigos adecuados (201, 400, 409)

Gestiona sesiones y login con /login y /logout

---

## 🧪 Pruebas Automatizadas

Usé `pytest` para crear casos de prueba que validan el comportamiento de la app.

### Casos testeados:

- ✔️ Creación de usuario válida (`/api/usuarios`)
- ✔️ Rechazo de campos vacíos
- ✔️ Email duplicado detectado
- ✔️ Login exitoso (`/login`)
- ✔️ Login fallido con credenciales incorrectas

Cada prueba evalúa el status code esperado (`201`, `400`, `409`), la respuesta del servidor y el contenido devuelto.

> Estos tests me ayudaron a validar errores reales durante el desarrollo (como el "monkey bug") y asegurar la lógica del backend.

Se pueden ejecutar fácilmente con:

python -m pytest test_app.py

---

🖥 Frontend (index.html)
Formulario para cargar:

nombre

email

nombre de usuario

contraseña

Envía los datos con fetch() al backend

Muestra mensajes visuales:

✅ Éxito

❌ Error (campos faltantes o email duplicado)

Agrega cada usuario creado al DOM

---

🤖 Herramienta de IA utilizada
ChatGPT (OpenAI) fue utilizada como guía en este proceso.

Me asistió en:

Estructura inicial del proyecto

Instalación y configuración de Python + Flask

Escritura del backend con validaciones y persistencia en archivo

Creación de frontend con manejo de errores en fetch()

Resolución de errores paso a paso

Branding, diseño visual y nombre del proyecto ✨

---

✍ Qué hice con IA y qué aprendí
🧠 Hecho con ayuda de IA:
Código base del backend y frontend

Validaciones en Python y JavaScript

Lógica para guardar en archivo JSON

Organización general del proyecto

Estilo visual y fraseología del proyecto

💪 Lo que modifiqué y aprendí en el proceso:
Cómo instalar y configurar Python correctamente

Uso de pip y la terminal en VSCode

Ejecutar un servidor Flask

Conectar frontend con backend usando fetch()

Validar entradas de usuario y manejar errores

Leer y escribir archivos .json en Python

Pensar en branding divertido y coherente

---

💬 Comentario personal
Disfruté mucho este challenge porque me permitió integrar herramientas reales de desarrollo web con automatización, validar conceptos fundamentales como API REST, y entender mejor cómo se conecta el frontend con el backend.

---

Además…

🎶 But here's my email... so login maybe?

---

🐙 GitHub-ready
¡Proyecto listo para brillar!
Nombre: log-me-maybe
Repositorio: público y con onda 🔥