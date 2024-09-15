# Jogo de cartas 


import random # importando a biblioteca random 


cartas = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

random.shuffle(cartas)  # Embaralhar a lista de nomes

jogadores = len(cartas)  # Quantidade de jogadores
cartas_por_jogador = 5 # Quantidade de cartas por jogador

jogo = {} # Dicionario

for jogador in range(jogadores): # For para percorrer os jogadores
    jogo[jogador] = random.sample(cartas, cartas_por_jogador)  # Distribuir cartas aleatórias para cada jogador

for jogador, cartas in jogo.items():  # For para percorrer os jogadores
    print(f"{cartas}")  # Imprimir os cartas
