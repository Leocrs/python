import requests
import time

# Criar um decorador calcular_tempo
def calcular_tempo(funcao):  # funcao recebe uma funcao
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f'A duração foi de {tempo_final - tempo_inicial} segundos') # tempo_final - tempo_inicial = tempo decorado
    return wrapper

      
    
@calcular_tempo    
def pegar_cotacao_dolar(): # pegar_cotacao_dolar recebe uma funcao
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()


