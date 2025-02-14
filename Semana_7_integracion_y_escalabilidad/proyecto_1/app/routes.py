from flask import Blueprint, jsonify, request

api_routes = Blueprint('api', __name__)

# Datos simulados (como si fuera una base de datos)
usuarios = [
    {"id": 1, "nombre": "Alice","edad": "34","ciudad": "Pereira","fecha":"14/02/2025"},
    {"id": 2, "nombre": "Carlos","edad": "25","ciudad": "Pereira","fecha":"14/02/2025"},
    {"id": 3, "nombre": "Maria","edad": "30","ciudad": "Bogota","fecha":"14/02/2025"},
    {"id": 4, "nombre": "Daniel","edad": "24","ciudad": "Cali","fecha":"14/02/2025"},
    {"id": 5, "nombre": "Camila","edad": "20","ciudad": "Cali","fecha":"14/02/2025"},
    {"id": 6, "nombre": "Jairo","edad": "34","ciudad": "Bogota","fecha":"14/02/2025"},
    {"id": 7, "nombre": "Andres","edad": "25","ciudad": "Medellin","fecha":"14/02/2025"},
    {"id": 8, "nombre": "Daniela","edad": "25","ciudad": "Medellin","fecha":"14/02/2025"},
    {"id": 9, "nombre": "Sonia","edad": "26","ciudad": "Cucuta","fecha":"14/02/2025"},
    {"id": 10, "nombre": "Fernando","edad": "28","ciudad": "Bucaramanga","fecha":"14/02/2025"},
]

# Obtener todos los usuarios
@api_routes.route('/users', methods=['GET'])
def get_users():
    return jsonify(usuarios)

# Obtener un usuario por ID
@api_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in usuarios if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Crear un nuevo usuario
@api_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {"id": len(usuarios) + 1, "name": data["name"]}
    usuarios.append(new_user)
    return jsonify(new_user), 201