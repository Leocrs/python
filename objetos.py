# POO Objetos são instanciados por meio da classe


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.ligada = False
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        
        
class ContaCorrente:
    contador = 4999
    def __init__(self, saldo, limite):
        self.numero = ContaCorrente.contador +1
        self.saldo = saldo
        self.limite = limite
          
        
        
class Usuario:
    def __init__(self, nome, senha, email):
        self.email = email
        self.nome = nome
        self.senha = senha
        
        