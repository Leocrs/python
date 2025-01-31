# condicional if, elif, else

# Programinha de Media de nota de alunos
n1 = n2 = 0.0
media = 0.0
n1 = float(input('Digite um numero:'))
n2 = float(input('Digite outro numero:'))

media = (n1 + n2) / 2
print(media)
if media >= 7:
     print('Aprovado')
elif media >= 5:
     print('Recuperacao')
else:
     print('Reprovado')
