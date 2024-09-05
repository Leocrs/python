from flask import Flask

app2 = Flask(__name__)

@app2.route('/')
def index():
    return "index"

def teste():
    return "<p> testando 1 </p>"

def teste2():
    return "<h1> testando 2 </h1>"


app2.add_url_rule('/teste', 'teste', teste)
app2.add_url_rule('/teste-2', 'teste2', teste2)


if __name__ == '__main__':
    app2.run(debug=True, port=3000) # debug=True para mostrar erros de test de forma visível e automatica