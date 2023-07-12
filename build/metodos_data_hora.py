# Métodos de data e hora

import datetime

agora = datetime.datetime.now()
print(agora) 
print(agora.strftime('%d/%m/%Y, %H:%M:%S')) # Data e hora no Python atual formatada par BR
print(type(agora))

