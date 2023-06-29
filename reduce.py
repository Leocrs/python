# reduce is a built-in function in python	é uma funcao que recebe uma funcao como argumento e retorna outra funcao

dados = ['a1','a2','a3','a4']
reduce(function,list)
a1 = a2 = a3 = a4 = 1
# Ele soma a1 e a2 e a cada passo ela aplica a funçao a3 e a4 e vai somando os resultados

from functools import reduce

lista = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
print(reduce(lambda x,y: x*y,lista))
print(reduce(lambda x,y: x+y,lista))
print(reduce(lambda x,y: x/y,lista))
print(reduce(lambda x,y: x-y,lista))