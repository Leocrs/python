
#filter filtra dados iteraveis de uma lista e retorna os valores que satisfazem a condição

import statistics

####################################################################

valores = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
media = statistics.mean(valores)
print(media)

###################################################################

# Assim como a função Map a Filter recebe 2 parametros sendo uma função e um valor iteravel
dados = [1.2, 2.3, 3.3, 4.5, 5.6, 6,8, 7, 8, 9, 0.10]
media = statistics.mean(dados)
print(f'A media é: {media}')

####################################################################

resultado = filter(lambda valor: valor > media, dados)
print(list(resultado))

####################################################################

import statistics

precos_produtos = [5000, 9000, 2000, 15000]
precos_aumentados = ["R${:.2f}".format(preco * 1.1) for preco in precos_produtos]
valor_medio = statistics.mean(precos_produtos)
valor_a_cima = filter(lambda preco: preco >= 5000, precos_produtos)
print(precos_aumentados)
print(valor_medio)
print(list(valor_a_cima))

####################################################################

paises = ["Brasil", "Argentina", "Chile", " ", "EUA", "Mexico", "França", " ", "Espanha", "Inglaterra", "Portugal"]
print(list(filter(lambda pais: pais != " ", paises))) 

####################################################################

# map recebe dois parametros sendo uma função e um iteravel e retorna um ojeto iteravel 
# filter recebe um iteravel uma funão apenas os os valores que satisfazem a condição














