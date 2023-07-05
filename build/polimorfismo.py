# POO Polimorphismo - Atributos e métodos disponiveis para determinar tipo de dados o variaveis
# podem ter diferentes tipos de atributos e métodos   


class Animal(object):
    def __init__(self, nome):
        self.__nome = nome
        
    def falar(self,):
        raise NotImplementedError("Método não implementado, apenas para herança de classe FILHA")
    
    def comer (self,):
        print(f'{self.__nome} está comendo')
        
           
        
    