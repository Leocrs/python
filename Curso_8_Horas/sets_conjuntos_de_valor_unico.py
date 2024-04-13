# sets - Conjunto de valores unicos

frutas = {'maca', 'banana', 'laranja', 'maca', 'banana'}
print(frutas)
print(len(frutas)) # Retorna o tamanho
print('maca' in frutas) # Verificando se existe valor na string

# adicionando valores
frutas.add('uva') # adicionando valores
print(frutas) # adicionando valores

# excluindo valores
frutas.remove('banana') # excluindo valores
print(frutas) # excluindo valores

for frutas in frutas: # Retorna todos os valores
    print(frutas.upper()) # Retorna todos os valores


astros1 = {'Lua', 'Sol', 'Mercurio', 'Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno'}
astros2 = {'Makemake', ' Haumea', ' Eris', ' Callisto', 'Lua'}

print(astros1)
print(astros2, end='') # Retorna todos os valores

astros_set = set(astros1) # Retorna todos os valores
print(astros_set) # Retorna todos os valores

print(astros1 in astros2) # Retorna todos os valores se existir
print(astros1 != astros2) # Retorna todos os valores se existir
print(astros1.union(astros2)) # Retorna todos os valores se existir
print(astros1.intersection(astros2)) # Retorna todos os valores se existir
print(astros1.difference(astros2)) # Retorna todos os valores se existir
print(astros1.symmetric_difference(astros2)) # Retorna todos os valores se existir