from flask_restful import Resource, reqparse



hoteis = [
    {'hotel_id': 'alpha', 'nome': 'Alpha Hotel', 'estrelas': 4.3,'diaria': 420.34, 'cidade': 'Rio de Janeiro'},
    {'hotel_id': 'bravo', 'nome': 'bravo Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'São Paulo'},
    {'hotel_id': 'charle', 'nome': 'charle Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'Belo Horizonte'},
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}  # Return the actual list of hotels
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hotel_id:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return {'message': 'Hotel not found'}, 404  # Return a 404 error if the hotel is not found

    def post(self, hotel_id):
        arguments = reqparse.RequestParser().parse_args()
        

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass