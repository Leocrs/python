"""  
debugger é um modo de interagir com o python para ver o que está sendo executado no momento da execução do código.
bug = erro de sintaxe ou erro de execução




"""
#OBS A utilização do debugger para debugar o código com print é uma pratica ruim. Existe forma mais profisiional utilizando o debugger.
def dividir (a,b):
    try:
        return int(a)/ int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'
        
print(dividir(2,1))
        


