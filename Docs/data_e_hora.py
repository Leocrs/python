# Data e hora no Python

import datetime

print(datetime.datetime.now()) # Data e hora no Python atual
print(datetime.MAXYEAR) # maior data em ano
print(datetime.MINYEAR) # menor data em ano
 
print(repr(datetime.datetime.now())) # Data e hora no Python



# Ajustar a hora para padrão BR 
inicio = datetime.datetime.now()
print(inicio)
print(inicio.strftime('%d/%m/%Y, %H:%M:%S')) # Data e hora no Python atual ajustada


