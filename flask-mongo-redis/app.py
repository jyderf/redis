from flask import Flask, jsonify
from pymongo import MongoClient
import redis
app = Flask(__name__)
# Conexión a MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db_mongo = mongo_client["mi_bd"]
usuarios_col = db_mongo["usuarios"]
# Conexión a Redis (usando base de datos 2)
cache = redis.Redis(host="localhost",port=6379,db=2, decode_responses=True)
@app.route("/usuario/<nombre>")
def obtener_usuario(nombre):
          if (usuario_cache := cache.get(nombre)):
                    return jsonify({"origen": "redis", "datos": eval(usuario_cache)})
          else:
                    usuario = usuarios_col.find_one({"nombre": nombre}, {"_id": 0})
          if usuario:
                    cache.set(nombre, str(usuario), ex=60) # Guarda en cache 60s
                    return jsonify({"origen": "mongo", "datos": usuario})
          else:
                    return jsonify({"error": "Usuario no encontrado"}), 404
          
if __name__ == "__main__":
          app.run(debug=True)