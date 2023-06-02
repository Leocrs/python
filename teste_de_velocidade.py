

# Teste de velocidade com expressões geradoras 

def numeros():
    for numero in range(1,11):
        yield numero
gerador1 = numeros()
print(next(gerador1)) # 1 é o primeiro elemento do gerador e vai até o numero 10 que é o limete que coloquei no range

#######################################################################################################################

gerador2 = (numero for numero in range(1, 11))
print(next(gerador2)) # gerador2 é um gerador

#######################################################################################################################

import time # importa a biblioteca time
#Generador com expressões geradoras (generator expressions)
gerador_inicio = time.time() # tempo decorrido
print(sum(numero for numero in range(1, 11))) # soma dos numeros
gerador_tempo = time.time() - gerador_inicio # tempo decorrido
print(gerador_tempo) # tempo decorrido

#######################################################################################################################

#list comprehension

lista_iniicio = time.time()
print(sum([numero for numero in range(1000000000)])) # 100 milhões de numeros
lista_tempo = time.time() - lista_iniicio
print(lista_tempo)