import time # Biblioteca para manipulação de tempo
from threading import Thread # Biblioteca para manipulação de thread

Contador = 50000000

def contagem_regressiva(n): # definindo a função
    while n > 0: # loop infinito
        n -= 1 # n = n - 1
        
t1 = Thread(target=contagem_regressiva, args=(Contador//2,)) # chamando a função
t2 = Thread(target=contagem_regressiva, args=(Contador//2,)) # chamando a função

inicio = time.time() # iniciando o tempo
t1.start() # iniciando a thread
t2.start() # iniciando a thread
t1.join() # esperando a thread
t2.join() # esperando a thread

fim = time.time() # finalizando o tempo

print(f'A duração foi de {fim - inicio} segundos') # tempo final - tempo inicial = tempo decorado

