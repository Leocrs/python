#POO Herança inherita os métodos da classe pai
#OBS: Usar a classe a partir de uma classe existente que possa herdar atributos da classe herdada.   

#CLiente
#-nome = "Leonardo"
#-sobrenome = "Campos"
#cpf = "123.456.789-10"
# Renda = 1000

#Funcionario
#-nome = "Naty"
#-sobrenome = "Natalia"
#-cpf = "123.456.789-10"
#-matricula = "123456"

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    def nome_completo(self):
        return (f"Seu nome completo é: {self.nome} {self.sobrenome} ")
    
class CLiente(Pessoa): # Cliente herda da classe pessoa os aributos
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.renda = renda
   
class Funcionario(Pessoa): # Funcionario herda da classe pessoa os aributos
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula
  
Cliente1 = CLiente("Leonardo", "Campos", "123.456.789-10", 1000)
Funcionario1 = Funcionario("Naty", "Natalia", "123.456.789-10", "123456")

print(Cliente1.nome_completo())
print(Funcionario1.nome_completo())






        

