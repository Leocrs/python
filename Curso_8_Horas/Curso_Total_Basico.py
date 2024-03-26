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