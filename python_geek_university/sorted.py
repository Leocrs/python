l 
#sorted é uma função que retorna uma lista ordenada.

#exemplo 1

nomes = ('João', 'Maria', 'José', 'Ana, karina')
print(sorted(nomes))

nomes = {'João', 'Maria', 'José', 'Ana, karina'}
print(sorted(nomes))

nomes = ['João', 'Maria', 'José', 'Ana, karina']
print(sorted(nomes, reverse=True))
print(sorted(nomes, key=len))
print(sorted(nomes, key=max))


