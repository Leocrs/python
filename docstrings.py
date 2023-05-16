"""   
Documentando funções com docstrings 

OBS: podemos ter acesso a funções com docstrings utilizando a função help() __doc__ 


def diz_oi():
    
    Essa função diz oi
    
    print("oi")

print(diz_oi.__doc__)
print(help(print))
help(diz_oi)
"""
from docstrings import *


def diz_oi():
    return "oi"
def exponencial (numero, potencia=2):
    return numero ** potencia

print(diz_oi())
print(exponencial(2,3))

