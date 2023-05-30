
# default_dict é um dicionário vazio.
# Ao criar um dicionário, o dicionário será inicializado com um valor padrão. nós pode definir um valor padrão para cada chave.
# um valor padrão pode ser definido de acordo com a necessidade do usuário. default_dict[chave] = valor
# podemos utilizar um lambda para definir um valor padrão.
# OBS: lambda é uma função anônima, que não tem nome e pode ser utilizada dentro de uma função com valores

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario ["curso"] ="Programação em Python: Essecial"
print(dicionario["curso"])
print(dicionario)
print(dicionario["outro"]) #key error não existe no dicionario default_dict = 0
