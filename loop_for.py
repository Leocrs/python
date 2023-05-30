# loop: for:
# Lopp: é uma estrutura de repetição.
# For: é uma dessas estruturas.

# Python

# for item in interavel:
# //execução do loop

# Utilizamos loop para interar sibre sequencias ou sobre valores iteraveis.

# EX: iteráveis:
# String ->
nome = "Leonardo Campos"
Lista = [1,2,3,4,5,6,7,8]
Range = [1,2,3,4,5,6,7]

# EX: iteráveis:
nome = "Leonardo Campos"
lista = [1,3,5,7,9]
numero = range(1,10) # temos que transformar em uma lista

# Ex: Iterando em uma String
for letra in nome:
    print(letra)

#Ex: Iterando sobrem uma Lista
for numeros in lista:
    print(numero)

#Ex: Iterando sobrem um range
for numero in range(1,10+1):
    print(numero)
    
for letra, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[1])
    
    nome = "Leonardo"
lista = [1,3,5,7,9]
numero = range(1,10) # temos que transformar em uma lista


#######################################################################

quantidade = int(input("Quantas vezez esse loop deve rodar?"))
for numero in range(1,quantidade):
    soma = 0
for numero in range(1, quantidade+1):
    numero = int(input(f"Informe {numero}/{quantidade} valor:"))
    soma = soma + numero
print(f"A soma é {soma}")
 # print(f'Imprimindo quantidades {numero+1}') 
 
########################################################################

nome = "Leonardo"
for letra in nome:
    print(letra, end="")



