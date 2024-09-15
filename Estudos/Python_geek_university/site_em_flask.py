# Framework Flask -> é uma ferramenta de desenvolvimento web sites
# websocket 
# pip install python-websocket flask-socketio simple-websocket
# Fiz essa instalação via comando

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
Socketio=SocketIO(app, cors_allowed_origins="*")

# Funçao para enviar mensagem
@Socketio.on('message')
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)
    
# Criar a nossa 1ª pagina = 1ª rota
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Roda o nosso aplicativo
Socketio.run(app, host= "localhost")






