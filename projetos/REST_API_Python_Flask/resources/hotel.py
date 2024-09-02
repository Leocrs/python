from flask_restful import Resource



hoteis = [
    {'hotel_id': 'alpha', 'nome': 'Alpha Hotel', 'estrelas': 4.3,'diaria': 420.34, 'cidade': 'Rio de Janeiro'},
    {'hotel_id': 'bravo', 'nome': 'bravo Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'São Paulo'},
    {'hotel_id': 'charle', 'nome': 'charle Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'Belo Horizonte'},
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}  # Return the actual list of hotels