  
# Erros mais comuns em Python são as exceções.
# syntax error -> erro de sintaxe (erro de sintaxe) ocorre quando um programa não está compilando corretamente.

#exemplo 1
# def funcao( )
#     print('oi')    faltau os : na função
    
#     exemplo 2
#  none 1 =    Não se pode usar palavrar reservadas na função
#     print('oi')        

##############################################################################
# NameError: name 'None' is not defined ocorre quando uuma função não está definida
# print(oi) está fora da aspas da função

# Namerror:
# exemplo 3

a = 18
if a > 10:
    mensagem = 'a é maior que 10'
print(mensagem)
# ATenção, nesse caso vai dar erro porque a variavel a nao está definida com um valor inferior ao 10 que será chamado na função

#############################################################################

# Typerror: ocorre quando uma função não está definida

# #exemplo 4

# print(len('oi')
###############################################################################
# IndexError: Ocorre quando uma função tenta acessar um índice que não existe
# exemplo 5
# tupla = (1,2,3)
# print(tupla[5]) não existe o índice 5 na tupla que está sendo utilizada na função print(tupla[5])

################################################################################
# valerror: ocorre quando uma função não está definida como built-in função integrada

#exemplo 6
print(int('oi'))

print(float('oi'))

################################################################################
# keyerror: ocorre quando uma função não está definida como uma chave do dicionário

#exemplo 7
dicionario = {'a':1, 'b':2, 'c':3}
print(dicionario['d'])  # não existe o índice d na dicionario que está sendo utilizada na função print(dicionario['d'])
################################################################################

# atributeerror: ocorre quando uma função não está definida como atributo do objeto






