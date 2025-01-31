# POO O método super() é referente a classe pai, super classe

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    def faz_som(self, som):
        print(f'faz {som}!!!')
        
class Gato(Animal):
    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie) # Essa forma chamando por nome tbm funciona porém não é o ideal
        super().__init__(nome, especie) # super().__init__(nome, especie) Essa é a forma correta por convencao 
        self.raca = raca


felix = Gato('Felix', 'Felino', 'Siberiano')
felix.faz_som('miau')
