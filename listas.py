# Listas funciona como vetores ou matrizes, ou seja (arrays) de forma dinâmico e podendo colocar QUALQUER
# arquivo de dados.

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = [11, 12, 13, 14, 15]
lista4 = [16, 17, 18, 19, 20]
lista5 = [21, 22, 23, 24, 25]
lista6 = [26, 27, 28, 29, 30]

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

#######################################################################
num = 1
if num in lista2:
    print( f"Tem o numero {num}")
else:
    print( f"Não tem o numero {num}")
lista2.sort()  # sort = é o comando para colocar em ordem numerica ou alfabetica.
print(lista2)
# Podemos contar o valor de uma lista
print(lista2.count(8))
print(lista5.count("o"))

########################################################################

# Para add elementos em lista usamos a função append. OBS: um elemento por vez!
print(lista2)
lista2.append(10)
print(lista2)
lista2.append(11)
print(lista2)
lista2.append([20, 25, 30])
print([lista2])
lista2.extend([11 ,12, 13])   # extend Add elementos de forma adicional á lista.
print(lista2)

########################################################################

lista2 = list(range(6))
print(lista2)
lista2.append(7)
lista2
lista2.insert(2,"2")
print(lista2)

#########################################################################

# Podemos colocar duas listas juntas

lista1.extend(lista2)  # Posso usar o "+" no lugar do extend
list = lista1+lista2+lista3
print(list)
# reverse ou [:: -1] faz o mesmo resultado!
lista1.reverse()
lista2.reverse()
lista5.reverse()
print(lista1)
print(lista2)
print(lista5)
print(lista5[::-1])

#########################################################################

#Copiar uma lista!
lista6 = lista2.copy()
print(lista6)

#len = usado para contar elementos
print(len(lista5))

# Podemos remover o ultimo elemento da lista
print(lista5)
lista5.pop()
print(lista5)

lista2.clear() # Apada dados da mesma

lista2 = lista2 * 3   # Multiplicar
print(lista2)

#########################################################################

frase = "Eu vou aprender Python de verdade!"
frase = frase.split()   # slip usado para separar as palavras em lista
print(frase)

frase = "Tudo posso naquele que me fortalece!"

frase = frase.split()
print(frase)
frase = " ".join(frase)
print(frase)

print(lista6)
print(type(lista6))

#########################################################################

#Iterando sobre lista Utilizando "for"
for elementos in lista1+lista2:
    print(elementos)

#Iterando sobre lista Utilizando "while"
carrinho = []
produto = ""
while produto != "sair":
    print ("Adicione um produto na lista ou digite sair para sair.")
    produto = input()
    if produto != "sair":
        carrinho.append(produto)

for produto in carrinho:
    print (produto)
    # Uitlizando variaeis de lista.
    
########################################################################

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9
num10 = 10

numeros = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
print(numeros)

########################################################################
cores = ["verde", "amarelo", "azul", "branco"]

print(cores[0])
# Indice negativo funciona como uma roda sempre pega o proximo da lista
print(cores[-0])
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

lista1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
lista2 = ["1","2","3","4","5","6","7","8","9"]
lista3 = ["EXIBI UM TEXTO"]
lista4 = list(range(1))
lista5 = list("Leonardo Campos R. dos Santos")
lista6 = [1, 2.34,True, "Leonardo", "d", ["1","2","3"]]

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice +1
    
#######################################################################

# Gerar indice de um for para ver qual a relação de ordem de numero.
for indice, cor in enumerate(cores):
    print(indice,cor)

# Em listas fazemos acesso aos elementos de forma indexadas.
#          0          1        2        3
cores = ['verde', "amarelo", "azul", "branco"]

#######################################################################
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Revisando Slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

print(numeros.index(2,1))  #buscando a partir de 1
print(numeros.index(3,2))  #buscando a partir de 2
print(numeros.index(7,3))  #buscando a partir de 2

#######################################################################

# Podemos fazer busca dentro de range
print(numeros.index(8,3,6))

print(sum(lista1)) #soma
print(max(lista2)) #maximo
print(min(lista3)) #minimo
print(len(lista4)) #tamanho

# Transforma em lista tuplas

print(lista1)
print(type(lista2))
tupla = tuple(lista3)
print(tupla)

# Trabalhando com slice de lista - com paramentro de inicio
lista = [ 1,2,3,4]

# Desempacotamento de listas
num1, num2, num3, num4 = lista
print(num1, num2, num3, num4)
#OBS: o mumero de desempacotamento tem que ter o mesmo numero der variaveis e vise versa.

lista = [ 1,2,3,4]
print(lista)
nova = lista
print(nova)
nova.append(5)
print(nova)


