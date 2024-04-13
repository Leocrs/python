# Tuplas (tuple) São bastante parecidas com listas, a diferença é,
# As tuplas são separar por parensetes ()
# e listas por []

# As tuplas são imuaveiis, ela não muda. Toda tupla gera uma nova tupla.
# Lisas são mutaveis ela mudam conforme os comandos solicitados.

##################################################################

lista = [1, 5, 2, 3, 4]
print(lista)
lista.sort()
print(lista)
lista.append(7)
print(lista)

###################################################################

# CUIDADO as tuplas são representadas por () mas veja

tupla1 = (1, 2, 3, 4)
print(tupla1)
print(type(tupla1))

###################################################################


tupla2 = (1, 2, 3, 4, 5, 6) #Tuplas com 1 elemento
print(tupla2)
print(type(tupla2))

###################################################################

tupla3 = (4) # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

####################################################################

tupla4 = (4,) # Isso é uma tupla!
print(tupla4)
print(type(tupla4))
# Conclusão tuplas são definas pelo uso da vurgula, e não do () parenteses.

#####################################################################

tupla5 = 4,  # Tupla defina SIMPLEMENTE p     uso  VIRGULA para definir
print(tupla5)
print(type(tupla5))

####################################################################

tupla =tuple(range(11))   # Podemos criar tuplas com o range de forma dinamica, com inicio, meio e passo.
print(tupla)
print(type(tupla))

####################################################################

tupla = ("Leonardo", "Campos")    # Dessa forma o valor de Str tem que ser o mesmo de variaveis para desempacotar.
escola, curso = tupla

print(escola)
print(curso)
print(tupla)

#####################################################################

# Metodos para adicião e remoção para tuplas não existe pelo fato de ser imutaveis.

tupla = (1, 2, 3, 4, 5, 6, 7)
print(sum(tupla)) # soma
print(min(tupla))  # minimo
print(max(tupla)) # maxima
print(len(tupla)) # len conta

##################################################################

#Concatenar de tuplas

tupla1 = (1, 2, 3, 4, 5, 6, 7)
tupla2 = (8, 9, 10)
print(tupla1 + tupla2)   #Concatenação de tuplas

tupla1 = tupla1 +tupla2
print(tupla1) # é possivel alerar sobreescrendo o valor da variavel, OBS as tuplas são imutaveis e não bloqueadas.

####################################################################

#Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
    
####################################################################

    # Contando elemento dentro de uma tupla

tupla = ("a", "b", "c", "d", "e", "a", "c")  # count, commando para contador elementos
print(tupla.count("c"))

####################################################################
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print(meses[0])
#Iterar com while loop
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

    #Verificamos em qual indice de elementos está na tupla.

print(meses.index("Junho"))

#####################################################################

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

# Pq utilizar tuplas? Tuplas são mais RAPIDAS que LISTAS!!!
#  copiando tuplas de forma facil com nova varial recebendo já existentes.

tuplas = (1, 2, 3)
print(tuplas)
nova = tuplas
print(nova)
outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tuplas)






