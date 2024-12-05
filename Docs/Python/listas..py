
 # listas

lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#for num in lista1:
valores = lista1 + lista2  # Concatenando listas
print(valores)
print(len(valores)) # Tamanho da lista
print(valores[0]) # Primeiro valor da lista
valores.append(11) # Acrescentando valor na lista
valores.pop(0) # Removendo valor da lista
valores.insert(12, 19) # Acrescentando valor na lista
print( 21 in valores) # Verificando se existe valor na lista

planetas = ['Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno', 'Urano']
for planeta in planetas:
      print(planeta)

bebidas = [] # criando lista
for indice in range(5): # 0 1 2 3 4
     print (f'Insira o nome de uma bebida:') # perguntando nome da bebida
     bebidas.append(input()) # Acrescentando valor na lista
bebidas.sort() # colocando em ordem
print(bebidas) # exibindo a lista


