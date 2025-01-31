# ordered_dict é um dicionário com chave e valor ordenado garantido.

dicionario = {"a":1, "b":2, "c":3}

for chave, valor in dicionario.items():
    print(f"chave={valor}:valor={valor}")
    
    from collections import OrderedDict
    
#######################################################################

dicionario = OrderedDict({"a":1, "b":2, "c":3, "d":4, "e":5})
print(dicionario)

for chave, valor in dicionario.items():
    print(f"chave={valor}:valor={valor}")

#######################################################################

from collections import OrderedDict #OrderedDict é um dicionario com chave e valor ordenado iguais

dicionario1 ={"a":1, "b":2, "c":3, "d":4, "e":5}
dicionario2 ={"e":5,"a":1, "b":2, "c":3, "d":4}
print(dicionario1 == dicionario2) #True A ordem dos elementos nao importa

########################################################################

dicionario1 = OrderedDict({"a":1, "b":2, "c":3, "d":4, "e":5})
dicionario2 = OrderedDict({"e":5,"a":1, "b":2, "c":3, "d":4})
print(dicionario1 == dicionario2) #False A ordem dos elementos importa quando usamos OrderedDict

       