from flask import Flask, make_response, jsonify, request
# Importa o Flask e o make_response

from bd import Carros

app = Flask(__name__) 
app.config['json_sort_keys'] = False # Evita que os dicionários sejam ordenados

@app.route('/carros', methods=["GET"]) 
def get_carros():
    return make_response(jsonify(Carros)) 

@app.route('/carros', methods=["POST"])
def create_carros():
    try:
        carro = request.json
        Carros.append(carro)
        return carro
    except Exception as e:
        return jsonify({"error": str(e)}), 400

app.run() 

