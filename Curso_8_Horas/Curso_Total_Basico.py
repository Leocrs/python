# ##############################################################
# # Variáveis e tipos de dados
# media = 0
# n1 = n2 =n3 = n4 = 0.0
# nome, idade = 'Leonardo', 47
# estado = True

# print (nome, idade) # strings
# print(type(media)) # numeros
# print(type(n1)) # numeros int
# print(type(n2)) # numeros reais
# print(type(1+2j)) # numeros complexos

# ##############################################################

# # Função isinstance verifica se o objeto e do tipo especificado
# print(isinstance(1, int)) # True
# print(isinstance(1.0, float)) # True
# print(isinstance(1+2j, complex)) # True
# print(isinstance(1, float)) # False

# ###############################################################
# # Operadores Aritméticos (+, -, *, /, //, %, **)

# # Soma +
# print(1+2)

# Subtração -
# print(1-2)

# # Multiplicação *
# print(1*2)

# # Divisão /
# print(1/2)

# # Divisão Inteira //
# print(1//2)

# # Resto da divisão %
# print(1%2)

# # Potência **
# print(1**2)

# ###############################################################

# # Operadores de Comparação (==)

# # Igual ==
# print(1==1) # True
# print(1==2) # False

# # Diferente !=
# print(1!=1) # False
# print(1!=2) # True

# # Maior >
# print(1>1) # False
# print(1>2) # False

# # Menor <
# print(1<1) # False
# print(1<2) # True

# # Maior ou Igual >=
# print(1>=1) # True
# print(1>=2) # False

# # Menor ou Igual <=
# print(1<=1) # True
# print(1<=2) # True

# ###############################################################
# # Operadores de atribuição (=, +=, -=, *=, /=, %=, **=, //=)

# x = y = z = False
# n1 = n2 = 0

# print('Digite um numero:')
# n1 = int(input())
# n2 = int(input('Digite outro numero:'))

# x = n1 == n2
# print('São iguais?', x, '\n')

# z = n1 > n2
# print(n1, ' É maior que ', n2, '?', z, '\n')

# y = n1 != n2
# print('São diferentes?', y, '\n')
# ###############################################################

# # Operadores logicos (and, or, not)

# x = True
# y = False

# print(x and y) # False
# print(x or y) # True
# print(not x) # False

###############################################################
# condicional if, elif, else

# # Programinha de Media de nota de alunos
# n1 = n2 = 0.0
# media = 0.0
# n1 = float(input('Digite um numero:'))
# n2 = float(input('Digite outro numero:'))

# media = (n1 + n2) / 2
# print(media)
# if media >= 7:
#     print('Aprovado')
# elif media >= 5:
#     print('Recuperacao')
# else:
#     print('Reprovado')
#############################################################

# Laços de repetição (for, while)

# num = 1
# while num <= 10: # 10 vezes
#     print(num) # 1 2 3 4 5 6 7 8 9 10
#     num += 1 # 2 3 4 5 6 7 8 9 10 11
#     print("Laço encerrado!")

#############################################################

# nome = None
# while True:
#     print("Digite seu nome, ou X para sair:") # X para sair
#     nome = input() # Entrada de dados
#     if nome == 'x' or nome == 'X': # Se o nome for X ou x para sair
#         break # Encerra o loop
# print ("Até logo!")

#############################################################

# Laço for

# for num in range(1, 11):
#     print(num)


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 0 1 2 3 4 5 6 7 8 9
# for num in lista: # 1 2 3 4 5 6 7 8 9
#     print(num) # 1 2 3 4 5 6 7 8 9

# for num in range(0, 10): # 0 1 2 3 4 5 6 7 8 9
#     print(num) # 0 1 2 3 4 5 6 7 8 9

# for num in range(0, 10, 2): # 0 2 4 6 8
#     print(num) # 0 2 4 6 8

# nome = input("Digite seu nome: ") # 0 1 2 3 4 5 6 7 8 9
# for x in range(10): # 0 1 2 3 4 5 6 7 8 9
#     print(f'{x+1} {nome}')

