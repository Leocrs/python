"""
Conjuntos fazem referencia a teoria dos conjuntos da matemática
  No Python são chamados de Sets 
  
  Sets são coleções de elementos não ordenados
  
     #forma1
  
conjunto = set ({1,2,3,4,5,1,2,3,4,5})
print(conjunto)
print(type(conjunto))
#OBS ao criar um conjunto ja add o mesmo ira ignorar e não fará parte do conjunto

conjunto =({1,2,3,4,5})
print(conjunto)
print(type(conjunto))

if 3 in conjunto:
    print("Existe")
else:
  print("Não existe")
  
  
   # importante lembra que alem de ñ termos valores duplicados ñ temos ordem.
 
conjunto = {1,2,2,3,4,5}.__len__() # conjuntos não aceitam valores duplicados 
print(conjunto)
lista = [1,2,2,3,4,5].__len__() # Listas aceiam valores duplicados
print(lista)
tupla = (1,2,2,3,4,5).__len__() # tuplas aceiam valores duplicados
print(tupla)
dicionario = {1:1,2:2,2:2,3:3,4:4,5:5}.__len__() #dicionarios não aceitam valores duplicados
print(dicionario)


#Assim como outro conjunto Python podemos colocar tipos de dados misturados em Sets
conjuntos = {1,2,3,4,5, 3.30, True, False, 'a', 'b'} 
print(conjuntos)
print(type(conjuntos))
print(conjuntos.__len__())  

#Podemos iterar em um Sets normalmente
for valor in conjuntos:
    print(valor)
    
    
    conjunto = {1,2,3,4,5,5,7}
print(conjunto)
novo = conjunto.__len__()
print(novo)

conjuntos = {1,2,3,4}
print(conjuntos)
conjuntos.add(5)
conjuntos.add(5) # não duplica e nem gera erro, é ignorado e não add.
conjuntos.add(6)
print(conjuntos)

print(conjuntos),conjuntos.remove(4),print(conjuntos)

#Forma de criar um conjunto que trás a opção de buscar numeros e com tratativa de erro exibindo
# se tem ou não o número no conjunto.   
conjuntos = {1,2,3,4,5,6,7}
try:
    numero = int(input("Digite um número por favor: "))
    if numero not in conjuntos:
        raise ValueError("Esse número não esta na lista")
    else:
        print("Esse número esta na lista")
except ValueError as erro:
    print(erro)
    
    #Forma de criar um conjunto que trás a opção de buscar numeros e com tratativa de erro exibindo
# se tem ou não o número no conjunto.   
conjunto = {1,2,3,4,5,6,7}
numero = int(input("Digite um número por favor: "))
if numero not in conjunto: raise ValueError("Esse número não esta na lista")
else: print("Esse número esta na lista")

#Forma de criar um conjunto que trás a opção de buscar numeros e com tratativa de erro exibindo
# se tem ou não o número no conjunto.   
conjunto = {1,2,3,4,5,6,7}
print(conjunto) 

novo = conjunto.copy() #Deep copy é uma cópia profunda
print(conjunto)

novo = conjunto.add(8) #slallow copy é uma cópia simples
print(conjunto)

conjunto.clear()
print(conjunto) # Limpa o conjunto

estudantes_Python = {'João', 'Maria', 'Pedro', 'Ana', 'Paula', 'Laura'}
estudandes_Java = {'Fernanda', 'Gustavo', 'Paulo', 'Ana'}
# Veja que alguns alunos que estudam Python também estudam Java
print(estudantes_Python.intersection(estudandes_Java)) # Intersecção, retorna apenas os elementos que estão em ambos
print(estudantes_Python.union(estudandes_Java)) # União, retorna todos os elementos
print(estudantes_Python.difference(estudandes_Java)) # Diferença entre os elementos
print(estudantes_Python.symmetric_difference(estudandes_Java)) # Diferença simetrica entre os elementos
print(estudantes_Python.isdisjoint(estudandes_Java)) # Diferença simetrica entre os elementos


conjuntos_numeros_inteiros = {1,2,3,4,5,6}
print(conjuntos_numeros_inteiros)
print(type(conjuntos_numeros_inteiros)) #type retorna o tipo de dado
print(conjuntos_numeros_inteiros.__len__()) #len retorna o tamanho
print(conjuntos_numeros_inteiros.__contains__(5)) #contains retorna True ou False
print(sum(conjuntos_numeros_inteiros)) #sum retorna a soma
print(max(conjuntos_numeros_inteiros)) #max retorna o maior
print(min(conjuntos_numeros_inteiros)) #min retorna o menor
print(len(conjuntos_numeros_inteiros)) #len retorna o tamanho
print(conjuntos_numeros_inteiros.pop()) #pop retorna o elemento removido
    """
 









