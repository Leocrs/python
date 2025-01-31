# Deque é uma lista de alto performance, que permite adicionar e remover elementos

from collections import deque

#criando deque
deq = deque("Leonardo") #criando deque com string
print(deq)
deq.append("Campos") #adicionando string ao final do deque
print(deq)
deq.appendleft("Santos") #adicionando string ao inicio do deque
print(deq)

