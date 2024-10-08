#Funções com parâmetro (argumentos) recebidos pelo usuário em uma função    
#refaturando uma função
def raiz_quadrado(numero):
#return numero * numero # Retorna o numero ao quadrado (raiz)
    return numero ** 2 # retorne o numero ao quadrado
print(raiz_quadrado(7))
print(raiz_quadrado(8))
print(raiz_quadrado(3))
retorno = raiz_quadrado(4) # Outro modo de chamar a função
print(retorno)    

###################################################################################

def cantar_parabens(nome):
    print(f'Parabéns pra você, nessa data querida, muitas felicidades muitos anos de vida ao {nome}!')
cantar_parabens('Leonardo')
  
###################################################################################  
    
# Funções podem ter N parâmetros de entrada, ou N parâmetros de saída, ele são separados pela vírgula
def soma(num1, num2): # recebe dois parâmetros
    return num1 + num2 # retorne o resultado da soma
print(soma(2, 3)) 
print(soma(2, 2))

##################################################################################

def multiplica(num1, num2): # recebe dois parâmetros
    return num1 * num2 # retorne o resultado da multiplicação
print(multiplica(2, 5))
print(multiplica(5, 5))

#################################################################################

def outra(num1, A, Mensagem): # recebe três parâmetros
    return(num1 + A) * Mensagem # retorne o resultado da multiplicação
print(outra(2, 2, 'Olá mundo! '))
print(" Olá mundo!" * 10)
#OBS: Se informa um numero errado de parâmetros, a função retorna um TypeError
 
#################################################################################
 
# Parâmetros são variáveis de declaração na definição da função
# Argumentos são dados declarados na execução da uma função
def nome_completo (nome, sobrenome): # recebe dois parâmetros
    return (f"Seu nome completo é: {nome} {sobrenome} ") # retorne o resultado dos nome completo
print(nome_completo('Leonardo', 'Campos R. dos Santos')) # chamando a função

#################################################################################

def soma_impares(numeros):
    total = 0
    for numero in numeros:
        if numero % 2 != 0:
            total = total + numero
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))