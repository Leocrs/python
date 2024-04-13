# função lambda

quadrado = lambda x: x ** 2
print(quadrado(5))

par = lambda x: x % 2 == 0
print(par(4))
print(par(5))

f_c = lambda x: (x - 32) * 5 / 9 # Formula de conversão de temperatura fahrenheit para celsius
print(f_c(32))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_par = lambda x: x % 2 == 0 # Formula de divisão pares
print(list(filter(num_par, num)))

num_impar = lambda x: x % 2 != 0 # Formula de divisão impares
print(list(filter(num_impar, num)))