import random
from flask import app, blueprints, jsonify, request

from symbol import funcdef # type: ignore

bp = blueprints("api", __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({"status": 200, "message": "API Isabella Galvão"})

@bp.route("/api/aleatorios", methods=["GET"])
def aleatorios():
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/api/argumentos/", methods=["GET"])
def argumentos(nome):
    return jsonify({"status": 200, "data": nome})

@bp.route("/api/argumentos", methods=["GET"])
def arg_implicito():
    nome = request.args.get("nome")
    return jsonify({"status": 200, "data": nome})

@bp.route("/api/idades", methods=["GET"])
def idades():
    pessoas = random_data.pessoas # type: ignore
    pessoa1, pessoa2, pessoa3 = funcdef.maior_de_50(pessoas)
    
    return jsonify({"status": 200 ,"dados" : {"pessoa1" : pessoa1, "pessoa2" : pessoa2, "pessoa3" : pessoa3}})

