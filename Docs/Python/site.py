from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Essa é minha HomePage'

@app.route('/contato')
def contatos():
    return 'Esses são os meus contatos'


app.run()