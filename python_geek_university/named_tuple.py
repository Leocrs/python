# named_tuple = tuple() é uma tupla não ordenada

tupla = (1, 2, 3)
print(tupla[1]) # tupla não é mutável e não é indexada

from collections import namedtuple

Pessoa = namedtuple('Pessoa', 'nome idade')# declaração de uma tupla
pessoa = namedtuple("pessoa", "idade") # declaração de uma tupla
pessoa = Pessoa('João', 22)
print(pessoa)

Joao = Pessoa(idade =22, nome='João')
print(Joao[1])
print(Joao.idade)
