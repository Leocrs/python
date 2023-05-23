"""   
Utilizando lambdas é uma funçao anonima

Função em Python

def soma(a, b):
    return a + b
       
def funcao(x):
    return x + 1
print(funcao(2))

def funcao2(x):
    return 3 * x + 1
print(funcao2(7))

# exemplo de uma funçao lambda
soma = lambda x, y: x + y
print(soma(2, 3))

lambda x: x + 1
print(funcao(2))

# Como utilizar a expressão lambda em uma funçao
soma = lambda x, y: x + y
print(soma(2, 3))

 # Podemos ter expressa~o lambda em uma funçao com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.title() + ' ' + sobrenome.strip().title()
print(nome_completo('joa~o','maria'))
print(nome_completo('maria','joa~o'))
print(nome_completo('jOa~o','mAria'))
print(nome_completo('jOa~o',     'mARIA'))


# Em funçoes Python podemos ter expressa~o lambda em uma funcao com multiplas entradas

amar = lambda: " Como não amar Pyton?"
uma = lambda x: 3 * x +1
duas = lambda x, y: (x *y) + 2
tres = lambda x, y, z: 3 * x +1/2 + 3 * x + 1
numero = lambda x: x + 1/2 + 3 * x + 1
print(amar())
print(uma(1))
print(duas(1, 1))
print(tres(2, 3, 4))
print(numero(1))
# Se passarmos mais argumentos, a funcao irá retornar a expressa~o type error
    
# Exemplo de uma funçao lambda tradicional
lista_autores = ["Mario de andrade", "Clarice Lispector", "Bianca de Almeida", "Machado de Assis", "Zibia Gasparetto", "Antonio de Paiva"]
lista_autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
lista_autores = sorted(lista_autores)
print(lista_autores)    
"""

# Exemplo de uma funçao lambda tradicional
lista_autores = ["Mario de andrade", "Clarice Lispector", "Bianca de Almeida", "Machado de Assis", "Zibia Gasparetto", "Antonio de Paiva"]
lista_autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
lista_autores = sorted(lista_autores)
print(lista_autores)
