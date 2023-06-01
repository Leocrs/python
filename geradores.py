

# geradores (generators) - funções que retornam iteráveis
#OBS: O contrario não é verdadeiro, ou seja nem todo iterável é gerador



# funções = Generator Function 

# Uitizam return = Ultilizam yield

# Retorna uma vez = podem utilizar yield multiplas vezes

# Quando executamos uma função, ela retorna um valor = quando executamos um  generator
###################################################################################################


# Exemplo de Generator Function
def contador(valor_maximo):   # criamos uma função
    contador = 1               # criamos um contador
    while contador <= valor_maximo:  # enquanto o contador for menor ou igual ao valor maximo
        yield contador   # retornamos o contador
        contador = contador + 1  # incrementamos o contador
        
gen = contador(5)    # gerador

print(next(gen))    # imprimimos o primeiro valor
print(next(gen))    # imprimimos o segundo valor
print(next(gen))    # imprimimos o terceiro valor