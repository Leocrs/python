#**kwargs - keyword arguments é um parâmetro que recebe uma lista de valores.
#Por convensão chamamos de **kwargs. 
#Diferente de **args, **kwargs recebem uma lista de valores nomedados. e transformam em um dicionário.

#Exemplo

def cores_favoritas(**kwargs):
    """Imprime as cores favoritas de cada pessoa."""
    for pessoa, cores in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cores}')

cores_favoritas(Leonardo='preto', Natalia='Rosa', Paula='Amarelo')

def cumprimento_especial(**kwargs):
    """Retorna uma mensagem especial baseada nos argumentos fornecidos."""
    if "Leonardo" in kwargs and kwargs["Leonardo"] == "Estudante de Python":
        return 'Você está estudando Python pra valer cara!'
    elif "Leonardo" in kwargs:
        return f'Você está estudando {kwargs["Leonardo"]}'
    return 'Você não está estudando Python direito!'

print(cumprimento_especial())
print(cumprimento_especial(Leonardo='Estudante de Python'))
print(cumprimento_especial(Leonardo='Uauu'))
print(cumprimento_especial(Leonardo='e seu futuro será especial!!!'))

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    """Imprime informações sobre a pessoa."""
    print(f'{nome} acima de {idade} anos')
    print(*args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(46, "Leonardo")
minha_funcao(18, 'Felicidade', 4, 3, 2, 1, solteiro=True)
minha_funcao(38, 'Natália', 'Eu=Não, você=Sim')
minha_funcao(46, "Leonardo", java=False, python=True)

# Nas nossas funçoes podem ter:(NESSA ORDEM DE EXECUCAO):
# Parametros obrigatorios
# parametros default (não obrigatorios)
# kwargs
#Entenda o porque dessa ordem dos parametros é importante
# Função com a ordem de execução incorreta de parametros
def mostra_informacao(a, b, *args, Estudante='Leonardo', **kwargs):
    """Retorna uma lista com as informações fornecidas."""
    return [a, b, args, Estudante, kwargs]

print(mostra_informacao(1, 2, 3, Estudante='Leonardo', Cargo='Programador'))

def mostra_nomes(**kwargs):
    """Retorna o nome completo baseado nos argumentos fornecidos."""
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

print(mostra_nomes(nome='Leonardo', sobrenome='Campos'))

nomes = {'nome': 'Leonardo', 'sobrenome': 'Campos'}
print(mostra_nomes(**nomes))
