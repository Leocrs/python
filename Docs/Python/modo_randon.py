# modo random - modulo aleatório

import random # Importando biblioteca random
num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
print(num) # 0 1 2 3 4 5 6 7 8 9

valor =  random.random() # 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
print(f'Numero gerado: {round(valor *10, 2)}') # 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 {valor} *10, ')

valor = random.uniform(1, 100) # 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9
print(f'Numero gerado: {round(valor),2}') # 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9

# Outra forma de gerar um valor aleatório tudo em uma linha
print(f'Numero gerado: {round(random.uniform(1, 100), 2)}') # 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9