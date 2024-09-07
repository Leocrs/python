from flask import Flask


APP = Flask(__name__)


@APP.route('/')


def index():
    return "Hello, World!"

