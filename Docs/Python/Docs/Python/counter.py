# Modulo collection - Counter (contador) High performance Container performance
# Ele recebe um dicionário como parâmetro e retorna um objeto do tipo Counter, que é parecido com um dicionário

##################################################################
lista = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] # lista com números

contador = Counter(lista) # cria um objeto do tipo Counter
print(contador) # imprime o contador, ele recebe um dicionário como parâmetro e retorna um objeto do tipo Counter mostrando o numeros repetidos
print(type(contador)) # imprime o tipo

print(Counter("Leonardo Campos")) # cria um objeto do tipo Counter mostrando o numeros repetidos

##################################################################
       
from collections import Counter # importa a biblioteca

texto = """Celina ama os animais. Ela tem uma gatinha chamada Viola.
Viola teve um filhotinho e Celina o chamou de Fulota.
Viola passa o dia brincando com o Fulota.
Quando Celina chega da escola ela vai correndo pegar Fulota no colo
Viola fica perto, olhando sua dona e seu filhotinho com um olhar mais carinhoso do mundo."""
#print(Counter(texto)) # cria um objeto do tipo Counter
#print(texto.split()) # cria um objeto do tipo Counter mostrando o numeros repetidos de cada palavra
resposta = Counter(texto.split()) 
print(resposta.most_common(5))
help(Counter)