# pedras = ('Rubi', 'Esmeralda', 'Safira', 'Diamante') # 0 1 2 3
# for pedra in pedras: # 0 1 2 3
#     if pedra == 'Diamante': # Se pedra for Diamante
#         continue # Ignora o valor
#     print(pedra) # 0 1 2 3

#############################################################

# laços_encadeados

# for cont_externo in range(1, 6):
#     print(f' \nRodada  {cont_externo}') # \n quebra de linha \t tabulac{cont_externo})
#     for cont_interno in range(5, 0, -1):
#         print(f'valor  {cont_interno}) ') # \n quebra de linha \t tabulac{cont_externo})
# print('Fim do laço!')

# import random # Importando biblioteca random
# num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
# print(num) # 0 1 2 3 4 5 6 7 8 9

# for A in range(0, 10): # 0 1 2 3 4 5 6 7 8 9
#     num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
#     print(num) # 0 1 2 3 4 5 6 7 8 9

#############################################################

# modulos

#import math # Importando biblioteca math
# num = math.sqrt(81) # raiz quadrada
# print(num) # exibindo o resultado

#############################################################

# modo random - modulo aleatório

import random # Importando biblioteca random
# num = random.randint(0, 10) # 0 1 2 3 4 5 6 7 8 9
# print(num) # 0 1 2 3 4 5 6 7 8 9

#############################################################

# valor =  random.random() # 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
# print(f'Numero gerado: {round(valor *10, 2)}') # 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 {valor} *10, ')

# valor = random.uniform(1, 100) # 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9
# print(f'Numero gerado: {round(valor),2}') # 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9


# # Outra forma de gerar um valor aleatório tudo em uma linha
# print(f'Numero gerado: {round(random.uniform(1, 100), 2)}') # 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9

#############################################################

 # listas

# lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# #for num in lista1:
# valores = lista1 + lista2  # Concatenando listas
# #print(valores)
# #print(len(valores)) # Tamanho da lista
# # print(valores[0]) # Primeiro valor da lista
# valores.append(11) # Acrescentando valor na lista
# valores.pop(0) # Removendo valor da lista
# valores.insert(12, 19) # Acrescentando valor na lista
# print( 21 in valores) # Verificando se existe valor na lista

# planetas = ['Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno', 'Urano']
# for planeta in planetas:
#      print(planeta)

# bebidas = [] # criando lista
# for indice in range(5): # 0 1 2 3 4
#     print (f'Insira o nome de uma bebida:') # perguntando nome da bebida
#     bebidas.append(input()) # Acrescentando valor na lista
# bebidas.sort() # colocando em ordem
# print(bebidas) # exibindo a lista

#############################################################

# tuplas

# tupla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Criando tupla, e a tupla e imutavel
# print(tupla)
# tupla = tuple(tupla) # Transformando em tupla
# print(tupla)

#############################################################

# Matematica

# funçoes built-in

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# soma = sum(valores)
# print(soma)
# print(max(valores)) # Retorna o maior valor da lista
# print(min(valores)) # Retorna o menor valor da lista
# print(pow(2, 3)) # Retorna o valor de 2 elevado a 3
# print(round(sum(valores)/len(valores))) # Retorna a media da lista


# import math

# x = 8
# y = 100

# raiz_x = math.sqrt(x)
# raiz_y = math.sqrt(y)

# print(raiz_x)
# print(raiz_y)
# print(math.pi) # Retorna o valor de pi
# print(math.floor(raiz_y)) # Arredonda para baixo
# print(round(raiz_y)) # Arredonda para cima

##############################################################

# string

# nome = 'Leonardo'
# sobrenome = 'Campos'
# nome_completo = nome + ' ' + sobrenome # Concatenando string
# print(nome_completo)

# frase = 'Vamos aprender Python pra valer'
# palavras = (frase.split()) # Transformando string em lista
# print(palavras[0])

# for palavra in palavras: # Transformando string em lista
#     print(palavra)

