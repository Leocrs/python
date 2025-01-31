# Tipo de string
# Uma string EXEMPLO: "234" "a" "True" "42,3"

nome = "Leonardo Campos"
print(nome)
print(type(nome))

##################################################################

nome = "Leonardo Campos Rodrigues dos Santos"
print(nome)
print(type(nome))

####################################################################

nome = "Leonardo Campos"
print(nome)
print(type(nome)) # type() mostra o tipo de dado
print(nome.lower()) # lower() deixa todas as letras minusculas
print(nome.upper()) # upper() deixa todas as letras maiusculas
print(nome.capitalize()) # capitalize() deixa a primeira letra maiuscula
print(len(nome)) # len() mostra o tamanho
print(nome.strip) # strip() retira espacos em branco
print(nome.casefold) # casefold() deixa todas as letras minusculas
print(nome.replace(" ", ""))    # replace() troca uma letra por outra no texto
print(nome.islower) # islower() verifica se todas as letras sao minusculas
print(nome[0:9]) # fatiamento de strings
print(nome[9:]) # fatiamento de strings
print(nome.count(" ")) # count() conta quantos espacos existem no texto
print(nome.find(" ")) # find() mostra em qual posicao o espaco se encontra
print(nome.split()[0]) # split() divide o texto
print(nome.split()[1]) # split() divide o texto
print(nome[::-1]) # fatiamento de strings
print(nome.replace("e","i")) # replace() troca uma letra por outra no texto

texto = "socorram me subino em marrocos "
print(texto) 
print(texto[::-1])
