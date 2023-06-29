 # raise é uma funcao que retorna um erro.

import colorama
colorama.init()

raise ValueError("Valor inválido")

def colore(texto, cor):
    if texto == "vermelho":
        raise ValueError("Valor inválido")
    elif texto == "verde":
        raise NameError("Nome inválido")     
    print(colorama.Fore.GREEN + texto + colorama.Fore.RESET)       
    
colore = colore("verde", "vermelho")    


