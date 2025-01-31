# por que testar codigo?
# Reduzir erros
# Testar funções
# Testar que problemas foram corrigidos
#TDD - Test Driven Development - Testando o código com base nas especificações do teste
#Red;
#Green;
#Refactor;
# Alerta sobre AssertionError se o programa for executado com parâmetros -O nenhum parâmetro é passado

class Gato:
    def __init__(self, nome,):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome
    def miar(self):
        print(f'{self.__nome} está miando!')
        
felix = Gato('Felix')
felix.miar()

        
def soma_numero_positivos(a,b):
    assert a > 0 and b > 0, 'Os números devem ser positivos'
    return a + b
ret = soma_numero_positivos(1,2) # AssertionError
print(ret)
    
def comida_fast_foot(comida):
    assert comida in ['pizza', 'hamburguer', 'Batata frita', 'pudim'], "A comida precisa ser fast food"
    return f"{comida} é uma comida de fast food"
print(comida_fast_foot('comida')) # AssertionError

   