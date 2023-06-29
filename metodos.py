#POO Métodos
# Métodos (função) representam um conjunto de acções que podem ser realizadas em um objeto. Ou seja um método é um conjunto de acções que podem ser executadas em um objeto
# Em python dividimos os métodos em dois grupos: métodos de classe e métodos de instância.
# Metodos de instância: 
# O método __init__ é executado sempre que um objeto é instanciado. ou seja a partir da classe.

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
        
class ContaCorrente:
    contador = 4999
    
    def __init__(self, munero, limite, saldo):
        self.__saldo = saldo
        self.__limite = limite
        self.__munero = ContaCorrente.contador + 1
        ContaCorrente.contador = self.__munero
        
class Produto:
    contador = 0
    
    def __init__(self, nome, descricao, preco):
        self.__id = Produto.contador +1
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao
        Produto.contador = self.__id
        
class Usurio:
    def __init__(self, nome, senha, email):
        self.__nome = nome
        self.__senha = senha   
        self.__email = email
        
  
        

        
        
        