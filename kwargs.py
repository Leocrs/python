"""  
**kwargs - keyword arguments é um parâmetro que recebe uma lista de valores.
Por convensão chamamos de **kwargs. 
Diferente de **args, **kwargs recebem uma lista de valores nomedados. e transformam em um dicionário.


#Exemplo

def cores_favoritas(**kwargs):
   # for cores in kwargs.values(): #kwargs recebe uma lista de valores
    for pessoa, cores in kwargs.items():
        print (f' A cor favorita de {pessoa.title()} é {cores}')
        #print(cores)
    
cores_favoritas(Leonardo='preto', Natalia='Rosa', Paula='Amarelo')
#print(cores_favoritas(Leonardo='preto', Natalia='vermelho', Paula='azul'))
   
   
   def cumprimento_especial(**kwargs):
    if "Leonardo" in kwargs and kwargs["Leonardo"] == "Estudante de Python":
        return 'Você está estudando Python pra valer cara!'
    elif "Leonardo" in kwargs:
        return f'Você está estudando {kwargs["Leonardo"]}'
    return 'Você não está estudando Python direito!'

print(cumprimento_especial())
print(cumprimento_especial(Leonardo='Estudante de Python'))
print(cumprimento_especial(Leonardo='Uauu'))
print(cumprimento_especial(Leonardo='e seu futuro será especial!!!'))  


def minha_fucao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} a cima {idade} anos')
    print(*args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)
    
minha_fucao(46, "Leonardo")
minha_fucao(18,'Felicidade', 4,3,2,1, solteiro=True)
minha_fucao(38,'Natália', 'Eu=Não, você=Sim')
minha_fucao(46, "Leonardo", java=False, python=True) 


# Nas nossas funçoes podem ter:(NESSA ORDEM DE EXECUCAO):

# Parametros obrigatorios
# parametros default (não obrigatorios)
# kwargs



#Entenda o porque dessa ordem dos parametros é importante

# Função com a ordem de execução incorreta de parametros
def mostra_informacao (a, b,*args, Estudante='Leonardo', **kwargs):
    return [a, b, args, Estudante, kwargs]

print(mostra_informacao(1,2,3, Estudante='Leonardo',Cargo='Programador'))


def mostra_nomes(**kwargs):
   return (f'{kwargs["nome"]} {kwargs["sobrenome"]}')
print(mostra_nomes(nome='Leonardo', sobrenome='Campos'))
 
 
nomes = {'nome':'Leonardo', 'sobrenome':'Campos'}
print(mostra_nomes(**nomes))
"""

# Desempacotamento de parametros com kwargs

def soma_multiplos_numeros (a,b,c):
    print(a+b+c)
    
lista = [1,2,3]    
tupla = (1,2,3)
conjunto = {1,2,3}
dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)