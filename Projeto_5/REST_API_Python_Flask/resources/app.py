from flask import Flask
from flask_restful import Api
from projetos.REST_API_Python_Flask.resources.hotel import Hoteis, Hotel


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

@app.before_request
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sqlalchemy import banco
    banco.init_app(app)
    app.run(debug=True)
