#  dados do usuario

from turtledemo.chaos import f

# Endrada de Dados
print("Qual o seu nome?")
nome = input() # Imput -> Entrada

print(f'Seja bem vindo(a){nome}')

print("Qual a sua idade?")
idade =input()

print(f" {nome} tem {idade} anos")

print("ELe Nasceu 1977")
#int(idade) cast é a conversão de dado para outro.
#print(" {nome} nasceu {1977 - int(idade)}")