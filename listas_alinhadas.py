"""   
listas alinhadas 

Algumas linguas de programação possuem estruturas de dados que se chamam arrays.
Unidimencionais arrays/vetores
multidimencionais arrays/matrizes

Em python não temos as listas alinhadas.

exemplo:

numeros = [1,2, 'b', 3.23, True, 5]


listas = [[1,2,3,], [4,5,6], [7,8,9]] #matriz 3x3
print(listas)    
print(type(listas))
print(listas[0])
#como acessar um elemento de numero 2?
print(listas[0][2])
print(listas[2][1])

#iterando com loops em listas alinhadas
for lista in listas:
    for elemento in lista:
        print(elemento)
        
        
#list comprehension
[[print (elemento) for elemento in lista] for lista in listas for elemento in lista]

#list comprehension 2
[[print(elemento) for elemento in lista] for lista in listas]

"""

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]   
print(tabuleiro)
    
 
    