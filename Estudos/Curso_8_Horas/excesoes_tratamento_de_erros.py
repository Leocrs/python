
# Exceções - Tratamento de erros

try: # bloco de tratamento de erros
      x = int(input('digite um valor: '))
      print(x)
except ValueError: # bloco de tratamento de erros
      print('Voce digitou um valor inválido')

def div(k, j):
     return round(k / j, 2)

if __name__ == '__main__':
    while True:
         try:
             n1 = int(input('digite um valor: '))
             n2 = int(input('digite outro valor: '))
             break
         except ValueError:
             print('Voce digitou um valor inválido')
         try:
             print(f'resultado: {div(n1, n2)}')
         except ZeroDivisionError:
             print('Impossível dividir por zero')