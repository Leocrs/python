 
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
    

# try/except - tratamento de erros e exceções 

# Utilizamos o bloco para tratarmos erros e exceções.

# try:
#      //execução do bloco problema
# except:
#     //tratamento que deve ser feito caso ocorra algum problema
    
    #exemplo 1
try:
    len()
except:
    print('Deu algum problema')
# Tente executar a função leo() e verifique se ocorreu algum problema. caso ocorra, execute o bloco except print('Deu algum problema')
    
#exemplo 2

try:
    len(5)
except TypeError:
    print('Você está tentando executar uma função que nao existe')
