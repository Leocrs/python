# random_1.py é uma biblioteca de geradores de números aleatórios.

##########################################################################

# Jogo cara e coroa
cara_e_coroa = randint(0, 1) # Gera um número aleatório entre 0 e 1
if cara_e_coroa == 0: #
    print('Cara')
else:
    print('Coroa')
    
##########################################################################

print(randint(0,  100)) # Gera um número aleatório entre 0 e 100

#########################################################################

sorteio_cores = ['vermelho', 'verde', 'azul']  # Gera uma lista de cores
print(random.choice(sorteio_cores))
#########################################################################

sorteia_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Gera um número aleatório entre 1 e 10
print(sorteia_numeros[randint(0, len(sorteia_numeros) )]) # Gera um número aleatório entre 0 e 10

#########################################################################

sorteia_nomes = ["Leo", "Pedro", "Ana" , "Maria" , "João"] # Gera um nome aleatório
print(sorteia_nomes[randint(1, len(sorteia_nomes ))]) # Gera um nome aleatório

########################################################################

print(random.uniform(4, 10)) # Gera um número decimal aleatório entre 4 e 10

########################################################################

cartas_de_um_baralho = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] # Gera uma lista de cartas de um baralho aleatório
print(choice(cartas_de_um_baralho))

#########################################################################

cartas_de_um_baralho = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] # Gera uma lista de cartas de um baralho aleatório
random.shuffle(cartas_de_um_baralho) # embaralha a lista de cartas com o método shuffle
print(cartas_de_um_baralho)# embaralha a lista de cartas

########################################################################
    
# Exemplo de utilização:
from random import randint
from random import random
from random import choice
import random   
from random import shuffle





