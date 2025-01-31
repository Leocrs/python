# tuplas

tupla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Criando tupla, e a tupla e imutavel
print(tupla)
tupla = tuple(tupla) # Transformando em tupla
print(tupla)

#############################################################

# Matematica

# funçoes built-in

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = sum(valores)
print(soma)
print(max(valores)) # Retorna o maior valor da lista
print(min(valores)) # Retorna o menor valor da lista
print(pow(2, 3)) # Retorna o valor de 2 elevado a 3
print(round(sum(valores)/len(valores))) # Retorna a media da lista


import math

x = 8
y = 100

raiz_x = math.sqrt(x)
raiz_y = math.sqrt(y)

print(raiz_x)
print(raiz_y)
print(math.pi) # Retorna o valor de pi
print(math.floor(raiz_y)) # Arredonda para baixo
print(round(raiz_y)) # Arredonda para cima
