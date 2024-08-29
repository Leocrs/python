"""   
generators.py - Generators in Python é uma estrutura de dados que permite criar sequências de valores. 

nomes = ['Luiz', 'Maria', 'João', 'Pedro', 'Ana']

print(any(nomes[0] == "J" for nome in nomes))
print(all(nomes[0] == "j" for nome in nomes))

print(getsizeof("Leonardo")) # mostrar o tamanho da string em bytes
"""

from sys import getsizeof 

#gerando uma lista de numeros com list comprehension
list_comp = getsizeof ([x * 10 for x in range(1000)])

#gerando uma lista de numeros com set comprehension
set_comp = getsizeof ({x * 10 for x in range(1000)})

#gerando uma lista de numeros com dictionary comprehension
dict_comp = getsizeof ({x: x* 10 for x in range(1000)})

#gerando uma lista de numeros com generator comprehension
gen_comp = getsizeof (x * 10 for x in range(1000))

print("Para fazer a mesma tarefa gastamos em memória:")
print(f' List Comprehesion: {list_comp} bytes')
print(f' Set Comprehesion: {set_comp} bytes')
print(f' Dictionary Comprehesion: {dict_comp} bytes')
print(f' Generator Comprehesion: {gen_comp} bytes')
