# map fazemos mapeameno de valores para função de outras variáveis

import math

def area(raio):
    return math.pi * raio**2
print(area(5))
print(area(3))

raios = [1,2,3,4,5] # lista

areas =[] # forma comum de criar uma lista
for raio in raios:
    areas.append(area(raio))
print(areas)

print(list(map(area, raios))) # list comprehension

print(list(map(lambda raio: math.pi * raio**2, raios))) # função lambda
 
# Para fixr Map temos dados iteraveis, dados a1, a2, a3, ... an. Temos ums função f(a1), f(a2), f(a3), ... 
# #Utilizamos o map para fazer a função f(a1), f(a2), f(a3), ... 
# O Map object retorna: uma lista com os valores da função f(a1), f(a2), f(a3), ...

########################################################################

# Exemplo 2 

cidades_lista = [('São Paulo',29),('Rio de Janeiro',30), ('Belo horizonte',27), ('Porto Alegre18',15)]
print(list(map(lambda cidade: cidade, cidades_lista)))


precos = [1000, 1500, 1250, 2500]
def adiciona_imposto (preco):
    return preco *1.1
preco_com_imposto = []
for preco in precos:
    preco_com_imposto.append(adiciona_imposto(preco))
print(preco_com_imposto)

#########################################################################

precos = [1000, 1500, 1250, 2500]
precos_com_imposto = list(map(lambda x: x * 1.1, precos)) # Aplica o imposto de 10% em cada valor da lista
precos_formatados = ["R${:,.2f}".format(valor) for valor in precos_com_imposto] # Formata cada valor da lista como uma string em moeda brasileira
print(precos_formatados)

##########################################################################

import pandas as pd
import statistics as display
import xlrd as xlrd
import matplotlib.pyplot as plt
import numpy as np
    
precos = [1000, 1500, 1250, 2500]
def adiciona_imposto (preco):
    return preco *1.1

precos_com_imposto = list(map(lambda x: x * 1.1, precos)) # Aplica o imposto de 10% em cada valor da lista
precos_formatados = ["R${:,.2f}".format(valor) for valor in precos_com_imposto] # Formata cada valor da lista como uma string em moeda brasileira
print(precos_formatados)

tabela = pd.read_excel("Base Vendas.xlsx")

tabela["Preco com imposto"] = list(map(adiciona_imposto, tabela ["Preco Unitario"]))
print(tabela)
tabela.to_excel("Base Vendas Atualizada.xlsx")

