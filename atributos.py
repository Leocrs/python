

# Atributos é uma característica de uma classe.

# Em Python, os atributos são chamados de propriedades. e dividos em 3 grupos


# Atributos de instância: exemplos:


# Atributos de classe: Exemplos: 
# Por convenção , os atributos de classe são chamados publicos. Ou seja pode ser acessado por todo o projeto, Agora caso queria que o atributo fosse privado, 
# deveria ser declarado como privado por duplo underscore "__" no ínicio do atributo. Isso tbm é conhecido como Mangling.


class Lampada:
    def __init__(self, cor, voltagem):
        self.cor = cor
        self.ligada = False
        self.voltagem = voltagem 
        
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
        


# Atributos de dinamicos: Exemplos:

