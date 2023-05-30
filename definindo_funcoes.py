
# Definindo funções, funções anônimas e lambda
# Funções são pequenos trechos de código que podem ser reutilizados em tarefas específicas.
        
#  Varias funções:
#  print()
#  len()
#  max()
#  min()
#  count()
 
###################################################################
              
cores = ['vermelho', 'azul', 'amarelo', 'verde']

#utilizando a função integrada no Python
print(cores)
cores.append('roxo')
print(type(cores))
print(cores)
print(len(cores))
print(cores[2]) 

###################################################################
   
# Exemplo 1 de utilizando funções:
# DRY - Don't Repeat Yourself - Não repita o código, não repita!
# Como definir uma função? def nome_da_função(parametros): 
# bloco_da_função
# snake_case = escrita tudo minúsculo com underline para paralavras compostas. 

# Definindo a primeira função

def primeira_funcao(): #definindo a primeira função
    print("Esta é a minha primeira função") 
    # Veja que dentro das nossas funçoes podemos utilizar outras funções
    # Veja que nossa função só executa 1 tarefa
    # Veja que essa fun~]ao não recebe nenhum parametro
    # Veja que está função tbm não retorna nada
    
primeira_funcao() #chamando a função
  # ATENÇÃO nunca esqueça de utilizar o parenteses para chamar a função 
  # ERRADO diz_oi
  # Certo diz_oi()
  
###################################################################
def minha_segunda_funcao():  #definindo a segunda função
    print("Esta é a minha segunda função")
    print("Desejo que essa função seja exemplo de muitos outros exemplos")
    print("Espero que eu enha sucesso em Python")
    print("Espero ter uma carreira solida igual a minha em gestão de TI por 20 anos")
       

    


























