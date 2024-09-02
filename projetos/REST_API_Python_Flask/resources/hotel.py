from flask import Flask  
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
        return {'hoteis': hoteis}  

class Hotel(Resource):  
    parser = reqparse.RequestParser()  
    parser.add_argument('nome', required=True, help="Nome do hotel é obrigatório.")  
    parser.add_argument('estrelas', type=float, required=True, help="Número de estrelas é obrigatório.")  
    parser.add_argument('diaria', type=float, required=True, help="Preço da diária é obrigatório.")  
    parser.add_argument('cidade', required=True, help="Cidade do hotel é obrigatória.")  

    def get(self, hotel_id):  
        for hotel in hoteis:  
            if hotel['hotel_id'] == hotel_id:  
                return hotel  
        return {'error': 'Hotel não encontrado'}, 404  

    def post(self, hotel_id):  
        if any(hotel['hotel_id'] == hotel_id for hotel in hoteis):  
            return {'error': 'Hotel já existe.'}, 400  

        args = self.parser.parse_args()  
        novo_hotel = {  
            'hotel_id': hotel_id,  
            'nome': args['nome'],  
            'estrelas': args['estrelas'],  
            'diaria': args['diaria'],  
            'cidade': args['cidade']  
        }  
        hoteis.append(novo_hotel)  
        return novo_hotel, 201  

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
                return hoteis[index], 200  
        return {'error': 'Hotel não encontrado'}, 404  

    def delete(self, hotel_id):  
        global hoteis  
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]  
        return {'message': 'Hotel deletado com sucesso.'}, 200  

# Registrando os recursos  
api.add_resource(Hoteis, '/hoteis')  
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')  

if __name__ == '__main__':  
    app.run(debug=True)

    # Para testar, utilize um cliente HTTP como curl ou Postman:
    # GET http://localhost:5000/hoteis
    # POST http://localhost:5000/hoteis/bravo -d 'nome=Novo Hotel&estrelas=4.5&diaria=350&cidade=Cidade do Novo Hotel'
    # GET http://localhost:5000/hoteis/novo_hotel
    # PUT http://localhost:5000/hoteis/novo_hotel -d 'nome=Novo Hotel Atualizado&estrelas=4.6&diaria=360&cidade=Cidade Atualizada'
    # GET http://localhost:5000/hoteis/novo_hotel
    # DELETE http://localhost:5000/hoteis/novo