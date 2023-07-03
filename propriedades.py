#POO Propriedades properties de uma classe

class Conta:
    contador =0
    
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1
    
    def extrato(self):
        return f'Saldo de {self.saldo} do clinte {self.titular}'
    
