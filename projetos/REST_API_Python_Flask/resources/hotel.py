from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

hoteis = [
    {'hotel_id': 'alpha', 'nome': 'Alpha Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'Rio de Janeiro'},
    {'hotel_id': 'bravo', 'nome': 'Bravo Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'São Paulo'},
    {'hotel_id': 'charle', 'nome': 'Charle Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'Belo Horizonte'}
]

class Hoteis(Resource):
    def get(self):
        return jsonify({'hoteis': hoteis, 'message': 'Lista de hoteis retornada com sucesso', 'status_code': 200})

class Hotel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome', required=True, help="Nome do hotel é obrigatório.")
    parser.add_argument('estrelas', type=float, required=True, help="Número de estrelas é obrigatório.")
    parser.add_argument('diaria', type=float, required=True, help="Preço da diária é obrigatório.")
    parser.add_argument('cidade', required=True, help="Cidade do hotel é obrigatória.")

    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return jsonify({'hotel': hotel, 'message': 'Hotel encontrado com sucesso', 'status_code': 200})
        return jsonify({'error': 'Hotel não encontrado', 'message': 'Hotel não encontrado', 'status_code': 404})

    def post(self, hotel_id):
        if any(hotel['hotel_id'] == hotel_id for hotel in hoteis):
            return jsonify({'error': 'Hotel já existe.', 'message': 'Hotel já existe', 'status_code': 400})

        args = self.parser.parse_args()
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': args['nome'],
            'estrelas': args['estrelas'],
            'diaria': args['diaria'],
            'cidade': args['cidade']
        }
        hoteis.append(novo_hotel)
        return jsonify({'hotel': novo_hotel, 'message': 'Hotel criado com sucesso', 'status_code': 200})

    def put(self, hotel_id):
        args = self.parser.parse_args()
        for index, hotel in enumerate(hoteis):
            if hotel['hotel_id'] == hotel_id:
                hoteis[index] = {
                    'hotel_id': hotel_id,
                    'nome': args['nome'],
                    'estrelas': args['estrelas'],
                    'diaria': args['diaria'],
                    'cidade': args['cidade']
                }
                return jsonify({'hotel': hoteis[index], 'message': 'Hotel atualizado com sucesso', 'status_code': 200})
        return jsonify({'error': 'Hotel não encontrado', 'message': 'Hotel não encontrado', 'status_code': 404})

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return jsonify({'message': 'Hotel deletado com sucesso', 'status_code': 200})

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True)

    # https://localhost:5000/hoteis
    # https://localhost:5000/hoteis/bravo
    # https://localhost:5000/hoteis/charle
    # https://localhost:5000/hoteis/alpha
    # https://localhost:5000/hoteis/bravo/estrelas
    # https://localhost:5000/hoteis/charle/diaria
    # https://localhost:5000/hoteis/alpha/cidade
    # https://localhost:5000/hoteis/bravo/estrelas/diaria
    # https://localhost:5000/hoteis/charle/diaria/cidade
    # https://localhost:5000/hoteis/alpha/cidade/estrelas/diaria
    # https://localhost:5000/hoteis/novohotel
    # https://localhost:5000/hoteis/novohotel/estrelas
    # https://localhost:5000/hoteis/novohotel/diaria
    # https://localhost:5000/hoteis/novohotel/cidade    