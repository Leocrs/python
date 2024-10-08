import time # Biblioteca para manipulação de tempo
from threading import Thread # Biblioteca para manipulação de thread

Contador = 50000000 # definindo a função

def contagem_regressiva(n):  # definindo a função
    while n > 0:  # loop infinito
        n -= 1  # n = n - 1
        
inicio = time.time()  # iniciando o tempo
contagem_regressiva(Contador)  # chamando a função
fim = time.time()  # finalizando o tempo

print(f'A duração foi de {fim - inicio} segundos')  # tempo final - tempo inicial = tempo decorado


    