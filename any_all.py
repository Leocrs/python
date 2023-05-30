
# any all é uma funcao que recebe uma lista como argumento e retorna um booleano indicando se ha algum elemento True ou False

# all() -> Retorna True se todos os elementos da lista forem True, False caso contrario

# any() -> Retorna True se algum elemento da lista for True, False caso contrario

##########################################################################

saldo = [10, 100, 1500, 3000, 3000, 2900, 2800, 3000, 4500, -10, 13, 20, 50, 50, 50, 50, 50]

if any ([item < 0 for item in saldo]): # Verifica se há algum elemento negativo
    print("Teve saldo negativo")
else:
    print("Nao teve saldo negativo") # Verifica se há algum elemento negativo

if all ([item > 0 for item in saldo]): # Verifica se todos os elementos são positivos
    print("Teve saldo positivo")
else:
    print("Nao teve saldo positivo") # Verifica se todos os elementos são positivos
    
#########################################################################

#exemplo1 all() # Verifica se todos os elementos são True
print(all([1,2,3,4])) # Verifica se todos os elementos são True
print(all([0,1,2,3,4,])) # Verifica se todos os elementos são True

##########################################################################


#exemplo2 any() 
print(any([1,2,3,4])) # Verifica se há algum elemento True
print(any([0,1,2,3,4,])) # Verifica se há algum elemento True







