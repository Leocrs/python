# Json e Pickle

# json - JavaScript Object Notation
# Pickle - Python Object Notation

# API - Application Programming Interface são meio de comunicação por empresas e terceiros EX: Youtube, Facebook, Instagram

import jsonpickle

class Gato:
    def __init__(self, nome):
        self.nome = nome
    def mia(self):
        print('mia mia')
    def comer(self, comida):
        print(f'{self.nome} está comendo {comida}')
        
felix = Gato("Felix")
ret = jsonpickle.encode(felix)
print(ret)

with open('felix.pkl', 'w') as file:
    ret = jsonpickle.decode(file)
    
    