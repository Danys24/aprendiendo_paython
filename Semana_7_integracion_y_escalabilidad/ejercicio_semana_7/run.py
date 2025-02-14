#El archivo run.py es el punto de entrada de la API
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5001)