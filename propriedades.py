#POO Propriedades properties de uma classe

class Conta:
    contador =0
    
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1
        
@property
def numero(self):
    return self.__numero
@property
def saldo(self):
    return self.__saldo
@property
def titular(self):
    return self.__titular
@property
def limite(self):
    return self.__limite

def extrato(self):
    return f'Saldo de {self.saldo} do clinte {self.titular}'  
def depositar(self, valor):
    self.__saldo += valor     
def sacar(self, valor):
    self.__saldo -= valor    
def transfer(self, valor, destino):
    self.__saldo -= valor
    destino.__saldo += valor 
    
@property
def valor_total(self):
    return self.__valor_total + self.__limite
    
@limite.setter
def limite(self, novo_valor):
    self.__limite = novo_valor

conta1 = Conta('Leonardo', 1000, 500)
conta2 = Conta('Maria', 2000, 700)

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')
print(conta1.limite)

    
