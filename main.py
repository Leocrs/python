# Framework Flask -> é uma ferramenta de desenvolvimento web sites

from flask import Flask, render_template

app = Flask(__name__)

# Criar a nossa 1ª pagina = 1ª rota
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Roda o nosso app
app.run()




