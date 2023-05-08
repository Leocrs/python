"""
Estrutas: logicas and, or, not, is

Operadores unários: not, is
Operadores binários: and, or

Regras de funcionamento:

Para and" ambos os valores precisam ser True
Para or" um ou outro valor precisam ser True
Para not" o valor do bolano é invertido, ou seja, se for True e False e se for False ele vira True.

"""
ativo = True
logado = False

if not logado:
    print("Você precisa ativar sua conta. Por favor, Cheque seu email!")
else:
    print("Bem vindo usuário!")

print(ativo is True)

