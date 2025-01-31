#POO Métodos
# Métodos (função) representam um conjunto de acções que podem ser realizadas em um objeto. Ou seja um método é um conjunto de acções que podem ser executadas em um objeto
# Em python dividimos os métodos em dois grupos: métodos de classe e métodos de instância.
# Metodos de instância: 
# O método __init__ é executado sempre que um objeto é instanciado. ou seja a partir da classe.
# Todo elemento em Python que inicia e finaliza com um duplo '__' é chamado de underline dunder (double Underline).

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
        
    def desconto(self, percentual):
        return self.__preco * (100 - percentual/100)
        
class Usurio:
    
    contador = 0
    @classmethod
    def nome_completo(cls, nome, sobrenome):
        print(f"Seu nome completo é: {nome} {sobrenome}")
    def __init__(self, nome, senha, email):
        self.__nome = nome
        self.__senha = senha   
        self.__email = email
        
video_game = Produto('Super Mario', 'Super Mario', 50)
print(video_game.desconto(50))    

 # Métodos de Classe são conhecidos em Python como método estatico em outras linguagens. 
 
user = Usurio('Leonardo Campos', '123', 'leonnardo_campos@gmail.com')
user.nome_completo('Leonardo', 'Campos')
 
 
        

        
        
        