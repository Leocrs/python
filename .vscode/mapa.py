"""
   Mapas São conhecidos em Python como dicionario
    for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])
    
for chave in receita:
    print(f'{receita[chave]}')
    """
    
receita = {'jan': 100, 'fev': 120, 'mar': 400}

for chave in receita:
    print(f'{chave} = R$ {receita[chave]}')
    print(type(chave))