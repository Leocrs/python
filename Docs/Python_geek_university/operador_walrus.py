# operador walrus - operador de atribuição e retorno de valores 

nome = "Leonardo"
print(nome)

print(nome := "Leonardo") # atribuição e retorno de valores 

# Modo tradicional
cesta =[]
fruta = input ("Digite uma fruta: ")
while fruta != "Jaca":
    cesta.append(fruta)
    fruta = input ("Digite uma fruta: ")

# Modo com walrus mais moderno e rápido
cesta =[]
while (fruta := input ("Digite uma fruta: ")) != "Jaca":
    cesta.append(fruta)
    fruta = input ("Digite uma fruta: ")
   
    