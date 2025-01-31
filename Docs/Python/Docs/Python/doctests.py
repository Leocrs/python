#Doctests são funcionais que testam a funcionalidade de um programa em Python.
# Para rodar precisamos instalar o python -m doctests -v nome_do_arquivo.py  

import doctests 
def soma(a, b):
    return a + b
print(soma(1, 2))

from doctests import soma
print(soma(1, 2))