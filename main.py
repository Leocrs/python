# Framework Flask -> é uma ferramenta de desenvolvimento web sites

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)

# Criar a nossa 1ª pagina = 1ª rota
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Roda o nosso app
app.run(debug=True)
SocketIO=SocketIO(app, cors_allowed_origins="*")



# websocket 
# pip install python-websocket flask-socketio simple-websocket
# Fiz essa instalação via comando


