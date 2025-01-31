from flask_sqlalchemy import SQLAlchemy
from flask import Flask

banco = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'


