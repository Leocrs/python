from flask_restful import Resource, reqparse

hoteis = [
    {'hotel_id': 'alpha', 'nome': 'Alpha Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'Rio de Janeiro'},
    {'hotel_id': 'bravo', 'nome': 'Bravo Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'São Paulo'},
    {'hotel_id': 'charle', 'nome': 'Charle Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'Belo Horizonte'}
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'error': 'Hotel não encontrado'}

    def post(self, hotel_id):
        arguments = reqparse.RequestParser().parse_args()
        # Implemente a lógica para criar um novo hotel aqui
        pass

    def put(self, hotel_id):
        arguments = reqparse.RequestParser().parse_args()
        # Implemente a lógica para atualizar um hotel aqui
        pass

    def delete(self, hotel_id):
        # Implemente a lógica para deletar um hotel aqui
        pass