# Métodos de data e hora

import datetime



agora = datetime.datetime.now()
print(agora) 
print(agora.strftime('%d/%m/%Y, %H:%M:%S')) # Data e hora no Python atual formatada par BR
print(type(agora))

hoje = datetime.datetime.today() # Data e hora no Python HOJE
print(hoje)
print(hoje.strftime('%d/%m/%Y, %H:%M:%S')) # Data e hora no Python atual
print(repr(hoje))


# Mudanças ocorrendo a meia-noite a combinar (hora e minuto) Exemplo para manutenção de backup etc.
manutencao= datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(manutencao)
print(manutencao.strftime('%d/%m/%Y, %H:%M:%S'))

"""
# como converter para data pt-BR

import datetime
import locale

# Configura o idioma para pt_BR
locale.setlocale(locale.LC_ALL, 'pt_BR')

# Obtém a data atual
data_atual = datetime.datetime.now()

# Converte a data atual para o formato pt_BR
data_formatada = data_atual.strftime('%d/%m/%Y')

# Imprime a data formatada
print(data_formatada)
"""
