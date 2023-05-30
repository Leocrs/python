
# debugger é um modo de interagir com o python para ver o que está sendo executado no momento da execução do código.
# bug = erro de sintaxe ou erro de execução

#OBS A utilização do debugger para debugar o código com print é uma pratica ruim. Existe forma mais profisiional utilizando o debugger.


breakpoint()  
#para debugar o código usando o debugger é necessario usar o breakpoint().
def dividir (a,b):
    try:
        return int(a)/ int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'
        
print(dividir(2,1))
        

# Comandos basicos de debugger
# pdb.set_trace()
# l lista onde estamos no codigo
# c continua a execução
# s salva o codigo
# q sai
# e executa a execução
# x sai da execução
# r reinicia
# c continua a execução
# p imprime o codigo

