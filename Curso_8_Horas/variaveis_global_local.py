#Escopo - Variaveis Globais e Locais

var_global = "Curso 8 Horas de Python" # Variavel Global"
var_local = "" # Definindo var_local como variável global

def escreve_texto():
    global var_global
    var_global = 'Curso muito bom para iniciantes e revisão'
    var_local = "Curso Total Básico ao avançado"
    print(f'Variavel Global: {var_global}')
    print(f'Variavel Local: {var_local}')

if __name__ == '__main':
    print(escreve_texto())
    escreve_texto()

print(var_global)
print(var_local)