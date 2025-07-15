from flask import Flask, request, render_template, jsonify, redirect, url_for, session
import os
import json

app = Flask(__name__)
app.secret_key = "secreto123"
DATA_FILE = "usuarios.json"

# Inicializar archivo si no existe
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Página principal protegida (requiere login)
@app.route("/")
def index():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

# API para crear usuarios (desde el frontend con fetch)
@app.route("/api/usuarios", methods=["POST"])
def crear_usuario():
    nuevo = request.json
    nombre = nuevo.get("name")
    email = nuevo.get("email")
    username = nuevo.get("username")
    password = nuevo.get("password")  # 💡 Nuevo: guardar contraseña

    if not (nombre and email and username and password):
        return jsonify({"error": "Faltan campos"}), 400

    with open(DATA_FILE, "r") as f:
        usuarios = json.load(f)

    for u in usuarios:
        if u["email"].lower() == email.lower():
            return jsonify({"error": "El email ya está registrado"}), 409

    nuevo["id"] = len(usuarios) + 1
    usuarios.append(nuevo)

    with open(DATA_FILE, "w") as f:
        json.dump(usuarios, f, indent=2)

    return jsonify(nuevo), 201

# Formulario y lógica de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        with open(DATA_FILE, "r") as f:
            usuarios = json.load(f)

        for user in usuarios:
            if user["email"].lower() == email.lower() and user.get("password") == password:
                session["usuario"] = user["email"]
                return redirect(url_for("index"))

        return render_template("login.html", error="Email o contraseña incorrectos")

    return render_template("login.html", error=None)

# Cerrar sesión
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
