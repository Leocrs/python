"""  
min e max traz o menor e o maior valor de uma lista


"""

#exemplo 1:

lista = [1, 2, 3, 4, 5 , 25, 30, 40, 50, 100]
nomes = ['João', 'Maria', 'Pedro', 'José', 'Ana']
print(min(lista)) #retorna o menor valor da lista
print(max(lista)) #retorna o maior valor da lista
print(len(lista)) #retorna o tamanho da lista
print(sum(lista)) #retorna a soma dos valores da lista


print(min(nomes, key=lambda nomes:len(nomes))) #retorna o menor valor da lista
print(max(nomes, key=lambda nomes:len(nomes))) #retorna o maior valor da lista 


