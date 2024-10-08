# Conhecendo Pickle  


import pickle

class Aninal:
    def __init__(self, nome):
        self.nome = nome
    def comer(self, comida):
        print(f'{self.nome} está comendo {comida}')
        
class Gato(Aninal):
    def __init__(self, nome):
        super().__init__(nome)
    def mia(self):
        print('mia mia')
        
    def comer(self, comida):
        print(f'{self.nome} está comendo {comida}')
        
class Cachorro(Aninal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def comer(self, comida):
        print(f'{self.nome} está comendo {comida}')
        
felix = Gato ("Felix")
pluto = Cachorro ("Pluto")
with open('felix.pkl', 'wb') as file:
    pickle.dump(felix, file)
with open('pluto.pkl', 'wb') as file:
    pickle.dump(pluto, file)
    
# Fazer a leitura de um arquivo Pickle

with open('felix.pkl', 'rb') as file:
    felix = pickle.load(file)
with open('pluto.pkl', 'rb') as file:
    pluto = pickle.load(file)
    print(felix)
    print(pluto)

    