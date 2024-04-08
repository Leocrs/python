# ##############################################################
# # Variáveis e tipos de dados
# media = 0
# n1 = n2 =n3 = n4 = 0.0
# nome, idade = 'Leonardo', 47
# estado = True

# print (nome, idade) # strings
# print(type(media)) # numeros
# print(type(n1)) # numeros int
# print(type(n2)) # numeros reais
# print(type(1+2j)) # numeros complexos

# ##############################################################

# # Função isinstance verifica se o objeto e do tipo especificado
# print(isinstance(1, int)) # True
# print(isinstance(1.0, float)) # True
# print(isinstance(1+2j, complex)) # True
# print(isinstance(1, float)) # False

# ###############################################################
# # Operadores Aritméticos (+, -, *, /, //, %, **)

# # Soma +
# print(1+2)

# # Subtração -
# print(1-2)

# # Multiplicação *
# print(1*2)

# # Divisão /
# print(1/2)

# # Divisão Inteira //
# print(1//2)

# # Resto da divisão %
# print(1%2)

# # Potência **
# print(1**2)

# ###############################################################

# # Operadores de Comparação (==)

# # Igual ==
# print(1==1) # True
# print(1==2) # False

# # Diferente !=
# print(1!=1) # False
# print(1!=2) # True

# # Maior >
# print(1>1) # False
# print(1>2) # False

# # Menor <
# print(1<1) # False
# print(1<2) # True

# # Maior ou Igual >=
# print(1>=1) # True
# print(1>=2) # False

# # Menor ou Igual <=
# print(1<=1) # True
# print(1<=2) # True

# ###############################################################
# # Operadores de atribuição (=, +=, -=, *=, /=, %=, **=, //=)

# x = y = z = False
# n1 = n2 = 0

# print('Digite um numero:')
# n1 = int(input())
# n2 = int(input('Digite outro numero:'))

# x = n1 == n2
# print('São iguais?', x, '\n')

# z = n1 > n2
# print(n1, ' É maior que ', n2, '?', z, '\n')

# y = n1 != n2
# print('São diferentes?', y, '\n')
# ###############################################################

# # Operadores logicos (and, or, not)

# x = True
# y = False

# print(x and y) # False
# print(x or y) # True
# print(not x) # False

###############################################################
# condicional if, elif, else

# # Programinha de Media de nota de alunos
# n1 = n2 = 0.0
# media = 0.0
# n1 = float(input('Digite um numero:'))
# n2 = float(input('Digite outro numero:'))

# media = (n1 + n2) / 2
# print(media)
# if media >= 7:
#     print('Aprovado')
# elif media >= 5:
#     print('Recuperacao')
# else:
#     print('Reprovado')
#############################################################

# Laços de repetição (for, while)

# num = 1
# while num <= 10: # 10 vezes
#     print(num) # 1 2 3 4 5 6 7 8 9 10
#     num += 1 # 2 3 4 5 6 7 8 9 10 11
#     print("Laço encerrado!")

#############################################################

# nome = None
# while True:
#     print("Digite seu nome, ou X para sair:") # X para sair
#     nome = input() # Entrada de dados
#     if nome == 'x' or nome == 'X': # Se o nome for X ou x para sair
#         break # Encerra o loop
# print ("Até logo!")

#############################################################

# Laço for

# for num in range(1, 11):
#     print(num)


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 0 1 2 3 4 5 6 7 8 9
# for num in lista: # 1 2 3 4 5 6 7 8 9
#     print(num) # 1 2 3 4 5 6 7 8 9

# for num in range(0, 10): # 0 1 2 3 4 5 6 7 8 9
#     print(num) # 0 1 2 3 4 5 6 7 8 9

# for num in range(0, 10, 2): # 0 2 4 6 8
#     print(num) # 0 2 4 6 8
     
# nome = input("Digite seu nome: ") # 0 1 2 3 4 5 6 7 8 9
# for x in range(10): # 0 1 2 3 4 5 6 7 8 9
#     print(f'{x+1} {nome}')

# pedras = ('Rubi', 'Esmeralda', 'Safira', 'Diamante') # 0 1 2 3
# for pedra in pedras: # 0 1 2 3
#     if pedra == 'Diamante': # Se pedra for Diamante
#         continue # Ignora o valor
#     print(pedra) # 0 1 2 3

#############################################################

# laços_encadeados 

# for cont_externo in range(1, 6):
#     print(f' \nRodada  {cont_externo}') # \n quebra de linha \t tabulac{cont_externo})
#     for cont_interno in range(5, 0, -1):
#         print(f'valor  {cont_interno}) ') # \n quebra de linha \t tabulac{cont_externo})
# print('Fim do laço!')

# import random # Importando biblioteca random
# num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
# print(num) # 0 1 2 3 4 5 6 7 8 9

# for A in range(0, 10): # 0 1 2 3 4 5 6 7 8 9
#     num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
#     print(num) # 0 1 2 3 4 5 6 7 8 9

#############################################################

# modulos 

#import math # Importando biblioteca math
# num = math.sqrt(81) # raiz quadrada
# print(num) # exibindo o resultado

#############################################################

# modo random - modulo aleatório

import random # Importando biblioteca random
num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
print(num) # 0 1 2 3 4 5 6 7 8 9