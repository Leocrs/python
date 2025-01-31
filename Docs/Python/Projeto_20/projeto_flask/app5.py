# Metodos HTTP

from flask import Flask, redirect, url_for, request

app5 = Flask(__name__, static_folder='public')

@app5.route('/add', methods=['GET', 'POST', 'PUT', 'DELETE'])
def add():
    if request.method == 'POST':
        # Aqui você pode redirecionar para outra rota ou retornar uma mensagem de sucesso
        return "Dados adicionados com sucesso!"
    return "Adicionado"

if __name__ == "__main__":
    app5.run(debug=True)














# GET: Busca dados (exibir, listar)
# POST: Cria dados (incluir, adicionar)
# PUT: Atualiza dados (alterar, alterar)
# DELETE: Remove dados (excluir, remover)
