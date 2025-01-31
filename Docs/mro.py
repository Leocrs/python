#POO MRO - Method Resolution Order (MRO) é o método de resolução de ordem

class Pessoa: # classe pai
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
class Cliente(Pessoa): # classe filha
    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome
        
class Funcionario(Pessoa): # classe filha
    def __init__(self, nome, email, senha, matricula):
        self.matricula = matricula
        self.email = email
        self.senha = senha
        self.nome = nome
        
class Leonardo(Cliente, Funcionario): # classe filha
    def __init__(self, nome, email, senha, cpf, matricula):
         self.matricula = matricula
         self.cpf = cpf
         self.nome = nome
         self.email = email
         self.senha = senha

Leonardo.mro
Cliente.mro
