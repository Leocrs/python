# WEB Arquivos estaticos

from flask import Flask

app4 = Flask(__name__, static_folder='public')

app4.route('/admin')
def admin():
    return '<h1>Admin</h1>'



if __name__ == "__main__":
    app4.run(debug=True)

