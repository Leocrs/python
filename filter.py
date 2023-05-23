"""  
filter filtra dados iteraveis de uma lista e retorna os valores que satisfazem a condição


# modelo de filtro de dados iteraveis
media = sum(dados) / len(dados) 
print(media)

# modelo de filtro de dados iteraveis com lambda
valores = filter(lambda x: x > media, dados)
print(list(dados))

valores = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
media = statistics.mean(valores)
print(media)
"""
# Assim como a função Map a Filter recebe 2 parametros sendo uma função e um valor iteravel

import statistics # importa a biblioteca statistics para calcular a media

dados = [1.2, 2.3, 3.3, 4.5, 5.6, 6,8, 7, 8, 9, 0.10]
media = statistics.mean(dados)
print(f'A media é: {media}')

resultado = filter(lambda valor: valor > media, dados)
print(list(resultado))















