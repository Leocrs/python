  
# zip = itera sobre dois iteráveis e retorna um iterável de tuplas com os elementos de ambos iteráveis.

lista = [1, 2, 3, 4, 5]
nomes= ['Leo', 'Maria', 'João' ,'Pedro', 'Paulo']

print(list(zip(lista, lista)))
print(list(zip(lista, nomes)))
print(list(zip(nomes, lista)))
