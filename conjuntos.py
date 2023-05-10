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
    """
    

 
#Uso interessante de conjuntos Sets

conjunto = {1,2,3,4,5}
print(conjunto)



