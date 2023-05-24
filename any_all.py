"""  
any all é uma funcao que recebe uma lista como argumento e retorna um booleano indicando se ha algum elemento True ou False

all() -> Retorna True se todos os elementos da lista forem True, False caso contrario

any() -> Retorna True se algum elemento da lista for True, False caso contrario

"""

# #exemplo1 all()
# print(all([1,2,3,4]))
# print(all([0,1,2,3,4,]))

# #exemplo2 any()
# print(any([1,2,3,4]))
# print(any([0,1,2,3,4,]))

saldo = [10, 100, 1500, 3000, 3000, 2900, 2800, 3000, 4500, -10, 13, 20, 50, 50, 50, 50, 50]

if any ([item < 0 for item in saldo]):
    print("Teve saldo negativo")
else:
    print("Nao teve saldo negativo")

if all ([item > 0 for item in saldo]):
    print("Teve saldo positivo")
else:
    print("Nao teve saldo positivo")