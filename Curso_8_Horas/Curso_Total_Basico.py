##############################################################
# Variáveis e tipos de dados
media = 0
n1 = n2 =n3 = n4 = 0.0
nome, idade = 'Leonardo', 47
estado = True

print (nome, idade) # strings
print(type(media)) # numeros
print(type(n1)) # numeros int
print(type(n2)) # numeros reais
print(type(1+2j)) # numeros complexos

##############################################################

# Função isinstance verifica se o objeto e do tipo especificado
print(isinstance(1, int)) # True
print(isinstance(1.0, float)) # True
print(isinstance(1+2j, complex)) # True
print(isinstance(1, float)) # False

###############################################################
# Operadores Aritméticos (+, -, *, /, //, %, **)

# Soma +
print(1+2)

# Subtração -
print(1-2)

# Multiplicação *
print(1*2)

# Divisão /
print(1/2)

# Divisão Inteira //
print(1//2)

# Resto da divisão %
print(1%2)

# Potência **
print(1**2)

###############################################################

# Operadores de Comparação (==)

# Igual ==
print(1==1) # True
print(1==2) # False

# Diferente !=
print(1!=1) # False
print(1!=2) # True

# Maior >
print(1>1) # False
print(1>2) # False

# Menor <
print(1<1) # False
print(1<2) # True       

# Maior ou Igual >=
print(1>=1) # True
print(1>=2) # False

# Menor ou Igual <=
print(1<=1) # True
print(1<=2) # True

###############################################################
# Operadores de atribuição (=, +=, -=, *=, /=, %=, **=, //=)

x = y = z = False
n1 = n2 = 0

print('Digite um numero:')
n1 = int(input())
n2 = int(input('Digite outro numero:'))

x = n1 == n2
print('São iguais?', x, '\n')

z = n1 > n2
print(n1, ' É maior que ', n2, '?', z, '\n')

y = n1 != n2
print('São diferentes?', y, '\n') 
###############################################################

# Operadores logicos (and, or, not)

x = True
y = False

print(x and y) # False
print(x or y) # True
print(not x) # False
