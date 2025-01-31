# Funçoes de maior grandeza  
# Higher Order Functions -hof 
# O que é Higher Order Function? é uma função que recebe outra função como parametro e retorna outra função como resultado.


def somar (a, b): # a e b são funções de soma
    return a + b

def subtrair (a, b): # a e b são funções de subtração
    return a - b

def multiplicar (a, b): # a e b são funções de multiplicação
    return a * b

def dividir (a, b):  # a e b são funções de divisão
    return a / b

def potencia (a, b): # a e b são funções de potenciação
    return a ** b

def calular (num1, num2, funcao): # num1 e num2 são funções de soma e subtração
    return funcao(num1, num2) # retorna a função passada como parametro

print(calular(4, 3, somar))
print(calular(4, 3, subtrair))
print(calular(4, 3, multiplicar))
print(calular(4, 3, dividir))
print(calular(4, 3, potencia))

########################################################################################

# Nested Functions - nf - funções aninhadas
# Podemos ter funções aninhadas dentro de funções

from random import choice

def cumprimento (pessoa):
    def humor():
        return choice(('E ai', 'Suma daqui', 'Gosto muito de você'))
    return humor() +  pessoa
print(cumprimento(' João'))
print(cumprimento(' Maria'))
















