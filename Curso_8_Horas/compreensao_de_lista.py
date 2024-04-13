
numeros = [1, 4, 7, 9, 12, 21]

quadrados = [num**2 for num in numeros]

print(quadrados)

# Criar uma lista de numeros pares

pares = [num for num in range (120) if num % 2 == 0]

print(pares)

#Criar uma frase com os valores de uma lista

frase = " A lógica é apenas uma das ferramentas da programação."

vogais = [a, e, i, o, u, á, é, í, ó, ü]

lista_vogais = [letra for letra in frase if letra in vogais]

print(f' A frase se possuiu as vogais {lista_vogais} vogais:')


