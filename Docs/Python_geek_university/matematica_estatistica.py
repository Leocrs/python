# mat.prod = retornar_produto 

import math # importa a biblioteca math matematica

nuns_v1 = [1, 2, 3,4, 5, 6, 7, 8, 9, 10]
nuns_v2 = (1, 2, 3,4, 5, 6, 7, 8, 9, 10)
nuns_v3 = {1, 2, 3,4, 5, 6, 7, 8, 9, 10}

print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

math.isqrt # raiz quadrada
print(math.isqrt(16))
print(math.isqrt(17))

math.dist # distancia entre dois pontos
print(math.dist((0, 0), (1, 1)))

math.degrees # graus 
print(math.degrees(math.pi))

math.radians # radianos
print(math.radians(180))

math.exp # exponencial
print(math.exp(1))  

math.log # logaritmo natural
print(math.log(2))

math.hypot # hipotenusa
print(math.hypot(3, 4))

math.sin # seno e cosseno
print(math.sin(math.pi/2))

math.cos # seno e cosseno
print(math.cos(math.pi/2))

# Estatisticas
import statistics 

valores_reais = [1.2, 2.3, 3.3, 4.5, 5.6, 6,8, 7, 8, 9, 0.10]
media = statistics.fmean(valores_reais)
print(media)

valores_inteiros = [1, 2, 3,4, 5, 6, 7, 8, 9, 10]
media = statistics.fmean(valores_inteiros)
print(media)

print(statistics.geometric_mean(valores_inteiros)) # Geometrica media

print(statistics.median(valores_inteiros))









