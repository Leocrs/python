"""
Diconarios, São conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor

Dicionarios são representados por {} chaves

Chaves e valor são separados por dois pontos "chaves:valor"
Tanto chave quanto valor podem ser de qualquer tipo de dados
"""


print(type({}))

# forma 2 menos comum
paises = dict(BR="Brasil", EUA="Estados Unidos", PY= "Paragay")
print(paises)
print(type(paises))

# Forma mais comum para criar Dicionarios.
paises = {"BR":"Brasil", "EUA":"Estados Unidos", "PY": "Paragay"}
#Acessando elementos
#Forma 1 via chave, da mesma forma que lita/tupla
print(paises["BR"])
print(paises)
print(paises.get("BR"))
print(paises.get("EUA"))


# Podemos usar qualquer tipo de dados " int, float, string, boolean, number " inclusive lista, tuple dicionarios como chaves.
# Tuplas são bastane utilizadas como chave de dicionarios    por serem imutaveis.
localidades = {
         (35.6895, 39.6917): "Escritorio no Japão",
         (35.6895, 39.6917): "Escritorio no Brasil",
         (35.6890, 56.5326): "Escritorio na Espana",
}
print(localidades)
print(type(localidades))

localidades = {
         (35.6895, 39.6917): "Escritorio no Japão",
         (35.6895, 39.6917): "Escritorio no Brasil",
         (35.6890, 56.5326): "Escritorio na Espana",
}
print(localidades)
print(type(localidades))



# add elementos em um dicionario

receita = {"jan":100, "fev":120, "Mar":300}
print(receita)
print(type(receita))

#Forma 1    Ele adiciona elemento ou atualiza o dicionario
receita["abr"] = 300
print(receita)

#Forma 2   Em dicionario não podemos ter chaves repetidas
receita.update({"mai": 600})
print(receita)

# Remover dados de um dicionario

receita = {"jan":100, "fev":120, "mar":300}

#forma 1
ret = receita.pop("mar")
print(ret)
print(receita)
del receita["fev"]
print(receita)
print(type(receita))
print(receita)
#Teste   




   
   
