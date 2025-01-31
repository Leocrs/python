# deltas Trabalhando com Deltas de Data e Hora diferentes

#Ex data inicio = dd/mm/yyyy, hh:mm:ss
#Ex data fim = dd/mm/yyyy, hh:mm:ss

#delta = inicio - fim

import datetime

# Data para ocorrer um evento
inicio = datetime.datetime.now()
fim = datetime.datetime(2023, 7, 13, 15, 0, 0)
delta = inicio - fim
print(delta)
print(f'{delta.days} dias, {delta.seconds} segundos')


# vencimento de boleto

data_de_compra = datetime.datetime.now()
print(data_de_compra)
data_de_vencimento = data_de_compra + datetime.timedelta(days=10)
print(f' O boleto vence em {data_de_vencimento}')

print(data_de_compra)

print(data_de_vencimento)

# exemplo 1

# data_de_compra = datetime.datetime.now()

print(data_de_compra)       

