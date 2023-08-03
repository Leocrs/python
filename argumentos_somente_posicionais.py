
valor = 67.3
print(float(valor))

def cumprimenta_v1(nome):
    return f'Oi {nome}!'
print(cumprimenta_v1('Leonardo'))
print(cumprimenta_v1(nome ='Leonardo Campos'))

def cumprimenta_v2(nome, /): # Variavel local com atributo posicional
    return f'Oi {nome}!'
print(cumprimenta_v2('Leonardo'))

