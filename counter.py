"""
Modulo collection - Counter (contador) High performance Container performance

Ele recebe um dicionário como parâmetro e retorna um objeto do tipo Counter, que é parecido com um dicionário

    """
    
from collections import Counter # importa a biblioteca

lista = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] # lista com números

contador = Counter(lista) # cria um objeto do tipo Counter
print(contador) # imprime o contador
print(type(contador)) # imprime o tipo
