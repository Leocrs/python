  # Entendo o *args 
# O *args é um parâmetro que recebe uma sequência de parâmetros qualquer.

########################################################################

def soma_todos_numeros(num1= 1, num2= 2, num3= 3): # O *args é um parâmetro que recebe uma sequência de parâmetros qualquer.
    return num1 + num2 + num3   
print(soma_todos_numeros(1, 2, 3, 4)) 

########################################################################

def soma_todos_numeros(*args): # O *args é um parâmetro que recebe uma sequência de parâmetros qualquer.
    print(sum(args))

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(1, 2,) 
soma_todos_numeros(1, 2, 3) 
soma_todos_numeros(1, 2, 3, 4)
soma_todos_numeros(1, 2, 3, 4, 5)

########################################################################

def verifica_info(*args): #
    if "leonardo Campos" in args and "Estuda Python" in args:
        return"Leonardo Campos seja bem vindo!"
    return "Eu não sei quem é você!"
print(verifica_info())
print(verifica_info("leonardo Campos"))
print(verifica_info("Estuda Python"))

########################################################################

# Entendo o *args

def soma_todos_numeros(*args): 
    print(sum(args))

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(1, 2,) 
soma_todos_numeros(1, 2, 3) 
soma_todos_numeros(1, 2, 3, 4)
soma_todos_numeros(1, 2, 3, 4, 5)
# Como rersolver para conseguir ler uma lista de argumentos [1, 2, 3, 4, 5]                    
numeros = [1, 2, 3, 4, 5]
soma_todos_numeros(*numeros) # Para conseguir somar todos os argumentos [1, 2, 3, 4, 5] usamos o *args (*numeros) (*) é o parametro
#Desempatando os argumentos [1, 2, 3, 4, 5] para conseguir somar todos os argumentos [1, 2, 3, 4, 5] usamos o *args (*numeros)