import random
from flask import Flask, jsonify, request
import random_data
import funcoes

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": 200, "message": "API Isabella Galvão"})

@app.route("/aleatorios", methods=["GET"])
def aleatorios():
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route("/argumentos/", methods=["GET"])
def argumentos(nome):
    return jsonify({"status": 200, "data": nome})

@app.route("/argumentos", methods=["GET"])
def arg_implicito():
    nome = request.args.get("nome")
    return jsonify({"status": 200, "data": nome})

@app.route("/idades", methods=["GET"])
def idades():
    pessoas = random_data.pessoas
    pessoa1, pessoa2, pessoa3 = funcoes.maior_de_50(pessoas)
    
    return jsonify({"status": 200 ,"dados" : {"pessoa1" : pessoa1, "pessoa2" : pessoa2, "pessoa3" : pessoa3}})

if __name__ == '__main__':
    app.run(debug=True)