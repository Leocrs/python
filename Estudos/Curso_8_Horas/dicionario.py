# Dicionarios - Conjunto de chaves e valores

frutas = {'maca': 10, 'banana': 8, 'laranja': 5}
print(frutas)
print(frutas['maca']) # acessando valor pela chave
print(frutas.get('laranja'))
print(frutas.keys()) # Retorna todas as chaves
print(frutas.values()) # Retorna todos os valores
print(frutas.items()) # Retorna todas as chaves e valores

for chave in frutas: # Retorna todas as chaves
     print(frutas[chave]) # Retorna todos os valores

# adicionando valores
frutas ['uva'] =3
print(frutas)

# excluindo valores
frutas ['laranja'] =0 # excluindo valores
print(frutas)

del frutas ['laranja'] # excluindo valores
print(frutas)

