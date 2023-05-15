"""   
Funções com retorno (return)

numeros = [1, 2, 3, 4, 5]
retorno_pop = numeros.pop() # remove o último elemento
print(f"O retorno da função pop é: {retorno_pop}") # O retorno da função pop é: 5
print(numeros) #   [1, 2, 3, 4]


#Modo de função simplificado
def quadrado_de_sete(): # criando uma função
    print(7*7) # 49
quadrado_de_sete() # 49

def quadrado_de_sete(numero): # criando uma função
    return numero ** 2 # retornando o quadrado do número

print(quadrado_de_sete(7)) # 49
def raiz_quadrada_sete():
    return 7*7
#retorna = raiz_quadrada_sete()
#print(f" Retorna o resultado da raiz quadrada de 7 que é: {retorna}")
# Não é necessario criar uma variavel para receber o retorno da função, podemos passar a função o print
print(f"Retorna o resultado da raiz quadrada de 7 que é: {raiz_quadrada_sete()}")

def diz_oi():
    return "Oi"
alguem = "Leonardo"
print(diz_oi())
print(alguem)

OBs: a palabra return retorna o resultado da função

def diz_oi():    # Ela finaliza apos a execução da função
    return "Oi!"
print("Estou sendo executado apos o retorno...")

def nova_funcao():
    variavel =False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return "Falsa"
print(nova_funcao())


def outra_funcao(): #Exemplo 3 de função 
    return 2, 3, 4, 5
num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
print(type(outra_funcao()))


#Vamos criar uma função para jogar moedas
from random import random
def jogar_moedas(): # criando uma função
    valor = random() # retorna um valor entre 0 e 1
    
    if valor > 0.5: # se o valor for maior que 0.5
        return "Deu Cara" # retorna "cara"
    return "Deu Coroa" # retorna "coroa"
print(jogar_moedas()) # retorna ou cara ou coroa de forma randomica "random"
"""




# Gerar numeros randomicos para Papel entre 1 e 3, Pedra entre 4 e 6, Tesoura entre 7 e 9
from random import randint
def jogo_papel_pedra_tesoura(): 
    valor = randint(1, 9)
    if valor <= 3:
        print("Papel")
    elif valor <= 6: 
        print("Pedra")
    else:
        print("Tesoura")
        
jogo_papel_pedra_tesoura()
    
    