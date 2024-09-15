#Funçoes Recursivas - formula geral para fatorial
# fatorial num, =1se num, =0 ou se num =1 'Caso Base"
# fatorial num, =num * fatorial(num - 1) para num >1 'Caso recursivo"

n1 =2
def fatorial(num):
      if num == 1 or num == 0: # Caso base
          return 1
      else:
          return num * fatorial(num - 1) # Caso recursivo
     
if __name__ == '__main__': # __name__ é o nome da classe
     n1 = int(input('digite um valor: '))
     try:
         print(fatorial(n1))
     except  RecursionError: # Erro de recursão
         print('Voce digitou um valor inválido')
else:
         print(f'O fatorial de {n1} é {fatorial(n1)}') 
