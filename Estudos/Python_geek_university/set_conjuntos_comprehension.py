# conjunto comprehension é uma forma de criar conjuntos.
listas = [1, 2, 3, 4, 5]
conjunto = {1,2,3,4,5}

# exemplo 1
numero = {numero for numero in range(1, 7)}
print(numero)

#exemplo 2
numero = [ x ** 2 for x in range(1, 10)]
print(numero)

# Exemplo 3 como tranforma um conjunto em um dicionario com chave e valor
dicionario = {x: x ** 2 for x in range(1, 10)}
print(dicionario)

# Exemplo 4
letras = {letras for letras in "Leonardo Campos"} 
print(letras)


