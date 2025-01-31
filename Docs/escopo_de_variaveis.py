# Escopo de variavel
# Dois casos:
# 1ª Variaveis globais, São reconhecidas, ou sej, seu escopo compreende , todo o programa.
# 2ª Variaveis local, São reconhecidas apenas no bloco onde foi declarada, ou seja, seu escopo compreende a limitação
# do bloco onde foi declarada.
# Para declarar variaveis em Python fazemos:

Nome_da_variavel = "valor_da_variavel"
numero = 42
print ("Nome_da_variavel")
print ("numero")

# Python é uma linguagem de tipagem dinamica, Isso significa que ao declaramos uma variavel e colocarmos o tipo de dado
# ela, identifica o tipo de atribuição.

# EX: em C
# int numero = 42

# Ex em Java
# int numero = 42

# EX de String global
# Python ela mesmo já idenfica e exibo "int" de numero inteiro.
numero = 42
print(type(numero))
numero = "Leonardo"
print(type(numero))

# EX String local
numero = 42
novo = 0
if numero > 10:
    novo= numero + 10 # A variavel novo está declarada locamente no bloco if então é local.
    print(novo)