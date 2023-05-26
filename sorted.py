"""  
sorted é uma função que retorna uma lista ordenada.




"""
#exemplo 1

nomes = ['João', 'Maria', 'José', 'Ana']
print(sorted(nomes))


nomes = ('João', 'Maria', 'José', 'Ana')
print(sorted(nomes))

nomes = {'João', 'Maria', 'José', 'Ana'}
print(sorted(nomes))
print(sorted(nomes, reverse=True))
print(sorted(nomes, key=len))
