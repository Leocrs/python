# int, str, float, bool, list, tuple, dict, set, frozenset,

def dobro(valor: int) -> int:
    return valor * 2

print(dobro(2))
print(dobro(4))


# Literal type, Union, Final, Typed dictionary, Protocols

from typing import Literal, Union, Final, TypedDict, Protocol


def pegar_status(usuario: str) -> Literal["ativo", "inativo"]:
    if usuario == "leonardo":
        return "ativo"
    return "inativo"

print(pegar_status("leonardo"))

