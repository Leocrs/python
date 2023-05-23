""" 
map fazemos mapeameno de valores para função de outras variáveis


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
"""

# Para fixr Map temos dados iteraveis, dados a1, a2, a3, ... an. Temos ums função f(a1), f(a2), f(a3), ... 
#Utilizamos o map para fazer a função f(a1), f(a2), f(a3), ... 
# O Map object retorna: uma lista com os valores da função f(a1), f(a2), f(a3), ...

# exemplo 2 

cidades_lista = [('São Paulo',29),('Rio de Janeiro',30), ('Belo horizonte',27), ('Porto Alegre18',15)]
print(list(map(lambda cidade: cidade, cidades_lista)))