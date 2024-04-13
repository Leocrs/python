# POO Polimorphismo - Atributos e métodos disponiveis para determinar tipo de dados o variaveis
# podem ter diferentes tipos de atributos e métodos   


class Animal(object):
    def __init__(self, nome):
        self.__nome = nome
        
    def falar(self):
        raise NotImplementedError("Método não implementado, apenas para herança de classe FILHA")
    def comer (self):
        print(f'{self.__nome} está comendo')
        
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
    def falar(self):
        print(f'{self.__nome} está falando WAuuu WAuuu')
        
class Gato(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome)
        self.especie = especie
    def falar(self):
        print(f'{self.__nome} está falando Meow')
        
class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def falar(self):
        print(f'{self.__nome} está falando')  
        
#Teste:

felix = Gato('felix', 'gato')
felix.comer()
felix.falar()

pluto = Cachorro('pluto', 'cachorro')
pluto.comer()
pluto.falar()

mickey = Rato('mickey')
mickey.comer()
mickey.falar()