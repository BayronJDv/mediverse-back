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
    puntaje = data.get('puntaje')
    imgurl = data.get('imgurl')

    nuevo_resultado = {
        'nombre': nombre,
        'user_id': user_id,
        'fecha': str(datetime.now()),
        'puntaje': puntaje,
        'imgurl': imgurl
    }
    mongo.db.resultadosquiz.insert_one(nuevo_resultado)
    return jsonify({'mensaje': 'Documento insertado correctamente', 'documento': nuevo_resultado})

@app.route('/TopResultados', methods=['GET'])
def top_resultados():
    top = list(mongo.db.resultadosquiz.find({}, {'_id': 0}).sort('puntaje', -1).limit(10))
    for resultado in top:
        print(resultado)
    return jsonify(top)

@app.route('/MejorResultado', methods=['POST'])
def mejor_resultado():
    data = request.get_json()
    user_id = data.get('userId')
    if not user_id:
        return jsonify({'mensaje': 'Falta el userId en la petición'}), 400
    resultado = mongo.db.resultadosquiz.find_one({'user_id': user_id}, {'_id': 0}, sort=[('puntaje', -1)])
    if resultado:
        # Calcular la posición del resultado respecto a todos
        puntaje = resultado.get('puntaje', 0)
        posicion = mongo.db.resultadosquiz.count_documents({'puntaje': {'$gt': puntaje}}) + 1
        resultado['position'] = posicion
        return jsonify(resultado)
    else:
        return jsonify({'mensaje': 'No se encontraron resultados para este usuario'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=(ENV != "prod"))

