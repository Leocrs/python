from flask import Flask, make_response # Importa o Flask e o make_response
from bd import Carros # Importa o bd carros


app = Flask(__name__) # Cria a aplicação Flask


@app.route('/carros', methods=["GET"]) # Cria uma rota para retornar os carros
def get_carros():
    return make_response(Carros) # Retorna os carros no formato json

app.run() # Roda a aplicação Flask


