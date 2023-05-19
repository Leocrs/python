"""  
list_comprehension_parte1 
lista comprehension é uma forma de criar listas.

sintaxe da list comprehension:

Para entender melhor o que é uma list comprehension, vamos ver como funciona: 
Devemos dividir nosso código em duas partes:
A primeira parte for numero in numeros:
A segunda parte for numero * 10:


#Exemplo
numeros = [1, 2, 3, 4, 5] # cria uma lista

resposta = [numero * 10 for numero in numeros] # cria uma lista
print(resposta) # imprime [10, 20, 30, 40, 50]  

resposta = [numeros / 2 for numeros in numeros]  
print(resposta) # imprime [0.5, 1.0, 1.5, 2.0, 2.5]

def funcao(valor):
    return valor * valor

resposta = [funcao (numeros) for numeros in numeros]
print(resposta)  

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

#loop
for numero in numeros: 
    numero_dobrado = numero *2
    numeros_dobrados.append(numero_dobrado)
print(numeros_dobrados)


#list comprehension
print([numero * 2 for numero in numeros])


nome = ('Leonardo Campos')
print([letra.upper() for letra in nome])

#Exemplo 2 - List Comprehension
amigos = ['Leonardo', 'Maria', 'Pedro']
print([amigo[0].upper() for amigo in amigos])

#Exemplo 3 - List Comprehension
print([numero * 3 for numero in range(1, 11)])

#Exemplo 4 - List Comprehension
# print([bool(valor) for valor in [0, [],'', True, 1, 3.14)]])


#Exemplo 5 - List Comprehension
print([str(numero) for numero in [1, 2, 3, 4, 5]])


"""
lista_precos = [500, 1500, 2000, 100, 25]

#Modo de criar uma lista cogigo tradicional   (exemplo1)
nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco *2)
print(nova_lista_precos)

#Modo de criar uma lista codigo em list comprehension  (exemplo1) 
nova_lista_precos = [preco * 2 for preco in lista_precos]
print(nova_lista_precos)

#Modo de criar uma lista cogigo tradicional   (exemplo2)
imposto = []
for preco in lista_precos:
    if preco >1000:
        imposto.append(preco * 0.5)
print(imposto)

#Modo de criar uma lista codigo em list comprehension  (exemplo2) 
imposto = [preco * 0.5 for preco in lista_precos if preco > 1000]
print(imposto)