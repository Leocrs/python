# laços_encadeados

for cont_externo in range(1, 6):
    print(f' \nRodada  {cont_externo}') # \n quebra de linha \t tabulac{cont_externo})
    for cont_interno in range(5, 0, -1):
         print(f'valor  {cont_interno}) ') # \n quebra de linha \t tabulac{cont_externo})
print('Fim do laço!')

import random # Importando biblioteca random
num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
print(num) # 0 1 2 3 4 5 6 7 8 9

for A in range(0, 10): # 0 1 2 3 4 5 6 7 8 9
    num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
    print(num) # 0 1 2 3 4 5 6 7 8 9

#############################################################

# modulos

import math # Importando biblioteca math
num = math.sqrt(81) # raiz quadrada
print(num) # exibindo o resultado

# Laço for

for num in range(1, 11):
     print(num)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 0 1 2 3 4 5 6 7 8 9
for num in lista: # 1 2 3 4 5 6 7 8 9
     print(num) # 1 2 3 4 5 6 7 8 9

for num in range(0, 10): # 0 1 2 3 4 5 6 7 8 9
     print(num) # 0 1 2 3 4 5 6 7 8 9

for num in range(0, 10, 2): # 0 2 4 6 8
     print(num) # 0 2 4 6 8

nome = input("Digite seu nome: ") # 0 1 2 3 4 5 6 7 8 9
for x in range(10): # 0 1 2 3 4 5 6 7 8 9
     print(f'{x+1} {nome}')

pedras = ('Rubi', 'Esmeralda', 'Safira', 'Diamante') # 0 1 2 3
for pedra in pedras: # 0 1 2 3
     if pedra == 'Diamante': # Se pedra for Diamante
         continue # Ignora o valor
     print(pedra) # 0 1 2 3


# Laços de repetição (for, while)

num = 1
while num <= 10: # 10 vezes
     print(num) # 1 2 3 4 5 6 7 8 9 10
     num += 1 # 2 3 4 5 6 7 8 9 10 11
     print("Laço encerrado!")


nome = None
while True:
     print("Digite seu nome, ou X para sair:") # X para sair
     nome = input() # Entrada de dados
     if nome == 'x' or nome == 'X': # Se o nome for X ou x para sair
         break # Encerra o loop
print ("Até logo!")