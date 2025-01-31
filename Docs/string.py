# string

nome = 'Leonardo'
sobrenome = 'Campos'
nome_completo = nome + ' ' + sobrenome # Concatenando string
print(nome_completo)

frase = 'Vamos aprender Python pra valer'
palavras = (frase.split()) # Transformando string em lista
print(palavras[0])

for palavra in palavras: # Transformando string em lista
    print(palavra)

for letra in frase: # Transformando string em lista
     print(letra)

print(frase[6:22]) # fatiamento de string


email = input('Digite seu email: ')
print(email[0:email.index('@')]) # fatiamento de string
print(email[0:email.find('@')]) # fatiamento de string

produtos = 'Leite, Cerveja, Arroz, Feijão, Frutas'
print(produtos.split(',')) # Transformando string em lista
print ('Leite' in produtos) # Verificando se existe valor na string

objetos = 'Leite, Cerveja, Arroz, Feijão, Frutas'
print (objetos) # Transformando string em lista
print (objetos.upper()) # Transformando string com todas as letras maiusculas
print (objetos.lower()) # Transformando string com todas as letras minusculas
print (objetos.capitalize()) # Transformando string com  primeira letra em maiuscula
print (objetos.title()) # Transformando string com a primeira letra em maiuscula


frase = 'Vamos aprender Python pra valer'
print(frase.lstrip()) # Removendo espacos em branco a esquerda
print(frase.rstrip()) # Removendo espacos em branco a direita
print(frase.strip()) # Removendo espacos em branco a esquerda e a direita

fruta = 'laranja'
print(fruta.rjust(20)) # Alinhando a direita
print(fruta.ljust(20)) # Alinhando a esquerda
print(fruta.center(20)) # Alinhando ao centro
print(fruta.center(20, '*')) # Alinhando ao centro com *

palavra = 'Leonardo Campos'
print(palavra.startswith('Le')) # Verificando se existe valor na string
print(palavra.endswith('s')) # Verificando se existe valor na string

texto = """docstrings - documentando funções com docstrings
# OBS: podemos ter acesso a funções com docstrings utilizando a função help() __doc__"""
print(texto)