# for letra in frase: # Transformando string em lista
#     print(letra)

# print(frase[6:22]) # fatiamento de string


# email = input('Digite seu email: ')
# print(email[0:email.index('@')]) # fatiamento de string
# print(email[0:email.find('@')]) # fatiamento de string

# produtos = 'Leite, Cerveja, Arroz, Feijão, Frutas'
# print(produtos.split(',')) # Transformando string em lista
# print ('Leite' in produtos) # Verificando se existe valor na string

# objetos = 'Leite, Cerveja, Arroz, Feijão, Frutas'
# print (objetos) # Transformando string em lista
# print (objetos.upper()) # Transformando string com todas as letras maiusculas
# print (objetos.lower()) # Transformando string com todas as letras minusculas
# print (objetos.capitalize()) # Transformando string com  primeira letra em maiuscula
# print (objetos.title()) # Transformando string com a primeira letra em maiuscula


# frase = 'Vamos aprender Python pra valer'
# print(frase.lstrip()) # Removendo espacos em branco a esquerda
# print(frase.rstrip()) # Removendo espacos em branco a direita
# print(frase.strip()) # Removendo espacos em branco a esquerda e a direita

# fruta = 'laranja'
# print(fruta.rjust(20)) # Alinhando a direita
# print(fruta.ljust(20)) # Alinhando a esquerda
# print(fruta.center(20)) # Alinhando ao centro
# print(fruta.center(20, '*')) # Alinhando ao centro com *

# palavra = 'Leonardo Campos'
# print(palavra.startswith('Le')) # Verificando se existe valor na string
# print(palavra.endswith('s')) # Verificando se existe valor na string

# texto = """docstrings - documentando funções com docstrings
# OBS: podemos ter acesso a funções com docstrings utilizando a função help() __doc__"""
# print(texto)

###############################################################

# Dicionarios - Conjunto de chaves e valores

# frutas = {'maca': 10, 'banana': 8, 'laranja': 5}
# print(frutas)
# print(frutas['maca']) # acessando valor pela chave
# print(frutas.get('laranja'))
# print(frutas.keys()) # Retorna todas as chaves
# print(frutas.values()) # Retorna todos os valores
# print(frutas.items()) # Retorna todas as chaves e valores

# for chave in frutas: # Retorna todas as chaves
#     print(frutas[chave]) # Retorna todos os valores

# # adicionando valores
# frutas ['uva'] =3
# print(frutas)

# # excluindo valores
# frutas ['laranja'] =0 # excluindo valores
# print(frutas)

# del frutas ['laranja'] # excluindo valores
# print(frutas)

##############################################################

# sets - Conjunto de valores unicos

# frutas = {'maca', 'banana', 'laranja', 'maca', 'banana'}
# print(frutas)
# print(len(frutas)) # Retorna o tamanho
# print('maca' in frutas) # Verificando se existe valor na string

# # adicionando valores
# frutas.add('uva') # adicionando valores
# print(frutas) # adicionando valores

# # excluindo valores
# frutas.remove('banana') # excluindo valores
# print(frutas) # excluindo valores

# for frutas in frutas: # Retorna todos os valores
#     print(frutas.upper()) # Retorna todos os valores


# astros1 = {'Lua', 'Sol', 'Mercurio', 'Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno'}
# astros2 = {'Makemake', ' Haumea', ' Eris', ' Callisto', 'Lua'}

# # print(astros)
# # print(astros, end='') # Retorna todos os valores

# # astros_set = set(astros) # Retorna todos os valores
# # print(astros_set) # Retorna todos os valores

# print(astros1 in astros2) # Retorna todos os valores se existir
# print(astros1 != astros2) # Retorna todos os valores se existir
# print(astros1.union(astros2)) # Retorna todos os valores se existir
# print(astros1.intersection(astros2)) # Retorna todos os valores se existir
# print(astros1.difference(astros2)) # Retorna todos os valores se existir
# print(astros1.symmetric_difference(astros2)) # Retorna todos os valores se existir

