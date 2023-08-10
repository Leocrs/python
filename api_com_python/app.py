# API é um lugar de comunicação recursos ou funcionalidades.

# Objetivo -  Criar uma API de disponibilização a consulta, criação

# URL - localhost 

# Endpoint - localhost/livros (GET) - 
# localhost/livros/id (GET) -
# # # # localhost/id (PUT) - 
# localhost/livros/id (DELETE)

# Quais recursos podem ser acessados
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [{'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J. R. R. Tolkien'},
          {'id': 2, 'titulo': 'O Hobbit', 'autor': 'J. R. R. Tolkien'},
          {'id': 3, 'titulo': 'Harry Potter e a Pedra Filosofal', 'autor': 'J. K. Rowling'}]

# Consulta(todos)
app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consulta(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({'message': 'Livro não encontrado'})
                 
                   
# Edita(id)
@app.route('/livros/<int:id>', methods=['PUT']) 
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro['id'] == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'message': 'Livro não encontrado'})

# Criar
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


# Exclui(id)
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro_por_id(id):
    for indice, livro in enumerate(livros):
        if livro['id'] == id:
            livros.pop(indice)
            return jsonify(livros)
    return jsonify({'message': 'Livro não encontrado'})


    

    
app.run(port=5000,host='localhost', debug=True)



