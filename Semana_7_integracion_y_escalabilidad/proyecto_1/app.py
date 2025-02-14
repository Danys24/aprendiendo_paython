from flask import Flask 
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Flask!"

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"Hola, {nombre}!"

@app.route('/api/datos')
def datos():
    return jsonify({"mensaje": "Hola, API!", "estado": "exitoso"})

@app.route('/api/data')
def data():
    return jsonify({"ID": "131321424", "NOMBRE": "DAVID","EDAD":"27"},
                   {"ID": "213432354", "NOMBRE": "PEDRO","EDAD":"24"},
                   {"ID": "233435456", "NOMBRE": "CAMILA","EDAD":"23"}
                   )

if __name__ == '__main__':
    app.run(debug=True)