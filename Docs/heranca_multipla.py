# POO Herança Multipla - Python Orientado a Objetos 
# Herança multipla é a porção de uma classe que pode ser herdada por outras classes.

# Exemplo Multiderificada Direto

class Usuario: # classe pai
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
class Cliente(Usuario): # classe filha
    def __init__(self, nome, email, senha, cpf):
        super().__init__(nome, email, senha)
        self.cpf = cpf
        
class Funcionario(Usuario): # classe filha
    def __init__(self, nome, email, senha, matricula):
        super().__init__(nome, email, senha)
        self.matricula = matricula
        
        