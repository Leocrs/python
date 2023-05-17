"""  
kwargs is a dictionary 
Esse é só mais um parametro que recebe um dicionario dentro do args


def cores_favoritas(**kwargs):
    #print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')
        
cores_favoritas(Natalia='vermelho', Leonardo='azul', Joao='verde')

"""

# Função na ordem correta
#Descompactando kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"
        
nome ={'nome':'Natalia','sobrenome':'Rita'}        

print(mostra_nomes(**nome))
        


def soma_multiplos_numeros (a, b, c, **kwargs):
    return a + b + c

lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}
dicionario = {'a':1,'b':2,'c':3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(*dicionario)

#OBS: os nomes dos parametros devem ser os mesmos da funcao


print(soma_multiplos_numeros(**dicionario))
print(soma_multiplos_numeros(*tupla))
print(soma_multiplos_numeros(*conjunto))
print(soma_multiplos_numeros(*lista))
