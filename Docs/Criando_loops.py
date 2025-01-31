# Criando sua propria versão de loops

for numeros in [1, 2, 3, 4, 5]:
    print(numeros)
    
 ###########################################################################
    
for letras in 'Leonardo':
    print(letras)
    
###########################################################################

def meu_for (iteravel): # criando o meu proprio "for" em "def"
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
meu_for(["Leonardo Campos"])

###########################################################################

numeros = [1, 2, 3, 4, 5]
meu_for (numeros) # criando o meu proprio "for"
print(numeros)