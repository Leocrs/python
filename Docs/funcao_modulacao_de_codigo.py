
# Funções - Modularização de código, Reuso de código, Legibilidade de código
# def<nome_da_funcao>(parametros):
#    bloco_da_funcao

def mensagem(msg):
     print('-' * 30)
     print(msg)
     print('-' * 30)
     mensagem('Ola, Mundo!')
def soma(a, b):
    print(a+b)
soma(2, 3)

def mult(x, y):
     return x * y
print(mult(2, 3))


def div(k, j):
     if j != 0: # se j for diferente de zero
         return k / j
     else:
         return 'Impossível dividir por zero!'

if __name__ == '__main__': # __name__ é o nome da classe
     a = int(input('digite o valor de a: '))
     b = int(input('digite o valor de b: '))
     r = div(a, b) # chamando a função
     print(f'a divisão de {a} por {b} é {r}')

def quadrado(valor):
     quadrados =[]
     for x in valor:
         quadrados.append(x ** 2)
     return quadrados

def contar(caracter, numero=11):
     for i in range(1, numero):
         print(caracter)

if __name__ == '__main__':

# contar(caracter='*', numero=5) # Os nome não precisam ser iguais a variaveis basta está na ordem correta da função

 x = 5
 y = 7
 z = 3
 def soma(a, b, c =0):
     if c == 0:
         return a * b
     else:
         return a + b + c

 if __name__ == '__main__':
     res = soma(x, y, z)
     print(res)


     valores = [1, 2, 3, 4, 5]
     quadrados = quadrado(valores)
 for x in quadrado(valores):
     print(x)