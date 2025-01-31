# decoradores de maior grandeza - decorators 
# decorators como funções sintaxe não recomendada

#Exemplo 1:

def seja_educada(funcao):
    def sendo():
        print('Estou sendo educada')
        funcao()
        print('Tenha um bom dia!')
    return sendo

def saudacao():
    print('Seja bem vindo')
    
# teste
teste = seja_educada(saudacao)
teste()

#######################################################################################

# Exemplo 2: Forma recomendada sytax sugar (Açucar de sintaxe)

def seja_educada_mesmo(funcao):     
    def sendo_mesmo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um bom dia!")
    return sendo_mesmo


@seja_educada_mesmo
def apresentando():
    print("Meu nome é Leonardo")
  
apresentando()


@seja_educada_mesmo
def dormir():
    print("Quero dormindo")
#########################################################################################################
