##############################################################

# Funções - Modularização de código, Reuso de código, Legibilidade de código

#def<nome_da_funcao>(parametros):
#    bloco_da_funcao

# def mensagem(msg):
#     print('-' * 30)
#     print(msg)
#     print('-' * 30)
# mensagem('Ola, Mundo!')

# def soma(a, b):
#    print(a+b)
# soma(2, 3)

# def mult(x, y):
#     return x * y
# print(mult(2, 3))


# def div(k, j):
#     if j != 0: # se j for diferente de zero
#         return k / j
#     else:
#         return 'Impossível dividir por zero!'

# if __name__ == '__main__': # __name__ é o nome da classe
#     a = int(input('digite o valor de a: '))
#     b = int(input('digite o valor de b: '))

#     r = div(a, b) # chamando a função
#     print(f'a divisão de {a} por {b} é {r}')

# def quadrado(valor):
#     quadrados =[]
#     for x in valor:
#         quadrados.append(x ** 2)
#     return quadrados

# def contar(caracter, numero=11):
#     for i in range(1, numero):
#         print(caracter)

# if __name__ == '__main__':
    # contar(caracter='*', numero=5) # Os nome não precisam ser iguais a variaveis basta está na ordem correta da função

# x = 5
# y = 7
# z = 3
# def soma(a, b, c =0):
#     if c == 0:
#         return a * b
#     else:
#         return a + b + c

# if __name__ == '__main__':
#     res = soma(x, y, z)
#     print(res)


#     valores = [1, 2, 3, 4, 5]
#     quadrados = quadrado(valores)
# for x in quadrado(valores):
#     print(x)

##############################################################

# Escopo - Variaveis Globais e Locais

# var_global = " Curso 8 Horas de Python" # Variavel Global"
# def escreve_texto():
#     global var_global
#     var_global = 'Curso muito bom para iniciantes e revisão'
#     var_local = "Curso Total Básico ao avançado" 
#     print(f'Variavel Global: {var_global}') 
#     print(f'Variavel Local: {var_local}')    

# if __name__ == '__main__':
#     print(escreve_texto())
#     escreve_texto()

# print(var_global)
# print(var_local)

##############################################################

# Exceções - Tratamento de erros

# try: # bloco de tratamento de erros
#      x = int(input('digite um valor: '))
#      print(x)
# except ValueError: # bloco de tratamento de erros
#      print('Voce digitou um valor inválido')

# def div(k, j):
#     return round(k / j, 2)

# if__name__ == '__main__':
# while True:
#         try:
#             n1 = int(input('digite um valor: '))
#             n2 = int(input('digite outro valor: '))
#             break
#         except ValueError:
#             print('Voce digitou um valor inválido')
#         try:
#             print(f'resultado: {div(n1, n2)}')
#         except ZeroDivisionError:
#             print('Impossível dividir por zero')

###############################################################

# Funçoes Recursivas - formula geral para fatorial
# fatorial num, =1se num, =0 ou se num =1 'Caso Base"
# fatorial num, =num * fatorial(num - 1) para num >1 'Caso recursivo"

# n1 =2
# def fatorial(num):
#      if num == 1 or num == 0: # Caso base
#          return 1
#      else:
#          return num * fatorial(num - 1) # Caso recursivo
     
# if __name__ == '__main__': # __name__ é o nome da classe
#     n1 = int(input('digite um valor: '))
#     try:
#         print(fatorial(n1))
#     except  RecursionError: # Erro de recursão
#         print('Voce digitou um valor inválido')
# else:
#         print(f'O fatorial de {n1} é {fatorial(n1)}') 

###############################################################

# função lambda

# quadrado = lambda x: x ** 2
# print(quadrado(5))

# par = lambda x: x % 2 == 0
# print(par(4))
# print(par(5))

# f_c = lambda x: (x - 32) * 5 / 9 # Formula de conversão de temperatura fahrenheit para celsius
# print(f_c(32))



###############################################################