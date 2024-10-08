# dunder Name é uma convenção de nomenclatura para métodos, atributos e variáveis
class Pessoa:
    def __init__(self, nome): # __init__ é o construtor
        self.nome = nome # atributo de instância
        
###################################################################################
        
# dunder Main é um método que é chamado quando a classe é instanciada
    def __str__(self): # __str__ é o método
        return f'{self.nome}'  # __str__ é o método
        
 ###################################################################################   
              
print(__name__) # __name__ é o nome da classe

####################################################################################

