# int, str, float, bool, list, tuple, dict, set, frozenset,
def dobro(valor: int) -> int:
    return valor * 2
print(dobro(2))
print(dobro(4))

# Literal type, Union, Final, Typed dictionary, Protocols
from typing import Literal, Union, Final, TypedDict, Protocol
def pegar_status(usuario: str) -> Literal["ativo", "inativo"]: # retorna "ativo" ou "inativo"
    if usuario == "leonardo":
        return "ativo"
    return "inativo"
print(pegar_status("leonardo"))

from typing import Union
# Exemplo Union
def soma(valor1: int, valor2: int) -> Union[str, int]: # recebe dois parâmetros
    resultado = valor1 + valor2
    if resultado > 50:
        return f'{resultado} é maior que 50'
    else:
        return resultado
print(soma(10, 20))

# Exemplo Final
from typing import Final
NOME: Final = "Leonardo" # nome do tipo final
print(NOME)

# Exemplo final 
from typing import final
@final
class Pessoas:
    def __init__(self, nome: str) -> None:
        self.nome = nome
print(Pessoas("Leonardo"))

# Exemplo Typed dictionary
from typing import TypedDict

class Pessoa(TypedDict):
    nome: str
    idade: int
    
pessoa = Pessoa(nome="Leonardo", idade=18)
print(pessoa)

# Exemplo Protocol
from typing import Protocol 
   
class Curso(Protocol):
    titulo: str
def estudar(curso: Curso) -> None:
    print(f'estudando {curso.titulo}')



    

