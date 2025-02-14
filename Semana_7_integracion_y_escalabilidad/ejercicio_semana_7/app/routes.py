from flask import Blueprint, jsonify, request
import requests as req
import pandas as pd
import json

#Para ejcutar este proceso primero se debe ejecutar la api que se encuentra que se llama proyecto_1 ejecutando el archivo run.py
url = "http://127.0.0.1:5000/api/users"

# Hace la solicitud tipo Get
response = req.get(url)

# Verificar que la respuesta es correcta (código 200)
if response.status_code == 200:
    data = response.json()  # Convertir la respuesta en un diccionario de Python
    
    # Crear un DataFrame de pandas
    df = pd.DataFrame(data)

    df_consolidado = pd.DataFrame(df['id'])
    df_consolidado['nombre'] = df['nombre']
    df_consolidado['edad'] = df['edad']
    df_consolidado['ciudad'] = df['ciudad']
    df_consolidado['dia'] = df['fecha'].astype(str).str.slice(0,2)
    df_consolidado['mes'] = df['fecha'].astype(str).str.slice(3,5)
    df_consolidado['anio'] = df['fecha'].astype(str).str.slice(6,10)

    
    # Mostrar las primeras filas
    print(df_consolidado)
else:
    print(f"Error en la petición: {response.status_code}")

api_routes = Blueprint('api', __name__)

# Transforma el dataframe a json 
usuarios_str = df_consolidado.to_json(orient="records")
usuarios = json.loads(usuarios_str)

#print(usuarios)

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

