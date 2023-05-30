 
# try: é um bloco de código que permite tratar exceções.
# except: esse bloco de código permite tratar exceções.
# else: esse bloco de código permite tratar exceções.
# finally: esse bloco de código permite tratar exceções.

# Dica de quando e onde tratar o codigo: Toda entrada do programa deve ser tratada

numero = int(input('Digite um número: '))
print(f'O número digitado foi {numero}')

try:    # O bloco de código que trata erro ao tentar digitar outros atributos que não sejam numeros 
    numero = int(input('Digite um número: '))
except ValueError:
    print('Digite um número válido')
else:
    print(f'O número digitado foi {numero}')
    
###############################################################################
    
#finally: esse bloco de código permite tratar exceções
try:
    numero = int(input('Digite um número: '))
except ValueError:
    print('Digite um número válido')
else:
    print(f'O número digitado foi {numero}')
finally:
    print('Fim do programa!')   #OBS: Sempre será executado ao final do programa dando erro ou não
    

