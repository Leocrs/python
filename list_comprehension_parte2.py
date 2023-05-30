 
# lista_comprehension_parte2
# Nósa podemos adicionar estruturas logicas, as nossas lists comprehension

######################################################################

#Exemplo 1 - List Comprehension

numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

######################################################################

#Refatorar  Qualquer numero par de 2 é 0, e 0 em Python é False, not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer numero impar de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

######################################################################

# Exemplo 2 - List Comprehension

resposta = [numero *2 if numero % 2 == 0 else numero /2 for numero in numeros]
print(resposta)

#######################################################################