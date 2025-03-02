from flask import Flask, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os 

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
def index():
    # Probar conexión
    users = list(mongo.db.users.find({}, {"_id": 0})) 
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
