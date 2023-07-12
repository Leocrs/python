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


