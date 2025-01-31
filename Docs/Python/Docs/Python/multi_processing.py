import time # Biblioteca para manipulação de tempo
from multiprocessing import Pool # Biblioteca para manipulação de thread

Contador = 50000000 # valor inicial

def contagem_regressiva(n): # definindo a função
    while n > 0: # loop infinito
        n -= 1 # n = n - 1
        
if __name__ == "__main__": # executando a função
    pool = Pool (processes=2) # cria 2 processos
    inicio = time.time() # iniciando o tempo
    r1 = pool.apply_async(contagem_regressiva, (Contador//2,)) # r1 = pool.apply_async(contagem_regressiva, (Contador//2,))
    r2 = pool.apply_async(contagem_regressiva, (Contador//2,)) # r2 = pool.apply_async(contagem_regressiva, (Contador//2,))
    pool.close() # fechando o pool
    pool.join() # juntando os resultados
    fim = time.time() # finalizando o tempo

    print(f'A duração foi de {fim - inicio} segundos') # tempo final - tempo inicial = tempo decorado