"""
Dictionary Comprehension é uma forma de criar dicionários.

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
dicionario = {'a': 1, 'b': 2, 'c': 3}
conjunto = {1, 2, 3, 4, 5} 


dicionario = {'a': 1, 'b': 2, 'c': 3}
Sintaxe:
dicionario = {chave: valor for valor, chave in iteravel} 

#Exemplo 1

numeros = {'a': 1, 'b': 2, 'c': 3}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

#Exemplo 2

numero =[1, 2, 3, 4, 5]

quadrado = {valor: valor ** 2 for valor in numero}
print(quadrado)

#exemplo 3

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura_tudo = {chaves[indice]: valores[indice] for indice in range(0,len(chaves))}
print(mistura_tudo)
"""
#exemplo 4

numero = [1, 2, 3, 4, 5]
resposta = {numero:("pares" if numero % 2 == 0 else "impares") for numero in numero}
print(resposta)