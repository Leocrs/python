from flask import Flask as Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [{'hotel_id': 'alpha', 'nome': 'Alpha Hotel',
             'estrelas': 4.3, 'diaria':
               420.34, 'diaria_completo': 498.40},]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': 'meus hoteis'}   
api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)

    