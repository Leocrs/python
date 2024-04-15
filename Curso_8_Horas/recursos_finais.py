var1 = 10
var2 = 20

# Trocar valores entre duas variáveis
var2, var1 = var1, var2 # Trocar valores entre duas variáveis
print('f Essa é a direção', var1, var2)

# Operadores Condicionais Ternário
menor = var1 if var1 < var2 else var2 # opção ternária 
print(f' Esse é o menor valor {menor}')
print (f' Esse é o menor valor {(var2, var1) [var1 < var2]}') # opção ternária com tupla UM POUCO MAIS COMPLEXA.

# Generators em Python - Geradores são um acesso mais rapido a dados. 

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = (item ** 2 for item in valores)
print(quadrados)
for item in quadrados:
    print(item) 

#Enumerate - Retorna um objeto enumerado

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = (item ** 2 for item in valores)
print(quadrados)
for item in enumerate(quadrados):
    print(f' Para os indices: {item[0]} - O valor de quadrado é: {item[1]}') # Retorna um objeto enumerado (item)

    