from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hoteis(Resource):
    def get(self):
        return {'hoteis': 'Hilton, InterContinental, Hilton'}

api.add_resource(Hoteis, '/hoteis')

app.run(port=5000, debug=True)