

# Teste de velocidade com expressões geradoras 

import time # importa a biblioteca time

#Generador com expressões geradoras (generator expressions)
gen_inicio = time.time() # tempo decorrido
print(sum(numero for numero in range(100))) # soma dos numeros
gen_tempo = time.time() - gen_inicio # tempo decorrido
print(gen_tempo) # tempo decorrido

#######################################################################################################################

#list comprehension

list_iniicio = time.time()
print(sum([numero for numero in range(100)])) # 100 de numeros
list_tempo = time.time() - list_iniicio

print(f'generator expression levou {gen_tempo}')
print(f'list comprehension levou {list_tempo}')

######################################################################################################################

