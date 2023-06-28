

# Atributos é uma característica de uma classe.

# Em Python, os atributos são chamados de propriedades. e dividos em 3 grupos


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
        
        
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
        
# Esse é um atributo privado por convenção, a linguagem não impede que você acesse atributos privados ou publicos, é apenas uma sinalização. 


# O que significam os atributos de instancia?
# Significa que criamos  instancias de uma classe e todas as instancias terão o mesmo atributo.

# user1 =Acesso('leo@gmail.com', '123')
# user2 =Acesso('eu@gmail.com', '456')
# user1.mostra_email()
# user2.mostra_email()


# Atributos de Classe

# Atributos de classe são item declarados, geralmente já inicializamos um valor inicial para aquele atributo.

class Produto:

    # atributo de classe
    imposto = 1.05 # valor do imposto
    
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = (preco * Produto.imposto)
        

P1 = Produto('Xbox','GamePass',2500)
P2 = Produto('Playstation','Psn',4500)
        
print(P1.preco) # Acesso de forma não muito usual
print(P2.preco)
   
print(Produto.imposto) # Acesso de atributo de classe
# Não precisamos fazer um atributo de classe para cada instância de uma classe

P2.peso = '10kg'



