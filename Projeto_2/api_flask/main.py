from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__) 
app.config['json_sort_keys'] = False 

@app.route('/carros', methods=["GET"]) 
def get_carros():
    return make_response(
        jsonify(
            mensagem = 'Lista de carros',
            dados = Carros                 
      ) 
  )

@app.route('/carros', methods=["POST"])
def create_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            mensagem = 'Carro criado com sucesso!',
        )
    )    
    

app.run() 

