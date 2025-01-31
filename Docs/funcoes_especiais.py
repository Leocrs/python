# funções especiais 

from functools import reduce # Função Reduce - Recebe uma função e uma lista e retorna o resultado

print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))) # Função Filter - Filtra dados iteraveis de uma lista e retorna os valores que satisfazem a condição

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5,6])) # Função Reduce - Recebe uma função e uma lista e retorna o 

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6]))) # Função Map - Recebe uma função e uma lista e retorna o resultado(filter(lambda x: x % 2
