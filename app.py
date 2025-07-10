from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from flask_cors import CORS
import os 
from datetime import datetime

load_dotenv()

app = Flask(__name__)

# Leer variable de entorno para saber el entorno
ENV = os.getenv("ENV", "dev")

# Configurar CORS según entorno
if ENV == "prod":
    frontend_origin = os.getenv("FrontendOrigin")
    CORS(app, origins=[frontend_origin])
else:
    CORS(app)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
def index():
    # Probar conexión
    return "<h1>API en funcionamiento</h1>"

@app.route('/EnviarRespuestas', methods=['POST'])
def insertar():
    data = request.get_json()
    nombre = data.get('nombre')
    user_id = data.get('userId')
    respuestas = data.get('respuestas', [])

    def calificar(respuestas):
        # Eaqui se deberia recorrer las respuestas y calcular el puntaje
        return 80
    
    puntaje = calificar(respuestas)
    nuevo_resultado = {
        'nombre': nombre,
        'user_id': user_id,
        'fecha': str(datetime.now()),
        'puntaje': puntaje
    }
    mongo.db.resultadosquiz.insert_one(nuevo_resultado)
    return jsonify({'mensaje': 'Documento insertado correctamente', 'documento': nuevo_resultado})

@app.route('/TopResultados', methods=['GET'])
def top_resultados():
    top = list(mongo.db.resultadosquiz.find({}, {'_id': 0}).sort('puntaje', -1).limit(10))
    return jsonify(top)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=(ENV != "prod"))
