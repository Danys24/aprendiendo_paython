from flask import Flask
from app.routes import api_routes

def create_app():
    app = Flask(__name__)

    # Configuración de Flask (por ejemplo, configuración de base de datos)
    app.config['SECRET_KEY'] = 'supersecreto'

    # Registrar rutas
    app.register_blueprint(api_routes, url_prefix='/api')

    return app