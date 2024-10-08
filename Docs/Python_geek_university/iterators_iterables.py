# iterators and iterables
# iterators é um objeto que pode ser iterado, sendo uma estrutura de dados que permite a iteração de uma função next() 
# iterables é um objeto que pode ser iterado, quando a função iter() for chamada

nome = 'Leonardo' # iterable mas não é um iterador
numeros = [1, 2, 3, 4, 5] # iterable mas não é um iterador

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))




    

