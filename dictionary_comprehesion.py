 
# dictionary_comprehesion é uma forma de criar um dicionário.

# Se quisermos criar uma lista
lista = [1,2,3,4,5]

# tupla
tupla = (1,2,3,4,5)

# conjunto set
conjunto = {1,2,3,4,5}

# dicionario
dicionario = {'a':1, 'b':2, 'c':3}

# Sintaxe

# {chave:valor for valor in iteravel}


numero = {'a':1, 'b':2, 'c':3,'d':4, 'e':5, 'f':6}

quadrado = {chave:valor**2 for chave, valor in numero.items()}
print(quadrado)