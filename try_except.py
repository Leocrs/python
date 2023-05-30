  
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






    