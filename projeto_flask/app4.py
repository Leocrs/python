# WEB Arquivos estaticos

from flask import Flask, redirect, url_for

app = Flask(__name__)

app.route('/admin')
def admin():
    return '<h1>Admin</h1>'



if __name__ == "__main__":
    app.run(debug=True)

