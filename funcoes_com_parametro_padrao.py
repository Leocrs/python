"""    
funções com parametro padrão (default) onde passagem de parametro seja opcional

Exemplo de função com parametro padrão onde a passagem de parametro obrigatória 

def soma(a=0, b=0, c=0):
    soma = a + b + c
    return soma
print(soma(1,2,3))

def quadrado (numero):
    quadrado = numero ** 2
    return quadrado                  
print(quadrado(4))

def dividir(numero):
    dividir =  8 / numero
    return dividir
print(dividir(4))

def subitrai(numero):
    subitrai = numero - 10
    return subitrai
print(subitrai(4))


def exponencial(numero, potencia=2): # valor padrão ( Se eu não defina um valor padrão, o valor padrão será 2) E
    exponencial = numero ** potencia # 
    return exponencial
print(exponencial(3)) # Por padrão eleva ao quadrado
print(exponencial(3,3))  # Por padrão eleva ao cubo ou a potencia informada pelo usuario 

def mostra_informacao(nome='Leonardo', instrutor=False):
    if nome == 'Leonardo' and instrutor:
        return "Olá Leonardo"
    elif nome == 'Leonardo' and not instrutor:
       return "Olá Leonardo"
   
print(mostra_informacao())
print(mostra_informacao('Leonardo'))
print(mostra_informacao(instrutor=True))
print(mostra_informacao(instrutor=False))
print(mostra_informacao("Pinha"))
    
     # Variavel global
# Variavel local

# Exemplo de variavel global
instrutor = "Nome Leonardo"
print(instrutor) # Variavel global

def diz_oi(nome='Leonardo'): # Variavel local
    print(f'Oi {nome}')

diz_oi()
# Se tivermos uma variavel local com o mesmo nome que a variavel global,a local terá preferencia 

 def Olá_mundo(): # Variavel global
    pessoa = ("Olá mundo") # Variavel local
    return pessoa
print(Olá_mundo()) # Variavel global

  
"""
#Atenção com variaveis GLOBAL, se pouder evitar a variavel global evite!

total =1 # Variavel global
def incremental():
    global total  # Variavel global, avisando que queremos usar a variavel global
    total = total + 4 # Variavel local
    return total
print(incremental())   
    


# Podemos ter funçoes que são declaradas dentrode funçoes, e tbm tem uma forma especial de escopo de variaveis
def fora():
    contador = 0
    def detro():
        nonlocal contador
        contador = contador + 1
        return contador
    return detro()
print(fora())
print(fora())
print(fora())
